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

A paragraph break is a character in the text. Pages has stored both U+000D (carriage return) and U+000A (line feed) as given, and each starts a new paragraph. The last paragraph has no break after it. *Likely* ([0005](../experiments/0005-paragraphs.md)). Which character Pages writes when a user presses Return is *unknown*.

## Positions in the text

Positions in the text count UTF-16 code units, not UTF-8 bytes or code points. So a character outside the Basic Multilingual Plane counts as 2, and a reader has to convert positions before using them on the UTF-8 text. *Confirmed* ([0003](../experiments/0003-non-ascii-word.md), [0004](../experiments/0004-larger-word.md))

## Runs

Several fields of a type-2001 record are run tables: lists of entries that apply something to ranges of the text. Each entry is a message whose field 1 is the position where a run starts. Where the run applies an object, its field 2 is a message whose field 1 is that object's ID. A run lasts until the next entry, or to the end of the text. *Likely* ([0004](../experiments/0004-larger-word.md), [0005](../experiments/0005-paragraphs.md)). What an entry with no field 2 means depends on the table: in field 8 it ends a character style, in field 5 it doesn't.

| Field | Runs of | Confidence |
| --- | --- | --- |
| 5 | Paragraph styles (type 2022). One entry per paragraph, at its first character; the break before it belongs to the previous paragraph. An entry with no field 2 seems to keep the previous paragraph's style. | *Likely* ([0002](../experiments/0002-one-word.md), [0004](../experiments/0004-larger-word.md), [0005](../experiments/0005-paragraphs.md)); the meaning of an entry with no field 2 is *unknown* |
| 7 | List styles (type 2023) | *Likely* ([0002](../experiments/0002-one-word.md), [0004](../experiments/0004-larger-word.md)) |
| 8 | Character styles (type 2021). Absent when no text has one. | *Likely* ([0004](../experiments/0004-larger-word.md)) |
| 12 | Objects of type 2024 | *Unknown* |
| 17 | Objects of type 10011 in `Document.iwa` | *Unknown* |

Field 2 of the record names the type-401 object that holds the styles, which is probably the stylesheet. Fields 6, 14, 24 and 28 hold entries of zeros in every document so far. *Unknown*

## Styles

Changing the size of part of the text creates a new, unnamed character style (type 2021) in `DocumentStylesheet.iwa`. It inherits from a character style whose identifier is `character-style-null`, and stores the size as a float in field 11.3. *Likely* ([0004](../experiments/0004-larger-word.md)). Styles get their own layer once more of them are understood.
