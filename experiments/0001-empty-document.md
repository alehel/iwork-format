# 0001: An empty document

**Status:** run

The baseline for every later experiment: what Pages writes for a new document with nothing in it. It answers the first container questions. Is the file a ZIP or a folder? Which parts does it hold? And how are the parts encoded?

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | New document |

## Recipe

```bash
mkdir -p samples/0001
osascript recipes/0001-empty-document.applescript "$PWD/samples/0001/empty-a.pages"
osascript recipes/0001-empty-document.applescript "$PWD/samples/0001/empty-b.pages"
cargo run --release -- list samples/0001/empty-a.pages
```

Saving two empty documents shows which bytes change between saves of the same content, such as IDs, timestamps or random values. Later experiments then know to ignore those.

The two documents were saved 13 seconds apart. Both were unzipped and compared part by part with `cmp`. `iwork-probe` can't yet decompress `.iwa` parts, so a throwaway script written from the public Snappy format description decoded them. That script also split the decoded bytes into records, using the layout described below. `iwork-probe proto` then printed individual records from the decoded bytes.

## Observation

### Container

Both files are ZIP files, not folder packages. Each has the same 13 parts, all stored without ZIP compression:

```
        size       stored  name
          23           23  Index/AnnotationAuthorStorage-1732609.iwa
         543          543  Index/CalculationEngine-1732610.iwa
        7683         7683  Index/Document.iwa
          77           77  Index/DocumentMetadata.iwa
       45708        45708  Index/DocumentStylesheet.iwa
       16883        16883  Index/Metadata.iwa
         723          723  Index/ViewState.iwa         (726 in empty-b)
         271          271  Metadata/BuildVersionHistory.plist
          36           36  Metadata/DocumentIdentifier
         525          525  Metadata/Properties.plist
         817          817  preview-micro.jpg
        1413         1413  preview-web.jpg
       13339        13339  preview.jpg
```

Byte-for-byte comparison of the two files:

| Part | Same in both saves? |
| --- | --- |
| `AnnotationAuthorStorage-1732609.iwa`, `DocumentMetadata.iwa`, `DocumentStylesheet.iwa` | Same |
| `BuildVersionHistory.plist`, the three `preview*.jpg` | Same |
| `CalculationEngine-1732610.iwa`, `Document.iwa`, `Metadata.iwa`, `ViewState.iwa` | Differ |
| `DocumentIdentifier`, `Properties.plist` | Differ |

### The plain parts

`Metadata/DocumentIdentifier` is a 36-character UUID with no line ending. It is different in each save (`7B6613B8-…` and `C382E958-…`).

`Metadata/Properties.plist` is a binary property list. In both saves, `documentUUID`, `shareUUID` and `stableDocumentUUID` all equal the `DocumentIdentifier`. `privateUUID` and `versionUUID` are new in each save, and `revision` is `0::` followed by the `versionUUID`. The other keys don't change between saves: `fileFormatVersion` = `26.4.0`, `isMultiPage` = false, and `hasExternalReferenceOrMissingData` and `hasUnmaterializedRemoteData` are both false.

`Metadata/BuildVersionHistory.plist` is a list of two strings: `Template: Blank (dev/15.4)` and `M15.4-7051.0.79-2`.

### `.iwa` chunks

Every `.iwa` part is a sequence of chunks. Each chunk is a 4-byte header followed by data:

```
00 ff 1d 00 | c4 6e 68 56 08 01 …        Document.iwa
^  ^^^^^^^^   ^^^^^ varint 14148 = decoded size
|  length 0x001dff = 7679 = part size − 4
type 0
```

The data after the header decodes as a raw Snappy block (not the Snappy framing format). Every chunk began with type `00`. Every chunk's declared decoded length matched what the Snappy decoder produced. Five parts fit in one chunk. `DocumentStylesheet.iwa` needed six, and its first five each decode to exactly 65,536 bytes:

```
DocumentStylesheet.iwa chunks (stored → decoded):
13852 → 65536, 7285 → 65536, 7065 → 65536, 8417 → 65536, 6281 → 65536, 2784 → 11302
```

### Records inside the decoded stream

The decoded bytes of every `.iwa` part split into records like this one from `DocumentMetadata.iwa`, with no bytes left over:

```
19                        varint 25: header length
08 47 12 15 … 18 01       header, a Protocol Buffers message (25 bytes)
08 00 1a 28 …             payload, 44 bytes
```

```
1: varint 71                 ← same number on every record of one object
2: message (21 bytes)
  1: varint 11011            ← differs between records; looks like a type
  2: bytes (3) 01 00 05      ← three packed varints
  3: varint 44               ← length of the payload that follows
  4: message (9 bytes) …
```

Within a header, field 1 is a number that is unique to one record in most parts. Field 2 holds a sub-message whose field 3 gives the length of the payload that follows the header. Some headers in `Document.iwa` repeat field 2. Those records are followed by one payload per field 2, in order. The parser consumed every part of both files exactly, with each record ending where the next began:

