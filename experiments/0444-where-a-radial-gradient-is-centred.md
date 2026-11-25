# 0444: Where a radial gradient is centred

**Status:** run

A radial gradient (kind 1) at 315°, the angle Pages uses, is centred on its shape; at other angles the centre moved, in a way not worked out ([0385](0385-writing-a-radial-gradient.md)). This experiment writes eight angles and finds the centre on a finer grid.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0384/radial.pages`: shape 1732647, 100 × 100 at (300, 300), with a radial gradient from red (first stop) to green, in style 1732719 |
| Writer | [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0444
O=samples/0444
for a in 0 45 90 135 180 225 270 315; do
  rad=$(python3 -c "import math; print(math.radians($a))")
  python3 -I recipes/0383-set-nth-path.py samples/0384/radial.pages $O/angle-$a.pages 1732719 1.11.1.2.5.2 float $rad
  sh recipes/0372-in-app.sh Pages $O/angle-$a.pages "export d to POSIX file \"$PWD/$O/angle-$a.pdf\" as PDF"
done
```

Each page was sampled every 4 points from (302, 302) to (398, 398), and the centre taken as the point where red minus green is largest: the first stop's colour.

## Observation

| Angle | Centre found | Offset from the shape's centre (350, 350) |
| --- | --- | --- |
| 315° | 350, 350 | 0, 0 |
| 0° | 338, 374 | −12, +24 |
| 270° | 374, 338 | +24, −12 |
| 45° | 350, 398 | 0, +48 (the bottom edge) |
| 225° | 398, 350 | +48, 0 (the right edge) |
| 90° | 374, 398 | +24, +48 (the bottom edge) |
| 180° | 398, 378 | +48, +28 (the right edge) |
| 135° | 398, 398 | +48, +48 (the corner) |

## Conclusion

With angles counter-clockwise and y down, let u(θ) = (cos θ, −sin θ). The centres fit

  centre = C + d · (u(315°) − u(θ)), with d = w / (2√2),

where C is the box's centre and w its width, so d ≈ 35.4 here. For 0° that gives an offset of (−10, +25), for 270° (+25, −10), for 45° (0, +50) and for 225° (+50, 0), matching the grid within its 4-point steps; at 90°, 135° and 180° the centre lies outside the shape, and the reddest point found is on its edge. Put another way: the point d from the centre towards the bottom right, (375, 375), stays where it is, and the centre lies d from it in the direction opposite the angle. At 315° the centre is the box's centre, which is why Pages' own radial gradients are centred.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `angle-0.pages` | `0384/radial.pages` | Only `2025#1732719 1.11.1.2.5.2: 4.7124 → 0.0` | *Likely*: the formula fits; the centre is found at 338, 374 |
| `angle-45.pages` | `0384/radial.pages` | Only `2025#1732719 1.11.1.2.5.2: 4.7124 → 0.7854` | *Likely*: the formula fits; the centre is found at 350, 398 |
| `angle-90.pages` | `0384/radial.pages` | Only `2025#1732719 1.11.1.2.5.2: 4.7124 → 1.5708` | *Likely*: the formula fits, with the centre outside the shape; the reddest point is on the edge, at 374, 398 |
| `angle-135.pages` | `0384/radial.pages` | Only `2025#1732719 1.11.1.2.5.2: 4.7124 → 2.3562` | *Likely*: the formula fits, with the centre outside the shape; the reddest point is on the edge, at 398, 398 |
| `angle-180.pages` | `0384/radial.pages` | Only `2025#1732719 1.11.1.2.5.2: 4.7124 → 3.1416` | *Likely*: the formula fits, with the centre outside the shape; the reddest point is on the edge, at 398, 378 |
| `angle-225.pages` | `0384/radial.pages` | Only `2025#1732719 1.11.1.2.5.2: 4.7124 → 3.927` | *Likely*: the formula fits; the centre is found at 398, 350 |
| `angle-270.pages` | `0384/radial.pages` | `same bytes`, `2025#1732719 1.11.1.2.5.2 = 4.7124` | *Likely*: the formula fits; the centre is found at 374, 338 |
| `angle-315.pages` | `0384/radial.pages` | Only `2025#1732719 1.11.1.2.5.2: 4.7124 → 5.4978` | *Likely*: the formula fits; the centre is the shape's centre |

## Confidence

*Likely*: the formula above, which fits eight angles within the grid's steps in one 100 × 100 shape. A shape that isn't square would test how width and height enter it.
