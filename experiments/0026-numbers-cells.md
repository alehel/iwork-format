# 0026: Cells in Numbers

**Status:** run

[0021](0021-table-cells.md) decoded how a Pages table stores a number and a text cell, from one experiment. This experiment puts the same values in the same cells of a Numbers table, through Numbers' AppleScript, to check that reading and whether Numbers stores cells the same way.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers`, copied as `samples/0026/empty.numbers`; and experiment [0021](0021-table-cells.md), `cells.pages` |

## Recipe

```bash
mkdir -p samples/0026
osascript recipes/0026-numbers-cells.applescript "$PWD/samples/0026/cells.numbers"
cp samples/0024/empty-a.numbers samples/0026/empty.numbers
```

The recipe makes a new spreadsheet, sets cell B2 of the first table to the number 42 and cell C3 to the text `abc`, and saves it. AppleScript doesn't trigger autocorrection, so the text stays lowercase. In 0021, Pages changed it to `Abc`.

## Observation

Compared with `empty.numbers`, the same parts changed in the same way as in 0021: `Tables/Tile.iwa` grew from 44 to 230 bytes, and one data list grew from 27 to 38 bytes and another from 29 to 58.

The string table:

```
cells.pages (0021)   Index/Tables/DataList.iwa          1: 1  2: 2  3: { 1: 1, 2: 1, 3: "Abc" }
cells.numbers        Index/Tables/DataList-904552.iwa   1: 1  2: 2  3: { 1: 1, 2: 1, 3: "abc" }
```

The decoded tile record (type 6002) of `cells.numbers` is byte-for-byte the same as that of `cells.pages`. Both have the SHA-1 `67e56451ad5e2eb0bd743e273f6a66a70f399843` over the decoded payload. That includes both rows' offset tables and cell bytes, with the type bytes 2 and 3, the decimal128 42, and the string key 1.

Numbers names its table parts `DataList-N.iwa`, `HeaderStorageBucket-N.iwa` and `Tile.iwa`, without the `-2` ending Pages adds.

## Conclusion

Numbers stores cells exactly as Pages does. The same values in the same cells give an identical tile, even though one table was filled by typing in Pages and the other through Numbers' AppleScript. This confirms the reading of [0021](0021-table-cells.md):

- Cells are kept per row in the tile.
- A cell has a version byte and a type byte, with 2 for a number and 3 for text.
- A number is stored as a decimal128.
- A text cell holds a key into the string table.

The string table's entry for a text cell doesn't depend on the string's content: the key and count were the same for `Abc` and `abc`.

The `-2` ending of table part names is Pages' own, and isn't part of the table format.

## Confidence

*Confirmed*:

- Cells are stored per row in the tile, with the type byte and value encodings for numbers and text described in 0021. That experiment and this one agree byte for byte.
- Numbers and Pages share the table format.

*Unknown*: the remaining cell bytes (flags and trailing keys), as in 0021.
