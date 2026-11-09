# 0164: A title on two lines

**Status:** run

This experiment sets a slide title with a line feed in it, to see whether it becomes a line break or a new paragraph.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md) |

## Recipe

```bash
mkdir -p samples/0164
osascript recipes/0159-keynote-slides.applescript titlebreak "$PWD/samples/0164/titlebreak.key"
```

## Observation

The title's text record holds `one\ntwo`: a line feed, not U+2028. Its paragraph-style runs have entries at 0 and 4.

## Conclusion

A line feed set through AppleScript becomes a paragraph break, even in a title. So a title can have several paragraphs. A reader should keep the line feed rather than flatten a title to one line. A line break inside a paragraph (U+2028) would need typing Shift-Return in Keynote.

## Confidence

*Likely*: a line feed in a title is a paragraph break.
