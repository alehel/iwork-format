# 0117: A date without a time

**Status:** run

[0031](0031-cell-kinds.md) stored a date with a time. This experiment stores a date at midnight.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0117
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0117/dateonly.numbers" dateonly
```

## Observation

The recipe puts 2026-01-02 00:00 in B2. The cell is type 5, with flags 0x9004, the double `00 00 00 00 a1 83 c7 41` and keys 3 and 1. Read as seconds since 2001-01-01, the double is exactly 2026-01-02 00:00.

## Conclusion

A date without a time is an ordinary date cell whose double falls on midnight. The time is simply zero, with no separate date-only kind. The format key (0x8000) decides whether a time is shown.

## Confidence

*Likely*: dates at midnight are plain date cells.
