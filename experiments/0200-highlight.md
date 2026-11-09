# 0200: A highlight

**Status:** run

Pages can highlight text for review, like a comment with nothing written in it. This experiment highlights a word through the menus.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0179/plain.pages`; experiment [0193](0193-tracked-insertion.md) for authors |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. Double-click `One`, then choose Insert → Highlight (*Sett inn → Utheving*). Pages shades the word yellow and reports "1 highlight".
3. Save it as `samples/0200/highlight.pages`.

## Observation

`Document.iwa` gains a type-2013 record and a type-3056 record:

```
type 2013:  1: { 1: 1732718 }     ← type 3056
            2: "7C51C7EB-45F8-4731-ACED-7CBEA7942578"
type 3056:  1: ""                 ← empty bytes
            2: { 1: 815942849.47 }   ← seconds since 2001: 2026-11-09
            3: { 1: 1732715 }     ← type 212, the author, in AnnotationAuthorStorage
            5: { 1: 17601293454552542702, 2: 13517010897067626687 }
```

The body text gains run table 23, with one entry at 0 pointing at the type-2013 record.

## Conclusion

A highlight is a type-2013 record, applied through run table 23. Its field 1 points at a type-3056 record that holds what a comment holds: the text (field 1, empty here), the time (field 2), the author (field 3, the same type-212 records as tracked changes) and a 128-bit ID as two 64-bit halves (field 5). A comment on text is probably the same pair of records with text in 3056.1. An empty comment is dropped on save, so it couldn't be tested this way. Field 2 of type 2013 is a UUID.

## Confidence

*Likely*: a highlight is type 2013 in run table 23, pointing at a type-3056 record with a time and an author.

*Unknown*: whether a comment uses the same records. Follow-up: a comment with text, which needs the comment editor in the foreground.
