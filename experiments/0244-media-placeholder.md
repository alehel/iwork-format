# 0244: A media placeholder

**Status:** run

Templates use images as placeholders that the user replaces by dropping in a picture. Pages can turn any image into one (Format → Advanced → Define as Media Placeholder). This experiment does that, to see how a placeholder image differs from an ordinary one.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0228/caption.pages`, the same image, with a caption |

## Recipe

```bash
mkdir -p samples/0244
osascript recipes/0244-pages-image.applescript "$PWD/samples/0023/red-8x4.png"
```

Then choose Format → Advanced → Define as Media Placeholder (*Format → Avansert → Definer som medieplassholder*) and save as `samples/0244/media-placeholder.pages`.

## Observation

Apart from IDs and the caption, the image record (type 3005) differs from the baseline in one top-level field:

```
7: 0 → 1
```

The image data is still stored, and the image's drawable is unchanged.

## Conclusion

Field 7 of an image record is 1 when the image is a media placeholder. The picture it holds is shown until the user replaces it, so a reader can draw it like any image. Only an editor needs the flag.

## Confidence

*Likely*: image field 7 marks a media placeholder.
