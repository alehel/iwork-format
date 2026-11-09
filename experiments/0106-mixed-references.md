# 0106: Mixed references

**Status:** run

[0031](0031-cell-kinds.md), [0035](0035-formula-references.md), [0064](0064-operators-and-functions.md) and [0066](0066-comparisons-and-if.md) decoded formula nodes for numbers, references, ranges, operators and a few functions. This experiment, one of ten (0103–0112) that each write one formula, asks: how are references that are absolute in only one direction, `$B2` and `B$2`, stored?

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0064](0064-operators-and-functions.md) |

## Recipe

```bash
mkdir -p samples/0106
osascript recipes/0103-numbers-formula.applescript "$PWD/samples/0106/mixed-references.numbers" '=$B2+B$2'
```

The recipe sets B2 to 4 and C2 to 2, and writes `=$B2+B$2` in E2.

## Observation

The formula's nodes:

```
36  26: {1: 2, 2: 1}   27: {1: 0, 2: 0}     $B2
36  26: {1: 5, 2: 0}   27: {1: 2, 2: 1}     B$2
1   add
```

The cell holds 8.

## Conclusion

The absolute flag (field 2) is kept separately for the column and the row. `$B2` has an absolute column (index 1, zigzag 2) and a relative row (offset 0). `B$2` has a relative column (offset −3, zigzag 5) and an absolute row (index 1, zigzag 2).

## Confidence

*Likely*: column and row each carry their own absolute flag.
