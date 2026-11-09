# 0034: Mixed paragraph styles

**Status:** run

[0033](0033-style-resolution.md) tested how styles combine, but no sample had a paragraph with no style entry that follows a paragraph of a different style. This experiment gives the second of four paragraphs the Heading style. It then looks at what Pages writes for the paragraphs after it, and checks the rule from 0033 against Pages' own reading.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0005](0005-paragraphs.md) (paragraph runs with no style entries) |

## Recipe

1. AppleScript makes a new document with the body text `one`, `two`, `three` and `four`, separated by line feeds.
2. In the Pages window, click in `two` and choose *Overskrift* (Heading) in the paragraph style menu, as in [0006](0006-typing-in-pages.md).
3. AppleScript saves the document as `samples/0034/mixed.pages`.
4. Each word's `font` and `size` are read back through AppleScript as in 0033. The 0033 script predicts them from the file.

## Observation

The paragraph-style runs (field 5 of the body):

```
{ 1: 0,  2: { 1: 1731511 } }     Body      "one"
{ 1: 4,  2: { 1: 1731502 } }     Heading   "two"
{ 1: 8,  2: { 1: 1731511 } }     Body      "three"
{ 1: 14 }                                  "four"
```

| Word | Pages reports | Predicted by the 0033 rule |
| --- | --- | --- |
| one | HelveticaNeue, 11 | same |
| two | HelveticaNeue-Bold, 18 | same |
| three | HelveticaNeue, 11 | same |
| four | HelveticaNeue, 11 | same |

## Conclusion

Pages names a paragraph style in a run entry whenever the style differs from the previous paragraph's. Here it wrote Body explicitly for `three`, after the Heading. It leaves the style out when a paragraph keeps the previous one's style, as for `four`. That fits reading an entry with no style as "the same as the previous paragraph". In this document, though, that style is also Body, so "Body" and "keep the previous" can't be told apart yet. The 0033 rule predicted all four words.

## Confidence

*Likely*: Pages writes a paragraph style in a run entry wherever it changes, and the 0033 rule holds with mixed paragraph styles.

*Unknown*: whether an entry with no style means "same as before" or "Body". Follow-up: give two consecutive paragraphs the Heading style and look at the second one's entry.
