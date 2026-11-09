# 0208: No ligatures

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
2. Double-click `two`, then choose Format → Font → Ligatures → Use None (*Ligatur → Bruk ingen*). No visible change: `two` has no letters that join.
3. Save it as `samples/0208/no-ligatures.pages`.

## Observation

The body's character style runs (field 8) gain an entry at 4, pointing at a new character style (type 2021) whose parent (1.3) is the default character style. Its only property, in field 11, is:

```
16: 0
```

## Conclusion

Character property 11.16 is the ligature setting, and 0 means none. Since the default (absent) uses the font's standard ligatures, Use All is probably a third value.

## Confidence

*Likely*: character property 16 is 0 for no ligatures.
