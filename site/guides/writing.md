# Writing a document

A specification is tested best by writing from it. Experiments [0287](../../experiments/0287-rewriting-a-document.md) to [0290](../../experiments/0290-writing-a-cell.md) rewrote documents with a small Python program built only from what the spec says, and opened the results in the apps. Each starts from a document an app saved and re-encodes or changes it; making a document with nothing to start from is a separate problem, not yet shown for any of the three apps. The program, [`recipes/0287-iwa-writer.py`](../../recipes/0287-iwa-writer.py), uses only the Python standard library.

## Re-encoding every part

The writer reads each `.iwa` part, decodes its chunks and records, and encodes them again:

1. Parse each record: the header length varint, the header, and the payloads whose lengths header field 2.3 gives.
2. Serialise each record again, recomputing field 2.3 from the payload's actual length.
3. Split the result into pieces of at most 65,536 bytes, the size the apps write (Pages reads larger chunks too, [0433](../../experiments/0433-writing-chunk-sizes.md)). Encode each as a raw Snappy block of literals only, without compression, and prefix it with a chunk header: `00` and the block's length as 24 bits, little-endian.
4. Write a ZIP with every entry stored.

A Snappy block of literals is a varint of the decoded length, then for each run a tag byte and the bytes themselves. A run longer than 60 bytes uses tag 60, 61 or 62 with a 1-, 2- or 3-byte length after it:

```python
def snappy_encode_literals(data):
    out = bytearray(write_varint(len(data)))
    for i in range(0, len(data), 65536):
        piece = data[i:i + 65536]
        n = len(piece) - 1
        if n < 60:
            out.append(n << 2)
        elif n < 1 << 8:
            out += bytes([60 << 2]) + n.to_bytes(1, "little")
        elif n < 1 << 16:
            out += bytes([61 << 2]) + n.to_bytes(2, "little")
        else:
            out += bytes([62 << 2]) + n.to_bytes(3, "little")
        out += piece
    return bytes(out)
```

Pages opened the re-encoded document, more than four times the size of the original (395 KB against 90), without a warning, and saved it normally. A writer doesn't need to compress ([0287](../../experiments/0287-rewriting-a-document.md)).

## New text

Setting field 3 of the body's type-2001 record to new text, and re-encoding, is enough for a one-paragraph body. Pages opened [written-by-script.pages](../files/written-by-script.pages), written without previews, and kept the record exactly as written when it saved it again ([0288](../../experiments/0288-writing-new-text.md)).

![written-by-script.pages, written by the Python writer, as Pages prints it](../files/written-by-script.png)

## Paragraphs need run entries

The run tables list positions in the text. When the text gains a paragraph, the paragraph run table (field 5) needs an entry at its start. Without it, Pages rebuilds the table on opening and gives every paragraph the stylesheet's default style, `paragraph-style-default`, instead of the style the writer named ([0289](../../experiments/0289-writing-two-paragraphs.md)). So writing `One` U+000A `Two` takes:

| Field | Written |
| --- | --- |
| 3 | `One\nTwo` |
| 5 | `{ 1: 0, 2: { 1: <Body style ID> } }`, `{ 1: 4 }` |

The second entry has no style; it continues the one before it.

## A new cell value

In Numbers, replacing the 16 bytes of a cell's decimal128 with another number is enough: Numbers opened [written-cell.numbers](../files/written-cell.numbers) and showed 42 where the original held 1. Nothing else in the file caches the value ([0290](../../experiments/0290-writing-a-cell.md)).

```python
old = (1).to_bytes(14, "little") + bytes([0x40, 0x30])   # 1 × 10⁰
new = (42).to_bytes(14, "little") + bytes([0x40, 0x30])  # 42 × 10⁰
```

![written-cell.numbers as Numbers prints it](../files/written-cell.png)

## What a writer still has to get right

- Any change that adds objects needs new IDs that are unique in the document, and every reference listed in the record header (fields 2.4 and 2.5).
- Run tables must cover the new text: positions are in UTF-16 code units.
- Cells that add strings need string table entries, with use counts.
- The previews are optional; Pages makes new ones when it next saves.
- `isMultiPage` in `Metadata/Properties.plist` should say whether the document now has more than one page, slide or sheet.

## What the app changes when it saves your document

Opening a written document in the app and saving it again is a good test of a writer: the app writes out only what it keeps. [Experiment 0476](../../experiments/0476-resaving-every-sample.md) did this for every sample, the written ones included, except the password-protected ones and the files written to make an app fail, in Pages, Numbers and Keynote 16.0, twice, with the same changes both times:

- Fields the app doesn't keep were dropped, such as fields the writer added to table models (type 6001) and formula owners (type 4008) that aren't part of those records.
- Data files were renamed to the app's own form, and files nothing refers to were left out.
- `isMultiPage` was corrected where a writer had changed the number of pages.
- Records the app makes as it needs them, such as view-state records, were counted again, and the calculation engine got its locale.

Everything else came back the same. Some of the copies that changed are published with the fixtures under `resaved/16.0/`, chosen so that they hold every field the 182 of them hold, each beside its original, so the two can be compared ([sample files](samples.md#all-fixtures)).
