# 0121: A reference to an empty cell

**Status:** run

This experiment writes a formula that refers to an empty cell, to see what result is cached.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0121
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0121/emptyref.numbers" emptyref
```

## Observation

The recipe writes `=C3` in B2, with C3 empty. The cell is type 2 with flags 0x3201 and the decimal128 value 0. Its keys are 1, 1 and 2: the formula (0x200), then the 0x1000 and 0x2000 keys.

## Conclusion

A reference to an empty cell gives 0, cached as a number. A reader treats an empty cell as 0 in arithmetic, as Numbers does.

## Confidence

*Likely*: an empty referenced cell is cached as 0.
