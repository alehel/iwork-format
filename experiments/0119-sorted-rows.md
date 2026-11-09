# 0119: Sorting rows

**Status:** run

This experiment sorts a column of a table, to see whether a sort order is stored or the data is rewritten.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0119
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0119/sort.numbers" sort
```

## Observation

The recipe puts 3, 1 and 2 in B2, B3 and B4, then sorts the table ascending by column B. The tile holds, by row, 1 (row 1), 2 (row 2) and 3 (row 3). The table model holds no sort setting that differs from an unsorted table.

## Conclusion

Sorting rewrites the cells in their new rows. A reader shows the rows in the stored order and needs nothing extra.

## Confidence

*Likely*: a sort rewrites the stored rows.
