# 0143: A JPEG image

**Status:** run

[0023](0023-an-image.md) placed a PNG. This experiment places a JPEG, to see whether its format is kept.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0023](0023-an-image.md) |

## Recipe

```bash
mkdir -p samples/0143
sips -s format jpeg samples/0023/red-8x4.png --out samples/0143/red-8x4.jpg
osascript recipes/0139-pages-container.applescript image "$PWD/samples/0143/jpeg.pages" "$PWD/samples/0143/red-8x4.jpg"
```

## Observation

The package holds `Data/red-8x4-24.jpg`, 777 bytes, the same size as the JPEG placed.

## Conclusion

A JPEG is stored unchanged with its own extension, as a PNG is. Pages doesn't convert images to one format, so a reader has to handle whatever formats users place.

## Confidence

*Likely*: image files are stored in their original format.
