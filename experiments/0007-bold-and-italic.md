# 0007: Bold and italic

**Status:** run

Experiment [0004](0004-larger-word.md) changed one word's size and found a character-style run pointing at a new, unnamed style. AppleScript can't make text bold or italic, so this experiment uses the Bold and Italic buttons in the Pages window, to see how those are stored.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0004](0004-larger-word.md): `plain.pages`, and `large.pages` for the same change with a size |

## Recipe

The text was set through AppleScript, so it is the same as in 0004 and Pages doesn't autocorrect it (see [0006](0006-typing-in-pages.md)). Each document was made like this:

1. With AppleScript, make a new document and set its body text to `hello world`:
   ```applescript
   tell application "Pages"
       set d to make new document
       set body text of d to "hello world"
   end tell
   ```
2. In the Pages window, double-click `world` to select it, then click buttons in the Style tab of the Format sidebar:

   | File | Buttons |
   | --- | --- |
   | `bold.pages` | Bold |
   | `italic.pages` | Italic |
   | `bold-italic.pages` | Bold, then Italic |

3. Save with AppleScript, `save front document in POSIX file "…"`, and close.

## Observation

### The run table

In all three files the body's type-2001 record has a field 8 just like the one in 0004's `large.pages`. It has an entry at 0 with no style, and an entry at 6 naming a new object. Compared with `large.pages`, the only difference in record 2001 is the ID of that object. Fields 19 and 20 from 0006 are absent, as expected for text set through AppleScript.

### The new character style

Each file has one more record in `DocumentStylesheet.iwa` than `plain.pages`: an unnamed type-2021 character style. Its parent (field 1.3) is the null character style 1731539, as in 0004. Fields 10 and 11 differ:

```
bold.pages            10: varint 1   11: { 1: varint 1 }
italic.pages          10: varint 1   11: { 2: varint 1 }
bold-italic.pages     10: varint 2   11: { 1: varint 1, 2: varint 1 }
0004 large.pages      10: varint 1   11: { 3: fixed32 24.0 }
```

Everything else in these records is the same as in 0004's style.

### Other changes

The other changes from `large.pages` are the save-to-save changes from 0001 and 0002, plus `ViewState.iwa` record type 10132. That record grew from 24 to 28 bytes, probably because `world` was still selected when the file was saved.

## Conclusion

Bold and italic are stored the same way as a size. They go in a new, unnamed character style that inherits from the null character style, and the run table points the range at it. Field 11 of a character style holds its properties:

| Field 11.n | Property | Seen as |
| --- | --- | --- |
| 1 | Bold | varint 1 |
| 2 | Italic | varint 1 |
| 3 | Size in points | float |

Field 10 of a character style was 1 when the style set one property and 2 when it set two. It may count the properties, or the edits that made the style. This experiment can't tell those apart.

## Confidence

*Likely*:

- Field 11.1 of a character style is bold, 11.2 is italic and 11.3 is the size.
- Each change to part of the text makes an unnamed character style. Follow-up: make two separate words bold, and see whether they share one style.

*Unknown*:

- What field 10 counts. Follow-up: set bold and size together with a single change, which is one edit setting two properties.
- How "not bold" is stored, for example in a bold heading where one word is made regular.
