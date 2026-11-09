# 0011: Back to left

**Status:** run

This experiment settles two questions left open by [0010](0010-alignment.md). The Body style stores alignment 4 but Pages shows it as left, so what does Pages write when a paragraph is explicitly set to left? And is field 10 of a style a count of its properties, or of the edits that made it? Centring a paragraph and then setting it back to left answers both: it takes two edits and leaves one property set.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0010](0010-alignment.md), `center.pages` |

## Recipe

As in 0010: AppleScript makes a new document and sets its body text to `one two three`. In the Pages window, click in the paragraph, click Centred (*sentrert*), then click Left (*venstre*). AppleScript saves the document as `center-then-left.pages`.

The sidebar still showed the paragraph style as `Brødtekst*` after the paragraph was back to left.

## Observation

The stylesheet has one new record, not two. It is an unnamed type-2022 paragraph style that inherits from Body (1731511), and the paragraph-style runs point the paragraph at it:

```
1732700, type 2022
  1: { 3: { 1: 1731511 }, 4: 1, 5: { 1: 1732613 } }
  10: varint 1
  11: bytes (0)
  12: { 1: varint 0 }
```

## Conclusion

A paragraph set explicitly to left gets alignment 0. That differs from Body's 4, which Pages also shows as left. So 4 is probably a "natural" alignment, which follows the direction of the text and comes out as left for Norwegian. A reader should treat 0 as left and 4 as left for left-to-right text.

Field 10 is 1 after two edits, so it doesn't count edits. In every unnamed style so far it has equalled the number of properties the style sets (1, 1, 2, 1). In the full named styles it is 57 against 59 fields, so it isn't exactly a property count there. It could count something close to it, such as properties excluding some kinds. It is still unknown, but a reader doesn't need it to apply a style.

Undoing a change in the sidebar doesn't remove the unnamed style. Pages updated the existing one rather than adding a second.

## Confidence

*Confirmed*: field 12.1 is the alignment, with 1 right, 2 centred and 3 justified (0010), and 0 left (this experiment).

*Likely*: 4 is a natural alignment, shown as left in left-to-right text. Follow-up: a paragraph in a right-to-left language.

*Unknown*: field 10.
