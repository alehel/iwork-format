# 0133: Merged cells in a Pages table

**Status:** run

[0026](0026-numbers-cells.md) found that Numbers stores cells exactly as Pages did when typing in the window. This experiment, one of eight (0131–0138) that repeat Numbers findings in the other apps, asks: are merged cells in Pages recorded as in Numbers?

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0044](0044-merged-cells.md) |

## Recipe

```bash
mkdir -p samples/0133
osascript recipes/0131-app-table.applescript Pages "$PWD/samples/0133/merge.pages" merge
```

The recipe makes a 5 × 5 table through Pages's AppleScript, using the same table commands as Numbers'.

## Observation

The recipe merges B2:C3 and puts 42 in B2. The table model's field 47.2 has the count 1 and a range expression: a range node (67) with a UUID-like field 28, the four flags of field 33 set to 1, and fields 40.3 and 40.4, as in 0044.

## Conclusion

Pages records merges like Numbers, in table model field 47.2.

## Confidence

*Confirmed*: merges are recorded in table model field 47.2 ([0044](0044-merged-cells.md) and this experiment).
