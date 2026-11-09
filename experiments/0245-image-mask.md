# 0245: An image masked with an oval

**Status:** run

Pages can crop an image to a shape (Format → Image → Mask with Shape). This experiment masks an image with an oval, to see how the mask is stored and whether the image itself is cropped.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0228/caption.pages`, the same image |

## Recipe

```bash
mkdir -p samples/0245
osascript recipes/0244-pages-image.applescript "$PWD/samples/0023/red-8x4.png"
```

Then:

1. Choose Format → Image → Mask with Shape → Oval (*Format → Bilde → Masker med figur → Oval*). Pages shows a 100 × 100 circle in the middle of the 200 × 100 image, with the rest faded, and a Done button.
2. Click Done (*Ferdig*). Only the circle is shown.
3. Save it as `samples/0245/oval-mask.pages`.

## Observation

The image record (type 3005) keeps its geometry: (300, 300), 200 × 100. It gains field 5, naming a new record of type 3006:

```
1: drawable: 1.1 geometry (50, 0), 100 × 100; 1.2 { 1: 1732647 }   ← the image
2: a path: 2.5, natural size 100 × 100, with move, curve … elements   ← an oval, as in 0218
```

The stored image file is unchanged.

## Conclusion

A mask is a type-3006 record named by image field 5. It is a drawable whose parent is the image, positioned relative to the image's corner, with an outline in the path form of shapes ([0217](0217-editable-shape.md), [0218](0218-oval.md)). The image itself is not cropped: a reader draws the whole image, clipped to the mask's outline placed at the mask's position. Here the oval sits at x = 50, centred on the 200-point-wide image.

## Confidence

*Likely*: image field 5 names a type-3006 mask, positioned relative to the image and holding a shape path.
