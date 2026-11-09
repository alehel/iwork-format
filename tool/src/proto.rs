//! A generic decoder for the Protocol Buffers wire format, from Google's public encoding
//! specification. It knows nothing about what any field means: it reports field numbers, wire
//! types and values, which is what format experiments compare.

use std::fmt;

/// Field numbers above this are invalid in the wire format (2^29 - 1).
const MAX_FIELD_NUMBER: u64 = (1 << 29) - 1;
/// The most fields one message may hold before decoding gives up.
pub const MAX_FIELDS: usize = 1_000_000;

/// One field's value, as the wire format carries it.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Value<'a> {
    /// Wire type 0.
    Varint(u64),
    /// Wire type 1: eight bytes, little-endian.
    Fixed64(u64),
    /// Wire type 2: a length-delimited run of bytes (a string, bytes, a nested message or a packed
    /// repeated field; the wire format doesn't say which).
    Bytes(&'a [u8]),
    /// Wire type 5: four bytes, little-endian.
    Fixed32(u32),
}

/// One decoded field.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct Field<'a> {
    pub number: u32,
    /// Where the field's key starts, relative to the decoded buffer.
    pub offset: usize,
    pub value: Value<'a>,
}

/// Why bytes aren't a valid message. Offsets are relative to the decoded buffer.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum DecodeError {
    Truncated { offset: usize },
    VarintTooLong { offset: usize },
    FieldNumberOutOfRange { offset: usize, number: u64 },
    UnsupportedWireType { offset: usize, wire_type: u8 },
    LengthOutOfRange { offset: usize, length: u64 },
    TooManyFields,
}

impl fmt::Display for DecodeError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::Truncated { offset } => write!(f, "truncated value at offset {offset}"),
            Self::VarintTooLong { offset } => write!(f, "varint longer than 10 bytes at offset {offset}"),
            Self::FieldNumberOutOfRange { offset, number } => {
                write!(f, "field number {number} out of range at offset {offset}")
            }
            Self::UnsupportedWireType { offset, wire_type } => {
                write!(f, "unsupported wire type {wire_type} at offset {offset}")
            }
            Self::LengthOutOfRange { offset, length } => {
                write!(f, "length {length} runs past the end at offset {offset}")
            }
            Self::TooManyFields => write!(f, "more than {MAX_FIELDS} fields"),
        }
    }
}

impl std::error::Error for DecodeError {}

/// Read a base-128 varint at `*pos`, moving `*pos` past it.
pub fn read_varint(buf: &[u8], pos: &mut usize) -> Result<u64, DecodeError> {
    let start = *pos;
    let mut result: u64 = 0;
    for i in 0..10u32 {
        let byte = *buf.get(*pos).ok_or(DecodeError::Truncated { offset: start })?;
        *pos += 1;
        let low = u64::from(byte & 0x7f);
        // The tenth byte may only carry the 64th bit.
        if i == 9 && byte > 1 {
            return Err(DecodeError::VarintTooLong { offset: start });
        }
        result |= low << (7 * i);
        if byte & 0x80 == 0 {
            return Ok(result);
        }
    }
    Err(DecodeError::VarintTooLong { offset: start })
}

fn take<'a>(buf: &'a [u8], pos: &mut usize, len: usize, offset: usize) -> Result<&'a [u8], DecodeError> {
    let end = pos.checked_add(len).ok_or(DecodeError::Truncated { offset })?;
    let bytes = buf.get(*pos..end).ok_or(DecodeError::Truncated { offset })?;
    *pos = end;
    Ok(bytes)
}

