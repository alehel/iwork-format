# 0205: Small caps

**Status:** run

This experiment applies one character option from the Format menu, which AppleScript can't set, to find where Pages stores it.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | A new document with the body text `One two` |

## Recipe

1. Make a document with the body text `One two`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One two"'
   ```
2. Double-click `two`, then choose Format → Font → Capitalisation → Small Caps (*Små/store bokstaver → Kapiteler*). `two` is drawn in small capitals.
3. Save it as `samples/0205/small-caps.pages`.

## Observation

The body's character style runs (field 8) gain an entry at 4, pointing at a new character style (type 2021) whose parent (1.3) is the default character style. Its only property, in field 11, is:

```
13: 2
```

## Conclusion

Character property 11.13 is the capitalisation, and 2 means small caps. The text in the body is still `One two`, in its original case: capitalisation is applied when drawing, so a reader must apply it itself to show the text as Pages does.

## Confidence

*Likely*: character property 13 is 2 for small caps, and the stored text keeps its case.
