# 0078: A formula error

**Status:** run

[0031](0031-cell-kinds.md) found that a formula cell keeps its last result as a value. This experiment writes a formula whose result is an error, a division by zero, to see what is stored instead.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0031](0031-cell-kinds.md), cell F2 (`=B2*2`) |

## Recipe

```bash
mkdir -p samples/0078
osascript recipes/0078-numbers-error.applescript "$PWD/samples/0078/error.numbers"
```

The recipe writes `=1/0` in B2. Reading the cell back through AppleScript gives `missing value` for both its value and its shown value.

## Observation

The cell's bytes:

```
05 08 00 00 00 00 00 00 00 02 00 00 01 00 00 00
```

- Type byte 8.
- Flags 0x0200: a formula key, with no value.
- One key: 1.

The formula entry has the nodes `17(1.0) 17(0.0) 4`, the numbers 1 and 0 and division. Each number node also has fields 42 (1 and 0) and 43 (the same large constant for both).

## Conclusion

A formula whose result is an error is stored as cell type 8, with only its formula key and no cached value. A reader shows an error for type 8, and can recompute the formula from its nodes if it wants the details. Which error it was (here division by zero) isn't stored in the cell.

The number nodes' fields 42 and 43 also appear in [0031](0031-cell-kinds.md)'s `=B2*2`. Field 42 seems to hold the number as an integer, but neither field is needed to read the value, which is in field 4 as a double.

## Confidence

*Likely*: cell type 8 is an error result, stored with the formula key and no value.

*Unknown*: number node fields 42 and 43.
