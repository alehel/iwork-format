# 0237: Ligatures off for the document

**Status:** run

[0236](0236-hyphenation.md) found hyphenation in the type-10012 document settings. The Document sidebar also has a ligature switch, separate from the character property of [0208](0208-no-ligatures.md). This experiment turns it off.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0236/plain.pages`, a new document with the body text `One` |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. Open the Document sidebar (the *Dokument* button in the toolbar) and untick Show Ligatures (*Vis ligaturer*).
3. Save it as `samples/0237/no-ligatures.pages`.

## Observation

Apart from the creation time, the only change is in the type-10012 record:

```
10: 1 → 0
```

## Conclusion

Field 10 of the type-10012 document settings says whether ligatures are used at all. A character style can still turn them off for some text (property 16, 0208). A reader should use ligatures only where both allow them.

## Confidence

*Likely*: type-10012 field 10 turns ligatures on for the document.
