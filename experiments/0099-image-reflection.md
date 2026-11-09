# 0099: An image reflection

**Status:** run

This experiment gives an image a reflection in Keynote, to find where reflections are stored.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0069](0069-keynote-image.md), `image.key` |

## Recipe

```bash
mkdir -p samples/0099
osascript recipes/0096-keynote-objects.applescript "$PWD/samples/0099/reflection.key" reflection "$PWD/samples/0023/red-8x4.png"
```

## Observation

The recipe places the PNG of 0023 on slide 1, sets `reflection showing` to true and `reflection value` to 40. The image record is unchanged except for its style, now a new unnamed image style (type 3016):

```
10: 1
11: { 4: { 1: 0.4 } }
```

## Conclusion

An image's reflection is field 11.4 of its image style. Its field 1 is the strength, 0.4 for 40 percent. A style without field 11.4 has no reflection, so the field's presence is the switch.

## Confidence

*Likely*: image style field 11.4 is the reflection, with its strength in 11.4.1.
