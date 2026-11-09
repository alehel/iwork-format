# 0210: A column break

**Status:** run

[0018](0018-page-break-and-left-page.md) found that a page break is U+0005 and [0040](0040-section-break.md) that a section break is U+0004. Pages also has a column break. This experiment inserts one, to find its character.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0018](0018-page-break-and-left-page.md) and [0040](0040-section-break.md) |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. Click after `One`, choose Insert → Column Break (*Sett inn → Spalteskift*), then type `Two`. The document has one column, so `Two` moves to the next page.
3. Save it as `samples/0210/column-break.pages`.

## Observation

The body text is the bytes `4f 6e 65 0c 54 77 6f`: `One`, U+000C, `Two`. The paragraph style runs (field 5) have two entries, at 0 and 4, so `Two` starts a new paragraph.

## Conclusion

A column break is U+000C (form feed). Like a page break, it also ends the paragraph. In a one-column section it acts as a page break. A reader that only extracts text can treat it as a paragraph break.

## Confidence

*Likely*: a column break is U+000C and ends its paragraph.
