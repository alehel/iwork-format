# 0359: Writing a page break and a page count

**Status:** run

A page break is the character U+0005 in the text, which also starts a new paragraph ([0018](0018-page-break-and-left-page.md)), and a page number field's record (type 2043) has field 1.2 = 0 for the page number and 1 for the page count ([0201](0201-page-count.md)). This experiment writes a page break after a page number field, then switches the field to the page count, and reads each exported page's text.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0048/page-number.pages`: the body `Page ` and a page number field (U+FFFC), record 1732717 with 1.2 = 0 |
| Writers | The writer of [0287](0287-rewriting-a-document.md) for the text, [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) for the field |

## Recipe

```bash
mkdir -p samples/0359
python3 -I recipes/0287-iwa-writer.py samples/0048/page-number.pages samples/0359/two-pages.pages \
  --text 1732539 "$(printf 'Page \xef\xbf\xbc\x05second page')"
python3 -I recipes/0302-set-path.py samples/0359/two-pages.pages samples/0359/count.pages 1732717 1.2 varint 1
```

Only the text changes in the first file: no paragraph run is added for the new paragraph, and the attachment run stays at position 5, where U+FFFC still is. Pages opened each file on its own and exported it as PDF; PDFKit extracted each page's text.

## Observation

| File | Pages | Page 1 | Page 2 |
| --- | --- | --- | --- |
| `two-pages.pages` | 2 | `Page  1` | `second page` |
| `count.pages` | 2 | `Page  2` | `second page` |

## Conclusion

U+0005 in the text breaks the page, and the text after it starts the next page. The page number field's 1.2 = 1 makes it show the page count, 2, while 0 shows the page's own number, 1; both are worked out from the layout. A paragraph that a writer adds without a paragraph run still lays out, in the default style ([0289](0289-writing-two-paragraphs.md)).

## Confidence

*Confirmed*: U+0005 as a page break, and field 1.2 of a page number field, by writing them.
