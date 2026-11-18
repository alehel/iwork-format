# 0446: Writing a removed background

**Status:** run

Remove Background leaves the image file alone: image field 10 holds the subject's outline as a path in the image's pixels, field 22 is 1, and a mask crops to the subject ([0285](0285-removed-background.md)). The image record also has a field 19 that experiment didn't describe. This experiment removes these fields, alone and together, and reads the colours over a blue page.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0285/no-background.pages`: a 64 × 48 PNG, white with a red square in its middle, drawn 133.3 × 100 at (300, 300), with its background removed. Image record 1732665 has field 5 (the mask), 10 (the outline), 19 (84 bytes) and 22 = 1. The stored PNG is byte for byte the original, white and all |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) for a blue page background ([0328](0328-writing-a-page-background.md)) and [`recipes/0412-drop-field.py`](../recipes/0412-drop-field.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0446
O=samples/0446
D=recipes/0412-drop-field.py
python3 -I recipes/0302-set-path.py samples/0285/no-background.pages $O/blue.pages 1732296 \
  30.1.1 varint 1 30.1.3 float 0 30.1.4 float 0 30.1.5 float 1.0 30.1.6 float 1.0
for fields in "5" "19" "10 19 22" "5 10" "5 19" "5 22" "5 10 19" "5 19 22" "5 10 19 22"; do
  n=no-$(echo $fields | tr ' ' '-')
  python3 -I $D $O/blue.pages $O/$n.pages 1732665 $fields
done
for f in $O/*.pages; do
  sh recipes/0372-in-app.sh Pages $f "export d to POSIX file \"$PWD/${f%.pages}.pdf\" as PDF"
  swift recipes/0384-pdf-colours.swift ${f%.pages}.pdf 310,310 366,350 420,390
done
```

The page is made blue so that a white background shows. (310, 310) and (420, 390) are inside the image but outside its red square; (366, 350) is in the square.

## Observation

| File | Fields removed | (310, 310) | (366, 350) | (420, 390) |
| --- | --- | --- | --- | --- |
| `blue.pages` | none | blue | red | blue |
| `no-5.pages` | the mask | blue | red | blue |
| `no-19.pages` | 19 | blue | red | blue |
| `no-10-19-22.pages` | 10, 19, 22 | blue | red | blue |
| `no-5-19.pages`, `no-5-22.pages`, `no-5-19-22.pages` | the mask, and 19 or 22 or both | blue | red | blue |
| `no-5-10.pages`, `no-5-10-19.pages` | the mask and 10 | white | red | white |
| `no-5-10-19-22.pages` | all four | white | red | white |

## Conclusion

Two things hide a removed background, each enough on its own. Field 10, the subject's outline, clips the image to the subject: with it, the white around the square isn't drawn even without the mask. The mask crops the image to the subject's box: with it, the background is gone even without the outline. Fields 19 and 22 change nothing drawn: 22 is probably the switch the app shows, and 19 is in ordinary images too ([0447](0447-writing-an-image-s-sizes.md)'s has one), so it isn't part of the removed background. The image file keeps its background, so a reader must apply the outline in field 10, or at least the mask, to draw what Pages draws.

## Confidence

*Confirmed*: image field 10 clips the image to its outline and the mask crops it, each alone hiding the background, while 19 and 22 don't change the drawing, by writing them. What field 19 holds is *unknown*.
