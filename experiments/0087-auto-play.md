# 0087: Auto play

**Status:** run

This experiment turns on a presentation's *auto play* setting, which starts the slideshow when the file is opened, to find where it is stored.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` |

## Recipe

```bash
mkdir -p samples/0087
osascript recipes/0087-keynote-document-settings.applescript "$PWD/samples/0087/autoplay.key" autoplay
```

The recipe sets the document's `auto play` to true.

## Observation

The presentation record (type 2) changed field 18 from 0 to 1. Apart from save-to-save changes, the only other difference was a template slide's thumbnail data ID, which was renumbered.

## Conclusion

Field 18 of the presentation is *auto play*: 1 starts the slideshow when the file opens.

## Confidence

*Likely*: presentation field 18 is auto play.
