# 0111: A percentage literal

**Status:** run

[0031](0031-cell-kinds.md), [0035](0035-formula-references.md), [0064](0064-operators-and-functions.md) and [0066](0066-comparisons-and-if.md) decoded formula nodes for numbers, references, ranges, operators and a few functions. This experiment, one of ten (0103–0112) that each write one formula, asks: how is `50%` inside a formula stored?

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0064](0064-operators-and-functions.md) |

## Recipe

```bash
mkdir -p samples/0111
osascript recipes/0103-numbers-formula.applescript "$PWD/samples/0111/percent-literal.numbers" '=50%*B2'
```

The recipe sets B2 to 4 and C2 to 2, and writes `=50%*B2` in E2.

## Observation

The formula's nodes:

```
17  50.0
15
36  B2
3   multiply
```

The cell holds the decimal128 20 × 10⁻¹ = 2.

## Conclusion

A percent sign is its own operator, node 15, applied after the number it follows (50), not folded into the literal. A reader divides the value before it by 100.

## Confidence

*Likely*: node 15 is the percent operator.
