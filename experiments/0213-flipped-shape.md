# 0213: A horizontally flipped shape

**Status:** run

AppleScript can rotate an object but not flip it. This experiment flips a shape through the Arrange menu, to find where a flip is stored.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0213/plain-shape.pages`, the same shape not flipped |

## Recipe

```bash
mkdir -p samples/0213
osascript recipes/0213-pages-shape.applescript 1
```

The recipe makes a document with a 100 × 100 shape at (300, 300), left selected. Then:

1. Choose Arrange → Flip Horizontally (*Ordne → Vend horisontalt*).
2. Save it as `samples/0213/flipped.pages`.

For the baseline, run the recipe again and save without flipping, as `samples/0213/plain-shape.pages`.

## Observation

The shape's type-2011 record differs from the baseline in one field of its geometry:

```
1.1.3: 3 → 7
```

Position, size and rotation (1.1.4, 0) are unchanged.

## Conclusion

Geometry field 1.1.3 is a set of flags, 3 for every object seen so far. Flipping horizontally sets the bit 0x4. A reader must mirror the object about its vertical centre line when the bit is set. The two bits always set (0x1 and 0x2) are probably "size and position are valid" flags. A vertical flip is stored differently ([0214](0214-vertically-flipped-shape.md)).

## Confidence

*Likely*: bit 0x4 of geometry field 1.1.3 is a horizontal flip.

*Unknown*: the meaning of bits 0x1 and 0x2.
