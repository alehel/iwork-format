# 0102: An image's description

**Status:** run

Keynote lets an image carry a description for screen readers. This experiment sets one, to find where it is stored.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0069](0069-keynote-image.md), `image.key` |

## Recipe

```bash
mkdir -p samples/0102
osascript recipes/0096-keynote-objects.applescript "$PWD/samples/0102/description.key" description "$PWD/samples/0023/red-8x4.png"
```

## Observation

The recipe places the PNG of 0023 on slide 1 and sets its `description` to `red bar`. The image record gained one field in its drawable block:

```
1.8: text "red bar"
```

## Conclusion

An object's accessibility description is text in field 1.8 of its drawable block. A reader that produces accessible output, such as alternative text in HTML, can take it from there.

## Confidence

*Likely*: drawable field 1.8 is the accessibility description.
