# 0330: Writing a shape's fill and stroke, measured on the page

**Status:** run

A shape style keeps its properties one level deeper than text styles, in field 1.11: 1.11.1.1 is the fill colour ([0077](0077-shape-fill.md)) and 1.11.2 the stroke, with its width in 1.11.2.2 ([0250](0250-shape-border.md)). This experiment writes a fill and a wider stroke into a shape's style and measures the shape on the exported page.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0250/border.pages`: a 100 × 100 shape at (300, 300) whose own style, record 1732710, holds only a black 5-point stroke; its fill, black, comes from the parent style |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0330
cp samples/0250/border.pages samples/0330/original.pages
python3 -I recipes/0302-set-path.py samples/0330/original.pages samples/0330/written.pages 1732710 \
  1.11.1.1.1 varint 1 1.11.1.1.3 float 1 1.11.1.1.4 float 0 1.11.1.1.5 float 0 1.11.1.1.6 float 1 \
  1.11.2.2 float 15
```

A first attempt wrote the same values at 11.1 and 11.2, without the leading 1, and nothing changed: the shape style's properties really are under field 1. Each file was opened in Pages on its own and exported as PDF; the page was drawn at 4 pixels per point, the pixel at the shape's centre read, and the inked extent of the row through the centre measured.

## Observation

| File | Centre (sRGB) | Row through the centre |
| --- | --- | --- |
| `original.pages` | 0, 0, 0 | 297.8 – 402.8 |
| `written.pages` | 1, 0, 0 | 292.8 – 407.8 |

## Conclusion

1.11.1.1 is the shape's fill colour and 1.11.2.2 its stroke width in points. The stroke is centred on the outline, so a 15-point stroke reaches 7.5 points outside the 300 – 400 box, against 2.5 for the original 5 points. Writing into the shape's own unnamed style changes only that shape.

## Confidence

*Confirmed*: shape style 1.11.1.1 (fill colour) and 1.11.2.2 (stroke width), by writing them and measuring.
