# 0445: A radial gradient in a wide shape

**Status:** run

In a 100 × 100 shape, a radial gradient's centre fitted C + d·(u(315°) − u(θ)), with d the width over 2√2 ([0444](0444-where-a-radial-gradient-is-centred.md)). This experiment repeats five angles in a shape twice as wide as it is high, to see how width and height enter.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0384/radial.pages`, with shape 1732647 made 200 × 100 by writing both its box width and its path's natural width ([0405](0405-writing-a-shape-size.md)); its centre C is (400, 350) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) and [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0445
O=samples/0445
python3 -I recipes/0302-set-path.py samples/0384/radial.pages $O/wide.pages 1732647 1.1.1.2.1 float 200 1.3.5.2.1 float 200
for a in 315 0 270 45 225; do
  rad=$(python3 -c "import math; print(math.radians($a))")
  python3 -I recipes/0383-set-nth-path.py $O/wide.pages $O/wide-$a.pages 1732719 1.11.1.2.5.2 float $rad
  sh recipes/0372-in-app.sh Pages $O/wide-$a.pages "export d to POSIX file \"$PWD/$O/wide-$a.pdf\" as PDF"
done
```

Each page was sampled every 4 points over the shape, and the centre taken where red minus green is largest, as in 0444.

## Observation

| Angle | Centre found | Offset from C | Offset predicted by 0444's formula with d = 35.4 | with d = 70.7 |
| --- | --- | --- | --- | --- |
| 315° | 402, 350 | +2, 0 | 0, 0 | 0, 0 |
| 0° | 398, 394 | −2, +44 | −10, +25 | −21, +50 |
| 270° | 434, 322 | +34, −28 | +25, −10 | +50, −21 |
| 45° | 422, 398 | +22, +48 (the bottom edge) | 0, +50 | 0, +100 |
| 225° | 478, 326 | +78, −24 | +50, 0 | +100, 0 |

## Conclusion

At 315° the gradient is centred in the wide shape too, so Pages' own radial gradients are centred whatever the shape. At other angles the centre doesn't follow 0444's formula with either the height or the width, nor with the width and height applied separately: at 225° it moves up as well as right, which no form of the formula allows. So the formula found in a square isn't the general rule, and how a radial gradient's angle places its centre in other shapes is still open. A writer should keep radial gradients at 315°, as Pages does.

## Confidence

*Confirmed*: a radial gradient at 315° is centred in a 200 × 100 shape as in a square. *Unknown*: how other angles place the centre in a shape that isn't square.
