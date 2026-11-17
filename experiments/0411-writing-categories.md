# 0411: Writing a category's value and rows

**Status:** run

Grouping a table's rows by a column (a category) moves no cells: the groups are a tree of type-6383 records, each with an ID (field 1), its value as a typed cell value (field 6), its rows (field 9) and its child groups (field 10) ([0226](0226-category.md)). This experiment writes a group's value and rows and reads the grouped table from the exported sheet.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0226/category.numbers`: `kind` a, b, a, b and `n` 1, 2, 3, 4 in rows 2–5, grouped by `kind`. The root group 904758 has three children: 905559 for the empty rows 5–21, 905560 for `a` with rows 1 and 3, and 905561 for `b` with rows 2 and 4. Each of the last two holds its value twice, in field 6 (6.1.5.1, beside the rows again in 6.4) and in field 7 (7.5.1) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) and [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0411
N=recipes/0383-set-nth-path.py
F=samples/0226/category.numbers
O=samples/0411
cp $F $O/original.numbers
python3 -I $N $F $O/value-z.numbers 905560 6.1.5.1 string z 7.5.1 string z
python3 -I recipes/0302-set-path.py $F $O/value-z-6-only.numbers 905560 6.1.5.1 string z
python3 -I $N $F $O/x.numbers 905560 9.1:1.1 varint 2 9.1:2.1 varint 4
python3 -I $N $O/x.numbers $O/rows-swapped.numbers 905561 9.1:1.1 varint 1 9.1:2.1 varint 3
rm $O/x.numbers
for f in original value-z value-z-6-only rows-swapped; do
  sh recipes/0372-in-app.sh Numbers $O/$f.numbers "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
```

## Observation

The table in each exported sheet, after its header row (each group's heading, then its rows):

| File | Written | Table |
| --- | --- | --- |
| `original.pdf` | | **a**: a 1, a 3; **b**: b 2, b 4; **(tom)** |
| `value-z.pdf` | a's value in 6 and 7: `z` | **z**: a 1, a 3; **b**: b 2, b 4; **(tom)** |
| `value-z-6-only.pdf` | a's value in 6 only: `z` | the same as `original.pdf`, pixel for pixel |
| `rows-swapped.pdf` | a's rows 2 and 4, b's rows 1 and 3 | **a**: b 2, b 4; **b**: a 1, a 3; **(tom)** |

*(tom)* is "(empty)", the group of rows with no value.

## Conclusion

Numbers draws a category from its stored tree and doesn't regroup the rows by their values when it opens a document. A group's heading is the value in its field 7. Field 6, the same value with the group's rows, didn't change the heading when written alone; it is probably the grouping key. The rows under a group are those in its field 9, whatever their cells hold: written so, group `a` showed the rows whose kind is `b`. A reader can show a category from the tree as stored.

## Confidence

*Confirmed*: a group's heading as its field 7 and its rows as field 9, and that Numbers doesn't regroup on opening, by writing them. What Numbers uses field 6 for is *unknown*.
