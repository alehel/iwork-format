# 0020: A table

**Status:** run

The first object other than text. This experiment inserts Pages' default *Basic* table after a word and looks at the new parts, at how the text refers to the table, and at where the table's size is stored. The cells stay empty.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `plain.pages`: the body text `one`, made by the [0002](0002-one-word.md) recipe |

## Recipe

```bash
mkdir -p samples/0020
osascript recipes/0002-one-word.applescript "$PWD/samples/0020/plain.pages" one
```

For `table.pages`, AppleScript makes a new document and sets its body text to `one`. In the Pages window, click at the end of `one`, then choose Insert → Table → Basic (*Sett inn → Tabell → Enkel*). Pages inserted a table of 5 rows and 4 columns, with one header row, below the text. AppleScript saves the document.

## Observation

### New parts

`table.pages` has the same 13 parts as `plain.pages`, plus 30 parts in a new folder, `Index/Tables/`:

| Parts | Count | Record type in each |
| --- | --- | --- |
| `Index/Tables/DataList.iwa`, `Index/Tables/DataList-N-2.iwa` | 1 + 23 | 6005 |
| `Index/Tables/HeaderStorageBucket.iwa`, `Index/Tables/HeaderStorageBucket-N-2.iwa` | 1 + 3 | 6006 |
| `Index/Tables/Tile.iwa`, `Index/Tables/Tile-N-2.iwa` | 1 + 1 | 6002 |

Each of these parts holds exactly one record. In a part named `…-N-2.iwa`, the record's ID is N. A part without a number holds the lowest ID of its kind. The chunk and record layout of [spec/container.md](../spec/container.md) held for all 43 parts.

`CalculationEngine-1732610.iwa` grew from 8 records to 40, among them one of type 6000 and one of type 6001. `Document.iwa` gained one record, of type 2003. `ViewState.iwa` gained one, of type 3061.

### The text

The body's text gained one character, U+FFFC (OBJECT REPLACEMENT CHARACTER), after `one`:

```
3: text (6 bytes) "one\u{fffc}"            6f 6e 65 ef bf bc
```

The body's type-2001 record gained a field 9, which is a run table with one entry at position 3, the U+FFFC:

```
9: { 1: { 1: 3, 2: { 1: 1732897 } } }
```

### From the character to the table

```
body 2001, field 9 at 3  →  1732897, type 2003 (Document.iwa)
                               1: { 1: 1732720 }
                               2–5: zeros
                         →  1732720, type 6000 (CalculationEngine)
                               1.1.1: { 1: 100.14, 2: 70.69 }     (floats)
                               1.1.2: { 1: 481.89, 2: 114.0 }
                               1.2:   { 1: 1732539 }              ← the body
                               2:     { 1: 1732723 }
                         →  1732723, type 6001 (CalculationEngine, 884 bytes)
                               1: "59BC6969-543E-4D8C-AB80-E93B6A5855AB"
                               6: 5
                               7: 4
                               8: "Tabell 1"
                               (and about 50 references to other objects)
```

The table's default size is 4 columns of 4.25 cm and 5 rows of 0.8 cm, as the sidebar showed. That is 481.9 × 113.4 points. Field 1.1.2 of the type-6000 record is 481.89 × 114.

### Headers that list references

The header of record 1732723 is 478 bytes, against about 20 for most records. It repeats header field 2.4 27 times, and each entry looks like this:

```
4: { 1: "F",  2: 3,  3: 0,  4: bytes b2 e2 69 b3 e2 69 }
```

Read as packed varints, 2.4.4 here is 1732914 and 1732915, two IDs of objects in the same part. The one-byte texts in 2.4.1 (`V`, `U`, `R`, `F`, `P` …) could be field numbers (86, 85, 82, 70, 80) that happen to be printable.

## Conclusion

A table sits in the text as one U+FFFC character. A run table in field 9 of the text record points that position at a type-2003 record. A reader can use field 9 to find the objects anchored in the text.

The type-2003 record points at a type-6000 record, which looks like the table's drawable. It holds a position and a size in points, and refers back to the text it is anchored in. The drawable points at the table model, type 6001, which holds the number of rows (field 6) and columns (field 7) and the table's name (field 8).

The table's cell data lives in the many small parts under `Index/Tables/`, which hold data lists (type 6005), header storage (type 6006) and tiles (type 6002). Pages names these parts after the ID of the record they hold, with a `-2` ending this experiment doesn't explain.

Header field 2.4 seems to list a record's references to other objects, grouped by the field that holds them. If so, a reader could find every object a record depends on without understanding the payload. That needs checking against records whose references are known.

## Confidence

*Likely*:

- A table is anchored by U+FFFC, with field 9 of the text record as the run table of attachments.
- A type-2003 record points at the table's type-6000 drawable, which holds the position and size and points at the type-6001 model.
- Fields 6, 7 and 8 of type 6001 are the rows, columns and name.

*Unknown*:

- How cells are stored in the `Index/Tables/` parts.
- Why there are two tiles, and what the `-2` in the part names means.
- Whether header field 2.4 lists references. Follow-up: compare 2.4 with the references in the body's type-2001 record, which are known.

Follow-up for the cells: type a word into one cell and compare (0021).
