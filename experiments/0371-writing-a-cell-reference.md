# 0371: Writing a cell reference

**Status:** run

In a cell formula, a single-cell reference is node type 36. Field 26 is the column and 27 the row; in each, field 1 is the value and field 2 is 1 for absolute. A relative value is a zigzag-encoded offset from the formula's cell, an absolute one the zigzag-encoded index ([0065](0065-cross-table-reference.md), [0106](0106-mixed-references.md)). This experiment writes each kind and reads the formula and its result back through Numbers' AppleScript.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0106/mixed.numbers`: B2 = 4, C2 = 2, and E2 = `$B2+B$2` = 8. In formula list 904540, the first reference has column (2, absolute) and row (0, relative); the second has column (5, relative) and row (2, absolute) |
| Writer | The new [`recipes/0371-cell-reference.py`](../recipes/0371-cell-reference.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0371
R=recipes/0371-cell-reference.py
M=samples/0106/mixed.numbers
python3 -I $R $M samples/0371/abs-c.numbers 904540 1 4 1 0 0
python3 -I $R $M samples/0371/rel-c.numbers 904540 2 3 0 2 1
python3 -I $R $M samples/0371/all-relative.numbers 904540 1 5 0 0 0
python3 -I $R $M samples/0371/all-absolute.numbers 904540 1 2 1 2 1
```

The arguments are the reference's number, then the column's value and absolute flag, then the row's. Numbers opened each file on its own and read E2.

## Observation

| File | Reference written | Formula | E2 |
| --- | --- | --- | --- |
| `abs-c.numbers` | 1st: column 4 absolute (index 2, C) | `=$C2+B$2` | 6 |
| `rel-c.numbers` | 2nd: column 3 relative (offset −2 from E, C) | `=$B2+C$2` | 6 |
| `all-relative.numbers` | 1st: column 5 relative (offset −3, B) | `=B2+B$2` | 8 |
| `all-absolute.numbers` | 1st: row 2 absolute (index 1, row 2) | `=$B$2+B$2` | 8 |

## Conclusion

The encoding reads as described. Zigzag 4 is index 2, column C; zigzag 3 is offset −2; zigzag 5 is offset −3. Field 2 of each axis decides whether Numbers shows a `$` before it. Changing a reference changes the result, since Numbers recalculates on opening: $C2 + B$2 = 2 + 4 = 6.

## Confidence

*Confirmed*: the cell-reference node's columns, rows and absolute flags, by writing them.
