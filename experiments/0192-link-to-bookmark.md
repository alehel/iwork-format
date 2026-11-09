# 0192: A link to a bookmark

**Status:** run

[0191](0191-bookmark.md) found that a bookmark is a type-2035 record with a UUID. This experiment links one word to a bookmark on another, to see how the link names its target.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0189](0189-web-link.md) and [0191](0191-bookmark.md) |

## Recipe

1. Make a document with the body text `one two`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "one two"'
   ```
2. Double-click `two`, then choose Insert → Bookmark.
3. Double-click `one`, then choose Format → Add Link → Bookmark (*Bokmerke*). Pages links to the only bookmark.
4. Save it as `samples/0192/bookmark-link.pages`.

## Observation

`Document.iwa` gains a type-2035 bookmark and a type-2039 record:

```
type 2035:  1: { 1: "B3EA9C7C-BDCF-41C7-9E6B-E441FE2FEF95" }, 3: 1, 4: 0
type 2039:  1: { 1: { 1: "2DE95AE6-29F8-4AD4-B266-29B4A1CF7737" } }
            2: "#B3EA9C7C-BDCF-41C7-9E6B-E441FE2FEF95"
```

The body's run tables:

| Field | Entries |
| --- | --- |
| 8, character styles | 0 → `Lenke`; 3 → none |
| 11, smart fields | 0 → the type-2039 link; 3 → none |
| 15, bookmarks | 0 → none; 4 → the type-2035 bookmark |

## Conclusion

A link to a bookmark is a type-2039 smart field. Its field 2 is `#` followed by the UUID of the bookmark (field 1.1 of the type-2035 record), like a fragment in a web address. Its UUID sits one message deeper than a type-2032 link's (1.1.1 rather than 1.1), so type 2039 probably extends the type-2032 record. A reader can follow the link by finding the bookmark with that UUID, then the bookmark's run in field 15.

Both run tables end the link at position 3, and the bookmark covers `two` from position 4.

## Confidence

*Likely*: a link to a bookmark is type 2039, naming the bookmark by `#` and its UUID in field 2.
