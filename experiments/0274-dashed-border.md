# 0274: A dashed border

**Status:** run

[0250](0250-shape-border.md) found that a stroke's pattern kind, in field 6.1, is 1 for a solid line and 2 for none. The rest of field 6, a value and six zeroes, was unexplained. This experiment picks a dashed line, to read the pattern.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0250](0250-shape-border.md), a solid 5-point border |

## Recipe

```bash
mkdir -p samples/0274
osascript recipes/0213-pages-shape.applescript 1
```

The new shape is left selected. Then, with Pages in front:

1. Choose Line (*Linje*) from the Border pop-up, as in 0250.
2. From the line style pop-up beside the colour, choose the second style, short dashes. The shape gets a dashed 5-point border.
3. Save as `samples/0274/dashed.pages`.

## Observation

The stroke (style field 1.11.2) matches 0250's in colour and width (5.0). Its field 6 is now:

```
1: 0
2: 0.0
3: 2
4: 1.0, 1.0, 0.0, 0.0, 0.0, 0.0
```

In the solid border of 0250 it was `{ 1: 1, 2: 0.0, 3: 0, 4: six zeroes }`.

## Conclusion

Stroke field 6 is the line's pattern:

- **Field 1:** the kind. 0 means a dash pattern, 1 a solid line and 2 no line.
- **Field 3:** how many of the six lengths in field 4 are used (2).
- **Field 4:** the lengths, alternating dash and gap: 1 and 1 here. They are probably multiples of the line width, since this 5-point line's dashes look about 5 points long.
- **Field 2:** probably the phase, where the pattern starts.

A reader draws a dashed line by repeating the used lengths, scaled by the width.

## Confidence

*Likely*: stroke pattern kind 0 is a dash pattern whose lengths are in field 4, with their count in field 3.

*Unknown*: the unit of the lengths, and field 2.
