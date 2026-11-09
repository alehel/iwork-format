# 0110: A text result

**Status:** run

[0031](0031-cell-kinds.md), [0035](0035-formula-references.md), [0064](0064-operators-and-functions.md) and [0066](0066-comparisons-and-if.md) decoded formula nodes for numbers, references, ranges, operators and a few functions. This experiment, one of ten (0103–0112) that each write one formula, asks: how is a formula whose result is text cached?

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0064](0064-operators-and-functions.md) |

## Recipe

```bash
mkdir -p samples/0110
osascript recipes/0103-numbers-formula.applescript "$PWD/samples/0110/text-result.numbers" '="a"&"b"'
```

The recipe sets B2 to 4 and C2 to 2, and writes `="a"&"b"` in E2.

## Observation

The formula's nodes are `19 "a"`, `19 "b"`, `6` (join). The cell's bytes:

```
05 03 …  08 12 02 00  02 00 00 00  01 00 00 00  05 00 00 00  02 00 00 00
```

That is type 3 (text) with flags 0x21208: a string key (0x8) of 2, a formula key (0x200) of 1, the 0x1000 key and a text format key (0x20000).

## Conclusion

A text result is cached like a text cell: its value (`ab`) goes into the string table, and the cell holds that string's key next to the formula's key.

## Confidence

*Likely*: text results are cached through the string table.
