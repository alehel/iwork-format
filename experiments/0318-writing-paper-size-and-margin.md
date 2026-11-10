# 0318: Writing the paper size and a margin

**Status:** run

Pages' document root (object 1) was read as holding the paper width and height in fields 30 and 31 and the left, right, top and bottom margins in 32 to 35, all in points ([0027](0027-document-roots.md), [0028](0028-margins.md)). AppleScript can't read either, so this experiment writes them and measures the PDF that Pages exports.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0002/hello.pages`: A4 (595.28 × 841.89) with 2 cm (56.69-point) margins and the word `hello` |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0318
cp samples/0002/hello.pages samples/0318/original.pages
python3 -I recipes/0302-set-path.py samples/0318/original.pages samples/0318/letter.pages 1 30 float 612 31 float 792
python3 -I recipes/0302-set-path.py samples/0318/original.pages samples/0318/margin.pages 1 32 float 150
```

Pages opened each file on its own and exported it as PDF. The PDFs' `MediaBox` gives the page size; rendering each page and finding the leftmost dark pixel gives where the text starts.

## Observation

| File | PDF page | Text starts at |
| --- | --- | --- |
| `original.pages` | 595.28 × 841.89 | 57 pt |
| `letter.pages` | 612 × 792 | |
| `margin.pages` | | 151 pt |

## Conclusion

Root fields 30 and 31 set the paper size, and 32 the left margin, as floats in points; Pages lays out the page from them as written. The word's first ink is about a point inside the margin, from the letter's side bearing.

## Confidence

*Confirmed*: fields 30, 31 and 32 of Pages' document root, by writing them.
