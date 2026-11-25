# 0456: Writing a chart series' colour

**Status:** run

A chart names six series styles (type 5028, `chart-0-series_0` and on) in its field 10000.17 ([0297](0297-chart-category-axis.md)). This experiment looks for the property that colours a column chart's bars, writing red into each colour property of the first series' style in turn.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0296/baseline.key`: a column chart (type 1) in the test theme with two series, blue and green. The first series' style is 2651484, whose properties in field 10000 include twelve colours, 6 to 17, all the same blue: 0.0006, 0.634, 1.0, with 12 = 1, the flag for a colour in Display P3 ([0329](0329-the-colour-space-field.md)) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

```bash
mkdir -p samples/0456
O=samples/0456
F=samples/0296/baseline.key
cp $F $O/baseline.key
for k in $(seq 6 17); do
  python3 -I recipes/0302-set-path.py $F $O/prop-$k.key 2651484 10000.$k.1.3 float 1 10000.$k.1.4 float 0 10000.$k.1.5 float 0
  sh recipes/0372-in-app.sh Keynote $O/prop-$k.key "export d to POSIX file \"$PWD/$O/prop-$k.pdf\" as PDF"
  swift recipes/0384-pdf-colours.swift $O/prop-$k.pdf 320,780
done
```

(320, 780) is inside the first series' first bar on the 1920 × 1080 slide.

## Observation

| Property written red | Bar's colour |
| --- | --- |
| none | 0, 0.64, 1 |
| 6 to 12, 14 to 17 | 0, 0.64, 1 |
| 13 | 1, 0.15, 0 |

Red written as 1, 0, 0 with the Display P3 flag is drawn as 1, 0.15, 0 in the exported page, as a P3 red converted to sRGB would be.

## Conclusion

Property 13 of a series style is the fill of that series' bars in a column chart. The other eleven colour properties hold the same colour but didn't change the bars; they are probably the series' colour for other chart types or parts, such as lines, areas, pie wedges and points, so a theme can colour each kind differently. Which is which is *unknown* until each is written into a chart of each type.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `baseline.key` | `0296/baseline.key` | `same bytes`, `5028#2651484 10000.13.1.5 = 1.0`, `5021#2655552 10000.1 = 1` | *Control*: the bars are blue |
| `prop-6.key` | `baseline.key` | Only `5028#2651484 10000.6.1.3: 0.0006 → 1.0`, `5028#2651484 10000.6.1.4: 0.6336 → 0.0`, `5028#2651484 10000.6.1.5: 1.0 → 0.0` | *Unknown*: what property 6 colours; the bar stays blue |
| `prop-7.key` | `baseline.key` | Only `5028#2651484 10000.7.1.3: 0.0006 → 1.0`, `5028#2651484 10000.7.1.4: 0.6336 → 0.0`, `5028#2651484 10000.7.1.5: 1.0 → 0.0` | *Unknown*: what property 7 colours; the bar stays blue |
| `prop-8.key` | `baseline.key` | Only `5028#2651484 10000.8.1.3: 0.0006 → 1.0`, `5028#2651484 10000.8.1.4: 0.6336 → 0.0`, `5028#2651484 10000.8.1.5: 1.0 → 0.0` | *Unknown*: what property 8 colours; the bar stays blue |
| `prop-9.key` | `baseline.key` | Only `5028#2651484 10000.9.1.3: 0.0006 → 1.0`, `5028#2651484 10000.9.1.4: 0.6336 → 0.0`, `5028#2651484 10000.9.1.5: 1.0 → 0.0` | *Unknown*: what property 9 colours; the bar stays blue |
| `prop-10.key` | `baseline.key` | Only `5028#2651484 10000.10.1.3: 0.0006 → 1.0`, `5028#2651484 10000.10.1.4: 0.6336 → 0.0`, `5028#2651484 10000.10.1.5: 1.0 → 0.0` | *Unknown*: what property 10 colours; the bar stays blue |
| `prop-11.key` | `baseline.key` | Only `5028#2651484 10000.11.1.3: 0.0006 → 1.0`, `5028#2651484 10000.11.1.4: 0.6336 → 0.0`, `5028#2651484 10000.11.1.5: 1.0 → 0.0` | *Unknown*: what property 11 colours; the bar stays blue |
| `prop-12.key` | `baseline.key` | Only `5028#2651484 10000.12.1.3: 0.0006 → 1.0`, `5028#2651484 10000.12.1.4: 0.6336 → 0.0`, `5028#2651484 10000.12.1.5: 1.0 → 0.0` | *Unknown*: what property 12 colours; the bar stays blue |
| `prop-13.key` | `baseline.key` | Only `5028#2651484 10000.13.1.3: 0.0006 → 1.0`, `5028#2651484 10000.13.1.4: 0.6336 → 0.0`, `5028#2651484 10000.13.1.5: 1.0 → 0.0` | *Confirmed*: property 13 is the fill of a column chart's bars; the bar is red |
| `prop-14.key` | `baseline.key` | Only `5028#2651484 10000.14.1.3: 0.0006 → 1.0`, `5028#2651484 10000.14.1.4: 0.6336 → 0.0`, `5028#2651484 10000.14.1.5: 1.0 → 0.0` | *Unknown*: what property 14 colours; the bar stays blue |
| `prop-15.key` | `baseline.key` | Only `5028#2651484 10000.15.1.3: 0.0006 → 1.0`, `5028#2651484 10000.15.1.4: 0.6336 → 0.0`, `5028#2651484 10000.15.1.5: 1.0 → 0.0` | *Unknown*: what property 15 colours; the bar stays blue |
| `prop-16.key` | `baseline.key` | Only `5028#2651484 10000.16.1.3: 0.0006 → 1.0`, `5028#2651484 10000.16.1.4: 0.6336 → 0.0`, `5028#2651484 10000.16.1.5: 1.0 → 0.0` | *Unknown*: what property 16 colours; the bar stays blue |
| `prop-17.key` | `baseline.key` | Only `5028#2651484 10000.17.1.3: 0.0006 → 1.0`, `5028#2651484 10000.17.1.4: 0.6336 → 0.0`, `5028#2651484 10000.17.1.5: 1.0 → 0.0` | *Unknown*: what property 17 colours; the bar stays blue |

## Confidence

*Confirmed*: series style property 13 as a column chart's bar fill, by writing it. *Unknown*: what properties 6 to 12 and 14 to 17 colour.
