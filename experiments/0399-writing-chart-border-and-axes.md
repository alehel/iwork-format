# 0399: Writing a chart's border and axis options

**Status:** run

A chart's border is chart style property 10000.18 = 1 ([0295](0295-chart-options.md)). For the value axis, style property 10000.25 = 1 draws the axis line, 10000.31 = 0 hides the minimum value, and setting 10000.14 = 1 shows the axis name ([0296](0296-chart-axis.md)). Keynote set the style properties through new unnamed styles. This experiment writes each into the baseline, here into the theme's own styles, and compares the exported slide with the one Keynote made for the same option.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0296/baseline.key`: a bar chart in the test theme, chart 2655552, whose 10000.9 names the theme's chart style 2651479, whose first 10000.13 names the theme's value-axis style 2651481, and whose first 10000.14 names an empty settings record, 2655559. Keynote's own versions: `samples/0295/border.key` and `samples/0296/axis-line.key`, `axis-title.key` and `no-minimum.key` |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and compared with the new [`recipes/0399-pdf-diff.swift`](../recipes/0399-pdf-diff.swift) |

*Corrected 2026-11-25:* settings record 2655559 holds 10001 = 1 and 10002 = 1 already; only its 10000 is empty.

## Recipe

```bash
mkdir -p samples/0399
R=recipes/0302-set-path.py
B=samples/0296/baseline.key
O=samples/0399
cp $B $O/baseline.key
for f in samples/0295/border.key samples/0296/axis-line.key samples/0296/axis-title.key samples/0296/no-minimum.key; do
  cp $f $O/keynote-$(basename $f)
done
python3 -I $R $B $O/axis-name.key 2655559 10000.14 varint 1 10001 varint 1 10002 varint 1
python3 -I $R $B $O/border.key 2651479 10000.18 varint 1
python3 -I $R $B $O/axis-line.key 2651481 10000.25 varint 1
python3 -I $R $B $O/no-minimum.key 2651481 10000.31 varint 0
python3 -I $R $O/keynote-border.key $O/keynote-border-off.key 2655837 10000.18 varint 0
for f in $O/*.key; do
  sh recipes/0372-in-app.sh Keynote $f "export d to POSIX file \"$PWD/${f%.key}.pdf\" as PDF"
done
swift recipes/0399-pdf-diff.swift $O/baseline.pdf $O/keynote-*.pdf $O/border.pdf $O/axis-line.pdf $O/axis-name.pdf $O/no-minimum.pdf
```

`recipes/0399-pdf-diff.swift` draws two first pages and reports how many pixels differ, and where. The settings record gets 10001 = 1 and 10002 = 1 as well, as Keynote wrote them. 2655837 is the unnamed style Keynote made for the border.

## Observation

Compared with the baseline's slide (1920 × 1080):

| File | Pixels that differ | Where | Same as Keynote's own |
| --- | --- | --- | --- |
| `keynote-border.pdf` | 12,429 | 95.5, 339.5 – 1826, 820.5 | |
| `border.pdf` | 12,429 | the same | yes |
| `keynote-border-off.pdf` | 0 | | |
| `keynote-axis-line.pdf` | 3,981 | 95.5, 339.5 – 169, 820.5 | |
| `axis-line.pdf` | 3,981 | the same | yes |
| `keynote-axis-title.pdf` | 5,980 | 43.5, 507 – 68.5, 653.5 | |
| `axis-name.pdf` | 5,980 | the same | yes |
| `keynote-no-minimum.pdf` | 861 | 124.5, 795.5 – 141.5, 820.5 | |
| `no-minimum.pdf` | 861 | the same | yes |

The PDF's text gains `Verdiakse` (value axis) with the axis name, and loses the `0` at the bottom of the axis without the minimum value.

## Conclusion

Each option draws exactly as Keynote's own, pixel for pixel: chart style property 10000.18 is the border, value-axis style property 10000.25 the axis line, 10000.31 = 0 hides the minimum value, and value-axis setting 10000.14 = 1 shows the axis name, in the app's language. Clearing 10000.18 in Keynote's unnamed style takes the border away again. It makes no difference whether a property is set in the theme's named style or in an unnamed child, as for text styles ([0393](0393-writing-a-style-parent.md)).

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `baseline.key` | `0296/baseline.key` | `same bytes` | *Control* |
| `keynote-border.key` | `0295/border.key` | `same bytes`, `5022#2655837 10000.18 = 1` | *Control*: Keynote's own border |
| `border.key` | `baseline.key` | Only `5022#2651479 10000.18: 0 → 1` | *Confirmed*: chart style 10000.18 is the border, drawn as Keynote's own |
| `keynote-border-off.key` | `keynote-border.key` | Only `5022#2655837 10000.18: 1 → 0` | *Confirmed*: clearing it takes the border away |
| `keynote-axis-line.key` | `0296/axis-line.key` | `same bytes`, `5026 10000.25 = 1` | *Control*: Keynote's own axis line |
| `axis-line.key` | `baseline.key` | Only `5026#2651481 10000.25: 0 → 1` | *Confirmed*: value-axis style 10000.25 is the axis line, drawn as Keynote's own |
| `keynote-axis-title.key` | `0296/axis-title.key` | `same bytes`, `5027 10000.14 = 1` | *Control*: Keynote's own axis name |
| `axis-name.key` | `baseline.key` | Only `5027#2655559 10000.14: absent → 1`, `5027#2655559 10000: "" → x"7001"` | *Confirmed*: value-axis setting 10000.14 shows the axis name, drawn as Keynote's own |
| `keynote-no-minimum.key` | `0296/no-minimum.key` | `same bytes`, `5026 10000.31 = 0` | *Control*: Keynote's own axis without the minimum |
| `no-minimum.key` | `baseline.key` | Only `5026#2651481 10000.31: 1 → 0` | *Confirmed*: value-axis style 10000.31 at 0 hides the minimum, drawn as Keynote's own |

## Confidence

*Confirmed*: the chart border, the value axis line, hiding the minimum value and the value axis name, by writing them.
