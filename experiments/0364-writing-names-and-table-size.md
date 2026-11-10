# 0364: Writing names and a table's size

**Status:** run

A sheet's field 1 is its name ([0124](0124-sheet-name.md)), and the table model (type 6001) holds the row count in field 6, the column count in field 7 and the name in field 8 ([0029](0029-numbers-root-to-table.md)). This experiment writes the names, then the counts, and reads them back through Numbers' AppleScript: the sheet's and table's `name`, `row count`, `column count` and the name of the table's last cell.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0226/plain.numbers`: sheet "Ark 1" (record 904532) with table "Tabell 1" (table model 904595), 22 rows × 7 columns |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) and the new [`recipes/0364-table-size.py`](../recipes/0364-table-size.py), both using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0364
R=recipes/0302-set-path.py
python3 -I $R samples/0226/plain.numbers samples/0364/x.numbers 904532 1 string Budget
python3 -I $R samples/0364/x.numbers samples/0364/names.numbers 904595 8 string Costs
python3 -I $R samples/0226/plain.numbers samples/0364/more-rows.numbers 904595 6 varint 40 7 varint 3
python3 -I recipes/0364-table-size.py samples/0226/plain.numbers samples/0364/five-by-four.numbers 5 4
```

The search for other places that hold the size found two records in `CalculationEngine.iwa`:

| Record | Type | Fields |
| --- | --- | --- |
| 904672 | 6305 | 1: 2, 2: 7 (columns), 3: 22 (rows) |
| 904603 | 6267 | 1: seven 128-bit UUIDs (two varints each), one per column; 2 and 3: the numbers 0–6 in two different orders; 4: 22 UUIDs, one per row; 5 and 6: the numbers 0–21 in two different orders |

Two more type-6267 records in the file are empty. Writing 6305's fields along with the table model's, or 6305 alone, was tried too. `recipes/0364-table-size.py` writes the counts into 6001 and 6305 and trims 6267: it keeps the first ROWS and COLUMNS UUIDs and only the map entries below those counts. `lists-only.numbers` is `five-by-four.numbers` with 6001 and 6305 set back to 22 and 7.

## Observation

| File | Sheet | Table | Size | Last cell |
| --- | --- | --- | --- | --- |
| `plain.numbers` | Ark 1 | Tabell 1 | 22 × 7 | G22 |
| `names.numbers` | Budget | Costs | 22 × 7 | G22 |
| `more-rows.numbers` (6001: 40 × 3) | Ark 1 | Tabell 1 | 22 × 7 | G22 |
| 6001 and 6305: 40 × 3, or 5 × 4 | | | 22 × 7 | G22 |
| 6305 alone: 5 × 4 | | | 22 × 7 | G22 |
| `five-by-four.numbers` | Ark 1 | Tabell 1 | 5 × 4 | D5 |
| `lists-only.numbers` | | | 5 × 4 | D5 |

In `five-by-four.numbers` cell B2 still held 1, and the exported PDF showed the table's remaining cells. When Numbers saved the file again, it kept the trimmed lists (4 column UUIDs and 5 row UUIDs) and the counts 5 and 4.

## Conclusion

The names are read from the fields written. A table's size isn't: it is the number of row and column UUIDs in its type-6267 record. Fields 6 and 7 of the table model and fields 3 and 2 of record 6305 are copies, which Numbers rewrites when it saves. Fields 2 and 3, and 5 and 6, look like a pair of maps between a column's (or row's) place and its UUID's place in the list, one each way. Making a table smaller is done by dropping UUIDs; making it larger would need new ones and wasn't tried.

## Confidence

*Confirmed*: the sheet and table names. Also confirmed: the size comes from the UUID lists of the type-6267 record, not from 6001's counts. *Likely*: fields 2/3 and 5/6 are index maps in each direction.
