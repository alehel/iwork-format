# 0037: A second sheet

**Status:** run

[0029](0029-numbers-root-to-table.md) followed a Numbers document from its root through one sheet to a table. This experiment adds a second sheet, to see how the root lists sheets.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0037
osascript recipes/0037-numbers-second-sheet.applescript "$PWD/samples/0037/two-sheets.numbers"
```

The recipe makes a new spreadsheet and adds a sheet named `Second` with `make new sheet with properties {name:"Second"}`. A first version that made the sheet `at end of sheets` failed with error −10000.

## Observation

The root (object 1, type 1) has two entries in field 1, where an empty spreadsheet has one. `Document.iwa` has two records of type 2:

| Sheet | Field 1 | References listed in its header |
| --- | --- | --- |
| 904532 | `Ark 1` | 904769 903871 904606 904900 904801 904721 904579 904667 904976 |
| 905230 | `Second` | 905262 903871 905231 905235 905236 905237 905232 905233 905234 |

Both sheets refer to object 903871. The new sheet came with a table of its own. The package gained a full set of table parts: 23 `DataList-N-N.iwa`, one more `DataList.iwa`, four `HeaderStorageBucket-N.iwa` and two `Tile-N.iwa`.

## Conclusion

Field 1 of Numbers' root lists the sheets in order, one reference per sheet. Each sheet (type 2) has its name in field 1 and refers to its own drawables, such as a table, which have their own table parts. A reader lists a document's sheets by reading root field 1.

The object both sheets share (903871) is probably a stylesheet or another document-wide object. It isn't identified here.

## Confidence

*Likely*: Numbers' root field 1 lists the sheets in order, and each new sheet brings its own table with its own parts.

*Unknown*: object 903871.
