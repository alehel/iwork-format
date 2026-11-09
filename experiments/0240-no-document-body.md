# 0240: No document body

**Status:** run

[0156](0156-page-layout-template.md) found that a page-layout document has root field 48 and an empty body. A word-processing document can be converted by turning off Document Body. This experiment does that, to see what else changes.

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
2. Open the Document sidebar (the *Dokument* button in the toolbar) and untick Document Body (*Dokumentbrødtekst*), then confirm the conversion (*Konverter*). Pages warns that the body text will be removed.
3. Save it as `samples/0240/no-document-body.pages`.

## Observation

The type-10012 record changes:

```
1: 1 → 0
```

The body text record (1732539) loses its text: field 3 is gone. The root (type 10000) gains field 48, and a type-10017 record is added, as in the page-layout template of 0156.

## Conclusion

Field 1 of the type-10012 document settings says whether the document has a body: 1 for word processing, 0 for page layout. Converting a document only clears the body and adds the page template, so the result looks like a document made from a page-layout template. A reader can tell the two kinds apart by this field as well as by root field 48.

## Confidence

*Confirmed*, with 0156: a page-layout document has root field 48 and an empty body.

*Likely*: type-10012 field 1 is 0 for page layout.
