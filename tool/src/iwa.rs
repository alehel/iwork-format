//! The `.iwa` parts under `Index/`, as experiment 0001 found them (confidence: *likely*).
//!
//! A part is a run of chunks. Each chunk is a type byte, a 3-byte little-endian length, then
//! that many bytes holding a raw Snappy block. Every chunk seen so far had type 0.
//!
//! The decoded chunks, joined, are a run of records. Each record is a varint length, a Protocol
//! Buffers header of that length, then one or more payloads. In the header, field 1 seems to be
//! an object ID. Field 2 repeats once per payload, and its field 3 gives the payload's length.
//! Fields 2.1 and 2.2 are reported as a type and a version, which is a hypothesis, not a finding.
//!
//! Fields 2.5 and 2.4.4, packed varints, list object IDs the payload refers to: the references
//! that lead down the object tree, but not those that lead back up (experiment 0022, *likely*).
//!
//! See `experiments/0001-empty-document.md` and `experiments/0022-header-references.md`.

use std::fmt;

use crate::proto::{self, Value};
use crate::snappy;

/// The most bytes all of a part's chunks may decode to together.
pub const MAX_DECODED_BYTES: usize = 512 * 1024 * 1024;
/// The most chunks one part may hold.
pub const MAX_CHUNKS: usize = 1_000_000;
/// The most records one part may hold.
pub const MAX_RECORDS: usize = 1_000_000;

/// Why a part doesn't fit the layout experiment 0001 found.
#[derive(Clone, Debug, PartialEq, Eq)]
pub enum Error {
    /// A chunk header or its data runs past the end of the part.
    TruncatedChunk {
        offset: usize,
    },
    /// A chunk has a type byte other than 0, which no experiment has seen yet.
    UnknownChunkType {
        offset: usize,
        chunk_type: u8,
    },
    /// A chunk's data isn't a valid Snappy block.
    Snappy {
        offset: usize,
        error: snappy::DecodeError,
    },
    /// The part decodes to more than [`MAX_DECODED_BYTES`].
    TooLarge,
    TooManyChunks,
    TooManyRecords,
    /// A record's header length or header runs past the end of the decoded bytes.
    TruncatedHeader {
        offset: usize,
    },
    /// A record's header isn't a valid Protocol Buffers message.
    BadHeader {
        offset: usize,
        error: proto::DecodeError,
    },
    /// A header without field 1 as a varint.
    MissingId {
        offset: usize,
    },
    /// A field 2 in a header that isn't a message with field 3 as a varint.
    MissingPayloadLength {
        offset: usize,
    },
    /// A payload runs past the end of the decoded bytes.
    TruncatedPayload {
        offset: usize,
        length: u64,
    },
}

impl fmt::Display for Error {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::TruncatedChunk { offset } => write!(f, "chunk at offset {offset} runs past the end of the part"),
            Self::UnknownChunkType { offset, chunk_type } => {
                write!(f, "chunk at offset {offset} has type {chunk_type}; only type 0 has been seen")
            }
            Self::Snappy { offset, error } => write!(f, "chunk at offset {offset}: {error}"),
            Self::TooLarge => write!(f, "decodes to more than {MAX_DECODED_BYTES} bytes"),
            Self::TooManyChunks => write!(f, "more than {MAX_CHUNKS} chunks"),
            Self::TooManyRecords => write!(f, "more than {MAX_RECORDS} records"),
            Self::TruncatedHeader { offset } => {
                write!(f, "record header at decoded offset {offset} runs past the end")
            }
            Self::BadHeader { offset, error } => write!(f, "record header at decoded offset {offset}: {error}"),
            Self::MissingId { offset } => write!(f, "record header at decoded offset {offset} has no field 1 varint"),
            Self::MissingPayloadLength { offset } => {
                write!(f, "record header at decoded offset {offset} has a field 2 without a field 3 varint")
            }
            Self::TruncatedPayload { offset, length } => {
                write!(f, "payload of {length} bytes at decoded offset {offset} runs past the end")
            }
        }
    }
}

impl std::error::Error for Error {}

