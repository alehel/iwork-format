# 0224: Chart types only the menu offers

**Status:** run

[0195](0195-remaining-chart-types.md) completed the chart types AppleScript offers, leaving numbers 10 and 11 unexplained. The Insert → Chart menu offers more types: mixed, two-axis, radar, donut, bubble and four interactive charts. This experiment inserts one of each in Pages.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0195](0195-remaining-chart-types.md) and [0222](0222-pages-chart.md) |

## Recipe

For each type, in a new document with the body text `One`:

```bash
osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
```

choose Insert → Chart → the type, then save the document in `samples/0224/` under the name in the table.

## Observation

Each document has one type-5021 chart. Its field 10000.1 and the grouping in 10000.5:

| Menu item | Sample | 10000.1 | 10000.5 |
| --- | --- | --- | --- |
| 2D Mixed (*2D blandet*) | `mixed.pages` | 10 | 1 |
| 2D 2-Axis (*2D-2-akse*) | `two-axis.pages` | 11 | 1 |
| Interactive Column (*Interaktiv kolonne*) | `interactive-column.pages` | 20 | 1 |
| Interactive Bar (*Interaktiv stolpe*) | `interactive-bar.pages` | 21 | 1 |
| 2D Bubble (*2D-boble*) | `bubble.pages` | 22 | 2 |
| Interactive Scatter (*Interaktivt punkt*) | `interactive-scatter.pages` | 23 | 2 |
| Interactive Bubble (*Interaktiv boble*) | `interactive-bubble.pages` | 24 | 2 |
| 2D Donut (*2D-smultring*) | `donut.pages` | 25 | 2 |
| 2D Radar (*2D-radardiagram*) | `radar.pages` | 27 | 1 |

The data is in 10000.7 as for other charts. The interactive column chart's sample data has four rows instead of two.

## Conclusion

Types 10 and 11 are the mixed and two-axis charts, which AppleScript can't make. Types from 20 up came later: the interactive charts (20, 21, 23, 24), bubble (22), donut (25) and radar (27). The scatter and bubble kinds, and the donut, start grouped by column (2), because their sample data is laid out that way. Type 26 is probably the 3D bubble or another later kind that the menu doesn't offer.

## Confidence

*Likely*: the type numbers in the table.

*Unknown*: type 26.
