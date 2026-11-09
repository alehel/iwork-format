# 0191: A bookmark

**Status:** run

Pages can mark a range of text as a bookmark, for links within the document to point at. This experiment adds one through the menus.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0179/plain.pages`, the body text `one` |

## Recipe

1. Make a document with the body text `one`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "one"'
   ```
2. Double-click `one`, then choose Insert → Bookmark (*Sett inn → Bokmerke*).
3. Save it as `samples/0191/bookmark.pages`.

## Observation

`Document.iwa` gains one record, of type 2035:

```
1: { 1: "505D17DE-1387-40A4-B6C8-7E342FB98A7C" }
3: 1
4: 0
```

The body text (type 2001) gains a run table in field 15, with one entry at position 0 pointing at the new record. The other run tables are unchanged, and no character style is added.

## Conclusion

A bookmark is a type-2035 record, applied to the bookmarked text through its own run table, field 15. It doesn't use the smart-field table (field 11) that links use. Its field 1 holds a UUID, by which links point at it ([0192](0192-link-to-bookmark.md)). The record stores no name: the Bookmarks list in Pages probably shows the bookmarked text.

## Confidence

*Likely*: a bookmark is a type-2035 record in run table 15, identified by the UUID in field 1.1.

*Unknown*: fields 3 and 4.
