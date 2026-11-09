# 0226: A category

**Status:** run

Numbers can group a table's rows by the values in one column (Organise → Add Category). The rows appear under a summary row for each value, without being copied. This experiment groups a small table, to see what is stored.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0226/plain.numbers`, the same table ungrouped |

## Recipe

```bash
mkdir -p samples/0226
osascript recipes/0226-numbers-grouping-data.applescript A2
```

The recipe fills table 1 with a column `kind` (a, b, a, b in A2:A5) and a column `n` (1, 2, 3, 4) and selects A2. Then:

1. Choose Organise → Add Category for "kind" (*Organiser → Legg til kategori for «kind»*). Numbers shows three groups, `a` (rows 1 and 3), `b` (rows 2 and 4) and `(empty)` for the remaining empty rows. The inspector now reports 25 rows and 8 columns.
2. Save it as `samples/0226/category.numbers`.

For the baseline, run the recipe again and save it without grouping.

## Observation

The table model (type 6001) still has 22 rows and 7 columns in fields 6 and 7, so the summary rows and the extra column the inspector counts aren't real rows. Its field 81.2 grows from 86 to 1,933 bytes. Field 81.2.6 changes from 0 to 1, and fields 81.2.2 and 81.2.15 appear. Field 49, naming a type-6305 record, is dropped.

`CalculationEngine.iwa` gains three records of type 6383. With the one already there, they form a tree:

| Record | Field 6, the group's value | Field 9, its rows | Field 10, its children |
| --- | --- | --- | --- |
| 904758, the root | empty | `{ 1: 1, 2: 21 }` | 905559, 905560, 905561 |
| 905559, `(empty)` | none | `{ 1: 5, 2: 21 }` | |
| 905560, `a` | `{ 1: 5, 5: { 1: "a", 2: { 1: 260 } … } }` | rows 1 and 3 | |
| 905561, `b` | `{ 1: 5, 5: { 1: "b", 2: { 1: 260 } … } }` | rows 2 and 4 | |

Each group also has a 128-bit ID in field 1. A new type-6267 record lists eight 128-bit IDs together with two permutations of 0–7.

## Conclusion

Categories don't move any cells. The table keeps its rows in their stored order, and a tree of type-6383 group records says which rows belong to each group. Each group holds its value as a typed cell value (type 5 with the text in 5.1 and the text format 260) and its rows as single row numbers, `{ 1: n }`, or as a range, `{ 1: first, 2: last }`. The summary rows Numbers shows are derived, not stored. Table model field 81.2.6 is probably the switch that turns categories on, and 81.2.2 names the column grouped by.

A reader that ignores categories still reads every cell correctly. Showing the groups needs the 6383 tree.

## Confidence

*Likely*: categories are a tree of type-6383 records naming rows by number, and they don't change the cells.

*Unknown*: the type-6267 permutations, field 81.2.15, and how the column grouped by is named.
