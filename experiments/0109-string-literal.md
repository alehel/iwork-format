# 0109: A text literal

**Status:** run

[0031](0031-cell-kinds.md), [0035](0035-formula-references.md), [0064](0064-operators-and-functions.md) and [0066](0066-comparisons-and-if.md) decoded formula nodes for numbers, references, ranges, operators and a few functions. This experiment, one of ten (0103–0112) that each write one formula, asks: how is text inside a formula stored?

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0064](0064-operators-and-functions.md) |

## Recipe

```bash
mkdir -p samples/0109
osascript recipes/0103-numbers-formula.applescript "$PWD/samples/0109/string-literal.numbers" '=LEN("abc")'
```

The recipe sets B2 to 4 and C2 to 2, and writes `=LEN("abc")` in E2.

## Observation

The formula's nodes:

```
19  6: "abc"
16  function 77, 1 argument
```

The cell holds 3.

## Conclusion

A text literal is node 19, with the text in field 6. It isn't put in the table's string table. LEN is function 77, which fits the alphabetical order (IF 62 < LEN 77 < MAX 84).

## Confidence

*Likely*: node 19 is a text literal, and LEN is function 77.
