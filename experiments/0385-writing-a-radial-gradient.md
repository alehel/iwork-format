# 0385: Writing a radial gradient's angle

**Status:** run

A radial gradient has kind 1 in gradient field 1, field 4 set to 1, and an angle of 315° in 5.2 ([0275](0275-radial-gradient.md)). Writing only the kind into a linear gradient at 270° gave a radial gradient that wasn't centred on the shape ([0384](0384-writing-a-gradient.md)). This experiment writes the other two fields and reads the colours over a grid.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/0384/radial.pages`: shape 1732647, 100 × 100 at (300, 300), with a red-to-green gradient of kind 1 at 270°, in style 1732719. `samples/0275/radial.pages`: a radial gradient Pages made, light blue to dark blue |
| Writer | [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0385
N=recipes/0383-set-nth-path.py
O=samples/0385
G=1.11.1.2
cp samples/0275/radial.pages $O/pages-radial.pages
cp samples/0384/radial.pages $O/written-radial.pages
python3 -I $N samples/0384/radial.pages $O/radial-advanced.pages 1732719 $G.4 varint 1
python3 -I $N samples/0384/radial.pages $O/radial-315.pages 1732719 $G.5.2 float 5.497787
python3 -I $N samples/0384/radial.pages $O/radial-90.pages 1732719 $G.5.2 float 1.570796
pts=""; for y in 305 325 350 375 395; do for x in 305 325 350 375 395; do pts="$pts $x,$y"; done; done
for f in pages-radial written-radial radial-advanced radial-315 radial-90; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0384-pdf-colours.swift $O/$f.pdf $pts
done
```

## Observation

The red component over a 5 × 5 grid of the shape, from (305, 305) at the top left to (395, 395) at the bottom right. For the written gradients red is 1 at the first stop and 0 at the second; for Pages' own, the first stop's red is 0.34 and the second's 0.

```
pages-radial (315°)          written-radial (270°)        radial-315                   radial-90
.04 .09 .13 .10 .04          .00 .15 .41 .53 .45          .12 .29 .37 .30 .12          .00 .00 .00 .00 .00
.10 .17 .22 .18 .10          .00 .26 .60 .80 .67          .28 .51 .65 .51 .30          .00 .00 .00 .00 .00
.13 .22 .33 .22 .12          .01 .28 .61 .85 .69          .37 .65 .99 .66 .37          .00 .00 .08 .15 .11
.09 .17 .22 .17 .10          .00 .14 .38 .50 .43          .28 .51 .65 .51 .29          .00 .13 .38 .49 .42
.04 .09 .13 .10 .04          .00 .00 .15 .23 .18          .11 .28 .37 .29 .12          .00 .26 .57 .77 .65
```

`radial-advanced.pages`, with field 4 set to 1, gave exactly the same colours as `written-radial.pages`.

## Conclusion

For a radial gradient the angle in 5.2 doesn't only turn it: it moves the centre. At 315°, the angle Pages uses, the first stop's colour is at the middle of the shape and the gradient falls off evenly towards the corners, as in Pages' own radial gradient. At 270° the centre moved right of the middle, and at 90° to the bottom right, partly outside the shape. Field 4 changes nothing that is drawn, which fits its reading as a mark of the advanced editor. So a writer should give a radial gradient the angle 315° to centre it. How the angle places the centre in general wasn't worked out.

## Confidence

*Confirmed*: a radial gradient (kind 1) at 315° is centred on the shape, and field 4 doesn't change the drawing, by writing them. How other angles place the centre is *unknown*; a finer grid over more angles would settle it.