/// One chunk of a part.
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Chunk {
    /// Where the chunk's 4-byte header starts in the part.
    pub offset: usize,
    pub chunk_type: u8,
    /// The length its header gives: the bytes after the header.
    pub stored: usize,
    /// How many bytes it decodes to.
    pub decoded: usize,
    /// Where its decoded bytes start in the part's decoded stream.
    pub decoded_offset: usize,
}

/// A part's chunks, and all their decoded bytes joined in order.
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Decoded {
    pub chunks: Vec<Chunk>,
    pub bytes: Vec<u8>,
}

/// Split a part into chunks and decode each one.
pub fn decode(part: &[u8]) -> Result<Decoded, Error> {
    let mut chunks = Vec::new();
    let mut bytes = Vec::new();
    let mut pos = 0;
    while pos < part.len() {
        if chunks.len() >= MAX_CHUNKS {
            return Err(Error::TooManyChunks);
        }
        let offset = pos;
        let header = part.get(pos..pos.saturating_add(4)).ok_or(Error::TruncatedChunk { offset })?;
        let (chunk_type, len) = match header {
            [t, a, b, c] => (*t, usize::from(*a) | usize::from(*b) << 8 | usize::from(*c) << 16),
            _ => return Err(Error::TruncatedChunk { offset }),
        };
        if chunk_type != 0 {
            return Err(Error::UnknownChunkType { offset, chunk_type });
        }
        let start = pos.saturating_add(4);
        let end = start.checked_add(len).ok_or(Error::TruncatedChunk { offset })?;
        let data = part.get(start..end).ok_or(Error::TruncatedChunk { offset })?;
        let (declared, _) = snappy::declared_len(data).map_err(|error| Error::Snappy { offset, error })?;
        if bytes.len().saturating_add(declared) > MAX_DECODED_BYTES {
            return Err(Error::TooLarge);
        }
        let decoded = snappy::decode(data).map_err(|error| Error::Snappy { offset, error })?;
        chunks.push(Chunk { offset, chunk_type, stored: len, decoded: decoded.len(), decoded_offset: bytes.len() });
        bytes.extend_from_slice(&decoded);
        pos = end;
    }
    Ok(Decoded { chunks, bytes })
}

/// One payload of a record.
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Payload {
    /// Header field 2.1, if it's a varint.
    pub type_number: Option<u64>,
    /// Header field 2.2 read as packed varints, if it's length-delimited and reads that way.
    pub version: Option<Vec<u64>>,
    /// Object IDs listed in header fields 2.5 and 2.4.4, in the order they appear.
    pub references: Vec<u64>,
    /// Where the payload starts in the decoded stream.
    pub offset: usize,
    pub len: usize,
}

/// One record of a decoded part.
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Record {
    /// Where the header's length varint starts in the decoded stream.
    pub offset: usize,
    /// Where the header message starts, and its length.
    pub header_offset: usize,
    pub header_len: usize,
    /// Header field 1.
    pub id: u64,
    pub payloads: Vec<Payload>,
}

/// A run of varints with no other bytes, as packed repeated fields are written.
fn packed_varints(bytes: &[u8]) -> Option<Vec<u64>> {
    let mut values = Vec::new();
    let mut pos = 0;
    while pos < bytes.len() {
        values.push(proto::read_varint(bytes, &mut pos).ok()?);
    }
    Some(values)
}

/// The IDs in field 4 of one header field 2.4 entry, read as packed varints.
fn reference_list_ids(entry: &[u8]) -> Vec<u64> {
    let Ok(fields) = proto::decode(entry) else { return Vec::new() };
    fields
        .iter()
        .filter_map(|f| match (f.number, f.value) {
            (4, Value::Bytes(b)) => packed_varints(b),
            _ => None,
        })
        .flatten()
        .collect()
}

