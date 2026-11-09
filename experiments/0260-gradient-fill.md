# 0260: A gradient fill

**Status:** run

[0077](0077-shape-fill.md) found a shape's fill colour in field 1.11.1.1 of its style. A shape can also be filled with a gradient, chosen from a pop-up in the sidebar that needs Pages in front. This experiment applies the default gradient.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0213/plain-shape.pages` |

## Recipe

```bash
mkdir -p samples/0260
osascript recipes/0213-pages-shape.applescript 1
```

The new shape is left selected. Then, with Pages in front:

1. In the Style tab, open Fill (*Fyll*) and choose Gradient Fill (*Forløpningsfyll*) from the pop-up. Pages fills the shape from light blue to dark blue, at an angle of 270°.
2. Save as `samples/0260/gradient.pages`.

## Observation

The shape's new style has one property, a fill in 1.11.1, with field 2 instead of the colour in field 1:

```
1.11.1.2:
  1: 0
  2: { 1: light blue (0.338, 0.758, 1.0), 2: 0.0, 3: 0.5 }
  2: { 1: dark blue (0.0, 0.462, 0.729), 2: 1.0, 3: 0.5 }
  3: 1.0
  4: 0
  5: { 2: 4.712389 }
```

## Conclusion

A shape's fill (1.11.1) holds either a colour (field 1) or a gradient (field 2). A gradient has:

- **Field 1:** its kind, probably 0 for linear. A radial gradient would be another value.
- **Field 2, repeated:** its stops, each with a colour (1), a position from 0 to 1 (2) and probably the midpoint towards the next stop (3, 0.5).
- **Field 3:** an opacity.
- **Field 5.2:** its angle in radians. 4.712389 is 3π/2, the 270° the sidebar shows.

A reader that can't draw gradients can fall back on the first stop's colour.

## Confidence

*Likely*: fill field 2 is a gradient with stops in 2.2 and the angle in radians in 2.5.2.

*Unknown*: fields 2.1 and 2.4, and the radial kind.
