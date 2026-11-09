# 0137: A currency cell in Keynote

**Status:** run

[0026](0026-numbers-cells.md) found that Numbers stores cells exactly as Pages did when typing in the window. This experiment, one of eight (0131–0138) that repeat Numbers findings in the other apps, asks: is a currency cell in Keynote stored like Numbers'?

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0031](0031-cell-kinds.md), cell B2 |

## Recipe

```bash
mkdir -p samples/0137
osascript recipes/0131-app-table.applescript Keynote "$PWD/samples/0137/currency.key" currency
```

The recipe makes a 5 × 5 table through Keynote's AppleScript, using the same table commands as Numbers'.

## Observation

The recipe puts 42 in B2 and sets its format to currency. The cell's bytes are

```
05 0a 00 00 00 00 02 08 01 50 00 00 <42 as decimal128> 02 00 00 00 02 00 00 00
```

They are identical to Numbers' currency cell in 0031. The format list has an entry with kind 257 and the currency `NOK`.

## Conclusion

Keynote stores a currency cell like Numbers: type 10, flags 0x5001 and a format-list entry of kind 257. Its bytes 6–7 are `02 08`, as in Numbers.

## Confidence

*Confirmed*: currency cells are type 10 with a kind-257 format ([0031](0031-cell-kinds.md) and this experiment).