/// Decode `buf` as one message: every byte must belong to a field.
pub fn decode(buf: &[u8]) -> Result<Vec<Field<'_>>, DecodeError> {
    let mut fields = Vec::new();
    let mut pos = 0;
    while pos < buf.len() {
        if fields.len() >= MAX_FIELDS {
            return Err(DecodeError::TooManyFields);
        }
        let offset = pos;
        let key = read_varint(buf, &mut pos)?;
        let number = key >> 3;
        if number == 0 || number > MAX_FIELD_NUMBER {
            return Err(DecodeError::FieldNumberOutOfRange { offset, number });
        }
        let number = u32::try_from(number).map_err(|_| DecodeError::FieldNumberOutOfRange { offset, number })?;
        let wire_type = (key & 7) as u8;
        let value = match wire_type {
            0 => Value::Varint(read_varint(buf, &mut pos)?),
            1 => {
                let bytes: [u8; 8] =
                    take(buf, &mut pos, 8, offset)?.try_into().map_err(|_| DecodeError::Truncated { offset })?;
                Value::Fixed64(u64::from_le_bytes(bytes))
            }
            2 => {
                let length = read_varint(buf, &mut pos)?;
                let len = usize::try_from(length).map_err(|_| DecodeError::LengthOutOfRange { offset, length })?;
                let bytes =
                    take(buf, &mut pos, len, offset).map_err(|_| DecodeError::LengthOutOfRange { offset, length })?;
                Value::Bytes(bytes)
            }
            5 => {
                let bytes: [u8; 4] =
                    take(buf, &mut pos, 4, offset)?.try_into().map_err(|_| DecodeError::Truncated { offset })?;
                Value::Fixed32(u32::from_le_bytes(bytes))
            }
            // 3 and 4 are the deprecated group markers; 6 and 7 are undefined.
            other => return Err(DecodeError::UnsupportedWireType { offset, wire_type: other }),
        };
        fields.push(Field { number, offset, value });
    }
    Ok(fields)
}

/// Bytes that read as text: valid UTF-8 with no control characters other than tab and newlines.
fn as_text(bytes: &[u8]) -> Option<&str> {
    let text = std::str::from_utf8(bytes).ok()?;
    let printable = text.chars().all(|c| !c.is_control() || matches!(c, '\t' | '\n' | '\r'));
    (printable && !text.is_empty()).then_some(text)
}

/// The first `max` characters of `text`, cut at a character boundary.
fn clip(text: &str, max: usize) -> (&str, bool) {
    match text.char_indices().nth(max) {
        Some((end, _)) => (text.get(..end).unwrap_or(text), true),
        None => (text, false),
    }
}

fn hex(bytes: &[u8], max: usize) -> String {
    let shown: Vec<String> = bytes.iter().take(max).map(|b| format!("{b:02x}")).collect();
    let more = if bytes.len() > max { " …" } else { "" };
    format!("{}{more}", shown.join(" "))
}

/// Print `buf` as a tree of fields, one per line, nesting into length-delimited values that
/// decode as messages, up to `max_depth` levels.
///
/// A length-delimited value is ambiguous on the wire. It's shown as text when it reads as
/// text, as a nested message when it decodes as one, and as hex otherwise. The tree is a
/// starting point for experiments, not a statement of what a field is.
pub fn render(buf: &[u8], max_depth: usize) -> Result<String, DecodeError> {
    let mut out = String::new();
    render_into(buf, 0, max_depth, &mut out)?;
    Ok(out)
}

