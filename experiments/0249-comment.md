# 0249: A comment

**Status:** run

[0200](0200-highlight.md) found that a highlight is a type-2013 record in run table 23, pointing at a type-3056 record with empty text. It predicted that a comment is the same with text. An empty comment is dropped on save, and the comment editor only opens with Pages in front. So this experiment ran with full control of the screen.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0200](0200-highlight.md), `highlight.pages` |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. With Pages in front, double-click `One` and choose Insert → Comment (*Sett inn → Kommentar*).
3. Type `note` in the comment and click Done (*Ferdig*). Pages capitalises it to `Note`.
4. Save it as `samples/0249/comment.pages`.

## Observation

`Document.iwa` has the same record types, in the same numbers, as the highlight of 0200. Run table 23 has one entry at 0, pointing at a type-2013 record. That record points at a type-3056 record:

```
1: "Note"
2: { 1: 815947123.80 }   ← seconds since 2001: 2026-11-09
3: { 1: 1732718 }        ← the author, type 212
5: { 1: …, 2: … }        ← a 128-bit ID
```

## Conclusion

A comment and a highlight are the same thing: a type-2013 annotation in run table 23, whose type-3056 record holds the comment's text in field 1. A highlight is a comment with empty text. A reader can list comments by walking table 23 and reading 3056.1, with the author and time alongside.

## Confidence

*Confirmed*, with 0200: comments and highlights are type-2013 records in run table 23, with their text, time and author in a type-3056 record.

The sample holds the author's name from the macOS contact card and shouldn't be shared.
