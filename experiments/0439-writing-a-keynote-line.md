# 0439: Writing a Keynote line

**Status:** run

Lines and shapes in Keynote have the same geometry and style identifiers as in Pages ([0166](0166-keynote-line.md)). In Pages, a line runs through its box turned by the rotation, and its length is its path's natural width, not its box's ([0403](0403-writing-a-line.md), [0404](0404-writing-a-line-length.md)). This experiment repeats those writes in Keynote.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/theme/0166/line.key`: line 2655554 from (100, 100) to (300, 200), its box at (88.2, 150), 223.6 wide, rotated 333.43°, in the test theme |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0439
R=recipes/0302-set-path.py
F=samples/theme/0166/line.key
O=samples/0439
cp $F $O/original.key
python3 -I $R $F $O/rot-90.key 2655554 1.1.1.4 float 90
python3 -I $R $F $O/natural-100.key 2655554 1.3.5.2.1 float 100
python3 -I $R $F $O/box-100.key 2655554 1.1.1.2.1 float 100
for f in original rot-90 natural-100 box-100; do
  sh recipes/0372-in-app.sh Keynote $O/$f.key 'set l to line 1 of slide 1 of d
return {start point of l, end point of l, rotation of l, width of l}'
done
```

## Observation

| File | Written | Start | End | `rotation` | `width` | Same as in Pages |
| --- | --- | --- | --- | --- | --- | --- |
| `original.key` | | 100, 100 | 300, 200 | 333 | 224 | |
| `rot-90.key` | rotation 90 | 200, 262 | 200, 38 | 90 | 224 | yes, [0403](0403-writing-a-line.md) |
| `natural-100.key` | path's natural width 100 | 100, 100 | 189, 145 | 333 | 100 | yes, [0404](0404-writing-a-line-length.md) |
| `box-100.key` | box width 100 | 93, 128 | 293, 228 | 333 | 224 | yes, [0403](0403-writing-a-line.md) |

## Conclusion

A Keynote line behaves exactly as a Pages line: it is turned about its box's centre by the rotation, counter-clockwise, and its length is its path's natural width, with the box's own width unused. The same reader code serves both apps.

## Confidence

*Confirmed*: Keynote lines' rotation and length work as in Pages, by writing them.