fn render_into(buf: &[u8], depth: usize, max_depth: usize, out: &mut String) -> Result<(), DecodeError> {
    let indent = "  ".repeat(depth);
    for field in decode(buf)? {
        let n = field.number;
        match field.value {
            Value::Varint(v) => out.push_str(&format!("{indent}{n}: varint {v}\n")),
            Value::Fixed64(v) => out.push_str(&format!("{indent}{n}: fixed64 {v} (as double {})\n", f64::from_bits(v))),
            Value::Fixed32(v) => out.push_str(&format!("{indent}{n}: fixed32 {v} (as float {})\n", f32::from_bits(v))),
            Value::Bytes(bytes) => {
                let len = bytes.len();
                if let Some(text) = as_text(bytes) {
                    let (shown, cut) = clip(text, 200);
                    let more = if cut { " …" } else { "" };
                    out.push_str(&format!("{indent}{n}: text ({len} bytes) {shown:?}{more}\n"));
                } else if depth < max_depth && !bytes.is_empty() && decode(bytes).is_ok() {
                    out.push_str(&format!("{indent}{n}: message ({len} bytes)\n"));
                    render_into(bytes, depth + 1, max_depth, out)?;
                } else {
                    out.push_str(&format!("{indent}{n}: bytes ({len}) {}\n", hex(bytes, 32)));
                }
            }
        }
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn varints_decode_as_the_public_spec_shows() {
        let cases: &[(&[u8], u64)] = &[
            (&[0x00], 0),
            (&[0x01], 1),
            (&[0x96, 0x01], 150),
            (&[0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x01], u64::MAX),
        ];
        for (bytes, want) in cases {
            let mut pos = 0;
            assert_eq!(read_varint(bytes, &mut pos), Ok(*want));
            assert_eq!(pos, bytes.len());
        }
    }

    #[test]
    fn overlong_and_truncated_varints_are_errors() {
        let mut pos = 0;
        assert_eq!(read_varint(&[0x80, 0x80], &mut pos), Err(DecodeError::Truncated { offset: 0 }));
        let mut pos = 0;
        let eleven = [0xff; 11];
        assert_eq!(read_varint(&eleven, &mut pos), Err(DecodeError::VarintTooLong { offset: 0 }));
        let mut pos = 0;
        let tenth_too_big = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x02];
        assert_eq!(read_varint(&tenth_too_big, &mut pos), Err(DecodeError::VarintTooLong { offset: 0 }));
    }

    #[test]
    fn every_wire_type_decodes() {
        // field 1 varint 150; field 2 string "hi"; field 3 fixed64 1; field 4 fixed32 2
        let buf = [0x08, 0x96, 0x01, 0x12, 0x02, b'h', b'i', 0x19, 1, 0, 0, 0, 0, 0, 0, 0, 0x25, 2, 0, 0, 0];
        let fields = decode(&buf).unwrap();
        let values: Vec<_> = fields.iter().map(|f| (f.number, f.value)).collect();
        assert_eq!(
            values,
            vec![(1, Value::Varint(150)), (2, Value::Bytes(b"hi")), (3, Value::Fixed64(1)), (4, Value::Fixed32(2)),]
        );
        assert_eq!(fields[1].offset, 3);
    }

    #[test]
    fn malformed_messages_are_errors() {
        assert_eq!(decode(&[0x00]), Err(DecodeError::FieldNumberOutOfRange { offset: 0, number: 0 }));
        assert_eq!(decode(&[0x0b]), Err(DecodeError::UnsupportedWireType { offset: 0, wire_type: 3 }));
        assert_eq!(decode(&[0x12, 0x05, b'a']), Err(DecodeError::LengthOutOfRange { offset: 0, length: 5 }));
        assert_eq!(decode(&[0x0d, 1, 2]), Err(DecodeError::Truncated { offset: 0 }));
    }

    #[test]
    fn render_nests_messages_and_shows_text() {
        // field 1 = message { field 1 varint 7, field 2 text "Hello" }
        let inner = [0x08, 0x07, 0x12, 0x05, b'H', b'e', b'l', b'l', b'o'];
        let mut buf = vec![0x0a, inner.len() as u8];
        buf.extend_from_slice(&inner);
        let tree = render(&buf, 8).unwrap();
        assert_eq!(tree, "1: message (9 bytes)\n  1: varint 7\n  2: text (5 bytes) \"Hello\"\n");
    }

    #[test]
    fn render_stops_nesting_at_the_depth_limit() {
        let buf = [0x0a, 0x02, 0x08, 0x07];
        assert_eq!(render(&buf, 0).unwrap(), "1: bytes (2) 08 07\n");
    }

    #[test]
    fn hostile_bytes_never_panic() {
        for a in 0..=255u8 {
            for b in 0..=255u8 {
                let buf = [a, b, 0xff, 0x80, b, a];
                let _ = decode(&buf);
                let _ = render(&buf, 64);
            }
        }
    }

    #[test]
    fn clipping_respects_character_boundaries() {
        assert_eq!(clip("æøå", 2), ("æø", true));
        assert_eq!(clip("ab", 5), ("ab", false));
    }
}
