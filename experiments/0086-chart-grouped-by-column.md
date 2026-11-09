# 0086: Chart grouped by column

**Status:** run

[0067](0067-chart.md) found a chart's data in field 10000.7 of its record (type 5021), but with only one chart, a vertical bar chart grouped by row, the other fields of 10000 couldn't be told apart. This experiment is one of eight (0079–0086) that each change one thing about the chart: here, the grouping.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0067](0067-chart.md), `chart.key` (vertical_bar_2d, grouped by row) |

## Recipe

```bash
mkdir -p samples/0086
osascript recipes/0079-keynote-chart-type.applescript "$PWD/samples/0086/vertical_bar_2d-column.key" vertical_bar_2d column
```

The recipe adds the same 2 × 3 chart as 0067 to slide 1, with the type `vertical_bar_2d`, grouped by chart column.

## Observation

Compared with 0067's chart grouped by row, field 10000.5 is **2** here and 1 there. Everything else is unchanged, including field 10000.1 (1, vertical bar) and the data grid in 10000.7. The rows are still `r1` and `r2`, the columns `a`, `b` and `c`, and the values {1, 2, 3} and {4, 5, 6}.

## Conclusion

Field 10000.5 of a chart is how its data is grouped into series: 1 by row, 2 by column. The data grid is stored the same way either way, as rows of values with row and column names. So a reader builds the series from the grid's rows when 10000.5 is 1, and from its columns when it is 2.

## Confidence

*Likely*: chart field 10000.5 is the grouping, with 1 for row and 2 for column.
