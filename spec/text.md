# 2. Text

Where a Pages document keeps its body text, and how the text is encoded. Every finding links to the experiments that support it, with a confidence level as defined in [CONTRIBUTING.md](../CONTRIBUTING.md#confidence). Records, object IDs and types are as described in [1. Container](container.md).

Observed with Pages 15.4 on macOS 26.5.2. Keynote 15.4 stores slide text in type-2001 records laid out the same way, referring to the same kinds of styles (types 401, 2022, 2023), so this layer applies to Keynote text too. *Likely* ([0025](../experiments/0025-keynote-title.md))

Field 3 of a type-2001 record is its text in all three apps. *Confirmed* over every sample of experiments 0001–0031 ([0032](../experiments/0032-reading-all-text.md)). Field 1 seems to say what kind of text the record holds: in Pages 0 is the body, 1 a header or footer and 2 a footnote ([0041](../experiments/0041-footnote.md)), Numbers uses 1 for text owned by a sheet, Keynote's presenter notes use 4 ([0039](../experiments/0039-presenter-notes.md)), and Keynote's shape text leaves it out. Text can contain U+00AD (soft hyphen). *Likely* ([0032](../experiments/0032-reading-all-text.md))

## The body text

The body text is in `Index/Document.iwa`, in field 3 of a record of type 2001. *Confirmed* ([0002](../experiments/0002-one-word.md), [0003](../experiments/0003-non-ascii-word.md))

- It is UTF-8, including characters outside the Basic Multilingual Plane, which take four bytes.
- It has no terminator or extra length prefix: the field's own length is the text's length in bytes.
- An empty body has no field 3 at all.

`Document.iwa` holds more than one type-2001 record: 19 in a new document. The body's record has field 1 set to 0, and the other 18 have field 1 set to 1. *Likely* ([0003](../experiments/0003-non-ascii-word.md)). The other 18 hold header and footer text, and use the paragraph style named for headers and footers. *Likely* ([0004](../experiments/0004-larger-word.md), [0016](../experiments/0016-header-and-footer.md))

## Page setup

Pages keeps its page setup in the document root (object 1, type 10000). All lengths are in points, as floats. *Likely* ([0027](../experiments/0027-document-roots.md), [0028](../experiments/0028-margins.md))

| Field | Holds |
| --- | --- |
| 30, 31 | Paper width and height |
| 32, 33, 34, 35 | Left, right, top and bottom margins |
| 36, 37 | Header and footer distance from the page edge |
| 43 | Printer name |
| 44 | Paper name, such as `iso-a4` |

## Headers and footers

Header and footer text is in type-2001 records, like the body. They are reached through the body's section runs (field 17), which point at a section (type 10011). Fields 23, 24 and 25 of a section each name a set of headers and footers (type 10143). In a set, field 1 lists the header and field 2 the footer, each as three text records in the order left, centre, right. A plain document uses the set in field 25. When section field 19 is 1, left-hand pages use the set in field 24 instead. *Likely* ([0016](../experiments/0016-header-and-footer.md), [0018](../experiments/0018-page-break-and-left-page.md), [0019](../experiments/0019-left-and-right-pages.md)). What the set in field 23 is for is *unknown*.

Other section fields hold switches from the Section tab of Pages' Document sidebar. *Likely* ([0017](../experiments/0017-section-switches.md))

| Section field | Switch | Values |
| --- | --- | --- |
| 17 | Same as previous section | 1 on (default), 0 off |
| 19 | Left and right pages are different (shown only with facing pages on) | 0 off (default), 1 on ([0019](../experiments/0019-left-and-right-pages.md)) |
| 28 | Hide header and footer on the section's first page | 0 off (default), 1 on |

The document-wide *Facing pages* setting is field 34 of the type-10012 record, which also holds the creation time and template name and is probably the document's settings. *Likely* ([0017](../experiments/0017-section-switches.md))

## Objects in the text

An object placed in the text, such as a table, is the character U+FFFC (OBJECT REPLACEMENT CHARACTER) in the text, with an entry in the attachment runs (field 9) at that position. *Likely* ([0020](../experiments/0020-a-table.md))

For a table, the attachment (type 2003, in `Document.iwa`) points at a drawable (type 6000, in `CalculationEngine`). The drawable holds the position and size in points (fields 1.1.1 and 1.1.2) and points at the table model (type 6001), whose fields 6, 7 and 8 are the number of rows, the number of columns and the table's name. *Likely* ([0020](../experiments/0020-a-table.md))

The table model's field 4 holds its storage: 4.3 lists the tiles, each entry giving a tile index (4.3.1.1) and the tile record (4.3.1.2), and 4.1 and 4.2 name header storage buckets (type 6006). Each tile covers 256 rows (field 4.3.2), and row numbers inside a tile are local, so a cell's row in the table is the tile index × 256 plus its row in the tile. A tile's field 4 counts its rows with content. *Likely* ([0029](../experiments/0029-numbers-root-to-table.md), [0030](../experiments/0030-tiles.md)), in Pages and Numbers alike.

A table's cells are stored by row in its tile (type 6002, `Index/Tables/Tile.iwa`). Each row with content is one field-5 entry: 5.1 is the row index, 5.4 a table of 255 little-endian 16-bit offsets into the row's cell bytes (one per column, `ffff` for an empty cell), and 5.6 the cell bytes. A cell starts with a version byte (5) and a type byte: 2 for a number, stored as a little-endian IEEE 754 decimal128, and 3 for text, stored as a 32-bit key into a string table (type 6005, `Index/Tables/DataList.iwa`) whose entries hold the key in field 3.1 and the string in 3.3. *Confirmed* ([0021](../experiments/0021-table-cells.md), [0026](../experiments/0026-numbers-cells.md)); Numbers stores cells identically.

When a row has several cells, it is field 5.7, not 5.4, that holds their byte offsets. *Likely* ([0031](../experiments/0031-cell-kinds.md))

A cell's bytes 8–11 are little-endian flags saying which values and keys follow, in order of their bits. Further type bytes are 5 (date), 6 (boolean) and 10 (currency). *Likely* ([0031](../experiments/0031-cell-kinds.md))

| Flag bit | Followed by |
| --- | --- |
| 0x0001 | A decimal128 number |
| 0x0002 | A double, for a boolean (type 6): 1.0 is true ([0036](../experiments/0036-more-cell-formats.md)) |
| 0x0004 | A date, as a little-endian double: seconds since 2001-01-01 00:00, with the shown clock time counted as UTC (no time-zone conversion) |
| 0x0200 | A key into the formula list (model field 4.6), whose entries are formulas as postfix lists of nodes |
| 0x0008 | A string key ([0021](../experiments/0021-table-cells.md)) |
| 0x0400 | A key into the cell-control list (list type 12), such as a checkbox or a rating's range ([0036](../experiments/0036-more-cell-formats.md)) |
| 0x1000 | A key into a list not identified yet (*unknown*) |
| 0x2000, 0x4000, 0x8000 | A key into the format list (model field 4.22), for a number, currency or date format |
| 0x10000, 0x20000, 0x40000 | A key into the format list, for a duration, text or boolean format ([0036](../experiments/0036-more-cell-formats.md)) |

The format list's entries give the kind of format in field 1 (256 number, 257 currency, 258 percent, 259 scientific, 260 text, 261 date, 262 fraction, 263 checkbox, 267 rating, 268 duration), plus its details, such as a currency code or a date pattern. A formula cell also keeps its last result as a value. *Likely* ([0031](../experiments/0031-cell-kinds.md))

A formula's nodes, in postfix order (*likely*, [0031](../experiments/0031-cell-kinds.md), [0035](../experiments/0035-formula-references.md)):

| Node type | Meaning | Fields |
| --- | --- | --- |
| 36 | Cell reference | 26 column, 27 row. In each, field 1 is the value and field 2 is 1 for an absolute reference. A relative value is the zigzag-encoded offset from the formula's own cell; an absolute one is the zigzag-encoded index. |
| 67 | Range | 40.1 first and last column, 40.2 first and last row, as signed offsets from the formula's cell (not zigzag) |
| 17 | Number | 4: the value as a double |
| 1, 3 | Addition, multiplication | |
| 16 | Function call | 2: the function (168 is SUM), 3: number of arguments |

An image placed on the page, rather than in the text, is a record of type 3005 in `Document.iwa`, listed next to the body text by page-level records (types 10015 and 10010). It holds its position and size in points in field 1.1, like a table's drawable, and the data ID of its file in field 11.1 (see [container.md](container.md#data-files)). *Likely* ([0023](../experiments/0023-an-image.md))

## Paragraphs

A paragraph break is a character in the text. Pressing Return in Pages writes U+000A (line feed). A U+000D (carriage return) set through AppleScript is kept as given and also starts a paragraph. The last paragraph has no break after it. *Confirmed* for U+000A ([0005](../experiments/0005-paragraphs.md), [0006](../experiments/0006-typing-in-pages.md)); *likely* for U+000D ([0005](../experiments/0005-paragraphs.md)).

Pressing Shift-Return writes U+2028 (line separator), a line break that doesn't start a paragraph. *Likely* ([0006](../experiments/0006-typing-in-pages.md))

A page break (Insert → Page Break) is the character U+0005, and it also starts a new paragraph. *Likely* ([0018](../experiments/0018-page-break-and-left-page.md))

A section break (Insert → Section Break) is the character U+0004. It starts a new paragraph and a new section: the section runs (field 17) gain an entry at the next character, pointing at a new section record with its own header-and-footer sets. *Likely* ([0040](../experiments/0040-section-break.md))

## Positions in the text

Positions in the text count UTF-16 code units, not UTF-8 bytes or code points. So a character outside the Basic Multilingual Plane counts as 2, and a reader has to convert positions before using them on the UTF-8 text. *Confirmed* ([0003](../experiments/0003-non-ascii-word.md), [0004](../experiments/0004-larger-word.md))

## Runs

Several fields of a type-2001 record are run tables: lists of entries that apply something to ranges of the text. Each entry is a message whose field 1 is the position where a run starts. Where the run applies an object, its field 2 is a message whose field 1 is that object's ID. A run lasts until the next entry, or to the end of the text. *Confirmed* ([0004](../experiments/0004-larger-word.md), [0005](../experiments/0005-paragraphs.md), [0008](../experiments/0008-runs-and-shared-styles.md)). Ranges with the same formatting point at the same object. *Likely* ([0008](../experiments/0008-runs-and-shared-styles.md)) What an entry with no field 2 means depends on the table: in field 8 it ends a character style, in field 5 it doesn't.

| Field | Runs of | Confidence |
| --- | --- | --- |
| 5 | Paragraph styles (type 2022). One entry per paragraph, at its first character; the break before it belongs to the previous paragraph. An entry names a style wherever it changes ([0034](../experiments/0034-mixed-paragraph-styles.md)); one with no field 2 seems to keep the previous paragraph's style. | *Likely* ([0002](../experiments/0002-one-word.md), [0004](../experiments/0004-larger-word.md), [0005](../experiments/0005-paragraphs.md), [0006](../experiments/0006-typing-in-pages.md)); the meaning of an entry with no field 2 is *unknown* |
| 6 | List levels. Entries start at paragraph boundaries; field 2 is a number, the level (0 for the first), not an object. Field 3 has always been 0. | *Likely* ([0015](../experiments/0015-list-levels.md)) |
| 7 | List styles (type 2023). A list is a list style on a range of paragraphs; the marker (a dash, a number) is not in the text. | *Likely* ([0002](../experiments/0002-one-word.md), [0004](../experiments/0004-larger-word.md), [0014](../experiments/0014-lists.md)) |
| 8 | Character styles (type 2021). Absent when no text has one. | *Likely* ([0004](../experiments/0004-larger-word.md)) |
| 9 | Attachments: each entry sits at a U+FFFC character in the text. In Pages it points at a type-2003 record, which points at the attached object (for a table, its drawable of type 6000). A Numbers sheet's text has an entry pointing at a type-2043 record instead, whose purpose is unknown. | *Likely* ([0020](../experiments/0020-a-table.md), [0032](../experiments/0032-reading-all-text.md)) |
| 12 | Objects of type 2024 | *Unknown* |
| 16 | Footnotes: an entry at each U+000E footnote mark points at a type-2008 record, whose field 2 names the footnote's text (a type-2001 record with field 1 = 2) | *Likely* ([0041](../experiments/0041-footnote.md)) |
| 17 | Sections (type 10011 in `Document.iwa`), which hold among other things the headers and footers | *Likely* ([0016](../experiments/0016-header-and-footer.md)) |
| 19 | Languages: field 2 is a language code as text, such as `nb`. Only text typed or rewritten in Pages has one; text set through AppleScript has no field 19, or an entry without field 2. | *Confirmed* ([0006](../experiments/0006-typing-in-pages.md), [0009](../experiments/0009-autocorrection.md)) |
| 20 | Autocorrections: each range Pages autocorrected has a UUID as text in field 2, and an entry without one closes it. Absent when nothing was corrected. | *Confirmed* ([0006](../experiments/0006-typing-in-pages.md), [0009](../experiments/0009-autocorrection.md)) |

Field 2 of the record names the type-401 object that holds the styles, which is probably the stylesheet. Fields 14, 24 and 28 hold entries of zeros in every document so far. *Unknown*

## Styles

Changing the size of part of the text, or making it bold or italic, creates a new, unnamed character style (type 2021) in `DocumentStylesheet.iwa`. It inherits (field 1.3) from a character style whose identifier is `character-style-null`. *Confirmed* ([0004](../experiments/0004-larger-word.md), [0007](../experiments/0007-bold-and-italic.md), [0008](../experiments/0008-runs-and-shared-styles.md))

Formatting a whole paragraph instead creates an unnamed paragraph style (type 2022) that inherits from the paragraph's style and carries the change. *Likely* ([0008](../experiments/0008-runs-and-shared-styles.md))

Field 11 of a character style or a paragraph style holds the character properties it sets. A property that is left out is inherited, and one set to 0 is turned off. *Likely* ([0004](../experiments/0004-larger-word.md), [0007](../experiments/0007-bold-and-italic.md), [0008](../experiments/0008-runs-and-shared-styles.md))

| Field 11.n | Property | Encoding |
| --- | --- | --- |
| 1 | Bold | varint: 1 bold, 0 not bold |
| 2 | Italic | varint: 1 italic |
| 3 | Size in points | float |
| 5 | Font name, such as `HelveticaNeue` | text |
| 7 | Text colour | message: red, green and blue in fields 3, 4 and 5 and alpha in field 6, as floats from 0 to 1; colour space unknown |
| 11 | Underline | varint: 1 underlined, 0 not |
| 12 | Strikethrough | varint: 1 struck through, 0 not |

Field 11.5 is *likely* ([0010](../experiments/0010-alignment.md)), and so are 11.7 ([0013](../experiments/0013-text-colour.md)), 11.11 and 11.12 ([0012](../experiments/0012-underline-and-strikethrough.md)); the rest as above.

A paragraph style also has a field 12 for paragraph properties. *Likely* ([0008](../experiments/0008-runs-and-shared-styles.md), [0010](../experiments/0010-alignment.md))

| Field 12.n | Property | Encoding |
| --- | --- | --- |
| 1 | Alignment | varint: 0 left, 1 right, 2 centred, 3 justified, 4 probably natural (the Body style's value, shown as left) |

Values 0 to 3 are *confirmed* ([0010](../experiments/0010-alignment.md), [0011](../experiments/0011-left-alignment.md)); 4 as natural alignment is *likely*.

Named styles such as Body set every property; unnamed ones set only what differs from their parent (field 1.3). *Likely* ([0010](../experiments/0010-alignment.md))

Field 10 has equalled the number of properties set in every unnamed style so far, and is 57 in the named paragraph styles, which set 59. It doesn't count edits. *Unknown* ([0010](../experiments/0010-alignment.md), [0011](../experiments/0011-left-alignment.md))

A list style (type 2023) stores most properties as nine repeated values, one per list level. Field 11 is the kind of marker (0 none, 2 a text character, 3 a number), field 16 the marker text for kind 2, and field 13 an indent in points that grows by a fixed step per level. *Likely* ([0014](../experiments/0014-lists.md))

To find a character's formatting, take each property from the first style that sets it. Look first in its character style (from the field-8 runs), then that style's parent (field 1.3), and so on. Then look in its paragraph style (from the field-5 runs) and that style's parents. A property set to 0 counts as set. A font name in 11.5 may already include a weight, such as `HelveticaNeue-Bold`. *Likely* for bold, italic, size and font: the rule predicted Pages' own reading of all 19 words of 8 documents ([0033](../experiments/0033-style-resolution.md), [0034](../experiments/0034-mixed-paragraph-styles.md)). It also holds for text colour ([0042](../experiments/0042-colour-resolution.md)).

Styles get their own layer once more of them are understood.
