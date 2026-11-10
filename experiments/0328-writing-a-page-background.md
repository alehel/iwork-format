# 0328: Writing a section's page background

**Status:** run

[0286](0286-section-background.md) found a section's page background in field 30 of the section (type 10011): a fill, like a shape's, whose field 1 is a colour. This experiment writes one into a blank document and samples the exported page.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0002/hello.pages`, whose section (record 1732296) has no field 30 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0328
python3 -I recipes/0302-set-path.py samples/0002/hello.pages samples/0328/background.pages 1732296 \
  30.1.1 varint 1 30.1.3 float 0.6 30.1.4 float 0.8 30.1.5 float 1.0 30.1.6 float 1.0
```

The colour message is laid out as in other colours: 1 = 1 for RGB, then red, green, blue and alpha. Pages opened the file on its own, exported it as PDF and saved it again; the PDF's first page was drawn and the pixel near its top-left corner read in sRGB, along with the same pixel of the unchanged document's PDF from [0318](0318-writing-paper-size-and-margin.md).

## Observation

| PDF | Corner pixel (sRGB) |
| --- | --- |
| Unchanged document | 1.00, 1.00, 1.00 |
| `background.pages` | 0.60, 0.80, 1.00 |

## Conclusion

Section field 30.1 is the page's background colour, and Pages fills the whole page with it, out to the edges. The colour comes out on the page with exactly the components written, read in sRGB. That supports [0309](0309-writing-a-cell-colour.md)'s finding that colours are stored as sRGB, from the drawn page this time rather than from AppleScript.

## Confidence

*Confirmed*: section field 30 as the page background, by writing it; colours are sRGB components (five colours matched).
