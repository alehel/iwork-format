# 0202: A table of contents

**Status:** run

Pages can insert a table of contents built from heading styles. This experiment inserts one after a single heading, to see how its entries and their page numbers are stored.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0179/plain.pages` |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. Click in `One` and choose the paragraph style Heading (*Overskrift*) in the Format sidebar.
3. Click after `One`, then choose Insert → Table of Contents → Document (*Sett inn → Innholdsfortegnelse → Dokument*). Pages shows `One` with the page number 1 below the heading.
4. Save it as `samples/0202/toc.pages`.

## Observation

The body text is `One`, U+FFFC, then U+0005. Its field 9 has an entry at 3, the U+FFFC, pointing at a chain of new records:

| Record | Holds |
| --- | --- |
| Type 2241, the attachment | 1.1: the type-2240 record, plus zeroed fields |
| Type 2240, the table of contents | 1: a drawable-like block whose 1.2 and 1.4 name the text below; 2: the settings (type 2051); 3: one entry (type 2052) |
| Type 2001, its text | Field 1 is 7. The text is `One`, a tab, U+FFFC. Field 9 has an entry at 4 pointing at a type-2010 record with field 2 `1` |
| Type 2051, its settings | `Standard TOC`, naming the Heading style (`text-11-paragraphstyle-Heading 1`) and a type-2026 record named `Innh.f.overskrift 1`, the style for level-1 entries |
| Type 2052, the entry | 4: `One`; 5: the Heading paragraph style; 6: the list style None; 9: `decimal` |

`iwork-probe text` already prints the table's text, as a record with field 1 = 7.

## Conclusion

A table of contents is an attachment in the body, at a U+FFFC, like a table. It has its own text record (field 1 = 7) that holds the finished entries: each heading's text, a tab, and its page number as an attached type-2010 record whose field 2 holds the number as text (`1`). The type-2052 records keep the source of each entry and the page number format, and type 2051 says which styles are included. A reader can show the table as stored, without laying out the document. Pages updates the stored page numbers itself.

Pages also added a page break (U+0005) after the table.

## Confidence

*Likely*: a table of contents is a type-2241 attachment holding type 2240, with a text record of kind 7 and cached page numbers in type-2010 records.

*Unknown*: why a page break follows the table.
