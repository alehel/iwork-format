//! A decoder for raw Snappy blocks, from Google's public description of the Snappy format
//! (`format_description.txt` in the Snappy repository). It decodes the block format only, not the
//! separate framing format.
//!
//! A block is a varint giving the decoded length, then a run of elements. Each element is a
//! literal (bytes copied from the input) or a copy (bytes repeated from earlier in the output).

use std::fmt;

use crate::proto;

/// The largest decoded block this decoder will produce. The format allows up to 2^32 - 1 bytes.
pub const MAX_DECODED_BYTES: usize = 512 * 1024 * 1024;

/// Why bytes aren't a valid Snappy block. Offsets are relative to the start of the block.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum DecodeError {
    /// The preamble isn't a valid varint.
    BadPreamble,
    /// The block declares more than [`MAX_DECODED_BYTES`].
    TooLarge { declared: u64 },
    /// An element runs past the end of the block.
    Truncated { offset: usize },
    /// A copy refers to bytes before the start of the output, or has offset 0.
    BadCopyOffset { offset: usize, distance: usize },
    /// The elements produce more bytes than the preamble declared.
    Overrun { offset: usize, declared: usize },
    /// The elements produce fewer bytes than the preamble declared.
    ShortOutput { declared: usize, produced: usize },
}

impl fmt::Display for DecodeError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::BadPreamble => write!(f, "the decoded length isn't a valid varint"),
            Self::TooLarge { declared } => {
                write!(f, "declares {declared} decoded bytes, over the {MAX_DECODED_BYTES}-byte limit")
            }
            Self::Truncated { offset } => write!(f, "element at offset {offset} runs past the end"),
            Self::BadCopyOffset { offset, distance } => {
                write!(f, "copy at offset {offset} reaches back {distance} bytes, before the start of the output")
            }
            Self::Overrun { offset, declared } => {
                write!(f, "element at offset {offset} produces more than the declared {declared} bytes")
            }
            Self::ShortOutput { declared, produced } => {
                write!(f, "produced {produced} bytes, but {declared} were declared")
            }
        }
    }
}

impl std::error::Error for DecodeError {}

/// The decoded length a block declares, and where its elements start.
pub fn declared_len(block: &[u8]) -> Result<(usize, usize), DecodeError> {
    let mut pos = 0;
    let declared = proto::read_varint(block, &mut pos).map_err(|_| DecodeError::BadPreamble)?;
    // The format stores the length in at most 32 bits.
    if declared > u64::from(u32::MAX) {
        return Err(DecodeError::BadPreamble);
    }
    let len = usize::try_from(declared).map_err(|_| DecodeError::TooLarge { declared })?;
    if len > MAX_DECODED_BYTES {
        return Err(DecodeError::TooLarge { declared });
    }
    Ok((len, pos))
}

/// `n` little-endian bytes at `pos`, as a number.
fn le(block: &[u8], pos: usize, n: usize, offset: usize) -> Result<usize, DecodeError> {
    let end = pos.checked_add(n).ok_or(DecodeError::Truncated { offset })?;
    let bytes = block.get(pos..end).ok_or(DecodeError::Truncated { offset })?;
    Ok(bytes.iter().rev().fold(0usize, |acc, &b| (acc << 8) | usize::from(b)))
}

