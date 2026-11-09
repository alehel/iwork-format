# 0262: A paragraph border

**Status:** run

The Layout tab can draw lines around a paragraph. The line style is chosen from a pop-up that needs Pages in front. [0250](0250-shape-border.md) found that a shape's border is a stroke with a colour, width and pattern. This experiment adds a paragraph border, to see whether it uses the same form.

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
2. With Pages in front, click in `One`, open the Layout tab, and choose the first solid line from the Paragraph Borders (*Avsnittskantlinjer*) pop-up. Pages draws a black 1-point line above the paragraph, with an offset of 6 pt, and selects the top-edge button.
3. Save it as `samples/0262/border.pages`.

## Observation

The paragraph runs point at a new paragraph style whose properties, in field 12, are:

```
15: 1
32: { 1: black, alpha 1,  2: 1.0,  3: 1,  4: 1,  5: 4.0,  6: { 1: 1, … } }
45: 1
```

## Conclusion

Paragraph property 32 is the border's stroke. It has the same layout as a shape's stroke (field 1.11.2, [0250](0250-shape-border.md)): colour in 1, width in points in 2, and the pattern kind in 6.1 (1, solid). Fields 3 and 4 are 1 here and 0 in a shape's stroke, so they are probably the line cap and join. One of properties 15 and 45 most likely says which edges get the line (the top here), and the other turns the border on. The 6-point offset isn't stored, so it is probably the default.

## Confidence

*Likely*: paragraph property 32 is the border stroke, in the shape stroke's layout.

*Unknown*: properties 15 and 45. Follow-up: choose a different edge, such as the bottom.