| Part | Records | Field 1 range | Field 2.2 values seen |
| --- | --- | --- | --- |
| `AnnotationAuthorStorage-1732609.iwa` | 1 | 1732609 | 1.0.5 |
| `CalculationEngine-1732610.iwa` | 8 | 1732610 – 1732654 | 1.0.5, 3.2.10 |
| `Document.iwa` | 58 | 1 – 1732624 | 1.0.5, 2.4.0, 2.0.0, 1.1.0 |
| `DocumentMetadata.iwa` | 1 | 71 | 1.0.5 |
| `DocumentStylesheet.iwa` | 493 | 1731481 – 1732639 | 1.0.5 |
| `Metadata.iwa` | 6 | 2 – 1732655 | 1.0.5 |
| `ViewState.iwa` | 10 | 1732641 – 1732653 | 1.0.5 |

The six `Document.iwa` records with two payloads (field 1 = 1732619 – 1732624) all have type 6247. Each has a 226-byte payload tagged 2.4.0 and a 68-byte payload tagged 2.0.0.

The number in the file names `AnnotationAuthorStorage-1732609` and `CalculationEngine-1732610` equals field 1 of the first record in that part.

### What changed between the two saves

After decompression, `DocumentStylesheet.iwa`, `DocumentMetadata.iwa` and `AnnotationAuthorStorage-…iwa` are still identical. In the other parts, the records with field 1 below 1732641 keep the same numbers in both saves. Records numbered 1732641 or higher got different numbers in each save, though the sequence of types in each part stayed the same:

```
ViewState.iwa, (field 1, type):
  a: (1732641,210) (1732645,10147) (1732646,10131) … (1732652,3091) (1732653,258)
  b: (1732641,210) (1732663,10147) (1732664,10131) … (1732651,3091) (1732652,258)
CalculationEngine-1732610.iwa:
  a: … (1732643,4008) (1732644,4003) (1732654,4004) …
  b: … (1732661,4008) (1732662,4003) (1732670,4004) …
Metadata.iwa:
  a: (2,11006) (1732655,11015) …
  b: (2,11006) (1732671,11015) …
```

Two of those payloads also changed for other reasons:

- `Document.iwa`, record 1732614 (type 10012): the only change is a creation time stored as text, `2026-11-09T13:00:20+0100` in one save and `…13:00:33+0100` in the other. The same payload holds the strings `nb`, `nb_NO`, `Blank` and `,`.
- `Metadata.iwa`, record 2 (type 11006): holds the `versionUUID` from `Properties.plist` as text at payload offset 8. Its other changes weren't traced.

`DocumentMetadata.iwa` holds a fixed64 that reads as 1603405944.07 when decoded as a double. As seconds since 1970, that is 2020-10-22, and it's the same in both saves. It may come from the Blank template.

## Conclusion

A Pages 15.4 document saved by AppleScript is a ZIP file. It holds three JPEG previews, three plain metadata files and seven `.iwa` parts under `Index/`. ZIP compression isn't used. Instead, each `.iwa` part is compressed in its own chunks: a 4-byte header (a type byte, then a 3-byte little-endian length), followed by a raw Snappy block that decodes to at most 64 KiB.

Decoded, an `.iwa` part is a list of records. Each record is a varint length, a Protocol Buffers header, then one or more payloads. The header seems to carry an object ID (field 1), and for each payload a type number (2.1), a three-part version (2.2) and the payload length (2.3). Every object ID is unique across the document. Some parts are named after the ID of their first object.

Between two saves of the same empty content, these things vary and later comparisons should ignore them:

- The UUIDs in `DocumentIdentifier`, `Properties.plist` and `Metadata.iwa` record 2.
- The creation time in `Document.iwa` record type 10012.
- The ID numbers of objects made at save time (here 1732641 and up), and anything that refers to them.

The template's objects keep their IDs and contents. The stylesheet and the previews are byte-for-byte identical.

## Confidence

*Likely* for the ZIP container, the chunk header, the Snappy encoding and the record framing. They held for every byte of 14 `.iwa` parts with no exceptions, but this is one experiment with one Pages version.

*Unknown* for the meaning of header fields 2.2, 4, 5 and 6. The same goes for the meaning of type numbers and the other `Metadata.iwa` record 2 changes. Treating field 1 as an object ID and 2.1 as a type is a hypothesis.

Follow-ups that would settle these:

- 0002 (type one word) should confirm the framing on a part that changes, and show which record holds text.
- Saving the same document twice, without making a new one, would show whether object IDs stay stable across saves of one document.
- Saving from the File menu instead of AppleScript would check that the recipe doesn't affect the container (for example ZIP versus folder package).
- A document large enough to need several chunks in `Document.iwa` would test whether a record can cross a chunk boundary.
