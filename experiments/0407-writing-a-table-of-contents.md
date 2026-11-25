# 0407: Writing a table of contents

**Status:** run

A table of contents is attached to the body as a type-2241 record, pointing at type 2240, which owns a text record of kind 7 with the finished entries; each ends in a type-2010 page number holding the number as text ([0202](0202-table-of-contents.md)). This experiment writes the finished text, the page number, the heading it lists, and a record the earlier experiment didn't describe, and reads the table from the exported PDF.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0202/toc.pages`: the heading `One` (body text 1732539) with a table of contents after it. Its text record 1732763 is `One`, a tab and U+FFFC, the attachment of page number 1732772, whose field 2 is `1`. A search for `One` found a third record, 1732770, of type 2052: field 4 `One`, 5 naming the heading's paragraph style (*Overskrift*), 6 another style, 9 `decimal`, and 1 = 0, 2 = 1, 3 = 0, 7 = 0, 8 = 0 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0407
R=recipes/0302-set-path.py
F=samples/0202/toc.pages
O=samples/0407
cp $F $O/original.pages
python3 -I $R $F $O/entry-text.pages 1732763 3 string "$(printf 'Two\t\xef\xbf\xbc')"
python3 -I $R $F $O/page-number.pages 1732772 2 string 9
python3 -I $R $F $O/heading-renamed.pages 1732539 3 string "$(printf 'Six\xef\xbf\xbc\x05')"
python3 -I $R $F $O/entry-model-text.pages 1732770 4 string "Written entry"
python3 -I $R $F $O/entry-model-roman.pages 1732770 9 string upper-roman
python3 -I $R $F $O/entry-model-field2.pages 1732770 2 varint 5
for f in original entry-text page-number heading-renamed entry-model-text entry-model-roman entry-model-field2; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
```

The body text is `One`, the table's U+FFFC and a page break (U+0005); `heading-renamed.pages` changes only its first word.

## Observation

| File | Written | Heading | Table of contents |
| --- | --- | --- | --- |
| `original.pages` | | One | One 1 |
| `entry-text.pages` | text record: `Two` | One | One 1 |
| `page-number.pages` | page number text: `9` | One | One 1 |
| `heading-renamed.pages` | body: `Six` | Six | One 1 |
| `entry-model-text.pages` | 2052 field 4: `Written entry` | One | Written entry 1 |
| `entry-model-roman.pages` | 2052 field 9: `upper-roman` | One | One I |
| `entry-model-field2.pages` | 2052 field 2: 5 | One | One 1 |

Each entry is a link to page 1 at (57, 786), the heading, in every file.

## Conclusion

Pages draws a table of contents from its type-2052 entry records, one per entry: field 4 is the entry's text, field 5 the paragraph style it was collected from, and field 9 the format of its page number, in the same names as page number fields ([0358](0358-writing-a-page-number-format.md)). It doesn't redraw the table from the headings when it opens a document: renaming the heading left the entry as `One` until the table is updated. Nor does it use the finished text record, whose words and page number it rebuilds from the entries: the page number is worked out when the page is laid out. So a reader should take a table of contents from its 2052 records, or from the finished text, which matches them in a document Pages saved.

Field 2 of the entry didn't change the drawing; it isn't the page number.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0202/toc.pages` | `same bytes` | *Control*: drawn `One 1` |
| `entry-text.pages` | `original.pages` | Only `2001#1732763 3: "One\t\ufffc" → "Two\t\ufffc"` | *Confirmed*: Pages ignores the finished text of a table of contents |
| `page-number.pages` | `original.pages` | Only `2010#1732772 2: "1" → "9"` | *Confirmed*: Pages ignores its cached page numbers |
| `heading-renamed.pages` | `original.pages` | Only `2001#1732539 3: "One\ufffc\u0005" → "Six\ufffc\u0005"` | *Likely*: the entry isn't made again from the heading when the document opens |
| `entry-model-text.pages` | `original.pages` | Only `2052#1732770 4: "One" → "Written entry"` | *Confirmed*: field 4 of type 2052 is the text drawn for an entry |
| `entry-model-roman.pages` | `original.pages` | Only `2052#1732770 9: "decimal" → "upper-roman"` | *Confirmed*: field 9 is the format of its page number |
| `entry-model-field2.pages` | `original.pages` | Only `2052#1732770 2: 1 → 5` | *Likely*: field 2 isn't the page number |

## Confidence

*Confirmed*: type 2052 as a table of contents entry, with field 4 its text and field 9 its page number format, by writing them; and that Pages ignores the finished text and cached page numbers when drawing. *Likely*: field 5 as the source paragraph style. What fields 2 and 6 hold is *unknown*.
