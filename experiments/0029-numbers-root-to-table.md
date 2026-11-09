# 0029: From Numbers' root to a table

**Status:** run

[0027](0027-document-roots.md) followed Keynote's root down to a slide's text. This experiment does the same for Numbers, from the root down to the tile that holds the cells written in [0026](0026-numbers-cells.md). It also checks how the table model points at its tile in both Numbers and Pages. It saves no new documents.

## Setup

| | |
| --- | --- |
| Apps | Numbers and Pages 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Documents | `samples/0026/cells.numbers`, `samples/0021/cells.pages` |

## Recipe

A breadth-first walk over `iwork-probe refs` output finds the path of header references from object 1 to the tile (`Index/Tables/Tile.iwa`). Each record along it was printed with `iwork-probe proto --decoded`.

## Observation

### The path

| Object | Type | Part | What it holds |
| --- | --- | --- | --- |
| 1 | 1 | `Document.iwa` | the shared document-properties block, the paper size |
| 904532 | 2 | `Document.iwa` | 1: `"Ark 1"` (Norwegian for "Sheet 1"); 2: `{ 1: 904769 }`; and more, see below |
| 904769 | 6000 | `CalculationEngine.iwa` | the table's drawable, as in [0020](0020-a-table.md) |
| 904595 | 6001 | `CalculationEngine.iwa` | 1: a UUID; 8: `"Tabell 1"` |
| 904547 | 6002 | `Tables/Tile.iwa` | the cells, as in [0026](0026-numbers-cells.md) |

The sheet's other fields include 10: four floats (54, 36, 54, 36), 13 and 14: 20.0 each, and 17: a reference to 904606.

### How the table model reaches its tile

The start of field 4 of the type-6001 model:

```
4:
  1: { 1: 1, 2: { 1: 904914 } }     ← HeaderStorageBucket-904914
  2: { 1: 904958 }                  ← HeaderStorageBucket-904958
  3: { 1: { 1: 0, 2: { 1: 904547 } }, 2: 256 }     ← the tile
  …
```

Pages' model (0021) has field 4 laid out the same way, with field 4.3.1.2 naming its tile (1732696) and 4.2 naming a header storage bucket (1732917).

## Conclusion

A Numbers document goes root (type 1) → sheet (type 2, with its name in field 1 and its first drawable in field 2) → the table's drawable (type 6000) → the table model (type 6001). From the model, field 4 holds the table's storage:

- 4.1 and 4.2 name header storage buckets (type 6006, in `Tables/HeaderStorageBucket-N.iwa`)
- 4.3 lists the tiles, each entry giving a tile index (4.3.1.1) and the tile record (4.3.1.2)

Field 4.3.2, 256, is probably the number of rows a tile covers. That would explain why a small table has a single tile, index 0.

Pages lays out the table model's field 4 the same way, so a table reader can be shared. Only the route to the drawable differs: through the sheet in Numbers, and through a text attachment (U+FFFC and a type-2003 record) in Pages.

Type 2 is the sheet in Numbers but, from [0027](0027-document-roots.md), the presentation in Keynote. Like type 1, it is a type number that means different things in different apps.

## Confidence

*Likely*:

- Numbers' chain is root → sheet (type 2) → drawable (6000) → table model (6001) → tile (6002).
- Table model field 4.3 lists the tiles, and 4.1 and 4.2 name header storage.

*Unknown*:

- Whether a tile covers 256 rows. Follow-up: put a value in row 300 of a Numbers table, and look for a second tile with index 1.
- What the header storage buckets hold.
