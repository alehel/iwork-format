# 0083: Area chart

**Status:** run

[0067](0067-chart.md) found a chart's data in field 10000.7 of its record (type 5021), but with only one chart, a vertical bar chart grouped by row, the other fields of 10000 couldn't be told apart. This experiment is one of eight (0079–0086) that each change one thing about the chart: here, the type, to area.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0067](0067-chart.md), `chart.key` (vertical_bar_2d, grouped by row) |

## Recipe

```bash
mkdir -p samples/0083
osascript recipes/0079-keynote-chart-type.applescript "$PWD/samples/0083/area_2d-row.key" area_2d row
```

The recipe adds the same 2 × 3 chart as 0067 to slide 1, with the type `area_2d`, grouped by chart row.

## Observation

Compared with the vertical bar chart of 0067, the chart record (type 5021) differs only in field 10000.1, which is **4** here and 1 there. Fields 10000.2 (2), 10000.5 (1) and the other scalar fields of 10000 are unchanged. So are the data grid in 10000.7 (rows `r1`, `r2`, columns `a`, `b`, `c`, values {1, 2, 3} and {4, 5, 6}) and the counts of the repeated fields 13, 14, 17 and 20.

## Conclusion

Field 10000.1 of a chart is its type, and 4 is a area chart. The data is stored the same way whatever the type, so a reader can always get the numbers and labels from 10000.7, even for a type it can't draw. The values of 10000.1 found so far:

| Type (AppleScript) | 10000.1 | Experiment |
| --- | --- | --- |
| vertical_bar_2d | 1 | [0067](0067-chart.md) |
| horizontal_bar_2d | 2 | [0080](0080-horizontal-bar-chart.md) |
| line_2d | 3 | [0082](0082-line-chart.md) |
| area_2d | 4 | [0083](0083-area-chart.md) |
| pie_2d | 5 | [0079](0079-pie-chart.md) |
| stacked_vertical_bar_2d | 6 | [0081](0081-stacked-vertical-bar-chart.md) |
| scatterplot_2d | 9 | [0084](0084-scatter-chart.md) |
| vertical_bar_3d | 12 | [0085](0085-3d-vertical-bar-chart.md) |

The numbers skip some values (7, 8, 10, 11), presumably for the stacked, 3D and other types not tried here.

## Confidence

*Likely*: chart field 10000.1 = 4 is a area chart.
