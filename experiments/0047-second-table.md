# 0047: A second table on a sheet

**Status:** run

[0029](0029-numbers-root-to-table.md) found that a Numbers sheet names a drawable in its field 2. [0032](0032-reading-all-text.md) found that a sheet also owns a text record holding one U+FFFC, and couldn't say whether tables are anchored there. This experiment adds a second table to the first sheet.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0047
osascript recipes/0047-numbers-second-table.applescript "$PWD/samples/0047/two-tables.numbers"
```

The recipe makes a new spreadsheet and adds a table named `Second` to its first sheet, with `make new table with properties {name:"Second"}`.

## Observation

The sheet (type 2) has two entries in field 2, where the empty spreadsheet has one:

```
2: { 1: 904769 }      ← drawable (type 6000) of model 904595: 22 rows, 7 columns, "Tabell 1"
2: { 1: 905254 }      ← drawable (type 6000) of model 905257: 10 rows, 5 columns, "Second"
```

`iwork-probe text` still finds a single text record for the sheet, with a single U+FFFC, as in the empty spreadsheet.

## Conclusion

A Numbers sheet lists its drawables, such as tables, in its repeated field 2, in order. Each is a drawable of type 6000 pointing at its own table model. The sheet's text record didn't change when a table was added. So tables on a Numbers sheet aren't anchored in that text, which fits what [0032](0032-reading-all-text.md) found. Its single U+FFFC is for something else.

A new table made through AppleScript has 10 rows and 5 columns. The spreadsheet's first table has 22 rows and 7 columns.

## Confidence

*Likely*:

- Sheet field 2 lists the sheet's drawables.
- Tables aren't anchored in the sheet's text.

*Unknown*: what the sheet's text and its U+FFFC are for.
