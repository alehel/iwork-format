# 0070: A skipped slide

**Status:** run

This experiment marks a slide as skipped, so that it isn't shown in a presentation, to find where that is stored.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` |

## Recipe

```bash
mkdir -p samples/0070
osascript recipes/0068-keynote-variants.applescript "$PWD/samples/0070/skipped.key" skipped
```

## Observation

The slide node (type 4) of slide 1 changed field 4 from 0 to 1. The only other change was a number inside the root (object 1) that changes on every save.

## Conclusion

Field 4 of a slide node is 1 when the slide is skipped. A reader that plays or exports a presentation leaves those slides out.

## Confidence

*Likely*: slide node field 4 marks a skipped slide.
