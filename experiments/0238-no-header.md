# 0238: No headers

**Status:** run

Headers and footers can be turned off for a whole document in the Document sidebar. This experiment turns off headers.

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
2. Open the Document sidebar (the *Dokument* button in the toolbar) and untick Header (*Topptekst*).
3. Save it as `samples/0238/no-header.pages`.

## Observation

The type-10012 record changes:

```
2: 1 → 0
```

In each of the three header-and-footer sets (type 10143, [0016](0016-header-and-footer.md)), the three header text records are replaced by new ones with new IDs. The footer records are unchanged.

## Conclusion

Field 2 of the type-10012 document settings says whether headers are shown. Turning headers off doesn't delete them as such, but Pages replaces their text records with fresh ones. A reader should skip headers when field 2 is 0.

## Confidence

*Likely*: type-10012 field 2 shows headers.
