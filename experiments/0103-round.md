# 0103: ROUND

**Status:** run

[0031](0031-cell-kinds.md), [0035](0035-formula-references.md), [0064](0064-operators-and-functions.md) and [0066](0066-comparisons-and-if.md) decoded formula nodes for numbers, references, ranges, operators and a few functions. This experiment, one of ten (0103–0112) that each write one formula, asks: how are a function with two arguments and a division by a literal stored?

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0064](0064-operators-and-functions.md) |

## Recipe

```bash
mkdir -p samples/0103
osascript recipes/0103-numbers-formula.applescript "$PWD/samples/0103/round.numbers" '=ROUND(B2/3;1)'
```

The recipe sets B2 to 4 and C2 to 2, and writes `=ROUND(B2/3;1)` in E2.

## Observation

The formula's nodes:

```
36  B2 (relative)
17  3.0     (field 42: 3, field 43: 3476778912330022912)
4   divide
17  1.0
16  function 126, 2 arguments
```

The cell holds the decimal128 13 × 10⁻¹ = 1.3.

## Conclusion

ROUND is function 126 and takes its two arguments in order, before the call node. That fits the alphabetical numbering found in 0064 (MIN 88 < ROUND 126 < SUM 168).

## Confidence

*Likely*: ROUND is function 126.
