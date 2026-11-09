# 0057: An image's opacity

**Status:** run

This experiment makes an image half transparent, to find where opacity is stored.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0023](0023-an-image.md), `image.pages` |

## Recipe

```bash
mkdir -p samples/0057
osascript recipes/0055-pages-image-property.applescript "$PWD/samples/0057/opacity.pages" "$PWD/samples/0023/red-8x4.png" opacity
```

The recipe places the PNG of 0023 and sets its `opacity` to 50.

## Observation

The image record's only change is in field 3, which in 0023 named object 1731560. It now names 1732653, a new record in `DocumentStylesheet.iwa`:

```
1732653, type 3016
  1: { 3: { 1: 1731560 }, 4: 1, 5: { 1: 1732613 } }     ← parent: the default image style
  10: 1
  11: { 2: 0.5 }
```

## Conclusion

Opacity is a property of the image's style, not of the image. Field 3 of an image names its style (type 3016), and changing the opacity made an unnamed image style that inherits from the default one and sets field 11.2 to 0.5. This is the same pattern as unnamed character and paragraph styles ([0004](0004-larger-word.md), [0008](0008-runs-and-shared-styles.md)), with field 1.3 as the parent and 11 as the properties. In an image style, though, 11.2 is opacity as a fraction, not italic.

## Confidence

*Likely*:

- Image field 3 names an image style (type 3016).
- Field 11.2 of an image style is the opacity, from 0 to 1.
