# 0269: A rejected insertion, and where tracking is turned on

**Status:** run

[0193](0193-tracked-insertion.md) found that a tracked insertion is a type-2060 record pointing at a type-2062 session record. This experiment rejects an insertion through the Edit menu, then looks for what still records that tracking is on.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0236/plain.pages`, the same text untracked |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. Choose Edit → Track Changes, click after `One` and type ` two`.
3. Choose Edit → Reject Change (*Rediger → Forkast endring*). The text is `One` again.
4. Save it as `samples/0269/rejected.pages`.

## Observation

The body text is `One`, with no run table 21 and no type-2060 record. One type-2062 record remains, naming the author and holding a time.

The document root (type 10000) differs from the untracked baseline in three fields:

| Field | Untracked | Tracking on |
| --- | --- | --- |
| 16 | absent | `{ 1: 1732722 }`, the type-2062 record |
| 17 | absent | `{ 1: 1732722 }` |
| 40 | 0 | 1 |

The type-10012 settings ([0236](0236-hyphenation.md)–[0240](0240-no-document-body.md)) are unchanged.

## Conclusion

Root field 40 is 1 while change tracking is turned on. The type-2062 record is the current editing session: the root names it in fields 16 and 17 (probably the session and the latest one), and new changes point at it. Rejecting an insertion removes the text and its change record, just as accepting a deletion does ([0268](0268-accepted-deletion.md)). Only the session remains. A reader can tell that a document is being tracked from field 40, even when it has no pending changes.

## Confidence

*Likely*:

- Root field 40 turns change tracking on.
- Root fields 16 and 17 name the current editing session (type 2062).
