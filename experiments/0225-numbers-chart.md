# 0225: A chart in Numbers

**Status:** run

Charts in Keynote and Pages keep their own copy of their data in field 10000.7 ([0067](0067-chart.md), [0222](0222-pages-chart.md)). A Numbers chart is drawn from table cells, and follows them when they change. This experiment makes a chart from cells, to see how the link is stored.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0222](0222-pages-chart.md) |

## Recipe

```bash
mkdir -p samples/0225
osascript recipes/0225-numbers-chart-data.applescript
```

The recipe fills A1:C3 of table 1 and selects it:

| | A | B | C |
| --- | --- | --- | --- |
| 1 | | x | y |
| 2 | r1 | 1 | 2 |
| 3 | r2 | 3 | 4 |

Then choose Insert → Chart → 2D Column (*Sett inn → Diagram → 2D-søyle*) and save as `samples/0225/linked.numbers`. Numbers draws two series, x and y, over the categories r1 and r2.

## Observation

The chart is a type-5021 record, in `CalculationEngine.iwa`. Its field 10000.1 is 1 and 10000.5 is 1. Field 10000.7 holds a copy of the data: `x` and `y` in 7.1, `r1` and `r2` in 7.2, then the values 1, 3 and 2, 4, so each 7.3 is a series. Unlike the Pages chart, field 10000.8 names another record, 905524, of type 12006:

```
1: { 2: 4294967295, 3: 2 }
2: "383AEA13-…"                  ← a UUID
3: { 1: formula, 1: formula,      ← series values
     3: formula, 3: formula,      ← category labels
     4: formula, 4: formula,      ← series names
     5: 2, 10: 0 }
```

Each formula uses the node form of cell formulas ([0035](0035-formula-references.md)). Each cell reference (type 36) names the table by UUID in 28.1. Columns and rows are zigzag-encoded and not absolute, so they read as indexes from A1.

| Field | Formulas |
| --- | --- |
| 3.1 | `B2`, `B3`, node 29, call 175 with 1 argument; then the same over `C2`, `C3` |
| 3.3 | `A2`, call 175; `A3`, call 175 |
| 3.4 | `B1`, call 175; `C1`, call 175 |

## Conclusion

A Numbers chart links to its table through a type-12006 record named in 10000.8. That record holds one formula per series for its values (3.1), plus formulas for the category labels (3.3) and the series names (3.4), and the grouping (3.5, 2 here: series are columns). Node type 29 joins two references into a range, the `:` operator. Function 175 seems to be an internal function that wraps a chart's references; it isn't one users type. Field 10000.7 still holds a copy of the values, so a reader can draw the chart without evaluating the formulas.

## Confidence

*Likely*:

- A Numbers chart links to cells through a type-12006 record whose field 3 holds formulas for values, labels and names.
- Node 29 is a range operator.

*Unknown*: function 175, field 1 of type 12006, and why its references are stored as relative.
