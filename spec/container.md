# 1. Container

How a Pages document is packaged, and how its parts are encoded. Every finding links to the experiments that support it, with a confidence level as defined in [CONTRIBUTING.md](../CONTRIBUTING.md#confidence).

Observed with Pages 15.4 on macOS 26.5.2. Keynote 15.4 and Numbers 15.4 write the same container: the package, chunk, record and reference findings below hold for their documents too ([0024](../experiments/0024-keynote-and-numbers.md)). The apps differ in their document root (object 1: type 10000 in Pages, type 1 in Keynote and Numbers) and in the parts they add, such as `Slide-N` and `TemplateSlide-N` in Keynote.

## The package

A document saved by Pages is a ZIP file by default. *Likely* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md)). It can also be a folder (File → Advanced → Change File Type → Package): the metadata files and previews are files in the folder, the `.iwa` parts are inside an `Index.zip` in it, under the same `Index/` names, and data files are in a `Data/` folder beside it. *Confirmed* for all three apps ([0076](../experiments/0076-package-format.md), [0146](../experiments/0146-keynote-package.md), [0147](../experiments/0147-numbers-package.md))

ZIP entry names are UTF-8, but Pages doesn't set the ZIP flag that says so; read them as UTF-8 regardless. *Likely* ([0144](../experiments/0144-non-ascii-file-name.md))

Part names aren't fixed: after a document is saved again, a part can be renamed after the ID of its new first record (`ViewState.iwa` became `ViewState-1732662.iwa`). Find parts by listing them. *Likely* ([0139](../experiments/0139-resave.md))

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

A document with a table also has parts under `Index/Tables/`: `DataList`, `HeaderStorageBucket` and `Tile`, each holding one record. Each is named `Name.iwa`, `Name-N.iwa` or `Name-N-2.iwa`, where N is the ID of the record inside. Both Pages and Numbers use all three forms. What the `-2` ending means is *unknown*. *Likely* ([0020](../experiments/0020-a-table.md), [0026](../experiments/0026-numbers-cells.md), [0030](../experiments/0030-tiles.md))

## Data files

Files a document embeds, such as images, are stored unchanged under `Data/`, each named after its original file name with `-N` before the extension. N is a data ID, by which records refer to the file. *Likely* ([0023](../experiments/0023-an-image.md))

Identical files are stored once ([0142](../experiments/0142-same-image-twice.md)), in their original format ([0143](../experiments/0143-jpeg-image.md)), and files nothing uses are dropped on save ([0145](../experiments/0145-deleted-image.md)). For a large image, Pages also stores a reduced copy (`name-small-N.ext`), which the image record names in field 12 ([0148](../experiments/0148-large-image.md)). *Likely*

`Metadata.iwa` record 2 (type 11006) lists the data in its repeated field 4. Each entry holds the data ID (field 1), the file's SHA-1 (field 2), the original file name (field 3) and the stored file name (field 4). Entries for resources of the template have no file in the package. *Likely* ([0023](../experiments/0023-an-image.md))

## Chunks

An `.iwa` part is a sequence of chunks, with nothing before, between or after them. *Confirmed* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md))

| Bytes | Holds |
| --- | --- |
| 1 | Chunk type. Always 0 so far. |
| 3 | Length of the data that follows, little-endian |
| length | A raw Snappy block (the block format, not the Snappy framing format) |

No chunk has decoded to more than 65,536 bytes, and a part that decodes to more is split into chunks of exactly 65,536 decoded bytes, then a shorter last one. *Confirmed* ([0001](../experiments/0001-empty-document.md), [0141](../experiments/0141-large-text.md))

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

Every object in a document can be reached by starting at objects 1 (in `Document.iwa`), 2 (in `Metadata.iwa`) and 71 (in `DocumentMetadata.iwa`) and following the IDs in record headers, plus object 61 in `ObjectContainer.iwa` when a document has a chart. *Confirmed*: all 240,278 objects of the 353 samples, the 6 protected ones decrypted, were reached this way ([0022](../experiments/0022-header-references.md), [0024](../experiments/0024-keynote-and-numbers.md), [0178](../experiments/0178-regression-check.md), [0247](../experiments/0247-second-regression-check.md), [0266](../experiments/0266-decrypting-in-the-tool.md)). A document with a chart also has `Index/ObjectContainer.iwa`, whose object 61 (type 11008) is a fourth root, listing chart styles ([0067](../experiments/0067-chart.md)).

Object 1, the document root, has a different type and layout in each app (type 10000 in Pages, type 1 in Keynote and in Numbers, and those two differ). Each embeds the same block of document properties as one large message (Pages field 15, Keynote field 3, Numbers field 8), holding the locale (field 1 starts with it, field 3 is the language) and the template path (field 9, such as `Application/Blank/ISO`). *Likely* ([0027](../experiments/0027-document-roots.md))

## Password protection

A document with a password has two extra files at the top of the package, `.iwph` and `.iwpv2`, and no previews. This holds in all three apps. *Confirmed* ([0179](../experiments/0179-password.md), [0180](../experiments/0180-password-in-other-apps.md))

- `.iwph` holds the password hint as plain text.
- `.iwpv2` is 104 bytes: two 16-bit values (2 and 1, meaning *unknown*), a 32-bit iteration count (100,000), a 16-byte salt, a 16-byte IV, then 64 encrypted bytes. Decrypted, those are 32 random bytes followed by their SHA-256, which checks the password.

The key is PBKDF2-HMAC-SHA1 of the password (as UTF-8), using that salt and iteration count, 16 bytes long. Every `.iwa` part, every data file and `BuildVersionHistory.plist` is encrypted with it, using AES-128-CBC with PKCS #7 padding. `DocumentIdentifier` and `Properties.plist` are not encrypted. An encrypted part is laid out as 16 bytes of unknown meaning, the IV, the ciphertext, and 20 bytes of unknown meaning, probably an integrity check. Decrypted, a part is the same as in an unprotected document. The salt is new on every save. *Confirmed* ([0179](../experiments/0179-password.md), [0180](../experiments/0180-password-in-other-apps.md)); that the password is UTF-8 is *likely*. `iwork-probe --password` decrypts documents this way; all six protected samples then frame and are fully reachable ([0266](../experiments/0266-decrypting-in-the-tool.md)).

## View state

`ViewState.iwa` holds how the document was last shown, which a reader can ignore. Its type-10133 record has the zoom as a scale factor in field 15 (1.25 for 125%) and in field 33 whether two pages are shown side by side. *Likely* ([0241](../experiments/0241-zoom.md), [0242](../experiments/0242-two-page-view.md))

## IDs and save-to-save changes

Saving the same content twice can change these, and nothing else in the `.iwa` parts. *Likely* ([0001](../experiments/0001-empty-document.md), [0002](../experiments/0002-one-word.md))

- The UUIDs in `DocumentIdentifier`, `Properties.plist` and `Metadata.iwa` record 2.
- A creation time stored as text in the `Document.iwa` record of type 10012, and a time in `CalculationEngine` record type 4000.
- 128-bit-looking values in `CalculationEngine` records.
- The IDs of objects made at save time, and every reference to them. They changed between the two documents in 0001 but not between the two in 0002. Objects that come from the template keep their IDs.
- The order of entries in one list in `Metadata.iwa` record 2.

When a document is saved again, existing objects keep their IDs and newly made ones (such as the view state) get new ones. Saving under a new name gives a new document UUID. *Likely* ([0139](../experiments/0139-resave.md), [0140](../experiments/0140-edit-and-save.md))
