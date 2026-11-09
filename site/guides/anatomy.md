# Reading a Pages document

This page follows one file from its ZIP listing down to the five bytes that hold its text. The file is [hello.pages](../files/hello.pages): a new blank document in which the word `hello` was typed and saved ([0002](../../experiments/0002-one-word.md)).

![hello.pages as Pages prints it: the word hello at the top of an A4 page](../files/hello.png)

## 1. The ZIP package

A `.pages` file is a ZIP archive whose entries are stored, not compressed ([container.md](../../spec/container.md#the-package)). This one holds 13 parts:

<!-- include: hello-list.txt -->

| Part | Holds |
| --- | --- |
| `Index/*.iwa` | The document's objects. Most of this page is about these. |
| `Metadata/Properties.plist` | A binary property list: UUIDs, file format version, flags |
| `Metadata/DocumentIdentifier` | The document's UUID, 36 ASCII characters |
| `Metadata/BuildVersionHistory.plist` | The template and the Pages build that wrote the file |
| `preview*.jpg` | Previews of the first page, which readers may ignore |

A name ending in a number, such as `CalculationEngine-1732610.iwa`, carries the ID of the part's first object. Names can change when a document is saved again, so a reader should list the parts rather than expect fixed names.

## 2. Chunks

The text lives in `Index/Document.iwa`. An `.iwa` part is a series of chunks, each with a four-byte header: a type byte, always 0, then the length of the chunk's data as a 24-bit little-endian number ([container.md](../../spec/container.md#chunks)). This part has one chunk:

<!-- include: hello-chunks.txt -->

These are the first bytes of the part as stored:

<!-- include: hello-stored-hex.txt -->

| Bytes | Meaning |
| --- | --- |
| `00` | Chunk type 0 |
| `06 1e 00` | Length 0x001e06 = 7,686 bytes of chunk data follow |
| `cb 6e` | Start of the chunk data, a raw Snappy block: its decoded length as a varint, 0x4b + (0x6e × 128) = 14,155 |
| `68` | A Snappy literal tag: 0x68 >> 2 = 26, so 27 literal bytes follow |
| `56 08 01 12 52 …` | Those literal bytes: the start of the decoded data |

Snappy is Google's public compression format; the chunk data is a raw block, without the framing format's stream header. Each chunk decodes to at most 65,536 bytes, and a part's decoded chunks are joined end to end.

## 3. Records

The decoded data is a list of records. Each record is a varint giving the header's length, a header message, then the payload. `iwork-probe records` lists them:

<!-- include: hello-records.txt -->

The first record starts at decoded offset 0:

<!-- include: hello-header-hex.txt -->

`56` is the header length, 86 bytes. The header itself is a Protocol Buffers message, decoded here field by field:

<!-- include: hello-header-proto.txt -->

| Field | Value | Meaning |
| --- | --- | --- |
| 1 | 1 | The object's ID |
| 2.1 | 10000 | The object's type: a Pages document root |
| 2.2 | `01 00 05` | A version, 1.0.5 |
| 2.3 | 1,398 | The payload's length in bytes |
| 2.4 | | Groups of further referenced IDs |
| 2.5 | packed varints | IDs of objects the payload refers to |

So the payload is the 1,398 bytes after the header, at offset 1 + 86 = 87, as the records listing shows. Field 2 can repeat when a record has more than one payload; the payloads then follow each other ([container.md](../../spec/container.md#records)).

## 4. The document root

Object 1 is the root of a Pages document. Its payload is another Protocol Buffers message. Without a schema, a reader sees only field numbers and wire types; the specification gives them meaning. These are some of its fields:

<!-- include: hello-root.txt -->

| Field | Meaning |
| --- | --- |
| 2 | A reference (field 1 inside holds an ID) to the stylesheet, object 1732613 |
| 4 | A reference to the body text, object 1732539 |
| 30, 31 | Paper width and height in points: 595.28 × 841.89 is A4 |
| 32–35 | Left, right, top and bottom margins: 56.69 points, which is 2 cm |

Floats are stored as 32-bit fixed-width fields, which `iwork-probe` shows both as integers and as floats. A reference is always a small message whose field 1 is an ID; every ID referenced this way is also listed in the record's header, which is how a reader can walk from the roots to every object without understanding each type ([container.md](../../spec/container.md#following-references)).

## 5. The body text

Following root field 4 leads to object 1732539, a record of type 2001: a text storage. Its payload starts with these bytes:

<!-- include: hello-body-hex.txt -->

| Bytes | Field | Meaning |
| --- | --- | --- |
| `08 00` | 1 = 0 | Field 1, varint 0: this is the body, not a header or footer |
| `12 04 08 85 e0 69` | 2 = { 1: 1732613 } | A reference to the stylesheet |
| `1a 05 68 65 6c 6c 6f` | 3 = "hello" | Field 3, length 5: the text, as UTF-8 |
| `2a …` | 5 | The paragraph run table follows |

The same record, decoded:

<!-- include: hello-body.txt -->

The text has no terminator; the field's length is the text's length in bytes ([text.md](../../spec/text.md#the-body-text)). Paragraphs are separated by U+000A. The fields after 3 are run tables: each lists positions in the text, in UTF-16 code units ([text.md](../../spec/text.md#positions-in-the-text)), and what applies from there on. Field 5 is the paragraph runs: one entry at position 0 naming paragraph style 1731511.

`iwork-probe text` does all of this in one step:

<!-- include: hello-text.txt -->

## 6. The paragraph style

Object 1731511 is in `Index/DocumentStylesheet.iwa`. It is a type-2022 paragraph style:

<!-- include: hello-body-style.txt -->

Field 1.1 is the style's name, as the app's language shows it (`Brødtekst` is Norwegian for Body, since this document was made in Norwegian) and 1.2 its identifier, which doesn't depend on the language. Field 11 holds its character properties and field 12 its paragraph properties. Styles inherit from a parent, and a property missing from a style comes from the parent ([text.md](../../spec/text.md#styles)).

## What was skipped

This walk-through followed one path. The same steps lead everywhere else: list the parts, decode the chunks, read the records, and follow references from objects 1, 2 and 71. The remaining 51 records in `Document.iwa` hold header and footer texts, the section, the document settings and more, each described in the [specification](../../spec/README.md).
