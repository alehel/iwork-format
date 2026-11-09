# 0253: Indents

**Status:** run

Paragraph indents are set in number fields in the Format sidebar, which can only be typed into with Pages in front. This experiment sets three different indents, to tell their properties apart.

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
2. With Pages in front, click in `One`, then open the Layout tab, expand Indents (*Innrykk*), and type 1, 2 and 3 into First (*Første*), Left (*Venstre*) and Right (*Høyre*), in centimetres.
3. Save it as `samples/0253/indents.pages`.

## Observation

The paragraph runs point at a new paragraph style whose properties, in field 12, are:

```
7:  28.346457   ← 1 cm in points
11: 56.692913   ← 2 cm
19: 85.03937    ← 3 cm
```

## Conclusion

Paragraph properties 7, 11 and 19 are the first-line, left and right indents, in points, whatever unit the app shows. A reader indents the first line by field 7 measured from the left edge of the text. Pages shows the first line's indent separately from the left indent, so the two are probably independent rather than added.

## Confidence

*Likely*: paragraph properties 7, 11 and 19 are the first-line, left and right indents in points.

*Unknown*: whether the first-line indent is measured from the margin or from the left indent. Follow-up: set only a left indent and check where the first line starts.
