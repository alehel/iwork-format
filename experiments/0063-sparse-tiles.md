# 0063: Tiles for a sparse table

**Status:** run

[0030](0030-tiles.md) found that a table's rows are split into tiles of 256, but its two tiles were the first two. This experiment fills three far-apart rows of a 1000-row table, to see whether empty tiles are stored and whether the local row numbers hold up.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0030](0030-tiles.md) |

## Recipe

```bash
mkdir -p samples/0063
osascript recipes/0063-numbers-sparse-rows.applescript "$PWD/samples/0063/sparse.numbers"
```

The recipe sets the first table's row count to 1000 and puts 1 in B2, 2 in B600 and 3 in B1000. Counted from 0, those are rows 1, 599 and 999.

## Observation

The table model's tile list (field 4.3):

| Tile index (4.3.1.1) | Tile | Row entries (5.1) | Field 4 |
| --- | --- | --- | --- |
| 0 | 904547, `Tables/Tile.iwa` | 1 | 1 |
| 2 | 905237, `Tables/Tile-905237.iwa` | 87 | 1 |
| 3 | 905241, `Tables/Tile-905241.iwa` | 231 | 1 |

Field 4.3.2 is 256. There is no tile with index 1. The empty tile `Tile-905022-2.iwa` from [0030](0030-tiles.md) is also present.

## Conclusion

Only tiles with content are stored, and the tile list skips the others: index 1, for rows 256–511, is missing. The rule from 0030 holds for every stored row: tile index × 256 + local row = 2 × 256 + 87 = 599 and 3 × 256 + 231 = 999. A reader has to use each entry's tile index, not its position in the list.

## Confidence

*Confirmed*: a cell's row is tile index × 256 + its local row ([0030](0030-tiles.md) and this experiment).

*Likely*: tiles without content are left out of the tile list.
