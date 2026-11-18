# 0459: A series' points in a scatter chart

**Status:** run

A scatter chart's points kept the theme's blue when the series style's fill properties 6 to 17 were changed ([0457](0457-series-colours-by-chart-type.md)), and a line chart's line is stroke property 48 ([0458](0458-a-series-line-stroke.md)). This experiment looks for what colours a scatter chart's points among the style's other colours, shadows and strokes.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0296/baseline.key`, with chart 2655552 made a scatter chart (10000.1 = 9); the first series' style is 2651484. Its properties 54 to 58 are colours like 6 to 17, 30 to 34 are shadows (a colour, an angle of 130°, an offset, a blur of 10, an opacity of 0.5 and a switch), and 47, 48, 50, 51 and 53 solid blue strokes |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0459
O=samples/0459
python3 -I recipes/0302-set-path.py samples/0296/baseline.key $O/scatter.key 2655552 10000.1 varint 9
for k in 54 55 56 57 58 47 48 50 51 53; do
  python3 -I recipes/0302-set-path.py $O/scatter.key $O/scatter-$k.key 2651484 \
    10000.$k.1.3 float 1 10000.$k.1.4 float 0 10000.$k.1.5 float 0 10000.$k.1.12 varint 0
  sh recipes/0372-in-app.sh Keynote $O/scatter-$k.key "export d to POSIX file \"$PWD/$O/scatter-$k.pdf\" as PDF"
  swift recipes/0384-pdf-colours.swift $O/scatter-$k.pdf $(for y in $(seq 470 520); do for x in $(seq 700 740); do printf "%s,%s " $x $y; done; done)
done
```

The box from (700, 470) to (740, 520) holds the first series' middle point, which covers 155 blue points of the grid in `scatter.key`.

## Observation

| Property written red | Red points | Blue points |
| --- | --- | --- |
| none | 0 | 155 |
| colours 54 to 58, each | 0 | 155 |
| strokes 47, 48, 50 and 51, each | 0 | 155 |
| stroke 53 | 49 | 102 |

## Conclusion

Stroke property 53 is the outline of a scatter chart's points: written red, it drew a red ring of 49 grid points around a still blue centre. The points' fill is in none of the colour properties 6 to 17 and 54 to 58, nor the strokes; where it is is *unknown*. The theme's series style keeps it the same blue as everything else, so a reader can use property 53's colour for the whole point and be right for the documents Keynote makes.

## Confidence

*Confirmed*: series style property 53 as the outline of scatter points, by writing it. *Unknown*: where the points' fill is.
