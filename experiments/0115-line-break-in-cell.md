# 0115: A line break in a cell

**Status:** run

This experiment puts text with a line break in a cell.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0115
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0115/newline.numbers" newline
```

## Observation

The recipe puts `one`, a line feed and `two` in B2. The string table holds `"one\ntwo"`. The cell's bytes are those of an ordinary text cell, except byte 4, which is 1 instead of 0:

```
05 03 00 00 01 00 00 00 08 10 02 00 …
```

## Conclusion

A line break in a cell is stored as U+000A inside the string. Byte 4 of the cell becomes 1. That may mark text with more than one line, but no other value of it has been seen. Bytes 6–7 changed with the format in [0036](0036-more-cell-formats.md), so bytes 4–7 seem to hold small extra flags.

## Confidence

*Likely*: line breaks are kept in the string.

*Unknown*: cell byte 4.
