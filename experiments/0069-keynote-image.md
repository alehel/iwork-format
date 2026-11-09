# 0069: An image in Keynote

**Status:** run

This experiment places the 8 × 4 image of [0023](0023-an-image.md) on a Keynote slide, to compare Keynote's image records and data files with Pages'.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key`; experiment [0023](0023-an-image.md) |

## Recipe

```bash
mkdir -p samples/0069
osascript recipes/0068-keynote-variants.applescript "$PWD/samples/0069/image.key" image "$PWD/samples/0023/red-8x4.png"
```

## Observation

- The slide's part gained a record of type 3005 with the position (956, 538), the size 8 × 4, and field 1.2 naming the slide.
- The package gained `Data/red-8x4-9076.png`, 75 bytes.

## Conclusion

Keynote stores images exactly as Pages does: an image record of type 3005 and the unchanged file under `Data/`, named after the original with `-N` added. Here N is 9076, the next data ID after the theme's images. Keynote placed the image in the middle of the 1920 × 1080 slide.

## Confidence

*Likely*: image records (type 3005) and data files are shared between Pages and Keynote.
