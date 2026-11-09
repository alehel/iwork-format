# 0174: A negative number

**Status:** run

[0112](0112-unary-minus.md) found a negative formula result stored with the decimal128 sign bit. This experiment types a negative number directly.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0026](0026-numbers-cells.md) |

## Recipe

```bash
mkdir -p samples/0174
osascript recipes/0169-numbers-controls.applescript negative "$PWD/samples/0174/negative.numbers"
```

Cell B2 of table 1 is decoded from `Index/Tables/Tile.iwa` as in [0036](0036-more-cell-formats.md).

## Observation

B2 is a number cell with flags 0x00003001 (number, then two format keys). Its decimal128 has the coefficient 5 and the top byte `b0` where a positive number has `30`.

## Conclusion

A negative number is stored with the decimal128 sign bit (bit 127) set, whether it's typed or a formula's result.

## Confidence

*Confirmed*: negative decimal128 numbers have the sign bit set ([0112](0112-unary-minus.md) and this experiment).
