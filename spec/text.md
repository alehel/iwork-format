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
| 42 | Orientation: 0 portrait, 1 landscape; 30 and 31 are already swapped ([0155](../experiments/0155-landscape-template.md)) |
| 44 | Paper name, such as `iso-a4` |
| 15.9 | The identifier of the template the document came from, such as `Application/Blank/ISO` ([0155](../experiments/0155-landscape-template.md)) |
| 48 | Only in page-layout documents: names a page template (type 10017). Their body text record is empty. ([0156](../experiments/0156-page-layout-template.md)) |

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

For a table, the attachment (type 2003, in `Document.iwa`) points at a drawable (type 6000, in `CalculationEngine`). The drawable holds the position and size in points (fields 1.1.1 and 1.1.2) and points at the table model (type 6001), whose fields 6, 7 and 8 are the number of rows, the number of columns and the table's name, and fields 9, 10 and 11 the numbers of header rows, header columns and footer rows (absent means 0; footer rows count within the rows, [0184](../experiments/0184-footer-row.md)), field 12 whether header rows are frozen ([0125](../experiments/0125-unfrozen-headers.md)) and field 13 whether header columns are ([0183](../experiments/0183-unfrozen-header-columns.md)). Rows, columns and name are *confirmed* ([0120](../experiments/0120-fewer-rows.md), [0122](../experiments/0122-table-name.md), [0123](../experiments/0123-fewer-columns.md)). A Numbers table's stored y is 28 points less than the y Numbers reports ([0126](../experiments/0126-table-at-origin.md)). Sorting rewrites the rows ([0119](../experiments/0119-sorted-rows.md)), and so does transposing, which also swaps fields 6 and 7 ([0182](../experiments/0182-transposed-table.md)). *Likely* ([0020](../experiments/0020-a-table.md), [0060](../experiments/0060-header-rows.md)). A table's size is the sum of its row heights and column widths. The drawable's size can be out of date ([0059](../experiments/0059-table-geometry.md)).

The table model's field 4 holds its storage: 4.3 lists the tiles, each entry giving a tile index (4.3.1.1) and the tile record (4.3.1.2), and 4.1 and 4.2 name the row and column header storage buckets (type 6006). A bucket lists rows or columns with their own size in its repeated field 2: field 1 is the index and field 2 the height or width in points ([0045](../experiments/0045-row-and-column-sizes.md)). Each tile covers 256 rows (field 4.3.2), and row numbers inside a tile are local, so a cell's row in the table is the tile index × 256 plus its row in the tile. A tile's field 4 counts its rows with content. *Likely* ([0029](../experiments/0029-numbers-root-to-table.md), [0030](../experiments/0030-tiles.md)), in Pages and Numbers alike. The row rule is *confirmed* ([0030](../experiments/0030-tiles.md), [0063](../experiments/0063-sparse-tiles.md)). Tiles without content are left out of the list, so a reader must use each entry's tile index. *Likely* ([0063](../experiments/0063-sparse-tiles.md))

A table's cells are stored by row in its tile (type 6002, `Index/Tables/Tile.iwa`). Each row with content is one field-5 entry: 5.1 is the row index, 5.4 a table of 255 little-endian 16-bit offsets into the row's cell bytes (one per column, `ffff` for an empty cell), and 5.6 the cell bytes. A cell starts with a version byte (5) and a type byte: 2 for a number, stored as a little-endian IEEE 754 decimal128, and 3 for text, stored as a 32-bit key into a string table (type 6005, `Index/Tables/DataList.iwa`) whose entries hold the key in field 3.1, the number of cells using it in 3.2 and the string, as UTF-8, in 3.3 ([0113](../experiments/0113-shared-string.md), [0118](../experiments/0118-emoji-in-cell.md)). Equal texts share an entry, unused entries are removed ([0114](../experiments/0114-cleared-cell.md)), and long texts are stored whole ([0130](../experiments/0130-long-text.md)). *Confirmed* ([0021](../experiments/0021-table-cells.md), [0026](../experiments/0026-numbers-cells.md)); all three apps store the same cells byte for byte, and keep formulas, merges and header counts the same way ([0131](../experiments/0131-pages-table-cells.md)–[0137](../experiments/0137-keynote-currency.md)).

When a row has several cells, it is field 5.7, not 5.4, that holds their byte offsets. *Likely* ([0031](../experiments/0031-cell-kinds.md))

