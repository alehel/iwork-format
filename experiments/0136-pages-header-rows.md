# 0136: Header rows in a Pages table

**Status:** run

[0026](0026-numbers-cells.md) found that Numbers stores cells exactly as Pages did when typing in the window. This experiment, one of eight (0131–0138) that repeat Numbers findings in the other apps, asks: is the header row count of a Pages table kept in the same field as in Numbers?

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0060](0060-header-rows.md) |

## Recipe

```bash
mkdir -p samples/0136
osascript recipes/0131-app-table.applescript Pages "$PWD/samples/0136/headers.pages" headers
```

The recipe makes a 5 × 5 table through Pages's AppleScript, using the same table commands as Numbers'.

## Observation

The recipe sets the header row count to 2. The table model has field 9 = 2, field 10 = 1 (one header column) and fields 6 and 7 = 5 (rows and columns).

## Conclusion

Pages keeps the header row count in model field 9, as Numbers does.

## Confidence

*Confirmed*: model field 9 is the header row count ([0060](0060-header-rows.md) and this experiment).
