# 0258: A filter

**Status:** run

Numbers can hide rows that don't match a rule (Organise → Show Filter Options). Rules are built in the sidebar with pop-up menus, which need Numbers in front. This experiment filters a small table to the rows where `n` is greater than 2.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0226/plain.numbers`, the same table without a filter |

## Recipe

```bash
mkdir -p samples/0258
osascript recipes/0226-numbers-grouping-data.applescript A2
```

The recipe fills table 1 as in [0226](0226-category.md): `kind` a, b, a, b and `n` 1, 2, 3, 4. Then, with Numbers in front:

1. Choose Organise → Show Filter Options (*Organiser → Vis filtervalg*), then Add a Filter → n, Number → Greater Than (*Legg til et filter → n, Tall → Større enn*), and type 2.
2. Numbers turns filters on and shows only the rows with n = 3 and 4, plus the header.
3. Save it as `samples/0258/filter.numbers`.

## Observation

The cells are unchanged. In the table model (type 6001), field 70 grows from 118 to 630 bytes. Its field 2.3 now lists 20 rows by their 128-bit IDs, each with field 3 set to 1. Those are the two rows with n = 1 and 2 and the 18 empty rows, which don't pass the rule either.

The rule itself is in two type-6220 records in `CalculationEngine.iwa`. Each holds it as a formula in the node form of cell formulas ([0035](0035-formula-references.md)):

```
36: a cell reference, column 0 and row 0, in the table with the table's UUID
17: the number 2
7:  >
```

One of the records also holds the rule's kind (7 in field 7.1.1) and its value, 2.0, in 7.1.5.2.

## Conclusion

A filter rule is stored as a formula that compares a cell with a value, written relative to the cell being tested. Here that is `cell > 2`, using the comparison node 7 of cell formulas ([0066](0066-comparisons-and-if.md)). Numbers also stores the result: table model field 70.2.3 lists the rows it hides. A reader can hide those rows without evaluating the rule, and keep them when it ignores filters, since the cells aren't touched.

## Confidence

*Likely*:

- Filter rules are formulas in type-6220 records.
- The hidden rows are listed in table model field 70.2.3.

*Unknown*: the other fields of the type-6220 records, and how several rules are combined (the sidebar's "match all").
