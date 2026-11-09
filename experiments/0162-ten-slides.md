# 0162: Ten slides

**Status:** run

This experiment saves ten slides, to see how the slide parts are named as their number grows.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0038](0038-second-slide.md), `two-slides.key` |

## Recipe

```bash
mkdir -p samples/0162
osascript recipes/0159-keynote-slides.applescript ten "$PWD/samples/0162/ten.key"
```

## Observation

Field 3.2 lists ten nodes, in order, each naming a slide in its own part. The parts are named:

| Slide | Part | Slide ID |
| --- | --- | --- |
| 1 | `Slide-2652175.iwa` | 2652175 |
| 2 | `Slide.iwa` | 2652480 |
| 3–9 | `Slide-2652603-2.iwa` … `Slide-2653342-2.iwa` | 2652603 … 2653342 |
| 10 | `Slide-2653677.iwa` | 2653677 |

Slides 2 to 10 use layout 2651826, and slide 1 uses 2651742.

## Conclusion

A slide's part name isn't a stable rule. The number in it, when there is one, is the ID of the slide inside, but one part has no number and others end in `-2`. A reader should list the parts and find each slide by its ID, as [0139](0139-resave.md) found for Pages.

New slides after the first get a different default layout from the first slide's.

## Confidence

*Likely*: part names hold the slide's ID, but not always, and sometimes with a suffix such as `-2`.
