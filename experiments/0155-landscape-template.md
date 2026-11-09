# 0155: The landscape template

**Status:** run

This experiment makes a document from Pages' blank landscape template, to see how orientation is stored.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0020/plain.pages` (the body text `one`) |

## Recipe

```bash
mkdir -p samples/0155
osascript recipes/0149-pages-text.applescript landscape "$PWD/samples/0155/landscape.pages"
```

## Observation

The document root (type 10000) differs from a portrait document's:

| Field | Portrait (`Application/Blank/ISO`) | Landscape |
| --- | --- | --- |
| 30, 31 (paper width and height) | 595.28 × 841.89 | 842 × 595 |
| 42 | 0 | 1 |
| 44 (paper name) | `iso-a4` | `iso-a4` |
| 15.9 | `Application/Blank/ISO` | `Application/BlankLandscape/ISO` |

The margins are the same.

## Conclusion

Root field 42 is the orientation: 1 for landscape. The paper size in 30 and 31 is already swapped, so a reader can use it as the page size without looking at 42. The paper name stays `iso-a4`.

Field 15.9 names the template the document was made from.

## Confidence

*Likely*: root field 42 is the orientation (1 landscape), and 30 and 31 hold the page size as laid out.

*Likely*: field 15.9 is the template's identifier.