A cell's bytes 8–11 are little-endian flags saying which values and keys follow, in order of their bits. Further type bytes are 0 (no value, formatting only, [0138](../experiments/0138-empty-styled-cell.md)), 5 (date), 6 (boolean), 8 (a formula whose result is an error, stored with no value, [0078](../experiments/0078-formula-error.md)) and 10 (currency). *Likely* ([0031](../experiments/0031-cell-kinds.md))

| Flag bit | Followed by |
| --- | --- |
| 0x0001 | A decimal128 number |
| 0x0002 | A double, for a boolean (type 6): 1.0 is true and 0.0 false, for a checkbox or a formula's result ([0036](../experiments/0036-more-cell-formats.md), [0169](../experiments/0169-unchecked-checkbox.md), [0175](../experiments/0175-boolean-formula.md)) |
| 0x0004 | A date, as a little-endian double: seconds since 2001-01-01 00:00, with the shown clock time counted as UTC (no time-zone conversion) |
| 0x0200 | A key into the formula list (model field 4.6), whose entries are formulas as postfix lists of nodes |
| 0x0008 | A string key ([0021](../experiments/0021-table-cells.md)) |
| 0x0020 | A key into the style list (list type 4) naming a cell style: type 6004, background colour in field 11.1.1, text wrap in 11.3 (0 off) ([0043](../experiments/0043-cell-styles.md), [0062](../experiments/0062-text-wrap.md)) |
| 0x0040 | A key into the style list naming a text style: an unnamed paragraph style (type 2022) with the cell text's character properties and its alignment in 12.1 ([0043](../experiments/0043-cell-styles.md), [0061](../experiments/0061-cell-alignment.md)) |
| 0x0400 | A key into the cell-control list (list type 12). Its entry's field 12.1 is the control (4 stepper, 5 slider, 6 rating, 8 checkbox) and 12.3, 12.4 and 12.5 the minimum, maximum and step ([0036](../experiments/0036-more-cell-formats.md), [0169](../experiments/0169-unchecked-checkbox.md)–[0172](../experiments/0172-stepper.md)) |
| 0x1000 | A key into a list not identified yet (*unknown*) |
| 0x2000, 0x4000, 0x8000 | A key into the format list (model field 4.22), for a number, currency or date format |
| 0x10000, 0x20000, 0x40000 | A key into the format list, for a duration, text or boolean format ([0036](../experiments/0036-more-cell-formats.md)) |

The format list's entries give the kind of format in field 1 (256 number, 257 currency, 258 percent, 259 scientific, 260 text, 261 date, 262 fraction, 263 checkbox, 267 rating, 268 duration, 269 numeral system ([0181](../experiments/0181-numeral-system.md)), whose field 8 is probably the base), plus its details, such as a currency code or a date pattern. A formula cell also keeps its last result as a value, as a cell of the result's type: a date, or text through the string table ([0108](../experiments/0108-today.md), [0110](../experiments/0110-text-result.md)). A negative decimal128 has its sign bit set, *confirmed* ([0112](../experiments/0112-unary-minus.md), [0174](../experiments/0174-negative-number.md)). Text that looks like a number is stored as a number unless the cell's format is text ([0176](../experiments/0176-number-as-text.md)). *Likely* ([0031](../experiments/0031-cell-kinds.md))

A formula's nodes, in postfix order (*likely*, [0031](../experiments/0031-cell-kinds.md), [0035](../experiments/0035-formula-references.md)):

| Node type | Meaning | Fields |
| --- | --- | --- |
| 36 | Cell reference | 26 column, 27 row (absent for a whole column, [0105](../experiments/0105-whole-column.md)), and for another table, on any sheet, 28.1: its UUID as four little-endian 32-bit words ([0065](../experiments/0065-cross-table-reference.md), [0107](../experiments/0107-other-sheet.md)). Column and row each have their own absolute flag ([0106](../experiments/0106-mixed-references.md)). In each, field 1 is the value and field 2 is 1 for an absolute reference. A relative value is the zigzag-encoded offset from the formula's own cell; an absolute one is the zigzag-encoded index. |
| 67 | Range | 40.1 first and last column, 40.2 first and last row, as signed offsets from the formula's cell (not zigzag) |
| 17 | Number | 4: the value as a double; 42 and 43: the same value as the low and high 64 bits of a decimal128 ([0104](../experiments/0104-nested-functions.md)) |
| 19 | Text literal | 6: the text ([0109](../experiments/0109-string-literal.md)) |
| 13, 15 | Unary minus, percent (both after their operand) ([0111](../experiments/0111-percent-literal.md), [0112](../experiments/0112-unary-minus.md)) | |
| 1–6 | Operators: 1 `+`, 2 `-`, 3 `*`, 4 `/`, 5 `^`, 6 `&` ([0064](../experiments/0064-operators-and-functions.md)) | |
| 7–12 | Comparisons: 7 `>`, 8 `>=`, 9 `<`, 10 `<=`, 11 `=`, 12 `<>` ([0066](../experiments/0066-comparisons-and-if.md)) | |
| 34, 35 | Bracket an argument that is evaluated only when needed, as IF's second and third ([0066](../experiments/0066-comparisons-and-if.md)) | |
| 16 | Function call | 2: the function, 3: number of arguments. Functions seen: 15 AVERAGE, 30 COUNT, 62 IF, 77 LEN, 84 MAX, 88 MIN, 126 ROUND, 154 TODAY, 168 SUM ([0103](../experiments/0103-round.md), [0108](../experiments/0108-today.md), [0109](../experiments/0109-string-literal.md)), numbered in alphabetical order ([0064](../experiments/0064-operators-and-functions.md)). A SUM node also ends a merged range ([0044](../experiments/0044-merged-cells.md)). |

