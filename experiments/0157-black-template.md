# 0157: The black template

**Status:** run

This experiment makes a document from the blank black template, to see how a template's look is stored.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0020/plain.pages` (the body text `one`) |

## Recipe

```bash
mkdir -p samples/0157
osascript recipes/0149-pages-text.applescript black "$PWD/samples/0157/black.pages"
```

## Observation

The root has `Application/20_Blank_Black/ISO` in field 15.9, and slightly different page setup: 595 × 842, all margins 57, header and footer distances 35 and 43.2. Object IDs start lower (the body is 1431005, not 1732539).

The body's paragraph style is the template's own Body style, 1430051, named `Brødtekst`. Its text colour, 11.7, is white (0.9999, 1, 0.9999, 1). As in the blank template, its field 10 is 57.

## Conclusion

A template's look is part of the document: the styles are copied in with their own values, such as Body's white text. The page's black background must be stored elsewhere, perhaps in the section; this experiment didn't find it.

Different templates also come with their own object ID ranges, so readers can't expect particular IDs.

## Confidence

*Likely*: a template's styles are copied into the document.

*Unknown*: where the page background colour is stored.
