# 0033: How styles combine

**Status:** run

Experiments 0004–0012 found character styles, paragraph styles and their parents (field 1.3), but not how they combine into the formatting a reader should show. [0008](0008-runs-and-shared-styles.md) suggested an order without testing it. This experiment states a rule and checks its predictions against what Pages itself reports for each word, in eight earlier samples.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Documents | `samples/0004/large.pages`, `0006/heading-ui`, `0007/bold`, `0007/italic`, `0007/bold-italic`, `0008/middle`, `0008/two-words`, `0008/unbold-middle` |

## Recipe

**What Pages shows.** Each document was opened in Pages through AppleScript, and for each word of the body text, `font` and `size` were read. The font name carries the bold and italic, for example `HelveticaNeue-BoldItalic`. The documents were closed without saving.

**What the file predicts.** A throwaway script read the same documents with `iwork-probe` only, and applied this rule to each word:

1. Find the word's character style from the character-style runs (field 8 of the text record). An entry without a style means none.
2. Find its paragraph style from the paragraph-style runs (field 5). An entry without a style keeps the previous paragraph's style.
3. For each property (bold 11.1, italic 11.2, size 11.3, font 11.5), take the value from the first style that sets it. Look first in the character style, then its parent (field 1.3), then that style's parent, and so on. If none of those sets it, do the same with the paragraph style and its parents.
4. Name the font as Pages does: the font in 11.5, with `-Bold`, `-Italic` or `-BoldItalic` added unless the name already ends that way.

## Observation

| Document | Word | Pages reports | Predicted |
| --- | --- | --- | --- |
| 0004/large | hello | HelveticaNeue, 11 | same |
| | world | HelveticaNeue, 24 | same |
| 0006/heading-ui | One | HelveticaNeue, 11 | same |
| | two | HelveticaNeue-Bold, 18 | same |
| 0007/bold | world | HelveticaNeue-Bold, 11 | same |
| 0007/italic | world | HelveticaNeue-Italic, 11 | same |
| 0007/bold-italic | world | HelveticaNeue-BoldItalic, 11 | same |
| 0008/middle | one, two, three | regular, bold, regular, 11 | same |
| 0008/two-words | one, two, three | bold, regular, bold, 11 | same |
| 0008/unbold-middle | one, two, three | bold, regular, bold, 11 | same |

The words not shown (`hello` in 0007) were regular 11 in Pages and in the prediction. All 19 words in the 8 documents matched.

The first version of the script mispredicted `two` in 0006 as `HelveticaNeue-Bold-Bold`. The Heading style's font (11.5) is `HelveticaNeue-Bold`, with bold also set in 11.1, and the script's naming added `-Bold` a second time. Bold and size had been predicted correctly. Step 4 above is the corrected naming.

## Conclusion

The rule held for every word, and the samples exercise each of its parts:

- **A character style wins over the paragraph style.** In `unbold-middle`, `two` has a character style with bold = 0 inside a paragraph whose style sets bold = 1, and Pages shows it regular.
- **Properties a style doesn't set come from its parent.** The unnamed paragraph style in `unbold-middle` sets only bold, and size and font come from its parent, Body. The unnamed character styles of 0004 and 0007 set one property each.
- **When the character chain sets nothing, the paragraph chain decides.** Every character style seen so far ends at the null character style, which sets no properties.
- **Named styles set their properties directly.** Heading sets its own font, bold and size.

A Heading style can name a bold font (`HelveticaNeue-Bold`) and also set bold. So a reader should treat 11.5 as a font name that may already carry a weight.

## Confidence

*Likely*: the rule above, for bold, italic, size and font. It held for all 19 words in 8 documents. It hasn't yet been tested with a named character style, or with differing paragraph styles where a paragraph's entry has no style.

*Unknown*: whether other properties, such as colour, underline and alignment, follow the same order. Underline and colour don't show in the font name, so checking them needs a different readback, such as the `color` property in AppleScript.
