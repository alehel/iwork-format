# 0008: Runs and shared styles

**Status:** run

Follow-ups from [0004](0004-larger-word.md) and [0007](0007-bold-and-italic.md). Does a character-style run in the middle of the text get closed by an entry? Do two bold ranges share one style object? And how is "not bold" stored?

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0004](0004-larger-word.md), `plain.pages`; experiment [0007](0007-bold-and-italic.md), `bold.pages` |

## Recipe

As in 0007: AppleScript makes a new document and sets the body text to `one two three`. Then the Pages window is used to select and format text, and AppleScript saves the document.

| File | Steps in the Pages window |
| --- | --- |
| `middle.pages` | Double-click `two`, click Bold |
| `two-words.pages` | Double-click `one`, click Bold; double-click `three`, click Bold |
| `unbold-middle.pages` | Triple-click the paragraph, click Bold; double-click `two`, click Bold again to turn it off |

Positions: `one` is 0–3, `two` is 4–7, `three` is 8–13.

## Observation

### `middle.pages`

The character-style runs (field 8 of the body's type-2001 record):

```
8: message (18 bytes)
  1: { 1: 0 }
  1: { 1: 4, 2: { 1: 1732696 } }
  1: { 1: 7 }
```

The bold run starts at 4 and is closed by an entry at 7 with no style. Object 1732696 is an unnamed type-2021 style with `11: { 1: 1 }`, the same as the bold style in 0007.

### `two-words.pages`

```
8: message (24 bytes)
  1: { 1: 0, 2: { 1: 1732696 } }
  1: { 1: 3 }
  1: { 1: 8, 2: { 1: 1732696 } }
```

Both bold words point at the same object. The stylesheet gained one record, not two. Because the first word starts at 0, the first entry carries the style itself.

### `unbold-middle.pages`

The stylesheet gained two records:

```
1732699, type 2022 (a paragraph style), 24 bytes
  1: { 3: { 1: 1731511 }, 4: 1, 5: { 1: 1732613 } }     ← parent: the Body paragraph style
  10: varint 1
  11: { 1: varint 1 }                                     ← bold
  12: bytes (0)

1732745, type 2021 (a character style), 22 bytes
  1: { 3: { 1: 1731539 }, 4: 1, 5: { 1: 1732613 } }     ← parent: the null character style
  10: varint 1
  11: { 1: varint 0 }                                     ← not bold
```

The body's runs:

```
5: { 1: { 1: 0, 2: { 1: 1732699 } } }             paragraph styles
8: { 1: { 1: 0 },                                  character styles
     1: { 1: 4, 2: { 1: 1732745 } },
     1: { 1: 7 } }
```

When the whole paragraph was bold, Pages didn't use a character style. It made an unnamed paragraph style that inherits from Body and adds bold, and pointed the paragraph at it. The Format sidebar showed the paragraph style as `Brødtekst*`. Turning bold off for `two` then made a character style that sets bold to 0.

## Conclusion

A character-style run lasts until the next entry. To end a run before the end of the text, Pages writes an entry with no style. When the styled range starts at 0, the first entry carries the style.

Ranges with the same formatting share one style object.

Unnamed styles exist for paragraphs too: type 2022 with a parent (field 1.3) and the changes. Formatting applied to a whole paragraph goes into such a paragraph style, not into character runs.

Paragraph styles use field 11 for the same character properties as character styles, so a reader can treat field 11 the same way for both. Paragraph styles also have a field 12, empty here, which is probably for paragraph properties.

A property turned off is stored explicitly: `11.1 = 0` means "not bold". That's not the same as leaving 11.1 out, which means "inherit". Here, the 0 overrides the bold that the paragraph style supplies.

So to find a character's bold setting, a reader has to look at the character style first, then the paragraph style, then each style's parents. The first one that sets 11.1 wins.

## Confidence

*Likely*:

- Runs, as described.
- Ranges with the same formatting share one style.
- Field 11 holds character properties in both character and paragraph styles, and an explicit 0 turns a property off.

*Unknown*:

- What field 12 of a paragraph style holds. Follow-up: change a paragraph's alignment or spacing.
- The order in which a reader should resolve character styles, paragraph styles and parents. It follows from how Pages draws this example, but the experiment only shows one combination.
