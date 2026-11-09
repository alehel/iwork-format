# 0222: A chart in Pages

**Status:** run

Keynote charts are type-5021 drawables with their data in field 10000.7 ([0067](0067-chart.md)). AppleScript can only add charts in Keynote. This experiment inserts one in Pages through the menus, to see whether Pages stores it the same way.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0067](0067-chart.md) |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. Choose Insert → Chart → 2D Column (*Sett inn → Diagram → 2D-søyle*). Pages inserts a chart with its sample data.
3. Save it as `samples/0222/column.pages`.

## Observation

The chart goes into the text: the body becomes `One` and U+FFFC, and `Document.iwa` holds one type-5021 record whose drawable field 1.2 names the body. Its field 10000 has:

- **10000.1:** 1, a vertical bar (column) chart, as in Keynote.
- **10000.5:** 1, grouped by row.
- **10000.7:** the sample data, in Keynote's layout:
  - row names in 7.1: `Område 1`, `Område 2`
  - column names in 7.2: `April`, `Mai`, `Juni`, `Juli`
  - one 7.3 per row, each value a double: 17, 26, 53, 96 and 55, 43, 70, 58
  - UUIDs in 7.4

## Conclusion

Pages stores a chart exactly as Keynote does: a type-5021 drawable with its type in 10000.1 and its own copy of the data in 10000.7. The sample data's labels are in the app's language. A chart inserted from the menu sits in the text, like shapes and tables inserted that way.

## Confidence

*Confirmed*, with 0067: charts are type-5021 drawables whose data is in 10000.7, in Pages as in Keynote.
