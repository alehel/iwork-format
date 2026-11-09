# 0134: Cells in a Keynote table

**Status:** run

[0026](0026-numbers-cells.md) found that Numbers stores cells exactly as Pages did when typing in the window. This experiment, one of eight (0131–0138) that repeat Numbers findings in the other apps, asks: does a Keynote table store cells identically to Numbers?

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0026](0026-numbers-cells.md), `cells.numbers` |

## Recipe

```bash
mkdir -p samples/0134
osascript recipes/0131-app-table.applescript Keynote "$PWD/samples/0134/cells.key" cells
```

The recipe makes a 5 × 5 table through Keynote's AppleScript, using the same table commands as Numbers'.

## Observation

The recipe puts 42 in B2 and `abc` in C3. The decoded tile record has the SHA-1 `67e56451ad5e…`, the same as in Numbers (0026) and Pages (0131).

## Conclusion

All three apps store a table's cells byte for byte the same.

## Confidence

*Confirmed*: Keynote stores cells like Numbers and Pages.
