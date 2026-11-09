# 0194: A tracked deletion

**Status:** run

[0193](0193-tracked-insertion.md) found that a tracked insertion is a type-2060 record in run table 21. This experiment deletes a word with tracking on.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0193](0193-tracked-insertion.md) |

## Recipe

1. Make a document with the body text `One two`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One two"'
   ```
2. Choose Edit → Track Changes.
3. Double-click `two` and press Delete. Pages strikes the word through rather than removing it.
4. Save it as `samples/0194/deleted.pages`.

## Observation

The body text (field 3) is still `One two`. It gains run table 22: no entry at 0, then at 3 a type-2060 record with field 1 set to 2. Its fields 2–4 are as in 0193: a type-2062 record naming the author, a time and a UUID. There is no run table 21.

Pages deleted the space before `two` along with it, so the deletion covers ` two` from position 3.

## Conclusion

A tracked deletion is a type-2060 record with kind 2, applied through run table 22. Insertions use kind 1 and table 21. The deleted text stays in the body until the change is accepted. A reader that shows the document as edited must leave out the ranges in table 22. A reader that ignores tracking shows the deleted text as if it were still there.

## Confidence

*Confirmed*, with 0193: tracked changes are type-2060 records whose field 1 gives the kind of change.

*Likely*: kind 2 and run table 22 are deletions, and deleted text stays in the body.
