# 0239: No footers

**Status:** run

[0238](0238-no-header.md) found that headers are turned on and off by field 2 of the type-10012 document settings. This experiment turns off footers.

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
2. Open the Document sidebar (the *Dokument* button in the toolbar) and untick Footer (*Bunntekst*).
3. Save it as `samples/0239/no-footer.pages`.

## Observation

The type-10012 record changes:

```
3: 1 → 0
```

## Conclusion

Field 3 of the type-10012 document settings says whether footers are shown, next to field 2 for headers.

## Confidence

*Confirmed*, with 0238: fields 2 and 3 of type 10012 show headers and footers.
