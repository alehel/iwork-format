# 0489: The text wrap menu, and Inline with Text

**Status:** run

Writing drawable field 1.3 showed it to be the text wrap ([0488](0488-writing-text-wrap.md)), but the values could only be matched to what was drawn, not to the names Pages gives them, and Inline with Text couldn't be chosen in the background ([0487](0487-move-with-text.md)). This experiment chooses each entry of the Arrange sidebar's wrap menu, the Text Fit buttons and the alpha, saving after each, and then sets the picture to Move with Text and Inline with Text.

## Setup

| | |
| --- | --- |
| Pages | 16.0 (7052.0.68), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-28 |
| Input | `0487/stay.pages`: a two-line paragraph and the red picture of [0023](0023-an-image.md) at 80 × 40 points on page 1, Stay on Page, with Pages' default wrap `{ 1: 4, 2: 2, 3: 1, 4: 12.0, 5: 0.5, 6: 0 }` |
| Recipe | In the Pages window, by hand (computer use with the window in front), each step saved with AppleScript's `save front document in` |

## Recipe

1. Copy `0487/stay.pages` to `samples/0489/work.pages`, open it with `open -a "Pages Creator Studio"`, select the picture and open the Arrange (*Ordne*) tab. The wrap menu (*Tekstbryting*) shows *Automatisk* and offers *Automatisk*, *Rundt*, *Over og under* and *Ingen* (Automatic, Around, Above and Below, None). It has no choice of sides.
2. Choose *Rundt* (Around); save as `around.pages`.
3. Choose *Ingen* (None); save as `none.pages`. Spacing and alpha grey out.
4. Choose *Over og under* (Above and Below); save as `above-and-below.pages`.
5. Choose *Rundt* again and the first Text Fit (*Tekstflyt*) button; the alpha field greys out. Save as `around-box-fit.pages`.
6. Choose the second Text Fit button and type 70 in the alpha (*Alfa*) field; save as `alpha-70.pages`.
7. Click *Flytt med tekst* (Move with Text). The wrap menu now has a fifth entry, *Bundet til teksten* (Inline with Text), between *Over og under* and *Ingen*. Save as `move-around.pages`.
8. Choose *Bundet til teksten*. The picture moved onto the paragraph's second line, after `once.`, and the line grew to its height; position, Text Fit, spacing and alpha grey out. Save as `inline.pages`. Close `work.pages` unsaved and delete it.

## Observation

Picture 1732688's field 1.3 after each step:

| File | Sidebar | 1.3.1 | 1.3.2 | 1.3.3 | 1.3.4 | 1.3.5 |
| --- | --- | --- | --- | --- | --- | --- |
| `0487/stay.pages` | Automatic | 4 | 2 | 1 | 12.0 | 0.5 |
| `around.pages` | Around | 1 | 2 | 1 | 12.0 | 0.5 |
| `none.pages` | None | 5 | 2 | 1 | 12.0 | 0.5 |
| `above-and-below.pages` | Above and Below | 2 | 2 | 1 | 12.0 | 0.5 |
| `around-box-fit.pages` | Around, first Text Fit button | 1 | 2 | 0 | 12.0 | 0.5 |
| `alpha-70.pages` | Around, second button, alpha 70 % | 1 | 2 | 1 | 12.0 | 0.7 |
| `move-around.pages` | Move with Text, Around | 1 | 2 | 1 | 12.0 | 0.7 |
| `inline.pages` | Inline with Text | 0 | 2 | 1 | 12.0 | 0.7 |

Move with Text made the attachment of [0487](0487-move-with-text.md): a U+FFFC at the paragraph's end, a type-2003 record (here 1732925) with the offset 230.107 and 316.907, the body's text in the picture's 1.2, and no entry in type 10010. Going on to Inline with Text changed only two things: 1.3.1 became 0, and the picture left type 10015, whose field 1 now lists only the body's text. The 2003 record, the picture's 1.1.1 = (286.8, 397.6) and the rest of 1.3 stayed as they were.

## Conclusion

The wrap menu's entries are 1.3.1 = 4 Automatic, 1 Around, 2 Above and Below and 5 None, and for an object that moves with the text, 0 Inline with Text. The menu has no choice of sides, so Pages always writes 1.3.2 = 2 (both); the other sides of [0488](0488-writing-text-wrap.md) can only be written. Wrap 3, which [0488](0488-writing-text-wrap.md) drew on one side, isn't offered.

The first Text Fit button, which greys out the alpha, writes 1.3.3 = 0, and the second, Pages' default, 1: box and outline fit. The alpha field is 1.3.5, as a fraction.

Inline with Text is not a third kind of anchor: it is a Move with Text attachment whose wrap is 0. Pages takes such an object out of the page's stacking list (type 10015), since it is drawn in the line, and leaves its offset and position in the file unused. [0490](0490-writing-inline-with-text.md) tests this by writing.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `around.pages` | `0487/stay.pages` | `3005#1732688 1.3.1: 4 → 1`, `3005#1732688 1.3.2 = 2` | *Confirmed*: Around is 1, and Pages writes both sides; [0488](0488-writing-text-wrap.md) drew 1 around |
| `none.pages` | `around.pages` | `3005#1732688 1.3.1: 1 → 5` | *Confirmed*: None is 5; [0488](0488-writing-text-wrap.md) drew 5 without wrap |
| `above-and-below.pages` | `none.pages` | `3005#1732688 1.3.1: 5 → 2` | *Confirmed*: Above and Below is 2, as [0488](0488-writing-text-wrap.md) drew it |
| `around-box-fit.pages` | `above-and-below.pages` | `3005#1732688 1.3.1: 2 → 1`, `3005#1732688 1.3.3: 1 → 0` | *Confirmed*: the first Text Fit button, the box, is 0 |
| `alpha-70.pages` | `around-box-fit.pages` | `3005#1732688 1.3.3: 0 → 1`, `3005#1732688 1.3.5: 0.5 → 0.7` | *Likely*: the alpha is 1.3.5, as a fraction |
| `move-around.pages` | `alpha-70.pages` | `3005#1732688 1.2.1: absent → 1732539`, `records 2003: 0 → 1`, `2003 1.1 = 1732688`, `10010#1732278 1: ×1 → ×0` | *Confirmed*: Move with Text makes the attachment of [0487](0487-move-with-text.md) |
| `inline.pages` | `move-around.pages` | `3005#1732688 1.3.1: 1 → 0`, `10015#1732364 1: ×2 → ×1`, `10015#1732364 1.1 ≠ 1732688`, `2003 1.1 = 1732688` | *Likely*: Inline with Text is wrap 0 on an attachment, outside 10015 |

## Confidence

*Confirmed*, by the sidebar here and by drawing in [0488](0488-writing-text-wrap.md): 1.3.1 = 1 Around, 2 Above and Below, 5 None, 4 Automatic (Pages' default), and 1.3.3 = 0 box fit, 1 outline fit.

*Likely*: 1.3.5 is the alpha threshold, and Inline with Text is 1.3.1 = 0 on an attached object, which [0490](0490-writing-inline-with-text.md) confirms by writing.
