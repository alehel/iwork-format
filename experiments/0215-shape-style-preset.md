# 0215: Another shape style preset

**Status:** run

[0077](0077-shape-fill.md) found that choosing a shape style preset points the shape at a named style, `shape-3-shapestyle` for the red one. This experiment picks a different preset, on two shapes at once, to confirm the reading.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0213/plain-shape.pages` |

## Recipe

```bash
mkdir -p samples/0215
osascript recipes/0213-pages-shape.applescript 2
```

Then:

1. Choose Edit → Select All (*Rediger → Marker alle*) and click the second shape. Both shapes end up selected.
2. In the Format sidebar's Style tab, click the blue preset, the second in the top row.
3. Save as `samples/0215/blue-style.pages`.

## Observation

Both shapes' style references (field 1.2) change from 1731553 to 1731554. No style is added to `DocumentStylesheet.iwa`.

| | `shape-0-shapestyle` (1731553) | `shape-1-shapestyle` (1731554) |
| --- | --- | --- |
| 1.11.1.1, fill colour | 0, 0, 0, alpha 1 | 0, 0.633, 1.0, alpha 1 |
| 1.11.2, stroke | as in 0077 | the same |

## Conclusion

Each preset in the sidebar is a named style in the stylesheet, `shape-N-shapestyle`, numbered in the order of the swatches: 0 black, 1 blue and, from 0077, 3 red. Choosing one only changes the shape's style reference. Several shapes can share one preset style.

## Confidence

*Confirmed*, with 0077: shape style presets are named type-2025 styles that shapes point at directly.
