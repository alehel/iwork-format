# 0090: Another theme

**Status:** run

Every Keynote sample so far used the default theme, *Basic White* in its wide (16:9) form. This experiment makes a presentation from the second theme Keynote lists, to see what changes with the theme.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` |

## Recipe

```bash
mkdir -p samples/0090
osascript recipes/0087-keynote-document-settings.applescript "$PWD/samples/0090/theme.key" theme
```

The recipe makes the document with `document theme` set to `theme 2`. Keynote names it *Enkel, svart* (Basic Black).

## Observation

| | Default (0025) | Theme 2 |
| --- | --- | --- |
| Root's template path (shared block, field 9) | `Application/21_BasicWhite/Wide` | `Application/20_BasicBlack/Standard` |
| `BuildVersionHistory.plist` | `Template: 21_BasicWhite (dev/15.4)` | `Template: 20_BasicBlack (dev/15.4)` |
| Presentation field 4, slide size | 1920 × 1080 | 1024 × 768 |
| Parts | 54 | 54 |
| Template slides | 17 | 17 |
| Data files | 23 | 23 |

The template slides hold the same Norwegian placeholder texts.

## Conclusion

A theme decides the template slides, their images and the slide size. The theme *Basic Black* in its *Standard* form gives 4:3 slides of 1024 × 768. The theme's identity is recorded as the template path in the root's document-properties block, and in `BuildVersionHistory.plist`. The parts and records are the same kinds as for the default theme. A reader needs the theme name only for display, since everything it draws from is in the file.

## Confidence

*Likely*: a presentation's theme is named in the root's template path, and its template slides, images and slide size are copied into the file.
