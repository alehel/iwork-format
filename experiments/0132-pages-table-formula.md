# 0132: A formula in a Pages table

**Status:** run

[0026](0026-numbers-cells.md) found that Numbers stores cells exactly as Pages did when typing in the window. This experiment, one of eight (0131–0138) that repeat Numbers findings in the other apps, asks: are formulas in a Pages table stored like Numbers'?

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0031](0031-cell-kinds.md) |

## Recipe

```bash
mkdir -p samples/0132
osascript recipes/0131-app-table.applescript Pages "$PWD/samples/0132/formula.pages" formula
```

The recipe makes a 5 × 5 table through Pages's AppleScript, using the same table commands as Numbers'.

## Observation

The recipe puts 4 in B2, 2 in C2 and `=B2*C2` in E2. The table's formula list has one entry with the nodes `36 36 3`: two cell references and a multiplication.

## Conclusion

Pages tables store formulas in the same postfix node format as Numbers, in the same kind of formula list.

## Confidence

*Likely*: formulas are stored the same way in Pages and Numbers.
