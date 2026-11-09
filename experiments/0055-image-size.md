# 0055: Resizing an image

**Status:** run

[0023](0023-an-image.md) found three 8 × 4 sizes in an image record: field 1.1.2, field 4 and field 9. This experiment resizes the image to tell them apart.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0023](0023-an-image.md), `image.pages` |

## Recipe

```bash
mkdir -p samples/0055
osascript recipes/0055-pages-image-property.applescript "$PWD/samples/0055/size.pages" "$PWD/samples/0023/red-8x4.png" size
```

The recipe places the 8 × 4 PNG of 0023 on page 1, then sets its `width` to 80 and `height` to 40.

## Observation

Compared with 0023, the image record (type 3005) differs only in two places, both changing from 8 × 4 to 80 × 40:

- field 1.1.2, the size in the geometry
- field 4

Field 9 is still 8 × 4, and the position (1.1.1) is unchanged.

## Conclusion

An image's field 9 is its natural size: the size of the image file, in pixels taken as points. Fields 1.1.2 and 4 are the size it is drawn at. Why the drawn size is stored twice isn't known. Field 4 may be the size before cropping by the mask path in field 19.

## Confidence

*Likely*: image field 9 is the natural size, and 1.1.2 and 4 are the displayed size.

*Unknown*: how fields 4 and 1.1.2 differ.
