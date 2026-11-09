# 0107: A reference to another sheet

**Status:** run

[0031](0031-cell-kinds.md), [0035](0035-formula-references.md), [0064](0064-operators-and-functions.md) and [0066](0066-comparisons-and-if.md) decoded formula nodes for numbers, references, ranges, operators and a few functions. This experiment, one of ten (0103–0112) that each write one formula, asks: how is a reference to a table on another sheet stored? [0065](0065-cross-table-reference.md) found a table's UUID in references to another table on the same sheet.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0064](0064-operators-and-functions.md) |

## Recipe

```bash
mkdir -p samples/0107
osascript recipes/0103-numbers-formula.applescript "$PWD/samples/0107/other-sheet.numbers" '=Andre::Tabell 1::B2' Andre
```

The recipe sets B2 to 4 and C2 to 2, and writes `=Andre::Tabell 1::B2` in E2. It first adds a sheet named `Andre` (Norwegian for "Other"), whose table has 9 in B2.

## Observation

The formula is one node:

```
36  26: {1: 5, 2: 0}  27: {1: 0, 2: 0}  28: {1: {2: 3398054789, 3: 3343495759, 4: 2618425731, 5: 1596672360}}
```

The cell holds 9.

## Conclusion

A reference to a table on another sheet is stored exactly like a reference to another table on the same sheet ([0065](0065-cross-table-reference.md)): by the table's UUID in field 28, with no mention of the sheet. Table UUIDs are unique in the document, so the sheet isn't needed.

## Confidence

*Likely*: references name the target table by UUID only, whichever sheet it is on.
