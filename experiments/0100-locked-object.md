# 0100: A locked object

**Status:** run

This experiment locks an image in Keynote, to find where locking is stored.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0069](0069-keynote-image.md), `image.key` |

## Recipe

```bash
mkdir -p samples/0100
osascript recipes/0096-keynote-objects.applescript "$PWD/samples/0100/locked.key" locked "$PWD/samples/0023/red-8x4.png"
```

## Observation

The recipe places the PNG of 0023 on slide 1 and sets `locked` to true. The image record (type 3005) changed field 1.5 from 0 to 1, in the drawable block that also holds the geometry. Nothing else changed.

## Conclusion

Field 1.5 of a drawable block is 1 for a locked object. Since the block is shared by images, shapes and tables, it presumably works the same for all of them. A reader that only displays a document can ignore it.

## Confidence

*Likely*: drawable field 1.5 is the lock.
