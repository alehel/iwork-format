# 0204: Subscript

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
2. Double-click `two`, then choose Format → Font → Baseline → Subscript (*Skriftlinje → Senket tekst*). `two` is drawn smaller and lowered.
3. Save it as `samples/0204/subscript.pages`.

## Observation

The body's character style runs (field 8) gain an entry at 4, pointing at a new character style (type 2021) whose parent (1.3) is the default character style. Its only property, in field 11, is:

```
10: 2
```

## Conclusion

Subscript is the same property as superscript ([0203](0203-superscript.md)), with the value 2. A reader can treat 0 or absent as normal, 1 as superscript and 2 as subscript.

## Confidence

*Confirmed*, with 0203: character property 10 is the baseline position. *Likely*: 2 is subscript.
