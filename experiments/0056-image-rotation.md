# 0056: Rotating an image

**Status:** run

[0051](0051-line.md) found a rotation of 333.43° in a line's geometry (field 1.1.4), but couldn't say which way rotation is measured. This experiment rotates an image by a known angle.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0023](0023-an-image.md), `image.pages` |

## Recipe

```bash
mkdir -p samples/0056
osascript recipes/0055-pages-image-property.applescript "$PWD/samples/0056/rotation.pages" "$PWD/samples/0023/red-8x4.png" rotation
```

The recipe places the PNG of 0023 and sets its `rotation` to 30.

## Observation

The image record's geometry field 1.1.4 is 30.0, where 0023 has 0. Nothing else in the record changed, including the position and size.

## Conclusion

Geometry field 1.1.4 holds the same angle as AppleScript's `rotation`, in degrees. The line of 0051 runs from (100, 100) down to the right to (300, 200). That is a clockwise turn on the page, with y pointing down, and it was stored as 333.43, which is −26.57. So a positive angle turns the object counter-clockwise as seen on the page. Position and size stay those of the unrotated object.

## Confidence

*Likely*: geometry field 1.1.4 is the rotation in degrees, counter-clockwise on the page, about the object's centre.
