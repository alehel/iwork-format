# 0179: A password

**Status:** run

Pages can protect a document with a password. This experiment sets one through AppleScript, to see what changes in the package and whether a reader that knows the password can get the document back.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `plain.pages`, made by the same recipe without a password |

## Recipe

```bash
mkdir -p samples/0179
osascript recipes/0179-password.applescript "$PWD/samples/0179"
```

The recipe makes four documents with the body text `one`:

- `plain.pages`: no password.
- `locked.pages` and `locked2.pages`: the password `pw1234` with the hint `test`, not saved in the keychain.
- `unlocked.pages`: the same password, then removed before saving.

## Observation

`unlocked.pages` is laid out like `plain.pages`. The two locked documents differ from it:

- They have no previews.
- Two files are added: `.iwph`, the hint `test` as 4 bytes of text, and `.iwpv2`, 104 bytes.
- `DocumentIdentifier` and `Properties.plist` are unchanged in form.
- Every `.iwa` part and `BuildVersionHistory.plist` no longer starts with a chunk header or `<?xml`. Each is about 60 bytes longer than the matching part in `plain.pages`.

The first 8 bytes of `.iwpv2` are the same in both locked documents: `02 00 01 00 a0 86 01 00`. Read as little-endian, that is 2 and 1 (16-bit), then 100,000 (32-bit). The rest differs between the two, although the password is the same.

I tried key derivations from the password against `BuildVersionHistory.plist`, whose plain text starts with `<?xml`. One fits:

- **Key:** PBKDF2 with HMAC-SHA1 over the password, the salt in `.iwpv2` bytes 8–23, 100,000 iterations (the 32-bit value), and a 16-byte key.
- **Cipher:** AES-128 in CBC mode.

With that key, every encrypted part splits the same way:

| Bytes | Holds |
| --- | --- |
| 0–15 | Unknown, different in each part |
| 16–31 | The IV |
| 32 to end − 20 | The ciphertext, with PKCS #7 padding |
| Last 20 | Unknown |

All eight parts decrypt with valid padding, to the same lengths as the matching parts of `plain.pages`. Every decrypted `.iwa` part frames as chunks and records. Repacked without `.iwph` and `.iwpv2`, the decrypted document gives the body text `one` in `iwork-probe text`.

The rest of `.iwpv2` decrypts with the same key. With bytes 24–39 as the IV, bytes 40–103 give 64 bytes: 32 bytes, then the SHA-256 of those 32 bytes. A reader can use this to check a password before decrypting any part.

The last 20 bytes of a part aren't an HMAC-SHA1 or SHA-1 of its plaintext, ciphertext or IV and ciphertext. Neither the encryption key nor the second half of a 32-byte PBKDF2 output matched as the HMAC key.

## Conclusion

A password-protected document keeps its package layout, but encrypts every `.iwa` part and `BuildVersionHistory.plist` with AES-128-CBC. The key is PBKDF2-HMAC-SHA1 of the password, with the salt and iteration count from `.iwpv2`. Each part has its own IV, at bytes 16–31. `.iwpv2` also holds a password check: an encrypted random 32 bytes followed by their SHA-256. `.iwph` holds the hint as plain text, and the previews are left out.

A reader with the password can decrypt each part and then read it as normal. A reader without it can still tell that a document is protected (by `.iwpv2`) and show the hint. The salt is new on each save.

## Confidence

*Likely*:

- The key derivation, the cipher and the layout of `.iwpv2` and of each encrypted part.
- Which files are encrypted and which aren't.

*Unknown*:

- The first 16 and last 20 bytes of each encrypted part. The trailer is probably an integrity check with a key I haven't found.
- The 16-bit values 2 and 1 at the start of `.iwpv2`.

Follow-up: a password in Keynote and Numbers, a non-ASCII password and a document with an image (experiment 0180).
