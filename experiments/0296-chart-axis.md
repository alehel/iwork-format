# 0296: A chart's value axis

**Status:** run

[0295](0295-chart-options.md) found a chart's title and legend switches in a type-5023 record and its border in its chart style. This experiment changes three options of a chart's value axis, to see where axis settings are kept and whether they follow the same split.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Theme | The test theme ([0291](0291-test-theme.md)) |
| Chart | A 2D vertical bar chart from the [0067](0067-chart.md) recipe |

## Recipe

```bash
mkdir -p samples/0296
for n in baseline axis-title axis-line no-minimum; do
  IWORK_KEYNOTE_THEME='iwork-format test' osascript recipes/0067-keynote-chart.applescript "$PWD/samples/0296/$n.key"
done
```

Each copy but the baseline was opened on its own, the chart selected, and one option changed on the Format sidebar's Axis tab, Value (Y) (*Akse, Verdi (Y)*), before saving in place:

- `axis-title.key`: Axis Name (*Aksenavn*) turned on.
- `axis-line.key`: Axis Line (*Akselinje*) turned on.
- `no-minimum.key`: Show Minimum Value (*Vis minimumsverdi*) turned off; the axis's 0 label disappears.

Using a fresh copy for each change avoids the autosave problem of [0295](0295-chart-options.md).

## Observation

A chart drawable (type 5021) names eight sets of records in field 10000, in pairs of a style and a settings record:

| Field | Type | Count |
| --- | --- | --- |
| 10000.9, 10000.10 | 5022 chart style, 5023 chart settings | 1 each |
| 10000.11, 10000.12 | 5024, 5025 | 1 each |
| 10000.13, 10000.14 | 5026, 5027 | 2 each |
| 10000.15, 10000.16 | 5026, 5027 | 1 each |

In the baseline, the styles are the theme's named styles, and the settings records are empty.

| Change | What changes |
| --- | --- |
| Axis Name | The first type-5027 record in 10000.14 gets 10000.14 = 1, with 10001 = 1 and 10002 = 1 |
| Axis Line | The first entry of 10000.13 names a new, unnamed type-5026 style whose parent is the theme's axis style, with 10000.25 = 1 |
| Show Minimum Value off | The first entry of 10000.13 names a new unnamed type-5026 style, with 10000.31 = 0 |

For Axis Name and Axis Line, Keynote also gave the chart drawable a new ID and remade its settings records, all empty except the one changed. The second entries of 10000.13 and 10000.14 didn't change.

## Conclusion

A chart keeps each part's options in two records: a style, for properties that styles can share, and a settings record, for switches of that one chart. Field 10000.13 and 10000.14 hold the axes, the first entry being the value axis. Its line (10000.25) and whether it shows its minimum value (10000.31) are style properties, set through an unnamed child style as with the border in [0295](0295-chart-options.md). Its name switch (10000.14) is a setting. By their pairing, 10000.11 and 10000.12 are probably the legend, and 10000.15 and 10000.16 another axis; neither was tested here.

## Confidence

*Likely*: the pairing of style and settings records per chart part; value-axis style properties 10000.25 (axis line) and 10000.31 (show minimum); value-axis setting 10000.14 (axis name).

*Unknown*: what 10000.11 to 10000.12 and 10000.15 to 10000.16 belong to; what 10001 and 10002 in the settings records mean.