/// Split a part's decoded bytes into records.
pub fn records(decoded: &[u8]) -> Result<Vec<Record>, Error> {
    let mut records = Vec::new();
    let mut pos = 0;
    while pos < decoded.len() {
        if records.len() >= MAX_RECORDS {
            return Err(Error::TooManyRecords);
        }
        let offset = pos;
        let header_len = proto::read_varint(decoded, &mut pos).map_err(|_| Error::TruncatedHeader { offset })?;
        let header_len = usize::try_from(header_len).map_err(|_| Error::TruncatedHeader { offset })?;
        let header_offset = pos;
        let header_end = pos.checked_add(header_len).ok_or(Error::TruncatedHeader { offset })?;
        let header = decoded.get(pos..header_end).ok_or(Error::TruncatedHeader { offset })?;
        let fields = proto::decode(header).map_err(|error| Error::BadHeader { offset, error })?;
        pos = header_end;

        let id = fields
            .iter()
            .find_map(|f| match (f.number, f.value) {
                (1, Value::Varint(v)) => Some(v),
                _ => None,
            })
            .ok_or(Error::MissingId { offset })?;

        let mut payloads = Vec::new();
        for field in fields.iter().filter(|f| f.number == 2) {
            let Value::Bytes(info) = field.value else {
                return Err(Error::MissingPayloadLength { offset });
            };
            let info = proto::decode(info).map_err(|_| Error::MissingPayloadLength { offset })?;
            let mut type_number = None;
            let mut version = None;
            let mut length = None;
            let mut references = Vec::new();
            for f in &info {
                match (f.number, f.value) {
                    (1, Value::Varint(v)) => type_number = type_number.or(Some(v)),
                    (2, Value::Bytes(b)) => version = version.or_else(|| packed_varints(b)),
                    (3, Value::Varint(v)) => length = length.or(Some(v)),
                    (4, Value::Bytes(b)) => references.extend(reference_list_ids(b)),
                    (5, Value::Bytes(b)) => references.extend(packed_varints(b).unwrap_or_default()),
                    _ => {}
                }
            }
            let length = length.ok_or(Error::MissingPayloadLength { offset })?;
            let payload_offset = pos;
            let len = usize::try_from(length).map_err(|_| Error::TruncatedPayload { offset: pos, length })?;
            let end = pos.checked_add(len).ok_or(Error::TruncatedPayload { offset: pos, length })?;
            if end > decoded.len() {
                return Err(Error::TruncatedPayload { offset: pos, length });
            }
            pos = end;
            payloads.push(Payload { type_number, version, references, offset: payload_offset, len });
        }
        records.push(Record { offset, header_offset, header_len, id, payloads });
    }
    Ok(records)
}

#[cfg(test)]
mod tests {
    use super::*;

    /// A chunk of type 0 holding `data` as one Snappy literal.
    fn chunk(data: &[u8]) -> Vec<u8> {
        assert!(!data.is_empty() && data.len() <= 60 && data.len() < 128);
        let block_len = 2 + data.len();
        let mut out = vec![0, block_len as u8, 0, 0, data.len() as u8, ((data.len() - 1) << 2) as u8];
        out.extend_from_slice(data);
        out
    }

    #[test]
    fn chunks_decode_and_join() {
        let mut part = chunk(b"hello ");
        part.extend(chunk(b"world"));
        let decoded = decode(&part).unwrap();
        assert_eq!(decoded.bytes, b"hello world");
        assert_eq!(decoded.chunks.len(), 2);
        assert_eq!(decoded.chunks[1], Chunk { offset: 12, chunk_type: 0, stored: 7, decoded: 5, decoded_offset: 6 });
    }

    #[test]
    fn bad_chunks_are_errors() {
        assert_eq!(decode(&[0, 5, 0]), Err(Error::TruncatedChunk { offset: 0 }));
        assert_eq!(decode(&[0, 5, 0, 0, 1]), Err(Error::TruncatedChunk { offset: 0 }));
        assert_eq!(decode(&[1, 0, 0, 0]), Err(Error::UnknownChunkType { offset: 0, chunk_type: 1 }));
        assert!(matches!(decode(&[0, 1, 0, 0, 5]), Err(Error::Snappy { offset: 0, .. })));
        assert_eq!(decode(&[]).unwrap(), Decoded { chunks: vec![], bytes: vec![] });
    }

