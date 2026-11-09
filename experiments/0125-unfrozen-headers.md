# 0125: Header rows not frozen

**Status:** run

This experiment turns off *freeze header rows*, which keeps header rows visible while scrolling.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0125
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0125/unfrozen.numbers" unfrozen
```

## Observation

The recipe sets the table's `header rows frozen` to false. Model field 12 changed from 1 to absent (0).

## Conclusion

Table model field 12 is 1 when the header rows are frozen. Absent means 0. It only affects scrolling on screen, so a reader can ignore it.

## Confidence

*Likely*: model field 12 is *header rows frozen*.
