# 0236: Hyphenation

**Status:** run

Pages can hyphenate a whole document from the Document sidebar. This experiment turns that on, to find where document-wide settings are stored. [0017](0017-section-switches.md) found facing pages in a type-10012 record, which seems to hold such settings.

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
2. Open the Document sidebar (the *Dokument* button in the toolbar) and tick Use Hyphenation in Document (*Bruk orddeling i dokument*).
3. Save it as `samples/0236/hyphenation.pages`.

## Observation

Apart from the creation time stored as text in field 26, the only record that changes in `Document.iwa` is the one of type 10012:

```
9: 0 → 1
```

No paragraph style changes.

## Conclusion

Field 9 of the type-10012 document settings turns on hyphenation for the whole document. It is a document setting, not a property of the paragraph styles, so a reader that lays out text should hyphenate every paragraph when it is 1.

## Confidence

*Likely*: type-10012 field 9 is document-wide hyphenation.
