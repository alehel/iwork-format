# 0250: A border on a shape

**Status:** run

[0077](0077-shape-fill.md) found that a shape style's field 1.11.2 is probably the stroke, with a colour and a width. It also found that the default style has no visible stroke, though its colour and width are set, and left open which field turns the stroke off. This experiment gives a shape a border through the sidebar's pop-up menu, which needs Pages in front.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0213/plain-shape.pages`, the shape with the default `shape-0-shapestyle` |

## Recipe

```bash
mkdir -p samples/0250
osascript recipes/0213-pages-shape.applescript 1
```

The new shape is left selected. Then, with Pages in front:

1. In the Format sidebar's Style tab, open Border (*Kantlinje*) and choose Line (*Linje*) from the pop-up. Pages draws a black 5-point border.
2. Save as `samples/0250/border.pages`.

## Observation

The shape's style reference (1.2) now names a new unnamed type-2025 style, whose parent (1.1.3) is `shape-0-shapestyle`. Its only property is a stroke, in 1.11.2. Compared with the parent's stroke:

| Field | Parent (no border) | New style |
| --- | --- | --- |
| 2.1, colour | black, alpha 1 | black, alpha 1 |
| 2.2 | 1.0 | 5.0 |
| 2.5 | 4.0 | 4.0 |
| 2.6.1 | 2 | 1 |

## Conclusion

Field 1.11.2 is the stroke: colour in 2.1 and width in points in 2.2. Field 2.6 is the stroke's pattern, and 2.6.1 its kind: 2 for no line and 1 for a solid line. So the default style has a stroke that is turned off, not a missing stroke. Field 2.5 is probably the miter limit, 4 by default. A reader should draw a shape's border only when 2.6.1 is 1 (or another visible pattern), with the width in 2.2.

## Confidence

*Likely*: field 1.11.2 is the stroke, with its width in 2.2 and its pattern in 2.6.1 (1 solid, 2 none).

*Unknown*: fields 2.3, 2.4 and 2.5, and the values of dashed patterns.
