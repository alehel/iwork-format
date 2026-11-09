# 0275: A radial gradient

**Status:** run

[0260](0260-gradient-fill.md) read a linear gradient fill, with its kind in field 1 (0) and an unexplained field 4 (0). The Fill pop-up's Advanced Gradient Fill can also be radial. This experiment makes one.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0260](0260-gradient-fill.md), a linear gradient at 270° |

## Recipe

```bash
mkdir -p samples/0275
osascript recipes/0213-pages-shape.applescript 1
```

The new shape is left selected. Then, with Pages in front:

1. Choose Advanced Gradient Fill (*Avansert forløpningsfyll*) from the Fill pop-up.
2. Click the radial button beside the angle. The sidebar shows 315°, and the gradient now spreads from the shape's centre.
3. Save as `samples/0275/radial.pages`.

## Observation

The fill's gradient (style field 1.11.1.2) has the same two blue stops as 0260 and differs in:

| Field | Linear (0260) | Radial |
| --- | --- | --- |
| 1 | 0 | 1 |
| 4 | 0 | 1 |
| 5.2 | 4.712389 (270°) | 5.497787 (315°) |

## Conclusion

Gradient field 1 is the kind: 0 linear, 1 radial. Field 4 is 1 for a gradient made with the advanced editor, which lets stops be added and moved, and 0 for the simple two-colour one. For a radial gradient the angle (field 5.2, in radians) probably sets the direction from the centre to the handle the sidebar draws, here towards the bottom-right corner, which marks the outer edge of the gradient.

## Confidence

*Likely*: gradient field 1 is 0 for linear and 1 for radial.

*Unknown*: whether field 4 marks the advanced editor, and how a radial gradient's centre and radius are set. Follow-up: an advanced linear gradient.
