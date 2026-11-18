# 0457: A series' colours by chart type

**Status:** run

A series style has twelve colour properties, 6 to 17, all the same colour in the theme, and property 13 is the fill of a column chart's bars ([0456](0456-writing-a-series-colour.md)). This experiment gives each of the twelve its own colour and draws the chart as other types.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0296/baseline.key`: chart 2655552 in the test theme, two series; the first series' style is 2651484 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh), looked at as pictures and read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) |

## Recipe

Each property gets a colour of its own, in sRGB (its field 12 set to 0):

| Property | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Colour | red | green | blue | yellow | magenta | cyan | dark red | dark green | navy | olive | purple | teal |

```bash
mkdir -p samples/0457
O=samples/0457
args=()
while read k r g b; do
  args+=(10000.$k.1.3 float $r 10000.$k.1.4 float $g 10000.$k.1.5 float $b 10000.$k.1.12 varint 0)
done <<EOF
6 1 0 0
7 0 1 0
8 0 0 1
9 1 1 0
10 1 0 1
11 0 1 1
12 0.5 0 0
13 0 0.5 0
14 0 0 0.5
15 0.5 0.5 0
16 0.5 0 0.5
17 0 0.5 0.5
EOF
python3 -I recipes/0302-set-path.py samples/0296/baseline.key $O/palette.key 2651484 "${args[@]}"
for t in 1 3 4 5 9; do
  python3 -I recipes/0302-set-path.py $O/palette.key $O/type-$t.key 2655552 10000.1 varint $t
  sh recipes/0372-in-app.sh Keynote $O/type-$t.key "export d to POSIX file \"$PWD/$O/type-$t.pdf\" as PDF"
done
```

Chart types: 1 column, 3 line, 4 area, 5 pie, 9 scatter ([keynote.md](../spec/keynote.md#charts)).

## Observation

| Type | The first series is drawn | Colour | Property |
| --- | --- | --- | --- |
| 1, column | bars | 0, 0.5, 0, dark green | 13 |
| 4, area | an area | 0, 1, 1, cyan | 11 |
| 5, pie | the first wedge | 0, 0.5, 0.5, teal | 17 |
| 3, line | a line | the theme's blue, unchanged | none of 6–17 |
| 9, scatter | points | the theme's blue, unchanged | none of 6–17 |

The second series kept its green throughout, since only the first series' style was written.

## Conclusion

The twelve colour properties are fills, one per kind of shape a series can be drawn as: 13 for bars, 11 for areas and 17 for pie wedges. Lines and points don't take their colour from any of them; they are probably in the style's stroke properties (the 86-byte properties 4, 5 and 45 to 53) and symbol properties. Which fill the other nine properties are, presumably for the other chart types such as 3D and bubble charts, is *unknown*.

## Confidence

*Confirmed*: series style properties 13, 11 and 17 as the fill of bars, areas and pie wedges, by writing them. *Likely*: lines and points are coloured by other properties.
