# 0088: Auto loop

**Status:** run

This experiment turns on *auto loop*, which repeats the slideshow, to find where it is stored.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` |

## Recipe

```bash
mkdir -p samples/0088
osascript recipes/0087-keynote-document-settings.applescript "$PWD/samples/0088/autoloop.key" autoloop
```

The recipe sets the document's `auto loop` to true.

## Observation

The presentation record (type 2) changed field 8 from 0 to 1, and nothing else changed apart from save-to-save values.

## Conclusion

Field 8 of the presentation is *auto loop*: 1 repeats the slideshow.

## Confidence

*Likely*: presentation field 8 is auto loop.
