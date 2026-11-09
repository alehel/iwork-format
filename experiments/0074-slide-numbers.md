# 0074: Slide numbers

**Status:** run

This experiment turns on slide numbers for a presentation, to see where that setting is kept.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key` |

## Recipe

```bash
mkdir -p samples/0074
osascript recipes/0068-keynote-variants.applescript "$PWD/samples/0074/slidenumbers.key" slidenumbers
```

AppleScript has `slide numbers showing` as a property of the document.

## Observation

Every slide node (type 4) changed field 18 from 0 to 1. That is the node of slide 1 and the 17 nodes of the template slides. The presentation record (type 2) didn't change.

## Conclusion

Although AppleScript offers it as a document setting, showing slide numbers is stored per slide, in field 18 of each slide node. Turning it on for the document set it on every slide, layouts included. A reader should check each slide's own flag.

## Confidence

*Likely*: slide node field 18 marks a slide whose number is shown.
