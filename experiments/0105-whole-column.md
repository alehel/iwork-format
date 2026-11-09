# 0105: A whole-column reference

**Status:** run

[0031](0031-cell-kinds.md), [0035](0035-formula-references.md), [0064](0064-operators-and-functions.md) and [0066](0066-comparisons-and-if.md) decoded formula nodes for numbers, references, ranges, operators and a few functions. This experiment, one of ten (0103–0112) that each write one formula, asks: how is a reference to a whole column, `B:B`, stored?

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0064](0064-operators-and-functions.md) |

## Recipe

```bash
mkdir -p samples/0105
osascript recipes/0103-numbers-formula.applescript "$PWD/samples/0105/whole-column.numbers" '=SUM(B:B)'
```

The recipe sets B2 to 4 and C2 to 2, and writes `=SUM(B:B)` in E2.

## Observation

The formula's nodes:

```
36  26: {1: 5, 2: 0}      (no field 27)
16  function 168 (SUM), 1 argument
```

The cell holds 4.

## Conclusion

A reference to a whole column is a cell-reference node (36) with a column (field 26, here relative: −3) and no row (field 27). Presumably a whole row would have a row and no column. SUM's argument here is that reference, not a range node.

## Confidence

*Likely*: a cell reference without field 27 means the whole column.
