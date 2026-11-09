# 0220: A star and an arrow

**Status:** run

[0219](0219-scalar-path-shapes.md) found that shapes reshaped by one number are stored as parameters in field 1.3.4. A star and an arrow each have two handles. This experiment inserts both.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0219](0219-scalar-path-shapes.md) |

## Recipe

For each shape, in a new document:

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. Choose Insert → Shape → Star (*Stjerne*), or Arrow (*Pil*).
3. Save it as ``samples/0220/star.pages` or `samples/0220/arrow.pages``.

## Observation

Each shape's outline is in field 1.3.3:

| | Star | Arrow |
| --- | --- | --- |
| 3.1 | 100 | 1 |
| 3.2, a pair | 5.0, 0.382 | 64.0, 0.34 |
| 3.3, natural size | 110 × 110 | 100 × 100 |

## Conclusion

Field 1.3.3 is a second kind of parametric path, with a pair of numbers in 3.2 rather than one. Kind 100 is a star: 3.2 holds its number of points and the inner radius as a fraction of the outer (0.382, close to the golden ratio's 1/φ²). Kind 1 is an arrow: 3.2 holds where the head starts along the length (64 of 100 points) and the shaft's thickness as a fraction of the height (0.34). The double arrow is probably another kind number.

## Confidence

*Likely*: 1.3.3 is a two-number parametric path, with kinds 100 (star: points, inner ratio) and 1 (arrow: head position, shaft thickness).
