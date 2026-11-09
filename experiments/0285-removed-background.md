# 0285: A removed background

**Status:** run

Pages can remove an image's background automatically (Format → Image → Remove Background). [0284](0284-image-adjustments.md) found that adjustments are stored with a pre-rendered copy. This experiment removes a background, to see whether it is stored as a new image with transparency or as instructions.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0245](0245-image-mask.md) and [0284](0284-image-adjustments.md) |

## Recipe

```bash
mkdir -p samples/0285
cd samples/0285
python3 -c "import struct,zlib; w,h=64,48; rows=b''.join(b'\x00'+b''.join((b'\xff\x00\x00' if 16<=x<48 and 12<=y<36 else b'\xff\xff\xff') for x in range(w)) for y in range(h)); c=lambda t,d: struct.pack('>I',len(d))+t+d+struct.pack('>I',zlib.crc32(t+d)&0xffffffff); open('square.png','wb').write(b'\x89PNG\r\n\x1a\n'+c(b'IHDR',struct.pack('>IIBBBBB',w,h,8,2,0,0,0))+c(b'IDAT',zlib.compress(rows))+c(b'IEND',b''))"
cd ../..
osascript recipes/0244-pages-image.applescript "$PWD/samples/0285/square.png"
```

`square.png` is 64 × 48 pixels: white, with a red square from (16, 12) to (48, 36). The recipe places it at 200 × 100 points; Pages keeps its proportions and shows it at 133.3 × 100. Then, with Pages in front:

1. Choose Format → Image → Remove Background (*Format → Bilde → Fjern bakgrunn*). The white disappears.
2. Click Done (*Ferdig*), and save as `samples/0285/no-background.pages`.

## Observation

The package still holds only `Data/square-24.png`, unchanged: 64 × 48 RGB with no alpha channel. The image record (type 3005) gains:

- **Field 22:** 1.
- **Field 10:** a path in the element layout of shape paths ([0217](0217-editable-shape.md)), with kinds 1 (move), 2 (line) ×6, 4 (curve) ×2, 5 (close) and 1. Its first point is (30, 36.06), in the image's pixels, on the lower edge of the red square.
- **Field 5:** a mask (type 3006, [0245](0245-image-mask.md)) at (32.3, 24.0), 68.75 × 52.2 points in the image's space, roughly the square's bounds.

## Conclusion

Removing a background doesn't touch the image file. Pages stores an outline of the subject in the image's own pixel coordinates (field 10), turns it on with field 22, and adds a mask that crops the image to the subject's bounds. A reader can show the result by clipping the image to the field-10 path, scaled from the image's pixel size (field 9) to its drawn size, or at least by applying the mask. A reader that ignores both shows the original image with its background.

## Confidence

*Likely*:

- Image field 10 is the outline left by Remove Background, in image pixels.
- Field 22 turns it on.

*Unknown*: whether the outline replaces or combines with the mask when both are shown.
