# 0131: Cells in a Pages table through AppleScript

**Status:** run

[0026](0026-numbers-cells.md) found that Numbers stores cells exactly as Pages did when typing in the window. This experiment, one of eight (0131–0138) that repeat Numbers findings in the other apps, asks: does a Pages table filled through AppleScript store cells identically to Numbers?

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0026](0026-numbers-cells.md), `cells.numbers` |

## Recipe

```bash
mkdir -p samples/0131
osascript recipes/0131-app-table.applescript Pages "$PWD/samples/0131/cells.pages" cells
```

The recipe makes a 5 × 5 table through Pages's AppleScript, using the same table commands as Numbers'.

## Observation

The recipe puts 42 in B2 and `abc` in C3. The decoded tile record has the SHA-1 `ec2d199f066c…`, the same as Numbers' in 0026 (and Pages' typed table in 0021, whose text was `Abc`, differs only in that string).

## Conclusion

Pages and Numbers produce byte-for-byte the same tile for the same cells, through AppleScript as through the window.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `cells.pages` | `0026/cells.numbers` | `6002 5.6 ~ x"0502000000000000013000002a0000000000000000000000000040300100000001000000"`, `6002 5.6 ~ x"050300000000000008100200010000000500000002000000"`; the tile is the same, byte for byte | *Confirmed*: Pages stores cells as Numbers does |

## Confidence

*Confirmed*: Pages and Numbers store cells identically ([0026](0026-numbers-cells.md) and this experiment).
