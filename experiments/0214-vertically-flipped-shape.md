# 0214: A vertically flipped shape

**Status:** run

[0213](0213-flipped-shape.md) found that flipping a shape horizontally sets bit 0x4 in geometry field 1.1.3. This experiment flips one vertically.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0213/plain-shape.pages` |

## Recipe

```bash
mkdir -p samples/0214
osascript recipes/0213-pages-shape.applescript 1
```

Then choose Arrange → Flip Vertically (*Ordne → Vend vertikalt*) and save as `samples/0214/flipped-vertically.pages`.

## Observation

The shape's geometry differs from the baseline in two fields:

```
1.1.3: 3 → 7
1.1.4: 0.0 → 180.0
```

## Conclusion

There's no separate vertical flip. Pages stores it as a horizontal flip (bit 0x4) plus a rotation of 180°, which gives the same picture: mirroring left to right and then turning half a turn mirrors top to bottom. A reader that handles the horizontal flip and the rotation (applying the flip first) handles both kinds of flip.

## Confidence

*Likely*: a vertical flip is stored as a horizontal flip and a 180° rotation.

*Unknown*: the order in which Pages applies the flip and the rotation. With 180° the order doesn't matter, but with other angles it would. Follow-up: rotate a flipped shape by 30°.
