# 0458: A series' line in a line chart

**Status:** run

A series style's colour properties 6 to 17 are fills, and a line chart's line took its colour from none of them ([0457](0457-series-colours-by-chart-type.md)). The style also has eleven stroke properties, 4, 5 and 45 to 53, each a stroke as for shapes: a colour in 1, a width in 2 and a pattern in 6, whose kind is 1 for solid and 2 for none ([0250](0250-shape-border.md)). This experiment writes red into each solid blue stroke and looks at the line.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0296/baseline.key`, with chart 2655552 made a line chart (10000.1 = 3). In the first series' style, 2651484, the strokes are black (4, 5), grey and none (45, 49), black and none (46, 52), and solid blue of width 1 (47, 50), 6 (48, 51) and 3 (53) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0458
O=samples/0458
python3 -I recipes/0302-set-path.py samples/0296/baseline.key $O/line.key 2655552 10000.1 varint 3
for k in 47 48 50 51 53; do
  python3 -I recipes/0302-set-path.py $O/line.key $O/line-$k.key 2651484 \
    10000.$k.1.3 float 1 10000.$k.1.4 float 0 10000.$k.1.5 float 0 10000.$k.1.12 varint 0
  sh recipes/0372-in-app.sh Keynote $O/line-$k.key "export d to POSIX file \"$PWD/$O/line-$k.pdf\" as PDF"
  swift recipes/0384-pdf-colours.swift $O/line-$k.pdf $(for y in $(seq 630 680); do printf "990,%s " $y; done)
done
```

The points run down a column through the first series' line, every point from y = 630 to 680.

## Observation

| Stroke written red | Red points | Blue points |
| --- | --- | --- |
| 47 (width 1) | 0 | 6 |
| 48 (width 6) | 6 | 0 |
| 50 (width 1) | 0 | 6 |
| 51 (width 6) | 0 | 6 |
| 53 (width 3) | 0 | 6 |

## Conclusion

Stroke property 48 draws a line chart's line: written red, the whole line is red, and the line is 6 points thick where it crosses the column, the stroke's width. The other solid strokes didn't change it; with their widths and the fills of 0457 they are probably the outlines and lines of other chart types. A reader drawing a line chart should take each series' line from its style's property 48.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `line.key` | `0296/baseline.key` | Only `5021#2655552 10000.1: 1 → 3` | *Control*: the input of the others |
| `line-47.key` | `line.key` | Only `5028#2651484 10000.47.1.3: 0.0006 → 1.0`, `5028#2651484 10000.47.1.4: 0.6336 → 0.0`, `5028#2651484 10000.47.1.5: 1.0 → 0.0`, `5028#2651484 10000.47.1.12: 1 → 0` | *Likely*: property 47 isn't the line's stroke; the line stays blue |
| `line-48.key` | `line.key` | Only `5028#2651484 10000.48.1.3: 0.0006 → 1.0`, `5028#2651484 10000.48.1.4: 0.6336 → 0.0`, `5028#2651484 10000.48.1.5: 1.0 → 0.0`, `5028#2651484 10000.48.1.12: 1 → 0` | *Confirmed*: property 48 is a line chart's line; the line is red, 6 points thick |
| `line-50.key` | `line.key` | Only `5028#2651484 10000.50.1.3: 0.0006 → 1.0`, `5028#2651484 10000.50.1.4: 0.6336 → 0.0`, `5028#2651484 10000.50.1.5: 1.0 → 0.0`, `5028#2651484 10000.50.1.12: 1 → 0` | *Likely*: property 50 isn't the line's stroke; the line stays blue |
| `line-51.key` | `line.key` | Only `5028#2651484 10000.51.1.3: 0.0006 → 1.0`, `5028#2651484 10000.51.1.4: 0.6336 → 0.0`, `5028#2651484 10000.51.1.5: 1.0 → 0.0`, `5028#2651484 10000.51.1.12: 1 → 0` | *Likely*: property 51 isn't the line's stroke; the line stays blue |
| `line-53.key` | `line.key` | Only `5028#2651484 10000.53.1.3: 0.0006 → 1.0`, `5028#2651484 10000.53.1.4: 0.6336 → 0.0`, `5028#2651484 10000.53.1.5: 1.0 → 0.0`, `5028#2651484 10000.53.1.12: 1 → 0` | *Likely*: property 53 isn't the line's stroke; the line stays blue |

## Confidence

*Confirmed*: series style property 48 as a line chart's line, colour and width, by writing its colour.
