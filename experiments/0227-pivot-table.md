# 0227: A pivot table

**Status:** run

Numbers can summarise a table in a pivot table that it keeps up to date. This experiment makes one from a small table, to see whether the summary is stored as cells or has to be worked out by a reader.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0226/plain.numbers`, the same source table alone |

## Recipe

```bash
mkdir -p samples/0227
osascript recipes/0226-numbers-grouping-data.applescript A1:B5
```

The recipe fills table 1 as in [0226](0226-category.md), with `kind` a, b, a, b and `n` 1, 2, 3, 4, and selects A1:B5. Then:

1. Choose Organise → Create Pivot Table → For Selected Cells on Current Sheet (*Organiser → Opprett pivottabell → For markerte celler på nåværende ark*). Numbers adds an empty table, "Pivot av Tabell 1", with the source `Tabell 1!$A$2:$B$5`.
2. In the sidebar's field list, tick `kind`, then `n`. Numbers puts `kind` under Rows and `n (Sum)` under Values, and the table shows a = 4, b = 6 and a total of 10.
3. Save it as `samples/0227/pivot.numbers`.

## Observation

`CalculationEngine.iwa` now has three table models (type 6001):

| Model | Name (field 8) | Rows × columns |
| --- | --- | --- |
| 904595 | `Tabell 1` | 22 × 7, the source |
| 905564 | `Pivot av Tabell 1` | 3 × 2, with a drawable (type 6000) on the sheet |
| 905536 | `Tabell 1 as Pivot Source Table` | 5 × 2, with no drawable |

The pivot table's tiles hold ordinary cells: the text `kind`, `a` and `b` in the first column, the numbers 4 and 6 beside them, and a row with `Totalsum` and 10. The total row is in a tile of its own. The number cells have flags 0x3201, rather than the 0x3001 of a typed number, so one more key follows their value.

The hidden model's strings include `kind`, `a` and `b`: it is a copy of the source data.

New record types appear: 6369, 6370, 6374 and 6382, plus more of types 6267, 6305 and 6383. Type 6370 names the source table (`Tabell 1` in field 12) and holds a time in field 9: 815944239.01 seconds since 2001, the update time the sidebar shows (20:10 on 2026-11-09, local time).

## Conclusion

A pivot table is stored as an ordinary table whose cells hold the current summary, so a reader can show it without understanding pivots. Numbers also keeps a hidden copy of the source data (a table model named "… as Pivot Source Table") and the pivot's settings and last update time in new record types. It probably uses these to rebuild the summary on demand. The extra key on the pivot's number cells (bit 0x200) is probably a link back to the pivot's definition.

## Confidence

*Likely*:

- A pivot table is a normal table with its results in its cells.
- The source data is copied into a hidden table model.

*Unknown*: record types 6369, 6370, 6374 and 6382 beyond the source name and time, and the 0x200 flag.
