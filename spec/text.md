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

Several fields of a type-2001 record are run tables: lists of entries that apply something to ranges of the text. Each entry is a message whose field 1 is the position where a run starts. Where the run applies an object, its field 2 is a message whose field 1 is that object's ID. A run lasts until the next entry, or to the end of the text. *Likely* ([0004](../experiments/0004-larger-word.md), [0005](../experiments/0005-paragraphs.md)). What an entry with no field 2 means depends on the table: in field 8 it ends a character style, in field 5 it doesn't.

| Field | Runs of | Confidence |
| --- | --- | --- |
| 5 | Paragraph styles (type 2022). One entry per paragraph, at its first character; the break before it belongs to the previous paragraph. An entry names a style where it changes; one with no field 2 seems to keep the previous paragraph's style. | *Likely* ([0002](../experiments/0002-one-word.md), [0004](../experiments/0004-larger-word.md), [0005](../experiments/0005-paragraphs.md), [0006](../experiments/0006-typing-in-pages.md)); the meaning of an entry with no field 2 is *unknown* |
| 7 | List styles (type 2023) | *Likely* ([0002](../experiments/0002-one-word.md), [0004](../experiments/0004-larger-word.md)) |
| 8 | Character styles (type 2021). Absent when no text has one. | *Likely* ([0004](../experiments/0004-larger-word.md)) |
| 12 | Objects of type 2024 | *Unknown* |
| 17 | Objects of type 10011 in `Document.iwa` | *Unknown* |
| 19 | Languages: field 2 is a language code as text, such as `nb`. Present only in text typed in Pages. | *Likely* ([0006](../experiments/0006-typing-in-pages.md)) |
| 20 | A UUID as text in field 2, on ranges that Pages autocorrected. Present only in text typed in Pages. | *Unknown* ([0006](../experiments/0006-typing-in-pages.md)) |

Field 2 of the record names the type-401 object that holds the styles, which is probably the stylesheet. Fields 6, 14, 24 and 28 hold entries of zeros in every document so far. *Unknown*

## Styles

Changing the size of part of the text, or making it bold or italic, creates a new, unnamed character style (type 2021) in `DocumentStylesheet.iwa`. It inherits (field 1.3) from a character style whose identifier is `character-style-null`. *Likely* ([0004](../experiments/0004-larger-word.md), [0007](../experiments/0007-bold-and-italic.md))

Field 11 of a character style holds the properties it sets. *Likely* ([0004](../experiments/0004-larger-word.md), [0007](../experiments/0007-bold-and-italic.md))

| Field 11.n | Property | Encoding |
| --- | --- | --- |
| 1 | Bold | varint, 1 for bold |
| 2 | Italic | varint, 1 for italic |
| 3 | Size in points | float |

Field 10 was 1 for styles setting one property and 2 for the style setting two. *Unknown*

Styles get their own layer once more of them are understood.
