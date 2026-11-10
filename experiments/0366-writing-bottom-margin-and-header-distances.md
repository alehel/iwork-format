# 0366: Writing the bottom margin and the header and footer distances

**Status:** run

The document root's fields 35, 36 and 37 are the bottom margin and the header's and footer's distance from the page edge, in points ([0027](0027-document-roots.md), [0028](0028-margins.md)). The other margins were confirmed by writing them in [0318](0318-writing-paper-size-and-margin.md) and [0326](0326-writing-top-and-right-margins.md). This experiment writes these three into a document with a header, a footer and three pages of body text, and measures the first page of each PDF with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift).

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0327/header.pages`: an A4 page (595.28 × 841.89) with 56.69-point margins, header distance 35.43 and footer distance 42.52, a header (LEFT, RIGHT) and a footer (FOOT) |
| Writer | The writer of [0287](0287-rewriting-a-document.md) and [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0366
R=recipes/0302-set-path.py
python3 -I recipes/0287-iwa-writer.py samples/0327/header.pages samples/0366/base.pages \
  --text 1732539 "$(python3 -c "print('\n'.join(f'line {i}' for i in range(1,61)), end='')")"
python3 -I $R samples/0366/base.pages samples/0366/header-72.pages 1 36 float 72
python3 -I $R samples/0366/base.pages samples/0366/footer-72.pages 1 37 float 72
python3 -I $R samples/0366/base.pages samples/0366/bottom-200.pages 1 35 float 200
```

Each file was opened in Pages on its own and exported as PDF. Each has three pages.

## Observation

Positions are in points from the top of the first page. Body lines are 24.8 points apart.

| File | Header ink top | First body line top | Body lines | Last body line top | Footer ink bottom |
| --- | --- | --- | --- | --- | --- |
| `base.pages` | 37.8 | 59.2 | 29 | 751.8 | 797.0 |
| `header-72.pages` | 74.2 | 88.2 | 28 | 756.0 | 797.0 |
| `footer-72.pages` | 37.8 | 59.2 | 28 | 727.0 | 767.5 |
| `bottom-200.pages` | 37.8 | 59.2 | 24 | 628.0 | 797.0 |

## Conclusion

Field 36 sets the header's distance from the top edge: going from 35.43 to 72 moves the header's ink down 36.4 points. Field 37 sets the footer's distance from the bottom edge: going from 42.52 to 72 moves the footer's ink up 29.5 points, against 29.48 written. Field 35 is the bottom margin: at 200 the body stops above 841.89 − 200 = 641.89, after 24 lines. A header or footer that reaches past the top or bottom margin pushes the body away. With the header 72 points down, the body starts below it at 88.2, not at the margin. With the footer 72 points up, the body loses a line.

## Confidence

*Confirmed*: field 35 as the bottom margin, and fields 36 and 37 as the header and footer distances, by writing them.
