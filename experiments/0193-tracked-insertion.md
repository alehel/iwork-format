# 0193: A tracked insertion

**Status:** run

With change tracking on, Pages keeps a record of each edit until it's accepted or rejected. This experiment types a word with tracking on, to see how an insertion and its author are stored.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | A new document with the body text `One` |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. Choose Edit → Track Changes (*Rediger → Spor endringer*).
3. Click after `One` and type ` two`.
4. Save it as `samples/0193/tracked.pages`.

A first attempt with the body text `one` was spoiled by Pages capitalising it while I typed, so the text starts with a capital.

## Observation

The body text (field 3) is `One two`. It gains two run tables:

- **Field 19, language:** `nb` from position 3, from typing.
- **Field 21:** no entry at 0, then at 3 a type-2060 record:

```
type 2060:  1: 1
            2: { 1: 1732723 }        ← type 2062
            3: { 1: 815942390.33 }   ← seconds since 2001-01-01: 2026-11-09 18:39:50 UTC
            4: "77F4A2EA-B91F-458A-9C39-04EDB6FF11E2"
type 2062:  1: 1
            2: { 1: 1732727 }        ← type 212, in AnnotationAuthorStorage
            3: { 1: 815942390.19 }
```

Record 1732727, of type 212, is in the `AnnotationAuthorStorage` part, next to its type-213 root. Its field 1 is the author's name, taken from the macOS user's contact card. Its field 2 holds the author's colour as RGBA floats (0.98, 0.94, 0.35, 1), the yellow Pages shows the change in.

## Conclusion

A tracked insertion is a type-2060 change record, applied to the inserted text through run table 21. The record's field 1 is the kind of change (1 here), field 3 its time and field 4 a UUID. Field 2 points at a type-2062 record, probably the editing session, which names the author. Authors are type-212 records in `AnnotationAuthorStorage`, each with a name and a colour.

The inserted text is already in the body, so a reader that ignores tracking shows the document as if the change were accepted.

## Confidence

*Likely*: tracked insertions are type-2060 records in run table 21, with kind 1, a time, and an author through type 2062.

*Unknown*: field 1 of type 2062.

A document with tracked changes stores its author's name. Samples made this way should not be shared.
