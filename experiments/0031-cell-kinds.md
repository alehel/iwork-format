# 0031: Kinds of cell

**Status:** run

[0021](0021-table-cells.md) and [0026](0026-numbers-cells.md) decoded a plain number and a text cell, but left the flag bytes and the keys after the value open. This experiment fills one row of a Numbers table with a currency, a percentage, a boolean, a date, a formula and a plain number, and decodes each cell.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0026](0026-numbers-cells.md) |

## Recipe

```bash
mkdir -p samples/0031
osascript recipes/0031-numbers-cell-kinds.applescript "$PWD/samples/0031/kinds.numbers"
```

| Cell | Set to | Numbers then showed |
| --- | --- | --- |
| B2 | 42, format currency | `42,00 kr` |
| C2 | 0.25, format percent | `25 %` |
| D2 | `true` | `1`, format automatic. AppleScript's true became a number, not a checkbox. |
| E2 | 2026-01-02 12:00 | `02.01.2026 12:00` |
| F2 | `=B2*2` | `84,00 kr` |
| G2 | 42 | `42` |

The shown values and formats were read back by opening the file in Numbers through AppleScript (`formatted value` and `format` of each cell).

## Observation

### Splitting the row into cells

The row's two offset tables, fields 5.4 and 5.7 of the tile, differ once a row has more than one cell:

```
5.4: column 1 → 0, 2 → 12, 3 → 24, 4 → 36, 5 → 48, 6 → 60
5.7: column 1 → 0, 2 → 36, 3 → 72, 4 → 108, 5 → 136, 6 → 176
```

Only 5.7 splits the cell bytes so that every cell starts with the version byte `05`. So 5.7 holds byte offsets, and 5.4 something else that grows by 12 per cell.

### The cells

| Cell | Bytes 0–1 | Bytes 8–11 (flags) | Then |
| --- | --- | --- | --- |
| G2 | `05 02` | `01 30 00 00` = 0x3001 | decimal128 42; keys 1, 1 |
| C2 | `05 02` | 0x3001 | decimal128 `19 00 … 3c 30` = 25 × 10⁻² = 0.25; keys 1, 3 |
| D2 | `05 02` | 0x3001 | decimal128 1; keys 1, 1 |
| B2 | `05 0a` | `01 50 00 00` = 0x5001 | decimal128 42; keys 2, 2 |
| E2 | `05 05` | `04 90 00 00` = 0x9004 | 8 bytes `00 00 00 60 f5 83 c7 41`; keys 3, 4 |
| F2 | `05 0a` | `01 52 00 00` = 0x5201 | decimal128 84; keys 1, 2, 2 |

B2's bytes 4–7 are `00 00 02 08`, and C2's are `00 00 01 00`. The other cells have zeros there.

E2's 8 bytes, read as a little-endian double, are 789,048,000. That is the number of seconds from 2001-01-01 00:00 to 2026-01-02 12:00, counting both as UTC. The clock time shown in the cell, 12:00, is stored as-is, with no conversion from the Mac's time zone (Oslo, UTC+1).

### The lists the keys point into

The table model's field 4.22 names data list 904541 (type 6005, list type 2). It has four entries:

| Key | Count | Entry |
| --- | --- | --- |
| 1 | 2 | `{ 1: 256, 2: 253 }` |
| 2 | 2 | `{ 1: 257, 2: 2, 3: "NOK" }` |
| 3 | 1 | `{ 1: 258, 2: 253 }` |
| 4 | 1 | `{ 1: 261, 14: "dd.MM.y HH:mm" }` |

Model field 4.6 names data list 904540 (list type 3), with one entry, key 1:

```
5: { 1: { 1: 36, 26: {…}, 27: {…} },     ← node type 36
          { 1: 17, 4: 2.0 },              ← node type 17, the number 2
          { 1: 3 } }                      ← node type 3
```

## Conclusion

A cell's bytes:

| Bytes | Holds |
| --- | --- |
| 0 | Version, 5 |
| 1 | Type: 2 number, 3 text ([0021](0021-table-cells.md)), 5 date, 10 currency |
| 2–7 | Mostly zero; B2 and C2 had something in 4–7 |
| 8–11 | Flags (little-endian), saying which values and keys follow, in order of their bits |
| then | The values and keys the flags name |

The flag bits:

| Bit | What follows |
| --- | --- |
| 0x0001 | A decimal128 number |
| 0x0004 | A date: a double, seconds since 2001-01-01 00:00, with the cell's clock time counted as UTC |
| 0x0200 | A formula: a key into the formula list (model field 4.6) |
| 0x1000 | A key into a list not identified yet |
| 0x2000 | A number format: a key into the format list (model field 4.22) |
| 0x4000 | A currency format: a key into the format list |
| 0x8000 | A date format: a key into the format list |

Text cells (type 3) carry their string key the same way, but their flags in 0021 (`08 10 02 00`) haven't been decoded bit by bit yet.

In the format list, field 1 of each entry is the format kind: 256 number, 257 currency, 258 percent and 261 date. A currency entry gives its currency code (`NOK`). A date entry gives its pattern (`dd.MM.y HH:mm`). Field 2 is probably the number of decimals, with 253 meaning automatic. A percentage is stored as the fraction (0.25) with a percent format, not as 25.

A formula cell keeps its last result as a value (84) next to the key of its formula. Formulas are stored as a list of nodes in postfix order: here a cell reference (type 36), the number 2 (type 17) and the multiplication (type 3), for `B2*2`. It also took B2's currency format.

AppleScript's `true` became the number 1. A real checkbox cell will need the Numbers window.

## Confidence

*Likely*:

- The cell layout and flag bits listed above, except 0x1000.
- Field 5.7 of a tile row holds byte offsets.
- Format list entries are as described.
- Formula entries are lists of postfix nodes.

*Unknown*:

- Bit 0x1000 and its list.
- Bytes 4–7 of a cell.
- What field 5.4 counts.
- The fields of the cell-reference node (26 and 27).

Follow-ups:

- A formula that references a different cell, to decode node 36.
- A checkbox cell made in the Numbers window.