Merged cells are recorded in the table model's field 47.2, as ranges in this node form, not in the cells. A merged cell keeps its value in its top-left cell. *Likely* ([0044](../experiments/0044-merged-cells.md))

An image placed on the page, rather than in the text, is a record of type 3005 in `Document.iwa`, listed next to the body text by page-level records (types 10015 and 10010). It holds its position and size in points in field 1.1, like a table's drawable, and the data ID of its file in field 11.1, with a reduced copy for a large image in field 12 ([0148](../experiments/0148-large-image.md)) (see [container.md](container.md#data-files)). *Likely* ([0023](../experiments/0023-an-image.md)). Field 9 is its natural size and fields 1.1.2 and 4 the size it is drawn at ([0055](../experiments/0055-image-size.md)). Field 3 names its image style (type 3016), whose field 11.2 is the opacity from 0 to 1 ([0057](../experiments/0057-image-opacity.md)) and 11.4 the reflection, with its strength in 11.4.1 ([0099](../experiments/0099-image-reflection.md)).

A text box, a shape and a line are all shapes of type 2011, listed by the same page-level record. A shape's position and size are in field 1.1, its outline path in 1.3 and its style (type 2025, such as `textbox-0-shapestyle`, `shape-0-shapestyle` or `line-0-shapestyle`) in 1.2. Fields 2 and 4 name its text, a type-2001 record with no field 1. *Likely* ([0049](../experiments/0049-text-box.md), [0050](../experiments/0050-shape.md), [0051](../experiments/0051-line.md)) A shape style keeps its properties one level deeper than text styles, in field 1.11; field 1.11.1.1 is the fill colour, in the same colour layout as text colour, and 1.11.3 the opacity. *Likely* ([0077](../experiments/0077-shape-fill.md), [0098](../experiments/0098-keynote-shape-opacity.md))

