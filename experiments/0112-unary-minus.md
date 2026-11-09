# 0112: Unary minus

**Status:** run

[0031](0031-cell-kinds.md), [0035](0035-formula-references.md), [0064](0064-operators-and-functions.md) and [0066](0066-comparisons-and-if.md) decoded formula nodes for numbers, references, ranges, operators and a few functions. This experiment, one of ten (0103–0112) that each write one formula, asks: how is a minus sign in front of a value stored, and how is a negative result kept?

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0064](0064-operators-and-functions.md) |

## Recipe

```bash
mkdir -p samples/0112
osascript recipes/0103-numbers-formula.applescript "$PWD/samples/0112/unary-minus.numbers" '=-B2'
```

The recipe sets B2 to 4 and C2 to 2, and writes `=-B2` in E2.

## Observation

The formula's nodes are `36 B2` and `13`. The cell's value is a decimal128 whose last two bytes are `40 b0` instead of `40 30`: the value is −4.

## Conclusion

Unary minus is node 13, after its operand, separate from subtraction (node 2). A negative number is stored as a decimal128 with its sign bit set, the top bit of the last byte (0xb0 instead of 0x30).

## Confidence

*Likely*: node 13 is unary minus, and negative values set the decimal128 sign bit.
