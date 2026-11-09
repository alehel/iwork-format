# 0284: Image adjustments

**Status:** run

Pages can adjust an image's exposure and saturation in the Image tab, without changing the original file. This experiment sets both, to see whether Pages stores the settings, an adjusted copy, or both.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0244/media-placeholder.pages`, the same image, unadjusted |

## Recipe

```bash
mkdir -p samples/0284
osascript recipes/0244-pages-image.applescript "$PWD/samples/0023/red-8x4.png"
```

The new image is left selected. Then, with Pages in front, open the Image tab (*Bilde*), type 30 into Exposure (*Eksponering*) and −40 into Saturation (*Metning*), and save as `samples/0284/adjusted.pages`. The red image turns a paler pink.

## Observation

The package holds the original `Data/red-8x4-24.png` and a new `Data/red-8x4-filtered-26.jpeg` (787 bytes). The image record (type 3005) gains:

```
14: { 1: 0.3, 2: -0.4, 13: 0, 14: 0 }
15: { 1: 26 }       ← the data ID of the filtered JPEG
```

(Its field 7 differs from the baseline only because the baseline is a media placeholder.)

## Conclusion

Adjustments are stored twice:

- **As settings, in image field 14:** exposure in 14.1 and saturation in 14.2, as fractions (30% is 0.3 and −40% is −0.4).
- **As a rendered copy:** a JPEG named `…-filtered-N`, which field 15 points at.

The original image is kept, so the adjustments can be undone. A reader that can't apply filters should draw the filtered copy named in field 15, which is what Pages shows. The other adjustments the sidebar can reveal are probably further fields of 14.

## Confidence

*Likely*:

- Image field 14 holds the adjustments as fractions.
- Field 15 names a pre-rendered filtered copy.
