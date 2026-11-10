# 0370: Writing a formula's range

**Status:** run

In a cell formula, a range is node type 67. Its field 40.1 holds the first and last column and 40.2 the first and last row, as signed offsets from the formula's own cell, not zigzag-encoded ([0064](0064-operators-and-functions.md), [0104](0104-nested-functions.md)). This experiment writes new offsets and reads the formula and its result back through Numbers' AppleScript.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian, so function names and the decimal comma are Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0104/nested.numbers`: B2 = 4, C2 = 2, and E2 = `ROUND(AVERAGE(B2:C2)*1.5,0)` = 5. The formula list is record 904540; its range node has 40.1 = (−3, −2) and 40.2 = (0), with no last row |
| Writer | The new [`recipes/0370-formula-range.py`](../recipes/0370-formula-range.py), using the writer of [0287](0287-rewriting-a-document.md). It finds the first range node in the formula list's nodes (field 3.5.1) and writes 40.1, and 40.2 if rows are given, as plain varints, negative values in ten bytes |

## Recipe

```bash
mkdir -p samples/0370
R=recipes/0370-formula-range.py
python3 -I $R samples/0104/nested.numbers samples/0370/b-only.numbers 904540 -3 -3
python3 -I $R samples/0104/nested.numbers samples/0370/c-only.numbers 904540 -2 -2
python3 -I $R samples/0104/nested.numbers samples/0370/b-to-c-rows.numbers 904540 -3 -2 0 1
```

Numbers opened each file on its own and read E2's value and formula.

## Observation

| File | Written: columns, rows | Formula | E2 |
| --- | --- | --- | --- |
| `nested.numbers` | −3 to −2, 0 | `=AVRUND(GJENNOMSNITT(B2:C2)×1,5;0)` | 5 |
| `b-only.numbers` | −3 to −3, 0 | `=AVRUND(GJENNOMSNITT(B2)×1,5;0)` | 6 |
| `c-only.numbers` | −2 to −2, 0 | `=AVRUND(GJENNOMSNITT(C2)×1,5;0)` | 3 |
| `b-to-c-rows.numbers` | −3 to −2, 0 to 1 | `=AVRUND(GJENNOMSNITT(B2:C3)×1,5;0)` | 5 |

## Conclusion

The offsets are read as written: a range of one cell is shown as that cell alone, and the second row value makes the range two rows tall. Numbers recalculates on opening: 4 × 1.5 = 6, 2 × 1.5 = 3, and the average of B2:C3's two numbers, 3, gives 4.5, rounded to 5. A missing last row (or last column) counts as 0, the formula's own row.

## Confidence

*Confirmed*: 40.1 and 40.2 as the columns and rows of a range, as signed offsets from the formula's cell, by writing them.
