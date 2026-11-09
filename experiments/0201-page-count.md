# 0201: A page count field

**Status:** run

[0048](0048-page-number.md) found that a page number field is a U+FFFC attachment pointing at a type-2043 record. Pages can also insert the total number of pages. This experiment inserts that field, to see what tells the two apart.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0048](0048-page-number.md) |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. Click after `One`, then choose Insert → Page Count (*Sett inn → Sideantall*). Pages shows `One1`.
3. Save it as `samples/0201/page-count.pages`.

## Observation

The body text is `One` followed by U+FFFC. Field 9 has one entry at 3, pointing at a new type-2043 record:

| Field | Page number (0048) | Page count |
| --- | --- | --- |
| 1 | `{ 2: 0 }` | `{ 2: 1 }` |
| 2 | 0 | 0 |
| 4 | `decimal` | `decimal` |

## Conclusion

Page numbers and page counts are the same type-2043 field, attached at a U+FFFC. Field 1.2 says which: 0 for the page number, 1 for the page count. Field 4 is the number format for both. A reader must lay out the document to know the count. Without layout, it can at least show a placeholder.

## Confidence

*Likely*: field 1.2 of type 2043 is 0 for a page number and 1 for a page count.
