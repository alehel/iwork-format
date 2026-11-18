# 0447: Writing an image's three sizes

**Status:** run

An image record holds three sizes: its geometry's size in 1.1.2, field 4, and field 9, its natural size. Fields 1.1.2 and 4 both seemed to be the size it is drawn at ([0055](0055-image-size.md)); writing them showed that 1.1.2 alone decides and field 4 is a copy ([0303](0303-writing-geometry.md), [0348](0348-writing-an-image-size.md)). This experiment repeats that in Pages and adds field 9.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0023/image.pages`: a red 8 × 4 PNG, image record 1732647, at (286.8, 397.6), with 1.1.2, 4 and 9 all 8 × 4 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and drawn with [`recipes/0373-draw-pdf.swift`](../recipes/0373-draw-pdf.swift) |

## Recipe

```bash
mkdir -p samples/0447
R=recipes/0302-set-path.py
F=samples/0023/image.pages
O=samples/0447
cp $F $O/original.pages
python3 -I $R $F $O/geometry-80.pages 1732647 1.1.2.1 float 80 1.1.2.2 float 40
python3 -I $R $F $O/field4-80.pages 1732647 4.1 float 80 4.2 float 40
python3 -I $R $F $O/field9-80.pages 1732647 9.1 float 80 9.2 float 40
python3 -I $R $F $O/both-80.pages 1732647 1.1.2.1 float 80 1.1.2.2 float 40 4.1 float 80 4.2 float 40
for f in original geometry-80 field4-80 field9-80 both-80; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
return {width of image 1 of d, height of image 1 of d}"
  swift recipes/0373-draw-pdf.swift $O/$f.pdf 280 390 120 60 1
done
```

The red area's extent was read from each drawing.

## Observation

| File | Written as 80 × 40 | `width`, `height` | Red drawn, x and y |
| --- | --- | --- | --- |
| `original.pages` | | 8, 4 | 287–295, 397–402 |
| `geometry-80.pages` | 1.1.2 | 80, 40 | 287–367, 397–438 |
| `field4-80.pages` | field 4 | 8, 4 | 287–295, 397–402 |
| `field9-80.pages` | field 9 | 8, 4 | 287–295, 397–402 |
| `both-80.pages` | 1.1.2 and field 4 | 80, 40 | 287–367, 397–438 |

## Conclusion

An image is drawn at the size in its geometry, 1.1.2, as in Keynote. Field 4, though it equals that size in every file Pages saved, isn't used for drawing, and neither is field 9, the natural size. Field 4 is probably the size the image had when its frame was last set, kept for the app's own use, as in 0446's image, whose field 4 was its full size. A reader should draw images by 1.1.2, and a writer should keep field 4 equal to it.

## Confidence

*Confirmed*: an image's drawn size as its geometry's 1.1.2, again, and that field 9 isn't used for drawing either, by writing each.