/// Decode one raw Snappy block.
pub fn decode(block: &[u8]) -> Result<Vec<u8>, DecodeError> {
    let (declared, mut pos) = declared_len(block)?;
    // Don't trust the declared length for the allocation: grow as elements actually arrive.
    let mut out: Vec<u8> = Vec::with_capacity(declared.min(1 << 20));
    while pos < block.len() {
        let offset = pos;
        let tag = *block.get(pos).ok_or(DecodeError::Truncated { offset })?;
        pos += 1;
        let (len, distance) = match tag & 3 {
            0 => {
                // A literal. Lengths up to 60 sit in the tag; longer ones in 1 to 4 extra bytes.
                let short = usize::from(tag >> 2);
                let len_minus_one = if short < 60 {
                    short
                } else {
                    let n = short - 59;
                    let value = le(block, pos, n, offset)?;
                    pos += n;
                    value
                };
                let len = len_minus_one.checked_add(1).ok_or(DecodeError::Truncated { offset })?;
                let end = pos.checked_add(len).ok_or(DecodeError::Truncated { offset })?;
                let bytes = block.get(pos..end).ok_or(DecodeError::Truncated { offset })?;
                if out.len().saturating_add(len) > declared {
                    return Err(DecodeError::Overrun { offset, declared });
                }
                out.extend_from_slice(bytes);
                pos = end;
                continue;
            }
            // A copy with a 1-byte offset: length 4 to 11, and an 11-bit offset.
            1 => {
                let len = usize::from((tag >> 2) & 7) + 4;
                let low = usize::from(*block.get(pos).ok_or(DecodeError::Truncated { offset })?);
                pos += 1;
                (len, (usize::from(tag >> 5) << 8) | low)
            }
            // A copy with a 2-byte offset: length 1 to 64.
            2 => {
                let distance = le(block, pos, 2, offset)?;
                pos += 2;
                (usize::from(tag >> 2) + 1, distance)
            }
            // A copy with a 4-byte offset: length 1 to 64.
            _ => {
                let distance = le(block, pos, 4, offset)?;
                pos += 4;
                (usize::from(tag >> 2) + 1, distance)
            }
        };
        if distance == 0 || distance > out.len() {
            return Err(DecodeError::BadCopyOffset { offset, distance });
        }
        if out.len().saturating_add(len) > declared {
            return Err(DecodeError::Overrun { offset, declared });
        }
        // Copies may overlap their own output (distance < len), so go a byte at a time.
        let start = out.len() - distance;
        for i in start..start + len {
            let byte = *out.get(i).ok_or(DecodeError::BadCopyOffset { offset, distance })?;
            out.push(byte);
        }
    }
    if out.len() != declared {
        return Err(DecodeError::ShortOutput { declared, produced: out.len() });
    }
    Ok(out)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn a_literal_decodes() {
        // length 5; literal of 5 bytes (tag (5-1)<<2)
        assert_eq!(decode(&[5, 4 << 2, b'h', b'e', b'l', b'l', b'o']).unwrap(), b"hello");
    }

    #[test]
    fn an_empty_block_decodes() {
        assert_eq!(decode(&[0]).unwrap(), b"");
    }

    #[test]
    fn a_long_literal_uses_extra_length_bytes() {
        // 61 bytes: tag 60<<2 says one extra byte holds length - 1 = 60.
        let mut block = vec![61, 60 << 2, 60];
        block.extend_from_slice(&[b'x'; 61]);
        assert_eq!(decode(&block).unwrap(), vec![b'x'; 61]);
        // 300 bytes: tag 61<<2 says two extra bytes hold 299.
        let mut block = vec![0xac, 0x02, 61 << 2, 0x2b, 0x01];
        block.extend_from_slice(&[b'y'; 300]);
        assert_eq!(decode(&block).unwrap(), vec![b'y'; 300]);
    }

    #[test]
    fn copies_with_every_offset_size_decode() {
        // "ab", then copy-1 of length 4 from 2 back (overlapping) -> "ababab"
        assert_eq!(decode(&[6, 1 << 2, b'a', b'b', 0x01, 2]).unwrap(), b"ababab");
        // "abc", then copy-2 of length 3 from 3 back -> "abcabc"
        assert_eq!(decode(&[6, 2 << 2, b'a', b'b', b'c', (2 << 2) | 2, 3, 0]).unwrap(), b"abcabc");
        // "abc", then copy-4 of length 2 from 2 back -> "abcbc"
        assert_eq!(decode(&[5, 2 << 2, b'a', b'b', b'c', (1 << 2) | 3, 2, 0, 0, 0]).unwrap(), b"abcbc");
    }

    #[test]
    fn a_copy_one_offset_carries_three_high_bits_in_the_tag() {
        // 300 literal bytes, then copy-1 of length 4 from 260 back: 260 = 1<<8 | 4.
        let mut block = vec![0xb0, 0x02, 61 << 2, 0x2b, 0x01];
        let literal: Vec<u8> = (0..300u32).map(|i| (i % 251) as u8).collect();
        block.extend_from_slice(&literal);
        block.extend_from_slice(&[(1 << 5) | 1, 4]);
        let out = decode(&block).unwrap();
        assert_eq!(&out[300..], &literal[40..44]);
    }

    #[test]
    fn malformed_blocks_are_errors() {
        assert_eq!(decode(&[]), Err(DecodeError::BadPreamble));
        assert_eq!(decode(&[0x80]), Err(DecodeError::BadPreamble));
        assert_eq!(decode(&[0xff, 0xff, 0xff, 0xff, 0x7f]), Err(DecodeError::BadPreamble));
        assert_eq!(decode(&[3, 4 << 2, b'a']), Err(DecodeError::Truncated { offset: 1 }));
        assert_eq!(decode(&[4, 1, 1]), Err(DecodeError::BadCopyOffset { offset: 1, distance: 1 }));
        assert_eq!(decode(&[5, 0, b'a', 1, 0]), Err(DecodeError::BadCopyOffset { offset: 3, distance: 0 }));
        assert_eq!(decode(&[1, 4, b'a', b'b']), Err(DecodeError::Overrun { offset: 1, declared: 1 }));
        assert_eq!(decode(&[3, 0, b'a']), Err(DecodeError::ShortOutput { declared: 3, produced: 1 }));
    }

    #[test]
    fn a_huge_declared_length_is_refused_before_allocating() {
        // 2^32 - 1 declared, over the limit.
        assert!(matches!(decode(&[0xff, 0xff, 0xff, 0xff, 0x0f]), Err(DecodeError::TooLarge { .. })));
    }

    #[test]
    fn hostile_bytes_never_panic() {
        for a in 0..=255u8 {
            for b in 0..=255u8 {
                let _ = decode(&[40, 4, b'x', b'y', a, b, a, 0xfc, b, 1, 0, 0]);
                let _ = decode(&[a, b, 0xff, 0xff, 0xff, 0xff]);
            }
        }
    }
}
