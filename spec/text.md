# 2. Text

Where a Pages document keeps its body text, and how the text is encoded. Every finding links to the experiments that support it, with a confidence level as defined in [CONTRIBUTING.md](../CONTRIBUTING.md#confidence). Records, object IDs and types are as described in [1. Container](container.md).

Observed with Pages 15.4 on macOS 26.5.2.

## The body text

The body text is in `Index/Document.iwa`, in field 3 of a record of type 2001. *Confirmed* ([0002](../experiments/0002-one-word.md), [0003](../experiments/0003-non-ascii-word.md))

- It is UTF-8, including characters outside the Basic Multilingual Plane, which take four bytes.
- It has no terminator or extra length prefix: the field's own length is the text's length in bytes.
- An empty body has no field 3 at all.

`Document.iwa` holds more than one type-2001 record: 19 in a new document. The body's record has field 1 set to 0, and none of the others has had a field 3 so far. *Likely* ([0003](../experiments/0003-non-ascii-word.md)). The other 18 use the paragraph style named for headers and footers, so they are probably the (empty) header and footer text. *Likely* ([0004](../experiments/0004-larger-word.md))

## Paragraphs

A paragraph break is a character in the text. Pressing Return in Pages writes U+000A (line feed). A U+000D (carriage return) set through AppleScript is kept as given and also starts a paragraph. The last paragraph has no break after it. *Confirmed* for U+000A ([0005](../experiments/0005-paragraphs.md), [0006](../experiments/0006-typing-in-pages.md)); *likely* for U+000D ([0005](../experiments/0005-paragraphs.md)).

Pressing Shift-Return writes U+2028 (line separator), a line break that doesn't start a paragraph. *Likely* ([0006](../experiments/0006-typing-in-pages.md))

## Positions in the text

Positions in the text count UTF-16 code units, not UTF-8 bytes or code points. So a character outside the Basic Multilingual Plane counts as 2, and a reader has to convert positions before using them on the UTF-8 text. *Confirmed* ([0003](../experiments/0003-non-ascii-word.md), [0004](../experiments/0004-larger-word.md))

## Runs

Several fields of a type-2001 record are run tables: lists of entries that apply something to ranges of the text. Each entry is a message whose field 1 is the position where a run starts. Where the run applies an object, its field 2 is a message whose field 1 is that object's ID. A run lasts until the next entry, or to the end of the text. *Confirmed* ([0004](../experiments/0004-larger-word.md), [0005](../experiments/0005-paragraphs.md), [0008](../experiments/0008-runs-and-shared-styles.md)). Ranges with the same formatting point at the same object. *Likely* ([0008](../experiments/0008-runs-and-shared-styles.md)) What an entry with no field 2 means depends on the table: in field 8 it ends a character style, in field 5 it doesn't.

| Field | Runs of | Confidence |
| --- | --- | --- |
| 5 | Paragraph styles (type 2022). One entry per paragraph, at its first character; the break before it belongs to the previous paragraph. An entry names a style where it changes; one with no field 2 seems to keep the previous paragraph's style. | *Likely* ([0002](../experiments/0002-one-word.md), [0004](../experiments/0004-larger-word.md), [0005](../experiments/0005-paragraphs.md), [0006](../experiments/0006-typing-in-pages.md)); the meaning of an entry with no field 2 is *unknown* |
| 7 | List styles (type 2023) | *Likely* ([0002](../experiments/0002-one-word.md), [0004](../experiments/0004-larger-word.md)) |
| 8 | Character styles (type 2021). Absent when no text has one. | *Likely* ([0004](../experiments/0004-larger-word.md)) |
| 12 | Objects of type 2024 | *Unknown* |
| 17 | Objects of type 10011 in `Document.iwa` | *Unknown* |
| 19 | Languages: field 2 is a language code as text, such as `nb`. Only text typed or rewritten in Pages has one; text set through AppleScript has no field 19, or an entry without field 2. | *Confirmed* ([0006](../experiments/0006-typing-in-pages.md), [0009](../experiments/0009-autocorrection.md)) |
| 20 | Autocorrections: each range Pages autocorrected has a UUID as text in field 2, and an entry without one closes it. Absent when nothing was corrected. | *Confirmed* ([0006](../experiments/0006-typing-in-pages.md), [0009](../experiments/0009-autocorrection.md)) |

Field 2 of the record names the type-401 object that holds the styles, which is probably the stylesheet. Fields 6, 14, 24 and 28 hold entries of zeros in every document so far. *Unknown*

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

Styles get their own layer once more of them are understood.
