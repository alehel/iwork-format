# 0373: Writing a flip

**Status:** run

Flipping a shape horizontally sets bit 0x4 of its geometry flags, field 1.1.3, from 3 to 7 ([0213](0213-flipped-shape.md)). A vertical flip is stored as the same bit plus a rotation of 180° in 1.1.4 ([0214](0214-vertically-flipped-shape.md)). AppleScript can't read a flip, so this experiment writes both forms into a shape that isn't symmetrical, has Pages export it as PDF and draws the shape.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/0333/moved.pages`: shape 1732647, 100 × 100 at (300, 300), an editable square whose bottom-right point was moved to (50, 100) ([0333](0333-writing-a-path-point.md)). Its top edge is full width and its left edge straight |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and drawn with the new [`recipes/0373-draw-pdf.swift`](../recipes/0373-draw-pdf.swift) |

## Recipe

```bash
mkdir -p samples/0373
R=recipes/0302-set-path.py
M=samples/0333/moved.pages
cp $M samples/0373/original.pages
python3 -I $R $M samples/0373/flipped.pages 1732647 1.1.1.3 varint 7
python3 -I $R $M samples/0373/flipped-180.pages 1732647 1.1.1.3 varint 7 1.1.1.4 float 180
python3 -I $R $M samples/0373/rotated-180.pages 1732647 1.1.1.4 float 180
for f in original flipped flipped-180 rotated-180; do
  sh recipes/0372-in-app.sh Pages samples/0373/$f.pages \
    "export d to POSIX file \"$PWD/samples/0373/$f.pdf\" as PDF"
  swift recipes/0373-draw-pdf.swift samples/0373/$f.pdf 300 300 100 100 10
done
```

A shape's drawable is field 1 of its payload, so its geometry flags are at 1.1.1.3 and its rotation at 1.1.1.4.

## Observation

The 100 × 100 box, one character per 10 points:

```
original     flipped      flipped-180  rotated-180
##########   ##########   #####.....   .....#####
#########.   .#########   ######....   ....######
#########.   .#########   ######....   ....######
########..   ..########   #######...   ...#######
########..   ..########   #######...   ...#######
#######...   ...#######   ########..   ..########
#######...   ...#######   ########..   ..########
######....   ....######   #########.   .#########
######....   ....######   #########.   .#########
#####.....   .....#####   ##########   ##########
```

AppleScript reports rotations of 0, 0, 180 and 180, and the same position for all four.

## Conclusion

Flag 0x4 mirrors the shape left to right within its box. With a rotation of 180° added, the result is the shape mirrored top to bottom, which is how Pages stores a vertical flip. A rotation of 180° alone turns the shape upside down and mirrors it both ways, which a reader that ignored the flag would draw instead.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0333/moved.pages` | `same bytes`, `2011#1732647 1.1.1.3 = 3` | *Control*: the cut-off corner is at the bottom right |
| `flipped.pages` | `original.pages` | Only `2011#1732647 1.1.1.3: 3 → 7` | *Confirmed*: flag 0x4 mirrors the shape left to right |
| `flipped-180.pages` | `original.pages` | Only `2011#1732647 1.1.1.3: 3 → 7`, `2011#1732647 1.1.1.4: 0.0 → 180.0` | *Confirmed*: the flag and 180° mirror it top to bottom |
| `rotated-180.pages` | `original.pages` | Only `2011#1732647 1.1.1.4: 0.0 → 180.0` | *Control*: 180° alone turns it upside down, mirrored both ways |

## Confidence

*Confirmed*: flag 0x4 of field 1.1.3 as a horizontal flip, and a vertical flip as that flag plus 180°, by writing them.
