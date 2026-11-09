# 0027: Document roots

**Status:** run

[0024](0024-keynote-and-numbers.md) found that object 1 is type 10000 in Pages and type 1 in both Keynote and Numbers. This experiment looks at what those roots hold. It also asks whether Keynote's and Numbers' type 1 are the same, and follows Keynote's root down to the slide title found in [0025](0025-keynote-title.md). It saves no new documents.

## Setup

| | |
| --- | --- |
| Apps | Pages, Keynote and Numbers 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Documents | `samples/0002/hello.pages`, `samples/0025/hello.key`, `samples/0026/cells.numbers` |

## Recipe

```bash
cargo run --release -- records samples/0025/hello.key Index/Document.iwa     # find object 1
cargo run --release -- proto samples/0025/hello.key Index/Document.iwa --decoded --offset <payload> --len <len> --depth 1
cargo run --release -- refs samples/0025/hello.key Index/Slide-2652175.iwa
```

The same was done for the Pages and Numbers files. The path from object 1 to the title's text record was found with a breadth-first walk over the output of `refs`.

## Observation

### The roots

| | Pages (type 10000) | Keynote (type 1) | Numbers (type 1) |
| --- | --- | --- | --- |
| Top-level fields | 2, 3, 4, 6, 7, 15, 20, 30–40, 42–44, 46, 47, 49 | 2, 3 | 1, 4, 5, 6, 8, 11, 12 |
| Field holding the shared block | 15 | 3 | 8 |

Keynote's and Numbers' type-1 roots share no field layout. But each of the three roots holds one large message with the same inner fields:

```
1: bytes (≈1190)  starting 22 05 "nb_NO" …
3: text "nb"
4, 5, 6, 12: each a small message naming an object
8, 14, 15, 16: 0
9: text "Application/Blank/ISO"            (Pages)
   text "Application/21_BasicWhite/Wide"  (Keynote)
   text "Application/Blank/Traditional"   (Numbers)
```

### Page setup in Pages' root

| Field | Value | Matches |
| --- | --- | --- |
| 30, 31 | 595.28, 841.89 | A4 in points |
| 32–35 | 56.69 each | the 2 cm margins the Document sidebar showed (see [0016](0016-header-and-footer.md)) |
| 36 | 35.43 | the header's 1.25 cm |
| 37 | 42.52 | the footer's 1.5 cm |
| 38 | 1.0 | |
| 43 | `EPSON_XP_760_Series` | the printer the sidebar showed |
| 44 | `iso-a4` | the paper size |

Numbers' root also has a paper size: field 11 `iso-a4`, and field 12 `{ 1: 595.0, 2: 842.0 }`.

### From Keynote's root to the title

Following header references from object 1 to the title's text record (2652192):

| Object | Type | Part | What it holds |
| --- | --- | --- | --- |
| 1 | 1 | `Document.iwa` | the shared block, and a reference to 2652410 |
| 2652410 | 2 | `Document.iwa` | references to 2652174, the stylesheet 2652414, and two other objects |
| 2652174 | 4 | `Document.iwa` | 2: the slide 2652175; 10: `{356.0, 200.0}`; 16: `{ 1: 9058 }` |
| 2652175 | 5 | `Slide-2652175.iwa` | references to 8 objects, among them 2652199 |
| 2652199 | 7 | `Slide-2652175.iwa` | a geometry message, a style (2651745), and 2: and 4: the text 2652192 |
| 2652192 | 2001 | `Slide-2652175.iwa` | the text `hello` |

Data ID 9058 is the file `Data/st-A11B23C4-404B-4AC4-98CB-13188B352B53-9058.jpg` in the package (see [0024](0024-keynote-and-numbers.md)).

## Conclusion

Type numbers aren't shared across apps for every type: Keynote's and Numbers' type 1 are different records. But all three apps' roots embed the same block of document properties: the locale (`nb_NO`, `nb`), the template it came from, and a few references. A reader can find it as the one large message in the root, and read it the same way for every app.

Pages keeps its page setup in the root:

- the paper size in points (fields 30 and 31)
- the four margins (32–35)
- the header and footer distances (36 and 37)
- the printer and paper names (43 and 44)

Keynote's document is a chain:

- the root (type 1) points at a presentation (type 2, probably)
- the presentation points at a slide node (type 4), which holds a thumbnail size and the data ID of the slide's thumbnail image
- the slide node points at the slide (type 5), which has its own part
- the slide holds shapes (type 7), and a shape with text owns a type-2001 text record

## Confidence

*Likely*:

- All three roots embed the same document-properties block.
- Fields 30–37, 43 and 44 of Pages' root are page setup, as listed.
- Keynote's chain from root to slide to shape to text is as described, with type 4 holding a thumbnail's data ID.

*Unknown*:

- Which margin is which among fields 32–35. All four are 2 cm here. Follow-up: set four different margins.
- The fields of the type-2 presentation and type-5 slide.
