# 0075: Slide size

**Status:** run

[0038](0038-second-slide.md) found a presentation's slide size, 1920 × 1080, in its field 4. This experiment changes it to 1024 × 768.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` |

## Recipe

```bash
mkdir -p samples/0075
osascript recipes/0068-keynote-variants.applescript "$PWD/samples/0075/size.key" size
```

The recipe sets the document's `width` to 1024 and `height` to 768.

## Observation

- The presentation (type 2) changed field 4 from (1920, 1080) to (1024, 768).
- Every slide node (type 4) changed field 14 from 0 to 1.

## Conclusion

The presentation's field 4 is the slide size in points, as 0038 suggested. Resizing set field 14 on every slide node, which may mark its thumbnail as out of date. A reader should take the size from the presentation, not from the thumbnails.

## Confidence

*Confirmed*: presentation field 4 is the slide size ([0038](0038-second-slide.md) and this experiment).

*Unknown*: slide node field 14.
