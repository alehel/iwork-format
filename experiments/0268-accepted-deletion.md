# 0268: An accepted deletion

**Status:** run

[0194](0194-tracked-deletion.md) found that a tracked deletion keeps the deleted text in the body, marked by a type-2060 record in run table 22. This experiment accepts such a deletion through the Edit menu, to see what accepting leaves behind.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0194](0194-tracked-deletion.md); `samples/0236/plain.pages` |

## Recipe

1. Make a document with the body text `One two`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One two"'
   ```
2. Choose Edit → Track Changes, double-click `two` and press Delete, as in 0194.
3. Click in the struck-through word and choose Edit → Accept Change (*Rediger → Godta endring*). The bar reads "0 comments and changes".
4. Save it as `samples/0268/accepted.pages`.

## Observation

The body text is `One`: the deleted ` two` is gone, along with run table 22 and the type-2060 change record. `Document.iwa` has the same record types as an untracked document, plus one type-2062 record. The type-212 author record stays in `AnnotationAuthorStorage`.

## Conclusion

Accepting a deletion removes the text and every trace of the change. What remains is the editing session (type 2062) and its author, because tracking is still on ([0269](0269-rejected-insertion.md)). A document whose changes have all been accepted reads like an ordinary one.

## Confidence

*Likely*: accepting a change leaves no change record, and the text is as edited.
