# 0203: Superscript

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
2. Double-click `two`, then choose Format → Font → Baseline → Superscript (*Skriftlinje → Hevet tekst*). `two` is drawn smaller and raised.
3. Save it as `samples/0203/superscript.pages`.

## Observation

The body's character style runs (field 8) gain an entry at 4, pointing at a new character style (type 2021) whose parent (1.3) is the default character style. Its only property, in field 11, is:

```
10: 1
```

## Conclusion

Character property 11.10 is the baseline position, and 1 means superscript. The size isn't stored: Pages works out the smaller size and the raised position when it draws the text.

## Confidence

*Likely*: character property 10 is 1 for superscript.
