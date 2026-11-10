# 0324: Writing text columns, measured on the page

**Status:** run

[0254](0254-columns.md) found a body's columns in a column style (type 2024), named by the text's field-12 runs: property 11.7.1 holds the number of columns in field 1 and the gap in field 2. This experiment writes two columns into a one-column document and measures the lines on the exported page with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift), which now also lists each line's separate pieces.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0320/long.pages`: one paragraph wrapping to several lines, whose column style is record 1732607, an unnamed child of the `None` column style with no columns of its own |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0324
cp samples/0320/long.pages samples/0324/one.pages
python3 -I recipes/0302-set-path.py samples/0324/one.pages samples/0324/two.pages 1732607 11.7.1.1 varint 2 11.7.1.2 float 0.05
```

The values are those 0254 found for Pages' own two columns. Each file was opened in Pages on its own, exported as PDF and measured.

## Observation

| File | First lines, left to right |
| --- | --- |
| `one.pages` | 57.5 – 506.0 |
| `two.pages` | 57.5 – 279.8 |

The text area is 481.9 points wide. With a gap of 0.05 of that, 24.1 points, each of two columns is 228.9 points wide, so the first column ends at 285.6. The paragraph fits in the first column, so the second stays empty.

## Conclusion

11.7.1.1 is the number of columns and 11.7.1.2 the gap between them, as a fraction of the text area's width; the lines wrap to the first column's width, which these values give.

## Confidence

*Confirmed*: column style 11.7.1, by writing it and measuring.
