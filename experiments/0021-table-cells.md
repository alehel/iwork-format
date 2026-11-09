# 0021: Table cells

**Status:** run

[0020](0020-a-table.md) inserted an empty table and found its cell data must be in the small parts under `Index/Tables/`. This experiment puts a number in one cell and a word in another, and looks for where each value went.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface and default autocorrection |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0020](0020-a-table.md), `table.pages` (the same table, empty) |

## Recipe

As in 0020: AppleScript makes a new document with the body text `one`, and Insert → Table → Basic adds a table of 5 rows and 4 columns. Then, in the Pages window:

1. Click cell B2 and type `42`. Pages aligned it right, as it does with numbers.
2. Click cell C3 and type `abc`. Pages capitalised it to `Abc`.
3. Click below the table, and save with AppleScript as `cells.pages`.

Rows and columns are counted from 0 below, with row 0 as the header row. So B2 is row 1, column 1, and C3 is row 2, column 2.

## Observation

The same parts exist as in `table.pages`. Five records under `Index/Tables/` changed size, the largest being `Tile.iwa` (44 → 230 bytes).

### The string

`Index/Tables/DataList.iwa` (record 1732697, type 6005) gained one entry:

```
1: varint 1
2: varint 2
3: { 1: varint 1,  2: varint 1,  3: text "Abc" }
```

### The tile

`Index/Tables/Tile.iwa` (record 1732696, type 6002) gained two entries in field 5, one for each row that has a value:

```
5: { 1: 1, 2: 1, 3: bytes(12), 4: bytes(510), 5: 5, 6: bytes(36), 7: bytes(510) }
5: { 1: 2, 2: 1, 3: bytes(12), 4: bytes(510), 5: 5, 6: bytes(24), 7: bytes(510) }
```

Fields 5.4 and 5.7 are 255 two-byte little-endian values each. They are `ff ff` everywhere except at the cell's column: index 1 in the first row and index 2 in the second, where the value is `00 00`. Field 5.2 is 1 in both, and each row has one cell with a value.

Field 5.6, the cell bytes:

```
row 1 (B2, "42"):
05 02 00 00 00 00 00 00 01 30 00 00 2a 00 00 00 00 00 00 00 00 00 00 00 00 00 40 30 01 00 00 00 01 00 00 00

row 2 (C3, "Abc"):
05 03 00 00 00 00 00 00 08 10 02 00 01 00 00 00 05 00 00 00 02 00 00 00
```

## Conclusion

Cells are stored by row in the table's tile (type 6002), with one field-5 entry per row that has content:

- Field 5.1 is the row index.
- Field 5.4 (or 5.7) gives, for each of up to 255 columns, the offset of that column's cell in the row's cell bytes, or `ffff` for an empty cell.
- Field 5.6 is the cell bytes.

The two copies of the offset table don't differ here.

Each cell starts with a version byte (5) and a type byte. The type byte was 2 for the number and 3 for the text:

- A number's value is stored in 16 bytes, starting 4 bytes after the type and flag bytes. `2a 00 … 00 40 30` read as a little-endian IEEE 754 decimal128 (binary integer decimal) is 42: coefficient 42, biased exponent 6176, so exponent 0.
- A text cell holds a 32-bit little-endian key (1) instead. It refers to the string table (type 6005, `DataList.iwa`). That table's entry has the key in field 3.1, what looks like a reference count in 3.2, and the string in 3.3. Field 2 of the string table, which is 2 here, may be the next free key.

The bytes after the type, `01 30 00 00` and `08 10 02 00`, look like flags saying which values follow. The words after the value (`01 00 00 00 01 00 00 00`, `05 00 00 00 02 00 00 00`) are probably keys into other data lists, such as styles and formats. They aren't decoded yet.

## Confidence

*Likely*:

- A table's cells are stored per row in the tile (type 6002), with an offset table per row and the cell bytes in field 5.6.
- Cell byte 1 is the type: 2 number, 3 text.
- Numbers are decimal128.
- Text is a key into a string table (type 6005) whose entries hold the strings.

*Unknown*:

- The flag bytes and the trailing keys.
- Why the offset table appears twice.
- What the other 23 data lists hold. Follow-up: give one cell a bold style, and another a currency format.
