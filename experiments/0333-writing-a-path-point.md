# 0333: Writing a point of a shape's path, measured on the page

**Status:** run

An editable shape keeps its outline as points in 1.3.8 ([0217](0217-editable-shape.md)): a list of points in 1.3.8.1.1, each with the point and its two control points in fields 1, 2 and 3 and a type in 4, a closing flag in 1.3.8.1.2, and the path's natural size in 1.3.8.2. This experiment moves one point and measures the shape on the exported page.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0217/editable.pages`: shape 1732647, 100 × 100 at (300, 300), an editable square with points (0, 0), (100, 0), (100, 100) and (0, 100) in a 100 × 100 path |
| Writer | [`recipes/0333-move-path-point.py`](../recipes/0333-move-path-point.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0333
cp samples/0217/editable.pages samples/0333/original.pages
python3 -I recipes/0333-move-path-point.py samples/0333/original.pages samples/0333/moved.pages 1732647 2 50 100
```

The third point, (100, 100), and its control points move to (50, 100). Each file was opened in Pages on its own and exported as PDF; the page was drawn at 4 pixels per point and the shape's inked extent measured on three rows.

## Observation

| File | y = 305 | y = 350 | y = 395 |
| --- | --- | --- | --- |
| `original.pages` | 300.2 – 400.2 | 300.2 – 400.2 | 300.2 – 400.2 |
| `moved.pages` | 300.2 – 397.8 | 300.2 – 375.2 | 300.2 – 352.8 |

A straight edge from (400, 300) to (350, 400) is at x = 397.5, 375 and 352.5 on those rows.

## Conclusion

The path's points are drawn as written: the right edge now runs from the second point to the moved third one, a straight line because the control points sit on the point. The path's coordinates map onto the shape's box, here one to one, since the natural size and the box are both 100 × 100.

## Confidence

*Confirmed*: editable path points 1.3.8.1.1, by writing one and measuring.

*Likely*: path coordinates are scaled from the natural size (1.3.8.2) to the box (1.1.2), not tested here.
