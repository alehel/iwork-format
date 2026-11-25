# 0403: Writing a line's rotation and width

**Status:** run

A line is a shape (type 2011) whose box has zero height and is rotated: a line from (100, 100) to (300, 200) is a box at (88.2, 150), 223.6 wide, rotated 333.43° ([0051](0051-line.md)). Pages' AppleScript gives a line's `start point` and `end point`. This experiment writes the rotation and the width.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0051/line.pages`: line 1732647, from (100, 100) to (300, 200) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0403
R=recipes/0302-set-path.py
F=samples/0051/line.pages
O=samples/0403
cp $F $O/original.pages
for r in 0 90 180; do python3 -I $R $F $O/rot-$r.pages 1732647 1.1.1.4 float $r; done
python3 -I $R $F $O/width-100.pages 1732647 1.1.1.2.1 float 100
for f in original rot-0 rot-90 rot-180 width-100; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages 'set l to line 1 of d
return {start point of l, end point of l, rotation of l, width of l, position of l}'
done
```

## Observation

| File | Written | Start | End | `rotation` | `width` |
| --- | --- | --- | --- | --- | --- |
| `original.pages` | | 100, 100 | 300, 200 | 333 | 224 |
| `rot-0.pages` | 1.1.4 = 0 | 88, 150 | 312, 150 | 0 | 224 |
| `rot-90.pages` | 1.1.4 = 90 | 200, 262 | 200, 38 | 90 | 224 |
| `rot-180.pages` | 1.1.4 = 180 | 312, 150 | 88, 150 | 180 | 224 |
| `width-100.pages` | 1.1.2 width = 100 | 93, 128 | 293, 228 | 333 | 224 |

## Conclusion

A line runs through the middle of its box, from the box's left end to its right end, turned about the box's centre (200, 150) by the rotation, counter-clockwise on the page: at 0° it runs left to right, at 90° from bottom to top, and at 180° right to left. So a reader finds the ends by rotating (±width/2, 0) about the centre.

The width alone doesn't set a line's length: written as 100, the line kept its length of 224 and moved. Pages takes the length from the line's path (field 1.3), as it takes a mask's size from its path ([0390](0390-writing-an-image-mask.md)). A writer changing a line's length must change its path too.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0051/line.pages` | `same bytes`, `2011#1732647 1.1.1.4 = 333.4349` | *Control*: from 100, 100 to 300, 200 |
| `rot-0.pages` | `original.pages` | Only `2011#1732647 1.1.1.4: 333.4349 → 0.0` | *Confirmed*: at 0° the line runs left to right through the middle of its box |
| `rot-90.pages` | `original.pages` | Only `2011#1732647 1.1.1.4: 333.4349 → 90.0` | *Confirmed*: at 90° from bottom to top, turned about the box's centre |
| `rot-180.pages` | `original.pages` | Only `2011#1732647 1.1.1.4: 333.4349 → 180.0` | *Confirmed*: at 180° right to left |
| `width-100.pages` | `original.pages` | Only `2011#1732647 1.1.1.2.1: 223.6068 → 100.0` | *Likely*: the box's width isn't the length: the line moves but stays 224 long |

## Confidence

*Confirmed*: a line as its box's horizontal middle turned by the rotation, by writing the rotation. *Likely*: a line's length comes from its path, not its width.
