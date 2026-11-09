# 0065: A reference to another table

**Status:** run

[0035](0035-formula-references.md) decoded references to cells in the same table. [0044](0044-merged-cells.md) saw a range node with a field 28 that looked like a UUID. This experiment writes a formula that refers to a cell in another table.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0035](0035-formula-references.md) |

## Recipe

```bash
mkdir -p samples/0065
osascript recipes/0065-numbers-cross-table.applescript "$PWD/samples/0065/cross.numbers"
```

The recipe adds a table named `Other` to the first sheet, sets its B2 to 9, and writes `=Other::B2` in E2 of the first table. Numbers shows 9 in E2.

## Observation

The formula is a single cell reference node:

```
1: 36
26: { 1: 5, 2: 0 }            column: zigzag −3, relative (E → B)
27: { 1: 0, 2: 0 }            row: 0, relative
28: { 1: { 2: 1367643781, 3: 2940280568, 4: 4033881747, 5: 2041614833 } }
```

The table `Other` has the UUID `85968451-F81E-41AF-9326-70F0F191B079` in its model's field 1. The four numbers in field 28, written as little-endian 32-bit words, give its bytes in order. For example, 1367643781 = 0x51849685 → `85 96 84 51`, and 2940280568 = 0xAF411EF8 → `f8 1e 41 af`.

## Conclusion

A reference to another table carries that table's UUID in field 28.1, as four 32-bit numbers (fields 2–5) whose little-endian bytes make up the UUID. A reader matches it against field 1 of the table models. The column and row stay relative to the formula's cell, as within a table. The range node of a merge ([0044](0044-merged-cells.md)) had the same field 28, so it names its table the same way.

## Confidence

*Likely*: field 28 of a reference or range node names the table by its UUID, stored as four little-endian 32-bit words.

*Unknown*: references to another sheet's table.