    #[test]
    fn records_split_as_experiment_0001_found() {
        // The record from DocumentMetadata.iwa in experiment 0001, with its 44-byte payload
        // replaced by 3 bytes: header { 1: 71, 2: { 1: 11011, 2: [1, 0, 5], 3: 3 } }.
        let header = [0x08, 0x47, 0x12, 0x0a, 0x08, 0x83, 0x56, 0x12, 0x03, 0x01, 0x00, 0x05, 0x18, 0x03];
        let mut bytes = vec![header.len() as u8];
        bytes.extend_from_slice(&header);
        bytes.extend_from_slice(&[0x08, 0x00, 0x10]);
        let records = records(&bytes).unwrap();
        assert_eq!(
            records,
            vec![Record {
                offset: 0,
                header_offset: 1,
                header_len: 14,
                id: 71,
                payloads: vec![Payload {
                    type_number: Some(11011),
                    version: Some(vec![1, 0, 5]),
                    references: vec![],
                    offset: 15,
                    len: 3,
                }],
            }]
        );
    }

    #[test]
    fn a_header_with_two_field_2s_has_two_payloads_in_order() {
        // { 1: 9, 2: { 1: 5, 3: 2 }, 2: { 1: 5, 3: 1 } }, then 2 + 1 payload bytes; then a second record.
        let mut bytes = vec![14, 0x08, 0x09, 0x12, 0x04, 0x08, 0x05, 0x18, 0x02, 0x12, 0x04, 0x08, 0x05, 0x18, 0x01];
        bytes.extend_from_slice(&[0xaa, 0xbb, 0xcc]);
        bytes.extend_from_slice(&[2, 0x08, 0x0a]);
        let records = records(&bytes).unwrap();
        assert_eq!(records.len(), 2);
        let lens: Vec<_> = records[0].payloads.iter().map(|p| (p.offset, p.len)).collect();
        assert_eq!(lens, vec![(15, 2), (17, 1)]);
        assert_eq!(records[1].id, 10);
        assert!(records[1].payloads.is_empty());
    }

    #[test]
    fn header_fields_2_5_and_2_4_4_are_read_as_references() {
        // { 1: 7, 2: { 1: 9, 3: 0, 4: { 1: "F", 4: [300, 5] }, 5: [1732539] } }
        let entry = [0x0a, 0x01, b'F', 0x22, 0x03, 0xac, 0x02, 0x05];
        let mut info = vec![0x08, 0x09, 0x18, 0x00, 0x22, entry.len() as u8];
        info.extend_from_slice(&entry);
        info.extend_from_slice(&[0x2a, 0x03, 0xbb, 0xdf, 0x69]);
        let mut header = vec![0x08, 0x07, 0x12, info.len() as u8];
        header.extend_from_slice(&info);
        let mut bytes = vec![header.len() as u8];
        bytes.extend_from_slice(&header);
        let records = records(&bytes).unwrap();
        assert_eq!(records[0].payloads[0].references, vec![300, 5, 1732539]);
    }

    #[test]
    fn bad_records_are_errors() {
        assert_eq!(records(&[5, 0x08]), Err(Error::TruncatedHeader { offset: 0 }));
        assert!(matches!(records(&[1, 0x00]), Err(Error::BadHeader { offset: 0, .. })));
        assert_eq!(records(&[2, 0x10, 0x01]), Err(Error::MissingId { offset: 0 }));
        assert_eq!(records(&[4, 0x08, 0x01, 0x10, 0x01]), Err(Error::MissingPayloadLength { offset: 0 }));
        assert_eq!(
            records(&[6, 0x08, 0x01, 0x12, 0x02, 0x18, 0x09, 0xff]),
            Err(Error::TruncatedPayload { offset: 7, length: 9 })
        );
    }

    #[test]
    fn hostile_bytes_never_panic() {
        for a in 0..=255u8 {
            for b in 0..=255u8 {
                let buf = [a, 0x08, b, 0x12, a, 0x18, b, 0xff, 0x80, a];
                let _ = records(&buf);
                let _ = decode(&[0, a, b, 0, a, b, 0x01, 0xff, 0x80]);
            }
        }
    }
}
