# 0045: Row and column sizes

**Status:** run

[0029](0029-numbers-root-to-table.md) found that a table model's field 4.1 and 4.2 name two header storage buckets (type 6006), and [0021](0021-table-cells.md) saw floats of 120.4 in one of them, but neither said what they hold. This experiment changes one column's width and one row's height.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0045
osascript recipes/0045-numbers-sizes.applescript "$PWD/samples/0045/sizes.numbers"
```

The recipe sets the `width` of column 2 (B) to 200 and the `height` of row 3 to 50.

## Observation

Apart from `Metadata.iwa`, `ViewState.iwa` and the previews, only the two header storage buckets changed:

```
HeaderStorageBucket-904914-2.iwa (model field 4.1.2)
  empty:  1: 1
  sizes:  1: 1
          2: { 1: 2, 2: 50.0, 3: 0, 4: 0 }

HeaderStorageBucket-904958-2.iwa (model field 4.2)
  empty:  1: 1
          2: { 1: 5, 2: 98.0, 3: 0, 4: 0 }
          2: { 1: 6, 2: 98.0, 3: 0, 4: 0 }
  sizes:  1: 1
          2: { 1: 1, 2: 200.0, 3: 0, 4: 0 }
          2: { 1: 5, 2: 98.0, 3: 0, 4: 0 }
          2: { 1: 6, 2: 98.0, 3: 0, 4: 0 }
```

## Conclusion

Table model field 4.1 names the row headers and field 4.2 the column headers. Each header storage bucket (type 6006) lists, in its repeated field 2, the rows or columns that have their own settings. Field 1 is the row or column index, counted from 0, and field 2 is its height or width in points. Only rows and columns with a non-default size appear. A new Numbers table already lists columns 5 and 6 at 98 points, so its default width must be something else. In Pages' table of [0021](0021-table-cells.md), the four columns were listed at 120.4 points each.

A reader needs the default row height and column width, which this experiment doesn't show. They are probably in the table model or its style.

## Confidence

*Likely*: header storage buckets list rows (model 4.1) and columns (model 4.2) by index with their size in field 2, in points.

*Unknown*:

- The default row height and column width.
- Header fields 3 and 4, which were 0 throughout.
