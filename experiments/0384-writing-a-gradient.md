# 0384: Writing a gradient's stops and angle

**Status:** run

A shape's fill can be a gradient, in field 1.11.1.2 of its style: its kind in field 1 (0 linear, 1 radial), its stops in the repeated field 2 (each a colour in 2.1, a position from 0 to 1 in 2.2 and a midpoint in 2.3) and its angle in radians in 5.2 ([0260](0260-gradient-fill.md), [0275](0275-radial-gradient.md)). AppleScript can't read a gradient, so this experiment writes new values, has Pages export the page, and reads the colours at points across the shape.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/0260/gradient.pages`: shape 1732647, 100 × 100 at (300, 300), whose style 1732719 has Pages' default gradient, light blue (0.34, 0.76, 1.0) at 0 to dark blue (0.0, 0.46, 0.73) at 1, at 4.712389 radians (270°) |
| Writer | [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with the new [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0384
N=recipes/0383-set-nth-path.py
F=samples/0260/gradient.pages
O=samples/0384
G=1.11.1.2
cp $F $O/original.pages
python3 -I $N $F $O/red-green.pages 1732719 \
  $G.2:1.1.3 float 1 $G.2:1.1.4 float 0 $G.2:1.1.5 float 0 \
  $G.2:2.1.3 float 0 $G.2:2.1.4 float 1 $G.2:2.1.5 float 0
python3 -I $N $O/red-green.pages $O/angle-0.pages 1732719 $G.5.2 float 0
python3 -I $N $O/red-green.pages $O/stops-moved.pages 1732719 $G.2:1.2 float 0.4 $G.2:2.2 float 0.6
python3 -I $N $O/red-green.pages $O/radial.pages 1732719 $G.1 varint 1
for f in original red-green angle-0 stops-moved radial; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0384-pdf-colours.swift $O/$f.pdf 350,302 350,330 350,350 350,370 350,398 302,350 398,350
done
```

## Observation

Red, green and blue at points down the middle of the shape (y = 302 to 398, x = 350) and at its left and right edges (y = 350):

| File | Top 302 | 330 | Centre | 370 | Bottom 398 | Left 302 | Right 398 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `original.pages` | .33 .75 .99 | .24 .67 .92 | .17 .61 .86 | .10 .55 .81 | .01 .47 .74 | .17 .61 .86 | .17 .61 .86 |
| `red-green.pages` | .97 .03 0 | .70 .30 0 | .50 .50 0 | .30 .70 0 | .03 .97 0 | .50 .50 0 | .50 .50 0 |
| `angle-0.pages` | .50 .50 0 | .50 .50 0 | .50 .50 0 | .50 .50 0 | .50 .50 0 | .97 .03 0 | .03 .97 0 |
| `stops-moved.pages` | 1 0 0 | 1 0 0 | .49 .51 0 | 0 1 0 | 0 1 0 | .49 .51 0 | .49 .51 0 |
| `radial.pages` | .37 .63 0 | .62 .38 0 | .61 .39 0 | .45 .55 0 | .11 .89 0 | 0 1 0 | .65 .34 0 |

## Conclusion

The stops' colours are drawn as written: the first stop's colour where the gradient starts and the second's where it ends, mixed evenly in between. A stop's position (2.2) is where along the gradient its colour is reached, so stops at 0.4 and 0.6 leave solid red and solid green bands. The angle (5.2) is the gradient's direction in radians, counter-clockwise from the right with y up: 0 runs from left to right, and 270° (4.712389) from top to bottom.

Writing the kind as 1 makes the gradient radial, but its centre isn't the middle of the shape (the left edge is already fully green and the top isn't red), so a radial gradient needs more than the kind; [0275](0275-radial-gradient.md)'s record would show what Pages adds.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0260/gradient.pages` | `same bytes`, `2025#1732719 1.11.1.2.1 = 0`, `2025#1732719 1.11.1.2.5.2 = 4.7124` | *Control*: light blue at the top to dark blue at the bottom |
| `red-green.pages` | `original.pages` | Only `2025#1732719 1.11.1.2.2.1.3: 0.34 → 1.00`, `2025#1732719 1.11.1.2.2.1.4: 0.76 → 0.00`, `2025#1732719 1.11.1.2.2.1.5: 1.00 → 0.00` | *Confirmed*: the stops' colours are drawn as written: red at the top to green at the bottom |
| `angle-0.pages` | `red-green.pages` | Only `2025#1732719 1.11.1.2.5.2: 4.7124 → 0.0` | *Confirmed*: field 5.2 is the angle: red at the left to green at the right |
| `stops-moved.pages` | `red-green.pages` | Only `2025#1732719 1.11.1.2.2.2: 0.0 → 0.4`, `2025#1732719 1.11.1.2.2.2: 1.0 → 0.6` | *Confirmed*: field 2.2 is a stop's position: solid bands before 0.4 and after 0.6 |
| `radial.pages` | `red-green.pages` | Only `2025#1732719 1.11.1.2.1: 0 → 1` | *Likely*: kind 1 is radial; where it is centred is unknown |

## Confidence

*Confirmed*: a linear gradient's stop colours, stop positions and angle, by writing them. Kind 1 as radial is *likely*; where a radial gradient is centred is *unknown*.
