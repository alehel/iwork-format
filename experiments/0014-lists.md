# 0014: Lists

**Status:** run

Since [0002](0002-one-word.md), field 7 of the body's type-2001 record has pointed at a list style named *Ingen* (None), `text-0-liststyle-None`. This experiment makes a dash list and a numbered list, to see how a list is attached to paragraphs and what a list style holds.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface and default autocorrection |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0006](0006-typing-in-pages.md), `return-ui.pages` (typed paragraphs, no list) |

## Recipe

There is no menu command for lists, and the list menu in the sidebar is a pop-up the test couldn't open. Instead, the lists were typed so that Pages' automatic list detection made them. AppleScript made an empty document, the keys were typed in the Pages window, and AppleScript saved the document.

| File | Typed |
| --- | --- |
| `dash-list.pages` | `- one`, Return, `two`, Return, `three` |
| `numbered-list.pages` | `1. one`, Return, `two`, Return, `three` |

After the first Return, Pages turned the paragraph into a list item. The sidebar then showed the list style as *Strek* (Dash) and *Nummerert* (Numbered).

While making the numbered list, Pages showed an autocorrection suggestion (`Three`) under the last word. As long as it was shown, Pages didn't answer AppleScript. It was dismissed with its close button, so the last word stayed lowercase in that file.

## Observation

### The text

```
dash-list.pages      3: text (13 bytes) "One\nTwo\nThree"
numbered-list.pages  3: text (13 bytes) "One\nTwo\nthree"
```

The `- ` and `1. ` that were typed aren't in the text. The marker is not stored as characters.

### The body's runs

Only field 7 differs from a plain document. In both files it has one entry, at 0, which covers all three paragraphs:

```
dash-list.pages      7: { 1: { 1: 0, 2: { 1: 1731488 } } }
numbered-list.pages  7: { 1: { 1: 0, 2: { 1: 1731486 } } }
```

The paragraph-style runs (field 5) have one entry per paragraph, as in 0005. Field 6 keeps its single entry of three zeros.

### The list styles

Both list styles were already in the stylesheet, so no record was added. The order of a few records in `DocumentStylesheet.iwa` changed, but their contents didn't.

All three list styles are type 2023 and store most properties as nine repeated values:

| Field | None (1731481) | Dash (1731488) | Numbered (1731486) |
| --- | --- | --- | --- |
| 1.1, 1.2 | `Ingen`, `text-0-liststyle-None` | `Strek`, `text-7-liststyle-Dash` | `Nummerert`, `text-5-liststyle-Numbered` |
| 10 | 4 | 5 | 6 |
| 11 (×9) | 0 | 2 | 3 |
| 12 (×9, float) | −0, then 0 | 1.0909091 | 1.6363636 |
| 13 (×9, float) | 0, 36, 72 … 288 | 0, 12, 24 … 96 | 0, 18, 36 … 144 |
| 14 (×9, message) | `{1: 1.0, 2: 0, 3: 1}` | `{1: 1.2, 2: 2.0, 3: 1}` | `{1: 1.0, 2: 0, 3: 1}` |
| 15 (×9) | — | — | 0 |
| 16 (×9, text) | — | `-` | — |
| 25 (×9) | — | — | 0 |

## Conclusion

A list is a list style attached to a range of paragraphs through the list-style runs (field 7). The marker, a dash or a number, is not part of the text. A reader has to draw it from the list style.

A list style describes nine levels, with each property stored as nine repeated values, one per level:

- Field 11 is the kind of marker: 0 none, 2 a text character, 3 a number.
- Field 16 is the marker text for kind 2.
- Field 15 is probably the number format for kind 3.
- Field 13 increases by a fixed step per level, so it is probably each level's indent in points.
- Field 12 equals the first indent step divided by 11, the Body font size (12 / 11 = 1.0909; 18 / 11 = 1.6364). It may be the same indent expressed relative to the font size.

Field 10 equals the number of distinct property fields each list style sets (4, 5 and 6). Together with the unnamed styles of 0007–0011, this suggests field 10 counts properties, though in the named paragraph styles of 0010 it was two less than the count.

Field 6 of record 2001 is unchanged by a single-level list, so it might hold list levels. A nested list would test that.

## Confidence

*Likely*:

- Field 7 runs attach list styles (type 2023) to paragraphs.
- List markers aren't stored in the text.
- A list style stores nine per-level values, with 11 as the marker kind and 16 as the marker text.

*Unknown*:

- Fields 12, 13, 14, 15 and 25 of a list style. Follow-up: number a list with letters, and start numbering at 5.
- Where list levels are stored. Follow-up: indent the second item of a list with Tab.
