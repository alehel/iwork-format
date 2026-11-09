# 0168: A title never set

**Status:** run

This experiment saves a slide whose title was never set, to see whether the placeholder's prompt is stored on the slide.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.key` |

## Recipe

```bash
mkdir -p samples/0168
osascript recipes/0159-keynote-slides.applescript untouched "$PWD/samples/0168/untouched.key"
```

## Observation

The slide's title record holds no text. The number of records of each type in each part is the same as in 0024's empty presentation. The prompt shown in Keynote, `Presentasjonstittel` (Presentation title), is only in the layout's template slide.

## Conclusion

An empty placeholder has an empty text record on the slide. The prompt text belongs to the layout, so a reader showing the slide as it would print can leave the title empty.

## Confidence

*Likely*: placeholder prompts are stored only in the layout.
