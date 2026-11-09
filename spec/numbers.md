# Numbers

What is specific to Numbers documents. The container is the same as Pages' ([container.md](container.md)), and tables are stored as described in [text.md](text.md#objects-in-the-text). Every finding links to the experiments that support it, with a confidence level as defined in [CONTRIBUTING.md](../CONTRIBUTING.md#confidence).

Observed with Numbers 15.4 on macOS 26.5.2.

## Parts

A new spreadsheet has the seven `.iwa` parts that Pages documents have, without numbers in their names. It also has the table parts under `Index/Tables/`, because a new spreadsheet holds an empty table. Those are named as in Pages (see [container.md](container.md#the-package)), including some with a `-2` ending. *Likely* ([0024](../experiments/0024-keynote-and-numbers.md), [0026](../experiments/0026-numbers-cells.md), [0030](../experiments/0030-tiles.md))

## From the root to a table's cells

| Type | Holds | Part |
| --- | --- | --- |
| 1 | The document root: field 1 lists the sheets in order ([0037](../experiments/0037-second-sheet.md)), field 8 holds the shared document-properties block, and fields 11 and 12 the paper name and size | `Document.iwa` |
| 2 | A sheet: field 1 is its name (*confirmed*, [0124](../experiments/0124-sheet-name.md)), and the repeated field 2 lists its drawables in order: tables, text boxes, shapes and images ([0047](../experiments/0047-second-table.md), [0127](../experiments/0127-text-box-on-sheet.md)–[0129](../experiments/0129-shape-on-sheet.md)). Tables aren't anchored in the sheet's text. | `Document.iwa` |
| 6000 | A table's drawable: position and size, and in field 2 the table model | `CalculationEngine.iwa` |
| 6001 | The table model: rows (6), columns (7), name (8), and its storage in field 4. Field 4.3 lists the tiles. | `CalculationEngine.iwa` |
| 6002 | A tile: the cells, by row | `Tables/Tile.iwa` |

*Likely* ([0029](../experiments/0029-numbers-root-to-table.md))

## Categories

Grouping rows by a column's values (Organise → Add Category) moves no cells. The groups are a tree of type-6383 records in `CalculationEngine.iwa`: each group has a 128-bit ID (field 1), its value as a typed cell value (field 6), its rows (field 9, single row numbers `{ 1: n }` or ranges `{ 1: first, 2: last }`) and its child groups (field 10). Table model field 81.2.6 becomes 1. The summary rows Numbers shows aren't stored. *Likely* ([0226](../experiments/0226-category.md))

## Pivot tables

A pivot table is an ordinary table model whose cells hold the current summary, so it reads like any table. Numbers also adds a hidden table model with a copy of the source data, named after the source with ` as Pivot Source Table`, and new record types (6369, 6370, 6374, 6382). Type 6370 names the source table in field 12 and holds the last update time in field 9. *Likely* ([0227](../experiments/0227-pivot-table.md))
