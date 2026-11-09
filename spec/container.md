# 1. Container

How a Pages document is packaged, and how its parts are encoded. Every finding links to the experiments that support it, with a confidence level as defined in [CONTRIBUTING.md](../CONTRIBUTING.md#confidence).

Observed with Pages 15.4 on macOS 26.5.2.

## The package

A document saved by Pages is a ZIP file. *Likely* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md); both saved through AppleScript, so a document saved from the File menu is still to be checked.)

Its entries are stored without ZIP compression. *Confirmed* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md))

A new document holds these 13 parts. *Confirmed* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md))

| Part | Holds |
| --- | --- |
| `Index/*.iwa` (seven parts) | The document's objects, encoded as below |
| `Metadata/DocumentIdentifier` | A UUID as 36 ASCII characters, with no line ending |
| `Metadata/Properties.plist` | A binary property list of UUIDs, a file format version and flags |
| `Metadata/BuildVersionHistory.plist` | A list of strings naming the template and the Pages build |
| `preview.jpg`, `preview-web.jpg`, `preview-micro.jpg` | JPEG previews of the first page |

The seven `.iwa` parts of a new document are `AnnotationAuthorStorage-N`, `CalculationEngine-N`, `Document`, `DocumentMetadata`, `DocumentStylesheet`, `Metadata` and `ViewState`. Where a name ends in a number, it is the ID of the part's first object. *Confirmed* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md))

A document with a table also has parts under `Index/Tables/`: `DataList`, `HeaderStorageBucket` and `Tile`, each holding one record. Each is named either without a number or as `Name-N-2.iwa`, where N is the ID of the record inside. *Likely* ([0020](../experiments/0020-a-table.md))

## Chunks

An `.iwa` part is a sequence of chunks, with nothing before, between or after them. *Confirmed* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md))

| Bytes | Holds |
| --- | --- |
| 1 | Chunk type. Always 0 so far. |
| 3 | Length of the data that follows, little-endian |
| length | A raw Snappy block (the block format, not the Snappy framing format) |

No chunk has decoded to more than 65,536 bytes, and a part that decodes to more is split into chunks of exactly 65,536 decoded bytes, then a shorter last one. *Likely* ([0001](../experiments/0001-empty-document.md); only `DocumentStylesheet.iwa` has needed more than one chunk.)

## Records

Decode every chunk and join the results in order. The joined bytes are a sequence of records, with nothing between them. A record can start in one chunk and end in the next, so the chunks have to be joined first. *Confirmed* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md))

| Holds | Encoding |
| --- | --- |
| Header length | Varint |
| Header | Protocol Buffers message of that length |
| Payloads | One after another, one per header field 2, in the order those fields appear |

The header's fields:

| Field | Holds | Confidence |
| --- | --- | --- |
| 1 | Object ID, a varint. Unique across the whole document. | *Confirmed* that it's unique ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md)); that it identifies an object is *likely*, since other records refer to these numbers ([0002](../experiments/0002-one-word.md)). |
| 2 | One message per payload (repeated) | *Confirmed* |
| 2.1 | A varint that differs between records with differently shaped payloads. Probably the payload's type. | *Unknown* |
| 2.2 | Three packed varints, such as `1 0 5`. Probably a version. | *Unknown* |
| 2.3 | The payload's length in bytes | *Confirmed* |
| 2.5 | Packed varints: IDs of objects the payload refers to | *Likely* ([0022](../experiments/0022-header-references.md)) |
| 2.4 | Repeated; field 4 of each entry holds more referenced IDs as packed varints, and field 1 is probably the field path that holds them | *Likely* ([0022](../experiments/0022-header-references.md)) |
| 2.6 | Present in some headers; meaning not established | *Unknown* |

Most records have one payload. In a new document, six records in `Document.iwa` have two, with the same 2.1 value and different 2.2 values. *Likely* ([0001](../experiments/0001-empty-document.md))

## Following references

Every ID in header fields 2.5 and 2.4.4 is a reference in the record's payload. *Confirmed* ([0022](../experiments/0022-header-references.md)). They are the references that lead down the object tree. References back up, such as a style's or a text's link to the stylesheet, or a table drawable's link to its text, aren't listed. *Likely* ([0022](../experiments/0022-header-references.md))

Every object in a document can be reached by starting at objects 1 (in `Document.iwa`), 2 (in `Metadata.iwa`) and 71 (in `DocumentMetadata.iwa`) and following the IDs in record headers. *Likely* ([0022](../experiments/0022-header-references.md))

## IDs and save-to-save changes

Saving the same content twice can change these, and nothing else in the `.iwa` parts. *Likely* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md))

- The UUIDs in `DocumentIdentifier`, `Properties.plist` and `Metadata.iwa` record 2.
- A creation time stored as text in the `Document.iwa` record of type 10012, and a time in `CalculationEngine` record type 4000.
- 128-bit-looking values in `CalculationEngine` records.
- The IDs of objects made at save time, and every reference to them. They changed between the two documents in 0001 but not between the two in 0002. Objects that come from the template keep their IDs.
- The order of entries in one list in `Metadata.iwa` record 2.

Whether IDs stay the same when one document is saved twice, rather than two new documents being saved, hasn't been tested.
