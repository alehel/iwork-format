# 0297: A chart's category axis, series and text styles

**Status:** run

[0296](0296-chart-axis.md) found that a chart names pairs of style and settings records for its parts, the value axis in fields 10000.13 and 10000.14, and left the pair in 10000.15 and 10000.16 unidentified. This experiment turns on the category axis's name, and lists the chart's other style references.

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
mkdir -p samples/0297
for n in baseline x-axis-name; do
  IWORK_KEYNOTE_THEME='iwork-format test' osascript recipes/0067-keynote-chart.applescript "$PWD/samples/0297/$n.key"
done
```

In `x-axis-name.key`, the chart was selected and Axis Name (*Aksenavn*) turned on in the Format sidebar's Axis tab, Category (X) (*Akse, Kategori (X)*), and the file saved in place. Value labels (Series tab) were also planned, but their setting is a pop-up menu, which needs the screen, so they weren't tested.

## Observation

Only field 10000.16 changed: it names a new type-5027 record with 10000.13 = 1, plus 10001 = 1 and 10002 = 1, as the value axis's settings did in [0296](0296-chart-axis.md). The value axis's name setting was 10000.14, so each axis has its own field for its name.

The chart's other references, in the baseline:

| Field | Records | Named, in the stylesheet |
| --- | --- | --- |
| 10000.17 | 6 of type 5028 | `chart-0-series_0` to `chart-0-series_5` |
| 10000.18, 10000.19 | A reference to 0 | |
| 10000.20 | 25 of type 2022 | `chart-0-paragraphStyle_0` and so on |

## Conclusion

A chart's category axis is the pair in 10000.15 (style, type 5026) and 10000.16 (settings, type 5027), and its name is shown when setting 10000.13 = 1. The pair in 10000.13 and 10000.14, which has two entries each, holds the value axes. The second is probably the second value axis of a two-axis chart. The chart names six series styles (type 5028), one per series colour of the theme, and 25 paragraph styles (type 2022) for its text, all of them the theme's named styles.

## Confidence

*Likely*: 10000.15 and 10000.16 are the category axis, with setting 10000.13 its name switch; 10000.17 the series styles; 10000.20 the chart's paragraph styles.

*Unknown*: what the second value-axis entries and 10000.18 and 10000.19 are for.
