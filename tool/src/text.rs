//! Text records, as `spec/text.md` describes them: a payload of type 2001 whose field 3 is the
//! text as UTF-8. In Pages, field 1 tells the body (0) from header and footer text (1). Numbers
//! also uses 1, for the text a sheet's objects are anchored in, and Keynote leaves field 1 out.
//!
//! See experiments 0002, 0003, 0005, 0006, 0016, 0018, 0020 and 0025.

use crate::iwa::Record;
use crate::proto::{self, Value};

/// The record type of text, the same in Pages and Keynote.
pub const TEXT_TYPE: u64 = 2001;

/// What a text record's field 1 says it is.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Kind {
    /// Field 1 is 0: a Pages document's body.
    Body,
    /// Field 1 is 1: a header or footer.
    HeaderOrFooter,
    /// Field 1 is another number.
    Other(u64),
    /// No field 1, as in Keynote's shapes.
    Unmarked,
}

/// One text record.
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Text {
    pub id: u64,
    pub kind: Kind,
    /// Field 3, or empty when the record has none (an empty text).
    pub text: String,
}

/// The text records among a part's records. `decoded` is the part's decoded bytes.
pub fn texts(decoded: &[u8], records: &[Record]) -> Vec<Text> {
    let mut out = Vec::new();
    for record in records {
        for payload in record.payloads.iter().filter(|p| p.type_number == Some(TEXT_TYPE)) {
            let Some(bytes) = payload.offset.checked_add(payload.len).and_then(|end| decoded.get(payload.offset..end))
            else {
                continue;
            };
            let Ok(fields) = proto::decode(bytes) else { continue };
            let mut kind = Kind::Unmarked;
            let mut text = String::new();
            for field in &fields {
                match (field.number, field.value) {
                    (1, Value::Varint(0)) => kind = Kind::Body,
                    (1, Value::Varint(1)) => kind = Kind::HeaderOrFooter,
                    (1, Value::Varint(n)) => kind = Kind::Other(n),
                    (3, Value::Bytes(b)) => text = String::from_utf8_lossy(b).into_owned(),
                    _ => {}
                }
            }
            out.push(Text { id: record.id, kind, text });
        }
    }
    out
}

/// The text with its special characters made readable: paragraph and line breaks as new lines,
/// a page break (U+0005) as `[page break]` on its own line, and an object anchored in the text
/// (U+FFFC) as `[object]`.
pub fn readable(text: &str) -> String {
    let mut out = String::with_capacity(text.len());
    for c in text.chars() {
        match c {
            '\r' | '\n' | '\u{2028}' => out.push('\n'),
            '\u{5}' => out.push_str("\n[page break]\n"),
            '\u{fffc}' => out.push_str("[object]"),
            other => out.push(other),
        }
    }
    out
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::iwa;

    /// A record of type 2001 with the given payload, as one decoded part.
    fn part(payload: &[u8]) -> Vec<u8> {
        // header { 1: 9, 2: { 1: 2001, 3: len } }
        let mut info = vec![0x08, 0xd1, 0x0f, 0x18, payload.len() as u8];
        let mut header = vec![0x08, 0x09, 0x12, info.len() as u8];
        header.append(&mut info);
        let mut bytes = vec![header.len() as u8];
        bytes.extend_from_slice(&header);
        bytes.extend_from_slice(payload);
        bytes
    }

    #[test]
    fn a_body_record_gives_its_text() {
        let bytes = part(&[0x08, 0x00, 0x1a, 0x05, b'h', b'e', b'l', b'l', b'o']);
        let records = iwa::records(&bytes).unwrap();
        assert_eq!(texts(&bytes, &records), vec![Text { id: 9, kind: Kind::Body, text: "hello".into() }]);
    }

    #[test]
    fn an_empty_text_has_no_field_3() {
        let bytes = part(&[0x08, 0x01]);
        let records = iwa::records(&bytes).unwrap();
        assert_eq!(texts(&bytes, &records), vec![Text { id: 9, kind: Kind::HeaderOrFooter, text: String::new() }]);
    }

    #[test]
    fn special_characters_are_made_readable() {
        assert_eq!(readable("a\nb\u{2028}c\u{5}d\u{fffc}"), "a\nb\nc\n[page break]\nd[object]");
    }

    #[test]
    fn hostile_payloads_never_panic() {
        for a in 0..=255u8 {
            let bytes = part(&[0x08, a, 0x1a, a, 0xff, a]);
            if let Ok(records) = iwa::records(&bytes) {
                let _ = texts(&bytes, &records);
            }
        }
    }
}
