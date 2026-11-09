# 0135: A formula in a Keynote table

**Status:** run

[0026](0026-numbers-cells.md) found that Numbers stores cells exactly as Pages did when typing in the window. This experiment, one of eight (0131–0138) that repeat Numbers findings in the other apps, asks: are formulas in a Keynote table stored like Numbers'?

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0132](0132-pages-table-formula.md) |

## Recipe

```bash
mkdir -p samples/0135
osascript recipes/0131-app-table.applescript Keynote "$PWD/samples/0135/formula.key" formula
```

The recipe makes a 5 × 5 table through Keynote's AppleScript, using the same table commands as Numbers'.

## Observation

The recipe puts 4 in B2, 2 in C2 and `=B2*C2` in E2. The formula list has one entry with the nodes `36 36 3`.

## Conclusion

Keynote tables store formulas in the same node format as Pages and Numbers.

## Confidence

*Confirmed*: formulas are stored the same way in all three apps ([0132](0132-pages-table-formula.md) and this experiment).
