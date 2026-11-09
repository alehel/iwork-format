# 0279: A pivot table that averages

**Status:** run

[0227](0227-pivot-table.md) found that a pivot table's settings are in new record types, including a type-6370 record that names the source table. This experiment changes how the pivot summarises its values, from Sum to Average, to find where the summary function is kept.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0279/sum.numbers`, the pivot of 0227 made again |

## Recipe

```bash
mkdir -p samples/0279
osascript recipes/0226-numbers-grouping-data.applescript A1:B5
```

Then, with Numbers in front:

1. Make the pivot table of 0227, with `kind` as rows and `n (Sum)` as values. Save it as `samples/0279/sum.numbers`.
2. Click the options button of `n (Sum)` under Values, and choose Average (*Gjennomsnitt*) from Summarise By (*Oppsummer etter*). The pivot shows a = 2, b = 3 and a total of 2.5.
3. Save it as `samples/0279/average.numbers`.

## Observation

In the type-6370 record, the value field's settings (field 5.1) change in one place:

```
5.1.3: 2 → 18
```

Field 3 lists the row field (`kind`), and field 5 the value field (`n`), each with a 128-bit ID. The formulas in field 17 call function 168, SUM, in both documents.

Elsewhere:

- The label table (type 6365) holds `(gjennomsnitt)`, "(average)", where it held `(summer)`.
- The pivot table's cells hold the new values.
- An internal number (50) becomes 51 in several records, probably a counter or version of the pivot's results.

## Conclusion

A pivot's value fields are listed in field 5 of its type-6370 record. Each names a column of the source, by ID, and gives its summary function in field 3: 2 for Sum and 18 for Average. These codes are their own list, not the function numbers of formulas (where SUM is 168 and AVERAGE 15). The column labels that show the function's name are stored as text in the app's language. A reader showing a pivot can use its cells, which hold the averaged results, as found in 0227.

## Confidence

*Likely*:

- Pivot field 5 lists value fields with their summary function in 5.1.3: 2 sum, 18 average.
- Field 3 lists the row fields.

*Unknown*: the codes of the other functions, and what the SUM formulas in field 17 compute.
