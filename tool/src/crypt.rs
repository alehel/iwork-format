//! Decrypt the parts of a password-protected document (experiments 0179 and 0180).
//!
//! `.iwpv2` holds two 16-bit values, a 32-bit little-endian iteration count, a 16-byte salt, a
//! 16-byte IV, and 64 encrypted bytes: 32 random bytes followed by their SHA-256, which checks
//! the password. The key is PBKDF2-HMAC-SHA1 of the password as UTF-8, 16 bytes long. Each
//! encrypted part is 16 bytes of unknown meaning, a 16-byte IV, AES-128-CBC ciphertext with
//! PKCS #7 padding, and 20 trailing bytes of unknown meaning.

use std::fmt;

use aes::Aes128;
use cbc::Decryptor;
use cbc::cipher::block_padding::{NoPadding, Pkcs7};
use cbc::cipher::{BlockModeDecrypt, KeyIvInit};
use sha2::{Digest, Sha256};

/// The file that marks a password-protected document and holds the key's parameters.
pub const HEADER: &str = ".iwpv2";
/// The file that holds the password hint as plain text.
pub const HINT: &str = ".iwph";

/// Bytes before a part's IV, of unknown meaning.
const PART_HEAD: usize = 16;
/// Bytes after a part's ciphertext, of unknown meaning.
const PART_TAIL: usize = 20;
/// The largest iteration count accepted, to keep a bad header from stalling the tool.
const MAX_ITERATIONS: u32 = 10_000_000;

#[derive(Debug, PartialEq, Eq)]
pub enum Error {
    /// `.iwpv2` isn't laid out as observed.
    BadHeader,
    /// The password doesn't pass the check in `.iwpv2`.
    WrongPassword,
    /// A part is too short, or its padding is wrong.
    BadPart(String),
}

impl fmt::Display for Error {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::BadHeader => write!(f, "{HEADER} is not laid out as expected"),
            Self::WrongPassword => write!(f, "wrong password"),
            Self::BadPart(name) => write!(f, "part {name:?} doesn't decrypt"),
        }
    }
}

impl std::error::Error for Error {}

/// The key that decrypts a document's parts.
pub struct Key([u8; 16]);

/// Whether a part is stored encrypted in a password-protected document. Only the two
/// password files, `Properties.plist` and `DocumentIdentifier` are left in the clear.
pub fn is_encrypted(name: &str) -> bool {
    !matches!(name, HEADER | HINT | "Metadata/Properties.plist" | "Metadata/DocumentIdentifier")
}

fn array16(bytes: Option<&[u8]>) -> Result<[u8; 16], Error> {
    bytes.and_then(|b| b.try_into().ok()).ok_or(Error::BadHeader)
}

/// The key for `password`, checked against the document's `.iwpv2`.
pub fn key(header: &[u8], password: &str) -> Result<Key, Error> {
    let iterations = header
        .get(4..8)
        .and_then(|b| b.try_into().ok())
        .map(u32::from_le_bytes)
        .filter(|&n| n > 0 && n <= MAX_ITERATIONS)
        .ok_or(Error::BadHeader)?;
    let salt = header.get(8..24).ok_or(Error::BadHeader)?;
    let iv = array16(header.get(24..40))?;
    let check = header.get(40..104).ok_or(Error::BadHeader)?;
    let key: [u8; 16] = pbkdf2::pbkdf2_hmac_array::<sha1::Sha1, 16>(password.as_bytes(), salt, iterations);
    let mut plain = check.to_vec();
    let len = Decryptor::<Aes128>::new(&key.into(), &iv.into())
        .decrypt_padded::<NoPadding>(&mut plain)
        .map_err(|_| Error::BadHeader)?
        .len();
    plain.truncate(len);
    let (random, digest) = plain.split_at_checked(32).ok_or(Error::BadHeader)?;
    if Sha256::digest(random).as_slice() == digest { Ok(Key(key)) } else { Err(Error::WrongPassword) }
}

