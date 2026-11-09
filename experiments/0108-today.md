# 0108: TODAY

**Status:** run

[0031](0031-cell-kinds.md), [0035](0035-formula-references.md), [0064](0064-operators-and-functions.md) and [0066](0066-comparisons-and-if.md) decoded formula nodes for numbers, references, ranges, operators and a few functions. This experiment, one of ten (0103–0112) that each write one formula, asks: how is a function with no arguments stored, and how is a date result cached?

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0064](0064-operators-and-functions.md) |

## Recipe

```bash
mkdir -p samples/0108
osascript recipes/0103-numbers-formula.applescript "$PWD/samples/0108/today.numbers" '=TODAY()'
```

The recipe sets B2 to 4 and C2 to 2, and writes `=TODAY()` in E2.

## Observation

The formula is one node, `16  function 154, 0 arguments`. The cell's bytes:

```
05 05 …  04 92 00 00  <8-byte double>  01 00 00 00  03 00 00 00  03 00 00 00
```

That is type 5 (date) with flags 0x9204: a date value (0x4), a formula key (0x200), the 0x1000 key and a date format key (0x8000).

## Conclusion

TODAY is function 154, called with no arguments. A formula's cached result keeps the kind of its value: here a date cell (type 5) with the date as a double, the formula key and a date format. A reader shows the cached date. TODAY changes daily, so Numbers recomputes it when it opens the file.

## Confidence

*Likely*: TODAY is function 154, and a formula's cached result is stored as a cell of the result's type.
