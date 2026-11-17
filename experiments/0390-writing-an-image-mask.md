# 0390: Writing an image mask's position and size

**Status:** run

A mask is a type-3006 record named by image field 5: a drawable whose parent is the image, positioned relative to the image's corner, with an outline in the path form of shapes (field 2.5, with a natural size in 2.5.2) ([0245](0245-image-mask.md)). This experiment moves the mask and changes its two sizes, and draws the exported page.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/0245/oval-mask.pages`: the red 8 × 4 image of [0023](0023-an-image.md), drawn 200 × 100 at (300, 300) and masked by an oval, mask 1732711, at (50, 0) and 100 × 100 within it, with a path of natural size 100 × 100 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and drawn with [`recipes/0373-draw-pdf.swift`](../recipes/0373-draw-pdf.swift) |

## Recipe

```bash
mkdir -p samples/0390
R=recipes/0302-set-path.py
F=samples/0245/oval-mask.pages
O=samples/0390
cp $F $O/original.pages
python3 -I $R $F $O/left.pages 1732711 1.1.1.1 float 0
python3 -I $R $F $O/wide.pages 1732711 1.1.1.1 float 0 1.1.2.1 float 200
python3 -I $R $F $O/natural-50.pages 1732711 1.1.1.1 float 0 1.1.2.1 float 200 2.5.2.1 float 50
python3 -I $R $F $O/natural-200.pages 1732711 1.1.1.1 float 0 2.5.2.1 float 200
for f in original left wide natural-50 natural-200; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0373-draw-pdf.swift $O/$f.pdf 300 300 200 100 10
done
```

## Observation

The image's 200 × 100 box, one character per 10 points; `o` is the red image, `.` the white page:

```
original                 left                     wide
........oooo........     ...oooo.............     ...oooo.............
......oooooooo......     .oooooooo...........     .oooooooo...........
.....oooooooooo.....     oooooooooo..........     oooooooooo..........
.....oooooooooo.....     oooooooooo..........     oooooooooo..........
......oooooooo......     .oooooooo...........     .oooooooo...........
........oooo........     ...oooo.............     ...oooo.............

natural-50               natural-200
.ooo................     ......oooooooo......
ooooo...............     .oooooooooooooooooo.
ooooo...............     oooooooooooooooooooo
ooooo...............     oooooooooooooooooooo
ooooo...............     .oooooooooooooooooo.
.ooo................     ......oooooooo......
```

Six of the ten rows drawn are shown; each row left out repeats a neighbour.

| File | Mask 1.1.1 | Mask 1.1.2 | Path 2.5.2 | Oval drawn |
| --- | --- | --- | --- | --- |
| `original.pages` | 50, 0 | 100 × 100 | 100 × 100 | x 50–150 |
| `left.pages` | 0, 0 | 100 × 100 | 100 × 100 | x 0–100 |
| `wide.pages` | 0, 0 | 200 × 100 | 100 × 100 | x 0–100 |
| `natural-50.pages` | 0, 0 | 200 × 100 | 50 × 100 | x 0–50 |
| `natural-200.pages` | 0, 0 | 100 × 100 | 200 × 100 | x 0–200 |

## Conclusion

The mask's position, 1.1.1, is measured from the image's corner, as read. Its size is not 1.1.2: Pages ignored a width of 200 there. It draws the mask's outline at the path's natural size, 2.5.2, stretching the path's points to fill it, so writing a natural width of 50 or 200 made the oval that wide. A reader should place a mask's outline at 1.1.1 and size it by 2.5.2; a writer should keep 1.1.2 equal to it, as Pages does.

## Confidence

*Confirmed*: a mask's position (1.1.1) relative to the image, and its drawn size as its path's natural size (2.5.2), by writing them. That 1.1.2 is ignored is *likely*.