/// A part's plain bytes.
pub fn decrypt(key: &Key, name: &str, stored: &[u8]) -> Result<Vec<u8>, Error> {
    let bad = || Error::BadPart(name.to_string());
    let iv = stored.get(PART_HEAD..PART_HEAD + 16).ok_or_else(bad)?;
    let iv: [u8; 16] = iv.try_into().map_err(|_| bad())?;
    let end = stored.len().checked_sub(PART_TAIL).ok_or_else(bad)?;
    let ciphertext = stored.get(PART_HEAD + 16..end).ok_or_else(bad)?;
    let mut plain = ciphertext.to_vec();
    let len = Decryptor::<Aes128>::new(&key.0.into(), &iv.into())
        .decrypt_padded::<Pkcs7>(&mut plain)
        .map_err(|_| bad())?
        .len();
    plain.truncate(len);
    Ok(plain)
}

#[cfg(test)]
mod tests {
    use super::*;
    use cbc::Encryptor;
    use cbc::cipher::BlockModeEncrypt;

    fn encrypt(key: &[u8; 16], iv: &[u8; 16], plain: &[u8]) -> Vec<u8> {
        let mut buf = plain.to_vec();
        buf.resize(plain.len() / 16 * 16 + 16, 0);
        let len = Encryptor::<Aes128>::new(&(*key).into(), &(*iv).into())
            .encrypt_padded::<Pkcs7>(&mut buf, plain.len())
            .unwrap()
            .len();
        buf.truncate(len);
        buf
    }

    /// A header for `password`, built the way experiment 0179 read Pages' own.
    fn header(password: &str) -> (Vec<u8>, [u8; 16]) {
        let salt = [3u8; 16];
        let iv = [5u8; 16];
        let iterations = 1000u32;
        let key: [u8; 16] = pbkdf2::pbkdf2_hmac_array::<sha1::Sha1, 16>(password.as_bytes(), &salt, iterations);
        let mut check = vec![9u8; 32];
        check.extend_from_slice(&Sha256::digest([9u8; 32]));
        let len = check.len();
        let encrypted = Encryptor::<Aes128>::new(&key.into(), &iv.into())
            .encrypt_padded::<NoPadding>(&mut check, len)
            .unwrap()
            .to_vec();
        let mut out = vec![2, 0, 1, 0];
        out.extend_from_slice(&iterations.to_le_bytes());
        out.extend_from_slice(&salt);
        out.extend_from_slice(&iv);
        out.extend_from_slice(&encrypted);
        (out, key)
    }

    #[test]
    fn the_right_password_decrypts_a_part() {
        let (head, raw_key) = header("påss");
        let key = key(&head, "påss").unwrap();
        let iv = [7u8; 16];
        let mut part = vec![0u8; PART_HEAD];
        part.extend_from_slice(&iv);
        part.extend_from_slice(&encrypt(&raw_key, &iv, b"hello, part"));
        part.extend_from_slice(&[0u8; PART_TAIL]);
        assert_eq!(decrypt(&key, "Index/Document.iwa", &part).unwrap(), b"hello, part");
    }

    #[test]
    fn a_wrong_password_is_refused() {
        let (head, _) = header("right");
        assert_eq!(key(&head, "wrong").err(), Some(Error::WrongPassword));
    }

    #[test]
    fn a_short_header_or_part_is_an_error() {
        assert_eq!(key(&[2, 0, 1, 0], "x").err(), Some(Error::BadHeader));
        let (head, _) = header("x");
        let key = key(&head, "x").unwrap();
        assert!(decrypt(&key, "p", &[0; 10]).is_err());
    }

    #[test]
    fn only_four_files_are_left_in_the_clear() {
        assert!(!is_encrypted(".iwpv2"));
        assert!(!is_encrypted(".iwph"));
        assert!(!is_encrypted("Metadata/Properties.plist"));
        assert!(!is_encrypted("Metadata/DocumentIdentifier"));
        assert!(is_encrypted("Index/Document.iwa"));
        assert!(is_encrypted("Data/image-24.png"));
        assert!(is_encrypted("Metadata/BuildVersionHistory.plist"));
    }
}
