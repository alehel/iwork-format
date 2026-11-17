# 0405: Writing a shape's size

**Status:** run

A drawable's size is in its geometry, 1.1.2, *confirmed* by writing an image's size in Keynote ([0303](0303-writing-geometry.md), [0348](0348-writing-an-image-size.md)). But a mask and a line are drawn at their path's natural size, whatever their box says ([0390](0390-writing-an-image-mask.md), [0404](0404-writing-a-line-length.md)). This experiment writes the two sizes of an ordinary shape with a path.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0218/oval.pages`: oval 1732657, 100 × 100 at (247.6, 68.7), its box in 1.1.1.2 and its path's natural size in 1.3.5.2 both 100 × 100 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and measured with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift) |

## Recipe

```bash
mkdir -p samples/0405
R=recipes/0302-set-path.py
F=samples/0218/oval.pages
O=samples/0405
cp $F $O/original.pages
python3 -I $R $F $O/box-200.pages 1732657 1.1.1.2.1 float 200
python3 -I $R $F $O/natural-200.pages 1732657 1.3.5.2.1 float 200
python3 -I $R $F $O/both-200.pages 1732657 1.1.1.2.1 float 200 1.3.5.2.1 float 200
for f in original box-200 natural-200 both-200; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
return {width of shape 1 of d, height of shape 1 of d}"
done
swift recipes/0319-measure-pdf.swift $O/*.pdf
```

## Observation

| File | Box width | Natural width | `width` × `height` | Oval's ink, left – right | Body text's line |
| --- | --- | --- | --- | --- | --- |
| `original.pages` | 100 | 100 | 100 × 100 | 248.0 – 347.8 | top 58.0 |
| `box-200.pages` | 200 | 100 | 100 × 100 | 248.0 – 347.8 | top 58.0 |
| `natural-200.pages` | 100 | 200 | 200 × 100 | 248.0 – 447.8 | top 182.0 |
| `both-200.pages` | 200 | 200 | 200 × 100 | 248.0 – 447.8 | top 182.0 |

## Conclusion

A shape with a path is drawn at its path's natural size, 1.3.5.2: writing 200 there made the oval 200 wide, and Pages reports that width and wraps the body text around it (the text moved below the wider oval). The box's size in 1.1.1.2 isn't used for drawing: written alone it changed nothing. So the rule found for masks and lines holds for every shape with a path: place it by the box's position and rotation, size it by the path. Images, which have no path, take their size from the box. A writer should keep the two sizes equal, as Pages does.

## Confidence

*Confirmed*: a shape's drawn size as its path's natural size, not its box's, by writing each.
