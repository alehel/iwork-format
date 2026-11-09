# 0104: Nested functions

**Status:** run

[0031](0031-cell-kinds.md), [0035](0035-formula-references.md), [0064](0064-operators-and-functions.md) and [0066](0066-comparisons-and-if.md) decoded formula nodes for numbers, references, ranges, operators and a few functions. This experiment, one of ten (0103–0112) that each write one formula, asks: how is a function inside another stored, and what are the number nodes' fields 42 and 43?

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0064](0064-operators-and-functions.md) |

## Recipe

```bash
mkdir -p samples/0104
osascript recipes/0103-numbers-formula.applescript "$PWD/samples/0104/nested-functions.numbers" '=ROUND(AVERAGE(B2:C2)*1,5;0)'
```

The recipe sets B2 to 4 and C2 to 2, and writes `=ROUND(AVERAGE(B2:C2)*1,5;0)` in E2.

## Observation

The formula's nodes:

```
67  range: columns −3 to −2, rows 0 (field 40.2 = {1: 0})
16  function 15 (AVERAGE), 1 argument
17  1.5     (field 42: 15, field 43: 3476215962376601600)
3   multiply
17  0.0     (field 42: 0, field 43: 3476778912330022912)
16  function 126 (ROUND), 2 arguments
```

The cell holds 5: (4 + 2) / 2 × 1.5 = 4.5, rounded.

## Conclusion

Nested calls are flattened into the postfix list: the inner call comes first and its result is the outer call's first argument.

Fields 42 and 43 of a number node hold the number as a decimal128: 42 is the low 64 bits (the coefficient, 15 for 1.5) and 43 the high 64 bits, which carry the exponent. 0x3040000000000000 = 3476778912330022912 is exponent 0, and 0x303E000000000000 = 3476215962376601600 is exponent −1, so 1.5 = 15 × 10⁻¹. The double in field 4 holds the same number. A reader can use either, but the decimal128 is exact.

A range within one row stores only the first row in 40.2 (`{1: 0}`, the formula's own row), with no last row.

## Confidence

*Likely*:

- Nested calls are flattened in postfix order.
- Number node fields 42 and 43 are the decimal128 form of the number.
