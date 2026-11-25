# 0437: Writing a tile's row count

**Status:** run

A tile (type 6002) holds a table's cells by row, one field-5 entry per row with content, and its field 4 counts those rows ([0029](0029-numbers-root-to-table.md), [0030](0030-tiles.md)). This experiment writes wrong counts and reads the cells back.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0226/plain.numbers`: the header row `kind`, `n` and four rows a 1, b 2, a 3, b 4, in tile 904547, which has five field-5 row entries, field 4 = 5 and field 6 = 5 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported and read with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0437
R=recipes/0302-set-path.py
F=samples/0226/plain.numbers
O=samples/0437
cp $F $O/original.numbers
for n in 0 2 9; do python3 -I $R $F $O/count-$n.numbers 904547 4 varint $n; done
python3 -I $R $F $O/field6-2.numbers 904547 6 varint 2
for f in original count-0 count-2 count-9 field6-2; do
  sh recipes/0372-in-app.sh Numbers $O/$f.numbers "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
set t to table 1 of sheet 1 of d
return {value of cell \"B5\" of t, value of cell \"A5\" of t}"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
```

## Observation

| File | Field 4 | Field 6 | B5, A5 | Table in the PDF |
| --- | --- | --- | --- | --- |
| `original.numbers` | 5 | 5 | 4, b | kind n / a 1 / b 2 / a 3 / b 4 |
| `count-0.numbers` | 0 | 5 | 4, b | the same |
| `count-2.numbers` | 2 | 5 | 4, b | the same |
| `count-9.numbers` | 9 | 5 | 4, b | the same |
| `field6-2.numbers` | 5 | 2 | 4, b | the same |

## Conclusion

Numbers doesn't use a tile's counts to read its rows: with field 4 written as 0, 2 or 9, or field 6 as 2, it read all five rows as before. It takes the rows from the field-5 entries themselves, each with its own row number. A reader should do the same and treat field 4 (and field 6, which held the same number here) only as a hint; a writer should still fill them in as Pages and Numbers do.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.numbers` | `0226/plain.numbers` | `same bytes`, `6002#904547 4 = 5`, `6002#904547 6 = 5` | *Control* |
| `count-0.numbers` | `original.numbers` | Only `6002#904547 4: 5 → 0` | *Confirmed*: field 4 isn't needed; all five rows are read |
| `count-2.numbers` | `original.numbers` | Only `6002#904547 4: 5 → 2` | *Confirmed*: field 4 isn't needed; all five rows are read |
| `count-9.numbers` | `original.numbers` | Only `6002#904547 4: 5 → 9` | *Confirmed*: field 4 isn't needed; all five rows are read |
| `field6-2.numbers` | `original.numbers` | Only `6002#904547 6: 5 → 2` | *Confirmed*: field 6 isn't needed; all five rows are read |

## Confidence

*Confirmed*: a tile's fields 4 and 6 aren't needed to read its rows, by writing them. What field 6 counts, if it differs from field 4, is *unknown*.
