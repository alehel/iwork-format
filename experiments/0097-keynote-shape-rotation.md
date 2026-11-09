# 0097: Rotating a shape in Keynote

**Status:** run

[0056](0056-image-rotation.md) found an image's rotation in field 1.1.4 in Pages. This experiment rotates a shape in Keynote.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0098](0098-keynote-shape-opacity.md) (the same shape at a different opacity) |

## Recipe

```bash
mkdir -p samples/0097
osascript recipes/0096-keynote-objects.applescript "$PWD/samples/0097/rotation.key" rotation
```

## Observation

The recipe makes a shape on slide 1 and sets its `rotation` to 45. Reading the file back through AppleScript gives a rotation of 45. The shape's record (type 2011) has geometry field 1.1.4 = 45.0, where the unrotated shape of 0098 has 0. The slide also has a second type-2011 record, the theme's own shape, which is not rotated.

## Conclusion

Geometry field 1.1.4 is the rotation in degrees for shapes in Keynote too, as for images and lines in Pages.

## Confidence

*Confirmed*: geometry field 1.1.4 is the rotation in degrees ([0056](0056-image-rotation.md) in Pages and this experiment in Keynote).
