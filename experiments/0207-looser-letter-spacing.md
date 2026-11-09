# 0207: Looser letter spacing

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
2. Double-click `two`, then choose Format → Font → Character Spacing → Loosen (*Tegnavstand → Løsere*), once. `two` is spaced slightly wider.
3. Save it as `samples/0207/looser.pages`.

## Observation

The body's character style runs (field 8) gain an entry at 4, pointing at a new character style (type 2021) whose parent (1.3) is the default character style. Its only property, in field 11, is:

```
27: 0.01 (a float)
```

## Conclusion

Character property 11.27 is the letter spacing (tracking), as a fraction of the font size: one step of Loosen adds 0.01, which the Format sidebar shows as 1%. Tighten probably stores a negative value.

## Confidence

*Likely*: character property 27 is the letter spacing as a fraction of the size.
