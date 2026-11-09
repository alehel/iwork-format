# 0251: A shadow on a shape

**Status:** run

[0250](0250-shape-border.md) found a shape's border in field 1.11.2 of its style. This experiment adds a drop shadow through the sidebar's pop-up menu, to find the shadow's fields.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0213/plain-shape.pages` |

## Recipe

```bash
mkdir -p samples/0251
osascript recipes/0213-pages-shape.applescript 1
```

The new shape is left selected. Then, with Pages in front:

1. In the Format sidebar's Style tab, open Shadow (*Skygge*) and choose Drop Shadow (*Skygge*) from the pop-up. The sidebar shows its settings: blur 5 pt, offset 2 pt, opacity 50%, angle 270°, black.
2. Save as `samples/0251/shadow.pages`.

## Observation

The shape's style reference names a new unnamed type-2025 style whose parent is `shape-0-shapestyle`. Its only property is in 1.11.4:

```
1: black, alpha 1   ← colour
2: 90.0
3: 2.0
4: 5                ← a varint
5: 0.5
6: 1
7: 0
```

## Conclusion

Field 1.11.4 of a shape style is its shadow:

| Field | Setting |
| --- | --- |
| 1 | Colour |
| 2 | Angle in degrees |
| 3 | Offset in points |
| 4 | Blur in points, as a whole number |
| 5 | Opacity, 0–1 |
| 6 | Shown (1) |
| 7 | Kind, probably 0 for a drop shadow (the pop-up also offers contact and curved shadows) |

The angle is stored as 90 while the sidebar shows 270°. The two differ by 180°: the sidebar probably gives the direction the light comes from, and the file the direction the shadow falls. With y pointing down on the page, 90° puts the shadow 2 points below the shape.

## Confidence

*Likely*: field 1.11.4 is the shadow, with colour, angle, offset, blur, opacity and visibility in fields 1–6.

*Unknown*: field 7, and the direction the angle is measured in. Follow-up: set the angle to 0° in the sidebar.
