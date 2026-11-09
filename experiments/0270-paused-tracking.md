# 0270: Paused change tracking

**Status:** run

[0269](0269-rejected-insertion.md) found that root field 40 is 1 while change tracking is on. Tracking can also be paused with a switch in the review bar, so that edits go untracked without turning tracking off. This experiment pauses it, to see whether the pause is part of the document.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0270/tracking.pages`: tracking on, not paused, no edits |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. Choose Edit → Track Changes, then click the review bar's tracking switch (*Pause / På*) to pause it.
3. Save it as `samples/0270/paused.pages`.

For the baseline, repeat step 1, turn tracking on, and save without pausing.

## Observation

`Document.iwa` doesn't differ between the two, apart from the creation time. Root field 40 is 1 in both. Neither has a type-2062 session record, because nothing was edited.

`ViewState.iwa` differs in the type-10133 view state ([0241](0241-zoom.md)):

| Field | Tracking | Paused |
| --- | --- | --- |
| 28 | 0 | 1 |
| 7.2 | 799.2 | 776.8 |

## Conclusion

Pausing tracking is a view setting, not a document setting. View state field 28 is 1 while tracking is paused, and the document itself still says tracking is on (root field 40). The visible area is 22.4 points shorter, probably because the review bar grows to show that tracking is paused. A reader can ignore the pause. An editor that honours it should read field 28.

## Confidence

*Likely*: view state field 28 is 1 while tracking is paused.

*Unknown*: why the visible area changes height.
