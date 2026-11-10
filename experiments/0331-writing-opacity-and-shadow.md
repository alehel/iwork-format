# 0331: Writing a shape's opacity and shadow, measured on the page

**Status:** run

A shape style's opacity was read as 1.11.3 ([0098](0098-keynote-shape-opacity.md)), and its shadow as 1.11.4: colour (1), angle in degrees with y down, 90 for a shadow below (2), offset in points (3), blur (4), opacity (5) and whether it is shown (6) ([0251](0251-shape-shadow.md), [0278](0278-shadow-angle.md)). This experiment writes both into a shape's style and measures the drawn page.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0330/written.pages`: a red 100 × 100 shape at (300, 300) with a black 15-point stroke, style record 1732710 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0331
R=recipes/0302-set-path.py
python3 -I $R samples/0330/written.pages samples/0331/half.pages 1732710 1.11.3 float 0.5
python3 -I $R samples/0330/written.pages samples/0331/shadow.pages 1732710 \
  1.11.4.1.1 varint 1 1.11.4.1.3 float 0 1.11.4.1.4 float 0 1.11.4.1.5 float 0 1.11.4.1.6 float 1 \
  1.11.4.2 float 90 1.11.4.3 float 20 1.11.4.4 float 0 1.11.4.5 float 1 1.11.4.6 varint 1
```

The shadow is black, straight down, 20 points away, unblurred and opaque. Each file was opened in Pages on its own and exported as PDF; the page was drawn at 4 pixels per point and the column through the shape's centre measured.

## Observation

| File | Centre (sRGB) | Column through the centre | At y = 415 |
| --- | --- | --- | --- |
| `samples/0330/written.pages` | 1, 0, 0 | 292.5 – 407.5 | white |
| `half.pages` (1.11.3 = 0.5) | 1, 0.57, 0.50 | 292.5 – 407.5 | white |
| `shadow.pages` | 1, 0, 0 | 292.5 – 428.5 | black |

## Conclusion

1.11.3 is the shape's opacity: at 0.5 the red is half see-through over the white page, close to the plain mix of 1, 0.5, 0.5. 1.11.4 is the shadow: with angle 90 and offset 20 it is drawn 20 points below the shape, extending its ink from 407.5 to 428.5 (the shadow of the stroke's outer edge, 21 points down with rounding), and with blur 0 and opacity 1 it is solid black.

## Confidence

*Confirmed*: shape opacity 1.11.3 and the shadow's colour, angle, offset, blur, opacity and switch, by writing them and measuring.
