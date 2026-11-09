# 0252: Double line spacing

**Status:** run

The Format sidebar's line spacing is a pop-up menu, which needs Pages in front. This experiment sets a paragraph to double spacing, to find the paragraph property.

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
2. With Pages in front, click in `One`, then choose 2.0 – Double (*2,0 – dobbel*) from the Spacing (*Avstand*) pop-up in the Style tab.
3. Save it as `samples/0252/double.pages`.

## Observation

The paragraph runs (field 5) point at a new paragraph style (type 2022) whose parent is Body (1731511). Its only paragraph property, in field 12:

```
13: { 2: 2.0 }
```

## Conclusion

Paragraph property 13 is the line spacing, a message whose field 2 is the amount: 2.0 for double. Single spacing is the default and isn't stored. Field 13.1, absent here, is probably the kind of spacing (lines, at least, exactly, between), so absent means a multiple of the line height.

## Confidence

*Likely*: paragraph property 13.2 is the line spacing as a multiple of the line height.

*Unknown*: the other spacing kinds.
