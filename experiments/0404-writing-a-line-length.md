# 0404: Writing a line's length

**Status:** run

Writing a line's width didn't change its length ([0403](0403-writing-a-line.md)). A mask is drawn at its path's natural size, not its box's ([0390](0390-writing-an-image-mask.md)). The line of [0051](0051-line.md) has a path (field 1.3.5) whose natural size, 5.2, is 223.6 × 0, while its two points are (0, 0) and (141.42, 0). This experiment writes the natural width, the width with it, and the second point.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0051/line.pages`: line 1732647, from (100, 100) to (300, 200), its box 223.6 wide at (88.2, 150), rotated 333.43° |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) and [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0404
R=recipes/0302-set-path.py
F=samples/0051/line.pages
O=samples/0404
cp $F $O/original.pages
python3 -I $R $F $O/natural-100.pages 1732647 1.3.5.2.1 float 100
python3 -I $R $F $O/natural-100-width-100.pages 1732647 1.3.5.2.1 float 100 1.1.1.2.1 float 100
python3 -I recipes/0383-set-nth-path.py $F $O/point-100.pages 1732647 1.3.5.3.1:2.2.1 float 100
for f in original natural-100 natural-100-width-100 point-100; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages 'set l to line 1 of d
return {start point of l, end point of l, width of l}'
done
```

A first attempt wrote the width at the wrong path (1.1.2.1, outside the shape's drawable), after which Pages stopped opening documents until it was restarted; the file was written again correctly.

## Observation

| File | Written | Start | End | Length | `width` |
| --- | --- | --- | --- | --- | --- |
| `original.pages` | | 100, 100 | 300, 200 | 224 | 224 |
| `natural-100.pages` | natural width 100 | 100, 100 | 189, 145 | 100 | 100 |
| `natural-100-width-100.pages` | natural width 100, box width 100 | 93, 128 | 183, 172 | 100 | 100 |
| `point-100.pages` | second point at 100 | 100, 100 | 300, 200 | 224 | 224 |

## Conclusion

A line's length is its path's natural width (5.2.1). Its points are stretched to fill that size, so moving the second point from 141.42 to 100 changed nothing. The path is laid out from the box's left end and the whole box turns about its centre: with the box still 223.6 wide, a 100-point line keeps its start at (100, 100); with the box made 100 wide too, the line is centred where that narrower box's middle is. AppleScript's `width` reports the path's width, not the box's.

So, as for a mask, a reader should draw a line's path at its natural size, from the box's corner, and turn it with the box. A writer should keep the box's width and the natural width the same, as Pages does.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0051/line.pages` | `same bytes`, `2011#1732647 1.3.5.2.1 = 223.6068` | *Control*: 224 long |
| `natural-100.pages` | `original.pages` | Only `2011#1732647 1.3.5.2.1: 223.6068 → 100.0` | *Confirmed*: the path's natural width is the line's length: 100 |
| `natural-100-width-100.pages` | `natural-100.pages` | Only `2011#1732647 1.1.1.2.1: 223.6068 → 100.0` | *Confirmed*: the box's width moves the line but leaves its length |
| `point-100.pages` | `original.pages` | Only `2011#1732647 1.3.5.3.1.2.1: 141.4214 → 100.0` | *Confirmed*: the points are stretched to the natural width: still 224 long |

## Confidence

*Confirmed*: a line's length as its path's natural width, with its points stretched to fill it, by writing them.
