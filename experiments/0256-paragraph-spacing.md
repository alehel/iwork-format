# 0256: Space before and after a paragraph

**Status:** run

[0252](0252-line-spacing.md) found line spacing in paragraph property 13. The same Spacing section of the Format sidebar sets the space before and after a paragraph, in number fields that need Pages in front. This experiment sets two different values, to tell them apart.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0236/plain.pages` |

## Recipe

1. Make a document with the body text `One`:
   ```bash
   osascript -e 'tell application "Pages" to set body text of (make new document) to "One"'
   ```
2. With Pages in front, click in `One`, expand Spacing (*Avstand*) in the Style tab, and type 6 in Before Paragraph (*Før avsnitt*) and 9 in After Paragraph (*Etter avsnitt*), in points.
3. Save it as `samples/0256/spacing.pages`.

## Observation

The paragraph runs point at a new paragraph style whose properties, in field 12, are:

```
20: 9.0
21: 6.0
```

## Conclusion

Paragraph property 21 is the space before the paragraph and 20 the space after, in points. The field numbers run in the opposite order to the sidebar's. A reader adds the larger of one paragraph's space after and the next one's space before, or both, depending on how Pages combines them. That isn't tested here.

## Confidence

*Likely*: paragraph properties 20 and 21 are the space after and before, in points.

*Unknown*: how Pages combines the spaces of adjacent paragraphs.
