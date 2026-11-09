# 0182: A transposed table

**Status:** run

Numbers can transpose a table, swapping its rows and columns. This experiment checks whether a transposed table is stored with its cells moved, or with a flag that a reader would have to apply.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0181/plain.numbers`, a new document |

## Recipe

```bash
mkdir -p samples/0182
osascript recipes/0181-numbers-table-options.applescript transpose "$PWD/samples/0182/transpose.numbers"
```

The recipe sets B2 to 1, C2 to 2 and B3 to 3 in table 1, then runs `transpose` on the table.

## Observation

The table model (type 6001) has 7 rows and 22 columns in fields 6 and 7. A new table has 22 rows and 7 columns. Its other fields are unchanged, including one header row and one header column (fields 9 and 10).

The tile holds two rows of cells:

| Row | Column | Value |
| --- | --- | --- |
| 1 | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 1 | 2 |

So B2 is 1, C2 is 3 and B3 is 2: the values of C2 and B3 have swapped.

## Conclusion

Transposing rewrites the table. The row and column counts swap, and each cell is stored at its new place. Nothing records that the table was transposed, so a reader needs no special handling.

## Confidence

*Likely*: a transposed table is stored as an ordinary table with its cells moved.
