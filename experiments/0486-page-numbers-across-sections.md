# 0486: Page numbers across sections and facing pages

**Status:** run

Type 10010 numbers the pages that have placed objects from 0 at the start of the document ([0482](0482-objects-on-later-pages.md)). This experiment checks whether a section break, a different first page, or different left and right pages change that numbering.

## Setup

| | |
| --- | --- |
| Pages | 16.0 (7052.0.68) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-28 |
| Input | `samples/0002/hello.pages`, written as below |
| Recipe | [`recipes/0287-iwa-writer.py`](../recipes/0287-iwa-writer.py) and [`recipes/0300-set-field.py`](../recipes/0300-set-field.py) write the inputs; [`recipes/0482-place-on-pages.sh`](../recipes/0482-place-on-pages.sh) places the red picture of [0023](0023-an-image.md) on pages 2 and 3; [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) exports, and [`recipes/0482-red-per-page.swift`](../recipes/0482-red-per-page.swift) checks the PDF |

## Recipe

```bash
mkdir -p samples/0486
S=$PWD/samples/0486
I=samples/0482/red-8x4.png
python3 -I recipes/0287-iwa-writer.py samples/0002/hello.pages $S/section-break.pages \
  --text 1732539 "$(printf 'one\005two\004three')"
sh recipes/0482-place-on-pages.sh $S/section-break.pages $S/section-on-2-and-3.pages $I 2 3
python3 -I recipes/0300-set-field.py samples/0482/three-pages.pages $S/tmp.pages 10011 18=1 19=1
python3 -I recipes/0300-set-field.py $S/tmp.pages $S/facing-three-pages.pages 10012 34=1
rm $S/tmp.pages
sh recipes/0482-place-on-pages.sh $S/facing-three-pages.pages $S/facing-on-2-and-3.pages $I 2 3
for f in section-on-2-and-3 facing-on-2-and-3; do
  cp $S/$f.pages $S/tmp.pages
  sh recipes/0372-in-app.sh Pages $S/tmp.pages "export d to POSIX file \"$S/$f.pdf\" as PDF"
  swift recipes/0482-red-per-page.swift $S/$f.pdf
done
rm $S/tmp.pages
```

`section-break.pages` has a page break between `one` and `two` and a section break (U+0004) between `two` and `three`. Pages made the second section on opening it, as in [0361](0361-writing-a-section-break.md): in `section-on-2-and-3.pages`, the body's section runs (field 17) point at section 1732660 from 0 and section 1732682 from 8, the start of `three`. `facing-three-pages.pages` has facing pages on (type-10012 field 34) and, in its one section, a different first page (field 18) and different left and right pages (field 19) ([0017](0017-section-switches.md)).

## Observation

| File | Pages | 10010 field 1 | Red drawn on |
| --- | --- | --- | --- |
| `section-on-2-and-3.pages` | 3, `three` alone in the second section | `{ 1: 1, … 1732732 }`, `{ 1: 2, … 1732739 }` | pages 2 and 3 |
| `facing-on-2-and-3.pages` | 3 | `{ 1: 1, … 1732688 }`, `{ 1: 2, … 1732695 }` | pages 2 and 3 |

Both are the same as without the section break or the switches ([0482](0482-objects-on-later-pages.md)): the first page of the second section is page 2, not 0, and the left page (page 2) and the right page (page 3) are numbered as any other. The pictures are at the same place on each page as in `0482/on-2-and-3.pdf`.

## Conclusion

The page number in type 10010 counts every page of the document from 0. It doesn't restart in a new section, and it doesn't depend on a different first page or on left and right pages.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `section-break.pages` | `0482/three-pages.pages` | Only `2001#1732539 3: "one\u0005two\u0005three" → "one\u0005two\u0004three"` | *Control*: the input, with a section break before `three` |
| `section-on-2-and-3.pages` | `0482/on-2-and-3.pages` | `2001#1732539 17.1: ×1 → ×2`, `records 10011: 1 → 2`, `10010#1732278 1.1 = 1`, `10010#1732278 1.1 = 2` | *Confirmed*: page numbers run on across a section break |
| `facing-three-pages.pages` | `0482/three-pages.pages` | Only `10011#1732296 18: 0 → 1`, `10011#1732296 19: 0 → 1`, `10012#1732614 34: 0 → 1` | *Control*: the input, with facing pages, a different first page and different left and right pages |
| `facing-on-2-and-3.pages` | `0482/on-2-and-3.pages` | `10011#1732296 18: 0 → 1`, `10011#1732296 19: 0 → 1`, `10010#1732278 1.1 = 1`, `10010#1732278 1.1 = 2` | *Confirmed*: these switches don't change the numbering |

## Confidence

*Confirmed*: page numbers in type 10010 count from the start of the document, whatever its sections and page switches, with [0482](0482-objects-on-later-pages.md) and [0484](0484-writing-an-object-s-page.md).
