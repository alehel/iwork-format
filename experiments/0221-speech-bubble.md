# 0221: A speech bubble

**Status:** run

[0219](0219-scalar-path-shapes.md) and [0220](0220-point-path-shapes.md) found two parametric outline forms. A speech bubble has a rounded box and a tail. This experiment inserts one.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0219](0219-scalar-path-shapes.md) and [0220](0220-point-path-shapes.md) |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. Choose Insert → Shape → Speech Bubble (*Snakkeboble*).
3. Save it as ``samples/0221/bubble.pages``.

## Observation

The outline is in field 1.3.6:

```
1: 130 × 64        ← natural size
2: (0.8, 76.8)
3: 8.0
4: 140.0
5: 1
```

## Conclusion

Field 1.3.6 is a third parametric form, for callouts. Field 1 is the size of the bubble's box and field 3 most likely its corner radius (8). Fields 2 and 4 describe the tail. The point (0.8, 76.8) lies below the 64-point-high box, so field 2 is probably the tail's tip, and field 4 something like the tail's position or width. Field 5 is probably whether the tail is shown.

## Confidence

*Likely*: field 1.3.6 is a callout path, with the box size in field 1 and the corner radius in field 3.

*Unknown*: fields 2, 4 and 5. Follow-up: move the tail's tip by a known amount.
