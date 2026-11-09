# 0219: A rounded rectangle and a polygon

**Status:** run

[0217](0217-editable-shape.md) and [0218](0218-oval.md) found two forms of a shape's outline: a path of elements (1.3.5) and an editable path (1.3.8). This experiment inserts two shapes that the app can reshape with a single slider, the corner radius of a rounded rectangle and the number of sides of a polygon, to see whether they are stored as paths at all.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0217](0217-editable-shape.md) and [0218](0218-oval.md) |

## Recipe

For each shape, in a new document:

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. Choose Insert → Shape → Rounded Rectangle (*Avrundet rektangel*), or Polygon.
3. Save it as ``samples/0219/rounded.pages` or `samples/0219/polygon.pages``.

## Observation

Neither shape has a 1.3.5 path. Each has field 1.3.4 instead:

| | Rounded rectangle | Polygon |
| --- | --- | --- |
| 4.1 | 0 | 1 |
| 4.2 | 15.0 | 5.0 |
| 4.3, natural size | 100 × 100 | 110 × 110 |
| 4.4 | 1 | 0 |

## Conclusion

Field 1.3.4 is a parametric path: a kind of shape in 4.1, one number in 4.2, and the natural size in 4.3. Kind 0 is a rounded rectangle with the corner radius in 4.2, and kind 1 a regular polygon with the number of sides in 4.2. A reader has to draw the shape from these values, as no path points are stored. Field 4.4 is probably whether the corners are drawn as smooth curves: 1 for the rounded rectangle, 0 for the polygon's sharp corners.

## Confidence

*Likely*: 1.3.4 is a parametric path, with kinds 0 (rounded rectangle, radius) and 1 (polygon, sides).

*Unknown*: field 4.4.
