# 0098: A shape's opacity

**Status:** run

[0057](0057-image-opacity.md) found an image's opacity in its image style, field 11.2. This experiment changes a shape's opacity in Keynote, to see where shape styles keep it.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0097](0097-keynote-shape-rotation.md) (the same shape at full opacity) |

## Recipe

```bash
mkdir -p samples/0098
osascript recipes/0096-keynote-objects.applescript "$PWD/samples/0098/opacity.key" opacity
```

## Observation

The recipe makes a shape on slide 1 and sets its `opacity` to 50. The shape's style reference changed from the default shape style (2651762) to a new unnamed shape style (2652495, type 2025):

```
1: { 1: { 3: { 1: 2651163 }, 4: 1, 5: { 1: 2652414 } }, 10: 1, 11: { 3: 0.5 } }
```

## Conclusion

A shape's opacity is field 1.11.3 of its shape style, from 0 to 1. Shape styles keep their properties in field 1.11, as found in [0077](0077-shape-fill.md). Images keep opacity in field 11.2 of their image style instead, so the field number depends on the kind of style.

## Confidence

*Likely*: shape style field 1.11.3 is the opacity.
