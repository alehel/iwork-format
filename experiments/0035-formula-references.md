# 0035: Cell references in formulas

**Status:** run

[0031](0031-cell-kinds.md) found that a formula is stored as a postfix list of nodes. It also found that `=B2*2` begins with a node of type 36 whose fields 26 and 27 weren't decoded. This experiment writes formulas that refer to cells in different ways, so those fields can be read.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0031](0031-cell-kinds.md) |

## Recipe

```bash
mkdir -p samples/0035
osascript recipes/0035-numbers-formulas.applescript "$PWD/samples/0035/formulas.numbers"
```

The recipe sets B2 to 1 and C3 to 2, then writes five formulas in column E. Rows and columns are counted from 0 below, so B2 is column 1, row 1, and E2 is column 4, row 1.

## Observation

The formula list (`DataList-904540.iwa`, list type 3) has one entry per formula, in the order they were written:

| Key | Cell | Formula | Nodes (field 5.1), in order |
| --- | --- | --- | --- |
| 1 | E2 | `=B2` | `{1: 36, 26: {1: 5, 2: 0}, 27: {1: 0, 2: 0}}` |
| 2 | E3 | `=C3` | `{1: 36, 26: {1: 3, 2: 0}, 27: {1: 0, 2: 0}}` |
| 3 | E4 | `=$B$2` | `{1: 36, 26: {1: 2, 2: 1}, 27: {1: 2, 2: 1}}` |
| 4 | E5 | `=B2+C3` | `{1: 36, 26: {1: 5}, 27: {1: 5}}`, `{1: 36, 26: {1: 3}, 27: {1: 3}}`, `{1: 1}` |
| 5 | E6 | `=SUM(B2:C3)` | `{1: 67, 33: {…}, 40: {1: {1: −3, 2: −2}, 2: {1: −4, 2: −3}, 5: 1}}`, `{1: 16, 2: 168, 3: 1}` |

In key 5, the values shown as −3, −2 and −4 are varints of 18446744073709551613 and similar: 64-bit two's complement.

## Conclusion

A cell reference is a node of type 36. Field 26 is the column and field 27 the row. In each, field 1 is the value and field 2 is 1 for an absolute reference (`$`).

- **Relative:** the value is the offset from the formula's own cell, zigzag-encoded (0 → 0, −1 → 1, 1 → 2, −2 → 3, −3 → 5).
  - From E2, B2 is 3 columns left: −3 → 5. From E3, C3 is 2 columns left: −2 → 3. From E5, both B2 and C3 are 3 and 2 places back in both directions.
- **Absolute:** the value is the column or row index itself, also zigzag-encoded: `$B$2` is column 1 → 2, row 1 → 2.

A range in a function's argument (`B2:C3`) is a node of type 67. Its field 40.1 gives the first and last column and 40.2 the first and last row, as offsets from the formula's cell (columns −3 to −2 and rows −4 to −3, from E6). These are plain signed varints, not zigzag.

Operators and functions are nodes in the postfix list:

- type 1 is addition, and type 3 is multiplication ([0031](0031-cell-kinds.md))
- type 16 is a function call: field 2 is the function, 168 for SUM, and field 3 the number of arguments. *Note after [0044](0044-merged-cells.md):* the same node `16, 168, 1` also ends the expression for a merged range. So 168 may not mean SUM specifically.
- type 17 is a number ([0031](0031-cell-kinds.md))

## Confidence

*Likely*:

- Node 36 is a cell reference, with zigzag offsets or absolute indices and the absolute flag in field 2.
- Node 67 with field 40 is a range of offsets.
- Node 16 is a function call (168 = SUM).
- Node 1 is addition.

*Unknown*:

- Field 33 of the range node, and field 40.5.
- The numbers of other functions and operators. Follow-up: a formula with several functions and with subtraction and division.
