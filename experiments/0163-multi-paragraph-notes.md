# 0163: Presenter notes with several paragraphs

**Status:** run

[0039](0039-presenter-notes.md) set one line of presenter notes. This experiment sets three paragraphs.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0039](0039-presenter-notes.md) |

## Recipe

```bash
mkdir -p samples/0163
osascript recipes/0159-keynote-slides.applescript notes "$PWD/samples/0163/notes.key"
```

## Observation

The notes text record (field 1 = 4) holds `one\ntwo\nthree`, with line feeds between the paragraphs. Its paragraph-style runs (field 5) have entries at 0, 4 and 8; only the first names a style.

## Conclusion

Presenter notes are stored like any other text, with paragraphs separated by line feeds and one paragraph-style entry each.

## Confidence

*Likely*: presenter notes hold paragraphs as body text does.
