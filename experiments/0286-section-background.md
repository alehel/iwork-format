# 0286: A section background

**Status:** run

The Document sidebar's Section tab can give a section's pages a background. Its colour well opens a popover that needs Pages in front. This experiment fills the section with yellow, to find where page backgrounds are kept.

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
2. With Pages in front, click in `One`, open the Document sidebar's Section tab (*Inndeling*), click the Background (*Bakgrunn*) colour well, and choose the yellow in the swatches' top row. The whole page turns yellow.
3. Save it as `samples/0286/yellow-section.pages`.

## Observation

The only record that changes, apart from the creation time, is the section (type 10011, [0016](0016-header-and-footer.md)). It gains:

```
30: { 1: { 1: 1, 3: 1.0, 4: 0.943, 5: 0.339, 6: 1.0, 12: 1, 13: 1.0 } }
```

## Conclusion

Section field 30 is the background of the section's pages, a fill in the layout of shape fills ([0077](0077-shape-fill.md)), here a colour in field 1. Since sections hold the background, each section of a document can have its own. A reader should paint each page with its section's field 30 before drawing anything else. The colour layout is the usual one: red, green and blue in 3–5 and alpha in 6.

## Confidence

*Likely*: section field 30 is the page background, as a fill.
