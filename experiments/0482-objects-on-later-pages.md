# 0482: Objects on later pages

**Status:** run

So far every object placed on the page ("Stay on Page") was on page 1. There, a type-10015 record lists it next to the body's text, and a type-10010 record lists it as `1: { 1: 0, 4: { 1: { 1: <id> } } }`, with a meaning not yet known ([0023](0023-an-image.md)). This experiment places pictures on pages 2 and 3 of a three-page document, and on page 1 for comparison, to see how a page is recorded.

## Setup

| | |
| --- | --- |
| Pages | 16.0 (7052.0.68) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-28 |
| Input | `three-pages.pages`: `samples/0002/hello.pages` with the body text written as `one`, U+0005, `two`, U+0005, `three`, so that it has three pages ([0018](0018-page-break-and-left-page.md)). AppleScript can't make a page break: Pages drops U+0005 from a body text set by script |
| Recipe | [`recipes/0482-place-on-pages.sh`](../recipes/0482-place-on-pages.sh) opens a document, places the 8 × 4 red picture of [0023](0023-an-image.md) on each page it is given, in that order, and saves a copy. Exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and checked with [`recipes/0482-red-per-page.swift`](../recipes/0482-red-per-page.swift), which says on which page of a PDF red is drawn, and where |

## Recipe

```bash
mkdir -p samples/0482
S=samples/0482
python3 -I recipes/0023-image.py "$PWD/$S/red-8x4.png"
python3 -I recipes/0287-iwa-writer.py samples/0002/hello.pages $S/three-pages.pages \
  --text 1732539 "$(printf 'one\005two\005three')"
R=recipes/0482-place-on-pages.sh
sh $R $S/three-pages.pages $S/on-2-and-3.pages $S/red-8x4.png 2 3
sh $R $S/three-pages.pages $S/on-1-and-1.pages $S/red-8x4.png 1 1
sh $R $S/three-pages.pages $S/on-2-and-2.pages $S/red-8x4.png 2 2
sh $R $S/three-pages.pages $S/on-3-then-2.pages $S/red-8x4.png 3 2
sh $R $S/three-pages.pages $S/on-1-and-3.pages $S/red-8x4.png 1 3
sh recipes/0372-in-app.sh Pages $S/on-2-and-3.pages "export d to POSIX file \"$PWD/$S/on-2-and-3.pdf\" as PDF"
swift recipes/0482-red-per-page.swift $S/on-2-and-3.pdf
```

Pages reported three pages for each document. In every one, the first picture placed is 1732688 and the second 1732695.

## Observation

### The two records

In all five documents the root (object 1, type 10000) names record 1732278, type 10010, in field 3 and record 1732364, type 10015, in field 20, as it does in `0023/image.pages`.

Record 1732364 (type 10015) always lists the body's text, then the pictures in the order they were placed:

```
1: { 1: 1732539 }   1: { 1: 1732688 }   1: { 1: 1732695 }
```

Record 1732278 (type 10010) has one field-1 entry for each page that has a picture:

| File | Pictures placed on | 10010 field 1 |
| --- | --- | --- |
| `on-2-and-3.pages` | 2, 3 | `{ 1: 1, 4: { 1: { 1: 1732688 } } }`, `{ 1: 2, 4: { 1: { 1: 1732695 } } }` |
| `on-1-and-1.pages` | 1, 1 | `{ 1: 0, 4: { 1: { 1: 1732688 } }, 4: { 1: { 1: 1732695 } } }` |
| `on-2-and-2.pages` | 2, 2 | `{ 1: 1, 4: { 1: { 1: 1732688 } }, 4: { 1: { 1: 1732695 } } }` |
| `on-3-then-2.pages` | 3, then 2 | `{ 1: 1, 4: { 1: { 1: 1732695 } } }`, `{ 1: 2, 4: { 1: { 1: 1732688 } } }` |
| `on-1-and-3.pages` | 1, 3 | `{ 1: 0, 4: { 1: { 1: 1732688 } } }`, `{ 1: 2, 4: { 1: { 1: 1732695 } } }` |

### The pictures' positions

Both pictures in `on-2-and-3.pages` are at about the same place, 1.1.1 = (286.8, 397.71) and (286.8, 397.51), the middle of an A4 page (595.28 × 841.89). In the PDF, page 2 has red at (286.8, 397.5)–(295.0, 401.8) and page 3 at (286.8, 397.2)–(295.0, 401.5), in points from each page's top-left corner. Page 1 has none.

## Conclusion

Type 10010 is the list of the pages that have objects placed on them. Each entry of its field 1 is one page: 1.1 is the page's number, counting from 0 for the document's first page, and each 1.4 names one object on it (4.1.1). A page with no placed object has no entry, so page 1 of `on-2-and-3.pages` is missing. Entries are in page order, whatever order the objects were placed in. Objects on the same page share one entry, with one field 4 each, in the order they were placed.

Type 10015 stays a single list for the whole document, whatever page an object is on: the body's text and every placed object, back to front ([0425](0425-writing-stacking-order.md)). An object on page 3 is in it like one on page 1, and the body's text is first in a document made by placing objects on a page.

An object's position (drawable field 1.1.1) is measured from the top-left corner of its own page, not of the document: both pictures sit at y ≈ 397.6 though one is a page lower.

The root (type 10000) names the 10010 record in field 3 and the 10015 record in field 20.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `three-pages.pages` | `0002/hello.pages` | Only `2001#1732539 3: "hello" → "one\u0005two\u0005three"` | *Control*: the input, three pages and no picture |
| `on-2-and-3.pages` | `three-pages.pages` | `10010#1732278 1.1 = 1`, `10010#1732278 1.1 = 2`, `10010#1732278 1.1 ≠ 0`, `10015#1732364 1.1 = 1732695`, `10000 3.1 = 1732278`, `10000 20.1 = 1732364` | *Likely*: one 10010 entry per page with an object, numbered from 0; one 10015 list for every page |
| `on-1-and-1.pages` | `on-2-and-3.pages` | `10010#1732278 1: ×2 → ×1`, `10010#1732278 1.4: ×2 → ×2`, `10010#1732278 1.1: 1 → 0` | *Likely*: two objects on one page share an entry, with a field 4 each |
| `on-2-and-2.pages` | `on-1-and-1.pages` | `10010#1732278 1.1: 0 → 1` | *Likely*: page 2 is numbered 1 |
| `on-3-then-2.pages` | `on-2-and-3.pages` | `10010#1732278 1: changed`, `10010#1732278 1.1 = 1`, `10010#1732278 1.1 = 2` | *Likely*: entries are in page order, not the order objects were placed |
| `on-1-and-3.pages` | `on-2-and-3.pages` | `10010#1732278 1.1: 1 → 0`, `10010#1732278 1.1 ≠ 1` | *Likely*: a page between two pages with objects has no entry |
| `0023/image.pages` | `on-1-and-1.pages` | `10000 3.1 = 1732278`, `10000 20.1 = 1732364`, `10010#1732278 1.1 = 0` | *Confirmed*: the root names 10010 in field 3 and 10015 in field 20, in 15.4 as in 16.0 |

## Confidence

*Confirmed*: the root's field 3 names the type-10010 record and field 20 the type-10015 record (this experiment and [0023](0023-an-image.md)). The page numbers, the position measured from the object's own page and the page order of the entries are confirmed by writing them in [0484](0484-writing-an-object-s-page.md), and the numbering across sections in [0486](0486-page-numbers-across-sections.md).

*Likely*: the rest of the reading of type 10010 above, and that 10015 is one list for the whole document.
