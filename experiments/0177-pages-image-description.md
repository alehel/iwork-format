# 0177: An image description in Pages

**Status:** run

[0102](0102-image-description.md) found a Keynote image's description in field 1.8 of its drawable. This experiment sets one in Pages.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0102](0102-image-description.md) |

## Recipe

```bash
mkdir -p samples/0177
osascript recipes/0177-pages-image-description.applescript "$PWD/samples/0177/described.pages" "$PWD/samples/0023/red-8x4.png"
```

## Observation

The image record (type 3005, 1732647) has `a red box` in field 1.8, next to 1.5 (0) and 1.7 (1), as in Keynote.

## Conclusion

Pages and Keynote store an image's description in the same place, field 1.8 of the drawable block. A reader can use it as alternative text in either app's documents.

## Confidence

*Confirmed*: field 1.8 is an image's description ([0102](0102-image-description.md) and this experiment).