An object is either in the text (a U+FFFC with an attachment, and its drawable's field 1.2 names that text) or on the page (listed by type 10015, with no field 1.2). *Likely* ([0020](../experiments/0020-a-table.md), [0052](../experiments/0052-floating-table.md))

In the geometry of any drawable (field 1.1), 1.1.1 is the position and 1.1.2 the size of the unrotated box, in points, and 1.1.4 its rotation in degrees about its centre, counter-clockwise on the page (*confirmed*, [0056](../experiments/0056-image-rotation.md), [0097](../experiments/0097-keynote-shape-rotation.md)). Field 1.5 is 1 for a locked object ([0100](../experiments/0100-locked-object.md)) and field 1.8 is its accessibility description, in Keynote and Pages alike (*confirmed*, [0102](../experiments/0102-image-description.md), [0177](../experiments/0177-pages-image-description.md)). A line is a box of zero height, rotated. *Likely* ([0051](../experiments/0051-line.md))

## Paragraphs

A paragraph break is a character in the text. Pressing Return in Pages writes U+000A (line feed). A U+000D (carriage return) set through AppleScript is kept as given and also starts a paragraph. The last paragraph has no break after it. *Confirmed* for U+000A ([0005](../experiments/0005-paragraphs.md), [0006](../experiments/0006-typing-in-pages.md)); *likely* for U+000D ([0005](../experiments/0005-paragraphs.md)).

Pressing Shift-Return writes U+2028 (line separator), a line break that doesn't start a paragraph. *Likely* ([0006](../experiments/0006-typing-in-pages.md))

A page break (Insert → Page Break) is the character U+0005, and it also starts a new paragraph. *Likely* ([0018](../experiments/0018-page-break-and-left-page.md))

A tab (U+0009) and a non-breaking space (U+00A0) are plain characters with no runs of their own. *Likely* ([0058](../experiments/0058-tab-and-nbsp.md))

A section break (Insert → Section Break) is the character U+0004. It starts a new paragraph and a new section: the section runs (field 17) gain an entry at the next character, pointing at a new section record with its own header-and-footer sets. *Likely* ([0040](../experiments/0040-section-break.md))

## Positions in the text

Positions in the text count UTF-16 code units, not UTF-8 bytes or code points. So a character outside the Basic Multilingual Plane counts as 2, and an emoji joined from several (such as 👨‍👩‍👧) counts every unit, joiners included. A reader has to convert positions before using them on the UTF-8 text. *Confirmed* ([0003](../experiments/0003-non-ascii-word.md), [0004](../experiments/0004-larger-word.md), [0149](../experiments/0149-family-emoji.md))

No writing direction is stored for right-to-left text set through AppleScript; lay text out by the Unicode bidirectional rules. *Likely* ([0150](../experiments/0150-arabic-text.md))

## Runs

Several fields of a type-2001 record are run tables: lists of entries that apply something to ranges of the text. Each entry is a message whose field 1 is the position where a run starts. Where the run applies an object, its field 2 is a message whose field 1 is that object's ID. A run lasts until the next entry, or to the end of the text. *Confirmed* ([0004](../experiments/0004-larger-word.md), [0005](../experiments/0005-paragraphs.md), [0008](../experiments/0008-runs-and-shared-styles.md)). Ranges with the same formatting point at the same object. *Confirmed* ([0008](../experiments/0008-runs-and-shared-styles.md), [0054](../experiments/0054-shared-sizes.md)) What an entry with no field 2 means depends on the table: in field 8 it ends a character style, in field 5 it doesn't.

| Field | Runs of | Confidence |
| --- | --- | --- |
| 5 | Paragraph styles (type 2022). One entry per paragraph, at its first character, even when the style doesn't change ([0151](../experiments/0151-thousand-paragraphs.md)); the break before it belongs to the previous paragraph. An entry names a style wherever it changes ([0034](../experiments/0034-mixed-paragraph-styles.md)); one with no field 2 seems to keep the previous paragraph's style. | *Likely* ([0002](../experiments/0002-one-word.md), [0004](../experiments/0004-larger-word.md), [0005](../experiments/0005-paragraphs.md), [0006](../experiments/0006-typing-in-pages.md)); the meaning of an entry with no field 2 is *unknown* |
| 6 | List levels. Entries start at paragraph boundaries; field 2 is a number, the level (0 for the first), not an object. Field 3 has always been 0. | *Likely* ([0015](../experiments/0015-list-levels.md)) |
| 7 | List styles (type 2023). A list is a list style on a range of paragraphs; the marker (a dash, a number) is not in the text. | *Likely* ([0002](../experiments/0002-one-word.md), [0004](../experiments/0004-larger-word.md), [0014](../experiments/0014-lists.md)) |
| 8 | Character styles (type 2021). Absent when no text has one. | *Likely* ([0004](../experiments/0004-larger-word.md)) |
| 9 | Attachments: each entry sits at a U+FFFC character in the text. In Pages it points at a type-2003 record, which points at the attached object (for a table, its drawable of type 6000). A page number field points directly at a type-2043 record, whose field 4 is the number format, such as `decimal`. A Numbers sheet's text holds one. | *Likely* ([0020](../experiments/0020-a-table.md), [0032](../experiments/0032-reading-all-text.md), [0048](../experiments/0048-page-number.md)) |
| 11 | Smart fields over ranges: placeholder text (type 2031), a date (type 2034, with its format and locale in fields 2 and 3), a merge field (type 2036, such as the author's name) and a link (type 2032, with the address in field 2 and a UUID in field 1.1; web, email and phone links differ only in the address scheme: `http:`, `mailto:` or a percent-encoded `tel:`, *confirmed* by [0189](../experiments/0189-web-link.md) and [0190](../experiments/0190-email-and-phone-links.md)) and a link to a bookmark (type 2039, whose field 2 is `#` and the bookmark's UUID, [0192](../experiments/0192-link-to-bookmark.md)). Linked text also gets the character style `character-style-hyperlink`. An entry with no field 2 ends a range, and the text inside is what the field shows now. | *Likely* ([0158](../experiments/0158-essay-template.md)) |
| 12 | Objects of type 2024 | *Unknown* |
| 16 | Footnotes: an entry at each U+000E footnote mark points at a type-2008 record, whose field 2 names the footnote's text (a type-2001 record with field 1 = 2) | *Likely* ([0041](../experiments/0041-footnote.md)) |
| 15 | Bookmarks (type 2035, identified by the UUID in field 1.1) | *Likely* ([0191](../experiments/0191-bookmark.md)) |
| 17 | Sections (type 10011 in `Document.iwa`), which hold among other things the headers and footers | *Likely* ([0016](../experiments/0016-header-and-footer.md)) |
| 19 | Languages: field 2 is a language code as text, such as `nb`. Only text typed or rewritten in Pages has one; text set through AppleScript has no field 19, or an entry without field 2. | *Confirmed* ([0006](../experiments/0006-typing-in-pages.md), [0009](../experiments/0009-autocorrection.md)) |
| 20 | Autocorrections: each range Pages autocorrected has a UUID as text in field 2, and an entry without one closes it. Absent when nothing was corrected. | *Confirmed* ([0006](../experiments/0006-typing-in-pages.md), [0009](../experiments/0009-autocorrection.md)) |

Field 2 of the record names the type-401 object that holds the styles, which is probably the stylesheet. Fields 14, 24 and 28 hold entries of zeros in every document so far. *Unknown*

## Styles

Changing the size of part of the text, or making it bold or italic, creates a new, unnamed character style (type 2021) in `DocumentStylesheet.iwa`. It inherits (field 1.3) from a character style whose identifier is `character-style-null`. *Confirmed* ([0004](../experiments/0004-larger-word.md), [0007](../experiments/0007-bold-and-italic.md), [0008](../experiments/0008-runs-and-shared-styles.md))

Formatting a whole paragraph instead creates an unnamed paragraph style (type 2022) that inherits from the paragraph's style and carries the change. *Likely* ([0008](../experiments/0008-runs-and-shared-styles.md), [0149](../experiments/0149-family-emoji.md))

Several properties set on one range go into one style ([0152](../experiments/0152-size-and-colour.md)). Setting a property to the value it already has makes no style ([0153](../experiments/0153-same-size-again.md)), and styles nothing uses are dropped on save ([0154](../experiments/0154-replaced-text.md)). A template's styles are copied into the document with their own values, such as white text in the black template ([0157](../experiments/0157-black-template.md)). *Likely*

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

Field 11.5 is *confirmed* ([0010](../experiments/0010-alignment.md), [0053](../experiments/0053-font.md)), and so are 11.7 ([0013](../experiments/0013-text-colour.md)), 11.11 and 11.12 ([0012](../experiments/0012-underline-and-strikethrough.md)); the rest as above.

A paragraph style also has a field 12 for paragraph properties. *Likely* ([0008](../experiments/0008-runs-and-shared-styles.md), [0010](../experiments/0010-alignment.md))

| Field 12.n | Property | Encoding |
| --- | --- | --- |
| 1 | Alignment | varint: 0 left, 1 right, 2 centred, 3 justified, 4 probably natural (the Body style's value, shown as left) |

Values 0 to 3 are *confirmed* ([0010](../experiments/0010-alignment.md), [0011](../experiments/0011-left-alignment.md)); 4 as natural alignment is *likely*.

Named styles such as Body set every property; unnamed ones set only what differs from their parent (field 1.3). *Likely* ([0010](../experiments/0010-alignment.md))

Field 10 has equalled the number of properties set in every unnamed style so far, and is 57 in the named paragraph styles, which set 59. It doesn't count edits. *Unknown* ([0010](../experiments/0010-alignment.md), [0011](../experiments/0011-left-alignment.md), [0152](../experiments/0152-size-and-colour.md))

A list style (type 2023) stores most properties as nine repeated values, one per list level. Field 11 is the kind of marker (0 none, 2 a text character, 3 a number), field 16 the marker text for kind 2, and field 13 an indent in points that grows by a fixed step per level. *Likely* ([0014](../experiments/0014-lists.md))

To find a character's formatting, take each property from the first style that sets it. Look first in its character style (from the field-8 runs), then that style's parent (field 1.3), and so on. Then look in its paragraph style (from the field-5 runs) and that style's parents. A property set to 0 counts as set. A font name in 11.5 may already include a weight, such as `HelveticaNeue-Bold`. *Likely* for bold, italic, size and font: the rule predicted Pages' own reading of all 19 words of 8 documents ([0033](../experiments/0033-style-resolution.md), [0034](../experiments/0034-mixed-paragraph-styles.md)). It also holds for text colour ([0042](../experiments/0042-colour-resolution.md)).

Styles get their own layer once more of them are understood.
