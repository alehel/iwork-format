# 0067: A chart

**Status:** run

Numbers' AppleScript has no command for charts, but Keynote's has `add chart`. This experiment adds a small bar chart to a slide, to find where a chart keeps its data.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` |

## Recipe

```bash
mkdir -p samples/0067
osascript recipes/0067-keynote-chart.applescript "$PWD/samples/0067/chart.key"
```

The recipe adds a `vertical_bar_2d` chart to slide 1. It has rows `r1` and `r2`, columns `a`, `b` and `c`, and the data {1, 2, 3} and {4, 5, 6}, grouped by row.

## Observation

### The chart record

The slide's part gained a record of type 5021 (2652476). Its field 1 is the usual drawable block: position (168.1, 351.7), size 1656.9 × 456.0, and parent (1.2), the slide 2652175. Its field 10000 holds the chart:

```
10000:
  1: 1
  2: 2
  3: { 1: (−861.5, −364.7), 2: (1650.0, 39.0) }
  4: { 1: 2651517 }
  5: 1
  7:
    1: "r1"   1: "r2"                       ← row names
    2: "a"    2: "b"    2: "c"              ← column names
    3: { 1: {1: 1.0}, 1: {1: 2.0}, 1: {1: 3.0} }     ← row r1
    3: { 1: {1: 4.0}, 1: {1: 5.0}, 1: {1: 6.0} }     ← row r2
    4: …
  9 … 20: references to other objects, some repeated
```

### A new part and a fourth root

The package gained `Index/ObjectContainer.iwa`. Its first record is object 61, type 11008, which lists five new records in the same part: one of type 5023, one of type 5025 and three of type 5027.

Following header references from objects 1, 2 and 71 reaches 970 of the document's 971 objects. Only object 61 is left out. Adding 61 as a starting point reaches all 971.

## Conclusion

A chart is a drawable of type 5021. Its data is kept in the chart itself, in field 10000.7:

- row names in 7.1
- column names in 7.2
- one 7.3 per row, each a list of values as doubles (in field 1 of each entry)

A reader can draw the chart's data without any other record. The other fields of 10000 (type, grouping, axis and series styles) aren't decoded.

Adding a chart created `Index/ObjectContainer.iwa`, whose object 61 (type 11008) is a fourth root. No other object refers to it, and it lists records that look like chart, axis and series styles (types 5023, 5025 and 5027, each three times for the three columns or series). So the roots of a document are objects 1, 2 and 71, plus 61 when `ObjectContainer.iwa` exists.

## Confidence

*Likely*:

- A chart is type 5021, with its data in field 10000.7 as described.
- Object 61 in `ObjectContainer.iwa` is a fourth root.

*Unknown*:

- The other fields of 10000, such as the chart type and grouping.
- Whether Numbers charts are stored the same way.
