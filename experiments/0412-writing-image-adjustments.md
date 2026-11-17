# 0412: Writing image adjustments

**Status:** run

Image adjustments are stored twice: as settings in image field 14 (exposure in 14.1 and saturation in 14.2, as fractions), and as a rendered JPEG, `…-filtered-N`, that field 15 names by data ID ([0284](0284-image-adjustments.md)). This experiment removes the rendered copy's reference and changes the settings, and reads the colour Pages draws.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0284/adjusted.pages`: the red PNG of [0023](0023-an-image.md), 200 × 100 at (300, 300), image record 1732665, with exposure +30% and saturation −40% (14.1 = 0.3, 14.2 = −0.4) and field 15 naming `Data/red-8x4-filtered-26.jpeg` |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) and the new [`recipes/0412-drop-field.py`](../recipes/0412-drop-field.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0412
R=recipes/0302-set-path.py
F=samples/0284/adjusted.pages
O=samples/0412
cp $F $O/original.pages
python3 -I recipes/0412-drop-field.py $F $O/no-filtered-copy.pages 1732665 15
python3 -I $R $F $O/exposure-minus.pages 1732665 14.1 float -0.8
python3 -I $R $O/no-filtered-copy.pages $O/exposure-minus-no-copy.pages 1732665 14.1 float -0.8
for f in original no-filtered-copy exposure-minus exposure-minus-no-copy; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0384-pdf-colours.swift $O/$f.pdf 400,350
done
```

## Observation

| File | Field 14.1 | Field 15 | Colour at the image's centre |
| --- | --- | --- | --- |
| `original.pages` | 0.3 | 26 | 0.93, 0.35, 0.36 |
| `no-filtered-copy.pages` | 0.3 | removed | 1, 0, 0 |
| `exposure-minus.pages` | −0.8 | 26 | 0.93, 0.35, 0.36 |
| `exposure-minus-no-copy.pages` | −0.8 | removed | 1, 0, 0 |

The image's position and size are the same in every file.

## Conclusion

Pages draws an adjusted image from the rendered copy that field 15 names: the pale, less saturated red. Without field 15 it draws the original file unadjusted, pure red, and doesn't apply the settings in field 14 when it opens the document, even when they are changed. Field 14 is only what the adjustment controls start from. So a reader should draw the file named in field 15 when there is one, as the spec already advises, and a writer that adjusts an image must render the copy itself.

## Confidence

*Confirmed*: Pages draws an adjusted image from field 15's rendered copy and doesn't apply field 14 on opening, by writing them.
