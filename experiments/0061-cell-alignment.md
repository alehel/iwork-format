# 0061: Centring a cell

**Status:** run

[0043](0043-cell-styles.md) found that a cell's text style is an unnamed paragraph style, and [0010](0010-alignment.md) found alignment in field 12.1 of Pages' paragraph styles. This experiment centres a Numbers cell, to see whether the two meet.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0043](0043-cell-styles.md) |

## Recipe

```bash
mkdir -p samples/0061
osascript recipes/0061-numbers-alignment.applescript "$PWD/samples/0061/center.numbers" center
```

The recipe sets B2 to `abc` and its `alignment` to `center`.

## Observation

The cell's flags are `48 10 02 00` = 0x00021048. That is 0x8 (string), 0x40 (text style), 0x1000 and 0x20000 (text format). Its keys are 1, 1, 5 and 1. The text style key (1) names record 905237, a type-2022 paragraph style:

```
10: 1
11: bytes (0)
12: { 1: 2 }
```

## Conclusion

Centring a cell gives it a text style that sets paragraph property 12.1 = 2, the same value Pages uses for a centred paragraph. Cell alignment is therefore read exactly like paragraph alignment ([text.md](../spec/text.md#styles)).

## Confidence

*Likely*: a cell's horizontal alignment is field 12.1 of its text style, with the same values as in Pages.
