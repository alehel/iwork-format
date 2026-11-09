# 0030: A second tile

**Status:** run

[0029](0029-numbers-root-to-table.md) found that a table model lists its tiles in field 4.3, next to the value 256, and guessed that a tile covers 256 rows. This experiment fills row 300 of a Numbers table to see whether a second tile appears.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0026](0026-numbers-cells.md), `cells.numbers` |

## Recipe

```bash
mkdir -p samples/0030
osascript recipes/0030-numbers-row-300.applescript "$PWD/samples/0030/row-300.numbers"
```

The recipe makes a new spreadsheet, sets the first table's row count to 300, and puts 42 in B2 and 7 in B300.

## Observation

The table model (type 6001) now has 300 rows (field 6) and lists two tiles in field 4.3:

```
3:
  1: { 1: 0, 2: { 1: 904547 } }      ← Tables/Tile.iwa
  1: { 1: 1, 2: { 1: 905237 } }      ← Tables/Tile-905237.iwa
  2: 256
```

The two tiles:

| Tile | Index | Field 4 | Row entries (field 5.1) |
| --- | --- | --- | --- |
| 904547 | 0 | 1 | 1 |
| 905237 | 1 | 1 | 43 |

Row 43 of tile 1 is row 256 + 43 = 299 counted from 0, which is row 300.

The file has a third tile, `Tables/Tile-905022-2.iwa`, with no rows (field 4 is 0). It is reached from the sheet through the drawable and a type-6316 record, not through the table model. `samples/0026/cells.numbers` already had it, along with three `HeaderStorageBucket-N-2.iwa` parts.

## Conclusion

A table's rows are split into tiles of 256 rows each. The model lists them in field 4.3, with the tile index in 4.3.1.1, and the tile size in 4.3.2. Row numbers inside a tile (field 5.1) are local to the tile. A cell's row in the table is the tile index × 256 + the local row. A tile's field 4 counts the rows in it that have content.

Numbers, like Pages, names some table parts with a `-2` ending: an empty tile and three header storage buckets in both `cells.numbers` and `row-300.numbers`. The [0026](0026-numbers-cells.md) write-up said Numbers doesn't use the ending. That was wrong, because the comparison there collapsed part names, and it has been corrected. What the ending means is still unknown.

## Confidence

*Likely*:

- Tiles cover 256 rows each, as given by model field 4.3.2.
- Row numbers in a tile are local.
- Tile field 4 counts the rows with content.

*Unknown*:

- The `-2` ending of part names.
- The type-6316 record that leads to the empty tile.
