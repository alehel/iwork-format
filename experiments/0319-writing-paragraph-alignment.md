# 0319: Writing paragraph alignment, measured on the page

**Status:** run

A paragraph style's alignment was read as property 12.1: 0 left, 1 right, 2 centred, 3 justified, and 4, the Body style's value, probably natural ([0010](0010-alignment.md), [0011](0011-left-alignment.md)). This experiment writes 1 and 2 into the Body style and measures where Pages puts the text on the exported page, with a measuring tool that later experiments reuse.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0005/two-lf.pages`: the paragraphs `one` and `two` in the Body style (record 1731511, 12.1 = 4), on A4 with 56.69-point margins |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |
| Measuring | [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift): draws a PDF's first page at 4 pixels per point and reports each line of ink, in points from the top-left corner |

## Recipe

```bash
mkdir -p samples/0319
cp samples/0005/two-lf.pages samples/0319/original.pages
for v in 1 2; do
  python3 -I recipes/0302-set-path.py samples/0319/original.pages samples/0319/align-$v.pages 1731511 12.1 varint $v
done
swift recipes/0319-measure-pdf.swift samples/0319/*.pdf
```

Each file was opened in Pages on its own, through Launch Services, and exported as PDF before measuring.

## Observation

| File | Line 1, left to right | Line 2, left to right |
| --- | --- | --- |
| `original.pages` (4) | 57.2 – 74.8 | 57.0 – 74.5 |
| `align-1.pages` (1) | 520.8 – 538.5 | 520.8 – 538.2 |
| `align-2.pages` (2) | 289.0 – 306.8 | 288.8 – 306.2 |

The text area runs from 56.69 to 538.59 points, so its centre is at 297.6.

## Conclusion

12.1 = 1 right-aligns the paragraphs to the right margin, and 2 centres them on the text area: the lines' middles are at 297.9 and 297.5. The Body style's 4 lays out as left in this left-to-right text, which fits natural alignment.

## Confidence

*Confirmed*: paragraph alignment values 1 and 2, by writing them and measuring.
