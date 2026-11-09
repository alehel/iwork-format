# 0206: All caps

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
2. Double-click `two`, then choose Format → Font → Capitalisation → All Caps (*Små/store bokstaver → Kun store*). `two` is drawn as `TWO`.
3. Save it as `samples/0206/all-caps.pages`.

## Observation

The body's character style runs (field 8) gain an entry at 4, pointing at a new character style (type 2021) whose parent (1.3) is the default character style. Its only property, in field 11, is:

```
13: 1
```

## Conclusion

All caps is the same property as small caps ([0205](0205-small-caps.md)), with the value 1. The stored text is still lowercase. The menu's other two options, title case and initial capitals, are probably further values of this property.

## Confidence

*Confirmed*, with 0205: character property 13 is the capitalisation. *Likely*: 1 is all caps.
