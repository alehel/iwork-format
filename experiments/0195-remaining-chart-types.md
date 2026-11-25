# 0195: The remaining chart types

**Status:** run

[0079](0079-pie-chart.md) to [0086](0086-chart-grouped-by-column.md) mapped eight chart types to their numbers in field 10000.1. Keynote's AppleScript offers nine more. This experiment makes one chart of each, to complete the table.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0079](0079-pie-chart.md)–[0086](0086-chart-grouped-by-column.md) |

## Recipe

```bash
mkdir -p samples/0195
for t in stacked_horizontal_bar_2d pie_3d stacked_vertical_bar_3d horizontal_bar_3d stacked_horizontal_bar_3d stacked_area_2d line_3d area_3d stacked_area_3d; do
  osascript recipes/0079-keynote-chart-type.applescript "$PWD/samples/0195/$t-row.key" $t row
done
```

Each presentation has the same 2 × 3 chart as 0067 on slide 1, grouped by row.

## Observation

In each chart drawable (type 5021), field 10000.1 is:

| AppleScript type | 10000.1 |
| --- | --- |
| `stacked_horizontal_bar_2d` | 7 |
| `stacked_area_2d` | 8 |
| `horizontal_bar_3d` | 13 |
| `line_3d` | 14 |
| `area_3d` | 15 |
| `pie_3d` | 16 |
| `stacked_vertical_bar_3d` | 17 |
| `stacked_horizontal_bar_3d` | 18 |
| `stacked_area_3d` | 19 |

Fields 10000.2 (2) and 10000.5 (1, by row) are the same in all nine. The data grid in 10000.7 is identical across them, apart from UUIDs.

## Conclusion

Chart types run from 1 to 19. The 2D types are 1–9, with the stacked ones after the plain ones. The 3D types are 12–19, in the order vertical bar, horizontal bar, line, area, pie, then the three stacked types. Numbers 10 and 11 weren't produced by any AppleScript type; they are probably the kinds AppleScript doesn't offer, such as bubble or mixed charts. As before, the type doesn't change how the data is stored.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `stacked_horizontal_bar_2d-row.key` | `0079/pie_2d-row.key` | `5021 10000.1: 5 → 7` | *Likely*: chart type 7 is a stacked horizontal bar chart |
| `stacked_area_2d-row.key` | `0079/pie_2d-row.key` | `5021 10000.1: 5 → 8` | *Likely*: chart type 8 is a stacked area chart |
| `horizontal_bar_3d-row.key` | `0079/pie_2d-row.key` | `5021 10000.1: 5 → 13` | *Likely*: chart type 13 is a 3D horizontal bar chart |
| `line_3d-row.key` | `0079/pie_2d-row.key` | `5021 10000.1: 5 → 14` | *Likely*: chart type 14 is a 3D line chart |
| `area_3d-row.key` | `0079/pie_2d-row.key` | `5021 10000.1: 5 → 15` | *Likely*: chart type 15 is a 3D area chart |
| `pie_3d-row.key` | `0079/pie_2d-row.key` | `5021 10000.1: 5 → 16` | *Likely*: chart type 16 is a 3D pie chart |
| `stacked_vertical_bar_3d-row.key` | `0079/pie_2d-row.key` | `5021 10000.1: 5 → 17` | *Likely*: chart type 17 is a 3D stacked vertical bar chart |
| `stacked_horizontal_bar_3d-row.key` | `0079/pie_2d-row.key` | `5021 10000.1: 5 → 18` | *Likely*: chart type 18 is a 3D stacked horizontal bar chart |
| `stacked_area_3d-row.key` | `0079/pie_2d-row.key` | `5021 10000.1: 5 → 19` | *Likely*: chart type 19 is a 3D stacked area chart |

## Confidence

*Likely*: the numbers in the table above.

*Unknown*: types 10 and 11.
