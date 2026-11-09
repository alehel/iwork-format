# 0278: The shadow angle

**Status:** run

[0251](0251-shape-shadow.md) found a drop shadow's angle stored as 90 while the sidebar showed 270°. Two rules fit that pair: the stored angle is the sidebar's plus 180°, or 360° minus it. This experiment sets two more angles to tell the rules apart.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0251](0251-shape-shadow.md) |

## Recipe

```bash
mkdir -p samples/0278
osascript recipes/0213-pages-shape.applescript 1
```

The new shape is left selected. Then, with Pages in front:

1. Add a drop shadow as in 0251.
2. Type 0 into the shadow's Angle (*Vinkel*) field and save as `samples/0278/shadow-0.pages`.
3. Type 45 and save as `samples/0278/shadow-45.pages`. Pages draws the shadow up and to the right of the shape.

## Observation

| Sidebar | Stored (shadow field 2) |
| --- | --- |
| 270° (0251) | 90 |
| 0° | 0 |
| 45° | 315 |

The other shadow fields are unchanged.

## Conclusion

The stored angle is 360° minus the sidebar's angle. The sidebar measures counter-clockwise, as on a compass rose drawn with y pointing up. The file measures clockwise on the page, where y points down, which is the same direction on screen. A reader can place the shadow at (offset × cos a, offset × sin a) from the shape in page coordinates, where a is the stored angle. At 315° that puts the shadow up and to the right, as Pages drew it.

## Confidence

*Likely*: the stored shadow angle is in page coordinates, with y down, and equals 360° minus the sidebar's angle.
