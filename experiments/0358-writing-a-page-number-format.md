# 0358: Writing a page number's format

**Status:** run

A page number field is an attachment (U+FFFC) pointing at a type-2043 record, whose field 4 is the number format, such as `decimal`, and field 1.2 chooses page number or page count ([0048](0048-page-number.md), [0201](0201-page-count.md)). Unlike a date field ([0357](0357-writing-a-date-field.md)), it has no text of its own in the body. This experiment writes other formats into field 4 and reads the exported page's text.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0048/page-number.pages`: the body `Page ` and a page number field, record 1732717 with field 4 = `decimal` |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0358
cp samples/0048/page-number.pages samples/0358/original.pages
for fmt in upper-roman lower-roman upper-alpha lower-alpha upper-latin lower-latin upper-alphabetic lower-alphabetic upper-letter; do
  python3 -I recipes/0302-set-path.py samples/0358/original.pages samples/0358/$fmt.pages 1732717 4 string $fmt
done
```

Pages opened each file on its own and exported it as PDF; PDFKit extracted the page's text.

## Observation

| Field 4 | Page text |
| --- | --- |
| `decimal` (original) | `Page 1` |
| `upper-roman` | `Page I` |
| `lower-roman` | `Page i` |
| `upper-alpha`, `lower-alpha`, `upper-latin`, `lower-latin`, `upper-alphabetic`, `lower-alphabetic`, `upper-letter` | `Page 1` |

## Conclusion

A page number is made when Pages lays out the page, in the format named by field 4: `decimal`, `upper-roman` and `lower-roman` work, and an unknown name falls back to decimal. Pages also offers letters, but their name wasn't among those tried.

## Confidence

*Confirmed*: page-number format names `decimal`, `upper-roman` and `lower-roman`, by writing them.

*Unknown*: the names of the letter formats.
