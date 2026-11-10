# 0348: Writing an image's size, measured on the page

**Status:** run

[0055](0055-image-size.md) found an image's size in two places, both changing when the image was resized: the drawable geometry's 1.1.2 and the image's field 4, with its natural size in field 9. This experiment writes a new size into each, and both, and measures the image on the exported page.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0023/image.pages`: the 8 × 4 red PNG on the page at (286.8, 397.6), image record 1732647, with 8 × 4 in 1.1.2, 4 and 9 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0348
cp samples/0023/image.pages samples/0348/original.pages
R=recipes/0302-set-path.py
python3 -I $R samples/0348/original.pages samples/0348/both.pages 1732647 1.1.2.1 float 200 1.1.2.2 float 100 4.1 float 200 4.2 float 100
python3 -I $R samples/0348/original.pages samples/0348/geometry-only.pages 1732647 1.1.2.1 float 200 1.1.2.2 float 100
python3 -I $R samples/0348/original.pages samples/0348/field4-only.pages 1732647 4.1 float 200 4.2 float 100
```

Each file was opened in Pages on its own and exported as PDF; the page was drawn at 2 pixels per point and the box around its red pixels measured.

## Observation

| File | Red area |
| --- | --- |
| `original.pages` | 8.5 × 4.5 at 287.0, 397.5 |
| `both.pages` | 200.5 × 100.5 at 287.0, 397.5 |
| `geometry-only.pages` (1.1.2) | 200.5 × 100.5 at 287.0, 397.5 |
| `field4-only.pages` (4) | 8.5 × 4.5 at 287.0, 397.5 |

The extra half point is the pixel grid.

## Conclusion

The geometry's 1.1.2 decides the size an image is drawn at, scaling the image to fill it. The image's field 4 doesn't change the drawing; Pages keeps it equal to 1.1.2, so a writer should set both.

## Confidence

*Confirmed*: 1.1.2 is the drawn size, by writing it and measuring.

*Unknown*: what field 4 is used for, if anything.
