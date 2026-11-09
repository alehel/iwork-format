# 0058: A tab and a non-breaking space

**Status:** run

Experiments [0005](0005-paragraphs.md), [0018](0018-page-break-and-left-page.md), [0040](0040-section-break.md) and [0041](0041-footnote.md) found control characters with special meanings in the text. This experiment checks two ordinary layout characters, a tab and a non-breaking space, to see whether either gets special treatment.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0002](0002-one-word.md), `hello.pages` |

## Recipe

```bash
mkdir -p samples/0058
osascript recipes/0058-pages-tab.applescript "$PWD/samples/0058/tab.pages"
```

The recipe sets the body text to `a`, a tab (U+0009), `b`, a non-breaking space (U+00A0) and `c`.

## Observation

```
3: text (6 bytes) "a\tb\u{a0}c"        61 09 62 c2 a0 63
```

Compared with `hello.pages`, field 3 is the only difference in the body record, apart from the creation time. No run table gained an entry.

## Conclusion

A tab is stored as U+0009 and a non-breaking space as U+00A0, as plain characters in the text with nothing else attached. A reader treats them as ordinary text. Where tabs stop is presumably set by the paragraph style, which this experiment doesn't look at.

## Confidence

*Likely*: tabs and non-breaking spaces are plain characters with no runs of their own.
