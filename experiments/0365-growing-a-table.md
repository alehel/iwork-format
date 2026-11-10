# 0365: Growing a table

**Status:** run

A Numbers table's size is the number of row and column UUIDs in its type-6267 record, so a table can be shrunk by dropping some ([0364](0364-writing-names-and-table-size.md)). This experiment makes a table larger by adding new UUIDs. Each new row or column gets two random 64-bit varints as its UUID, and its number is appended to both of that list's maps (fields 2 and 3 for columns, 5 and 6 for rows).

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0226/plain.numbers`: one table, 22 rows × 7 columns, with 1 in B2 |
| Writer | [`recipes/0364-table-size.py`](../recipes/0364-table-size.py), extended to add UUIDs, using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0365
python3 -I recipes/0364-table-size.py samples/0226/plain.numbers samples/0365/thirty-by-nine.numbers 30 9
```

Numbers opened the file and read the size and B2 through AppleScript. It set the new corner cell, I30, to 7 and saved a copy (`thirty-by-nine-resaved.numbers`). That copy was then opened again, read and exported as PDF.

## Observation

| File | Size | Last cell | Cells |
| --- | --- | --- | --- |
| `thirty-by-nine.numbers` | 30 × 9 | I30 | B2 = 1; I30 could be set to 7 |
| `thirty-by-nine-resaved.numbers` | 30 × 9 | | I30 = 7 |

The resaved table model has 30 and 9 in fields 6 and 7. The PDF's page is 1028 × 792 points, against 832 × 792 for the 22 × 7 table: 196 points more, two columns of 98 points. The table's ink ends at 703.0 points from the top, against 542.5.

## Conclusion

A table grows when new UUIDs are added, each with its number appended to both maps. Numbers accepts random UUIDs, lets cells in the new rows and columns be set, and keeps them on saving. Only the row and column lists are needed: no tile or header storage changed.

## Confidence

*Confirmed*: a table can be grown by adding row and column UUIDs, by writing them.
