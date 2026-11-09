# 0118: An emoji in a cell

**Status:** run

Text in a Pages document is UTF-8 ([0003](0003-non-ascii-word.md)). This experiment checks text in a cell.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0118
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0118/emoji.numbers" emoji
```

## Observation

The recipe puts `hi🙂` in B2. The string table holds 6 bytes: `68 69 f0 9f 99 82`.

## Conclusion

Cell text is UTF-8 in the string table, like body text, including characters outside the Basic Multilingual Plane.

## Confidence

*Likely*: string-table text is UTF-8.
