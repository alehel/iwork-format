# 0181: The numeral system format

**Status:** run

[0036](0036-more-cell-formats.md) mapped the format kinds of number, currency, percent, scientific, text, date, fraction, checkbox, rating and duration cells. This experiment sets the one kind AppleScript offers that hadn't been tried: the numeral system format, which shows a number in another base.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `plain.numbers`, a new document from the same recipe |

## Recipe

```bash
mkdir -p samples/0181
osascript recipes/0181-numbers-table-options.applescript numeral "$PWD/samples/0181/numeral.numbers"
osascript recipes/0181-numbers-table-options.applescript plain "$PWD/samples/0181/plain.numbers"
```

The recipe sets the format of B2 in table 1 to `numeral system`, then its value to 10.

## Observation

B2 in `Index/Tables/Tile.iwa` is a number cell (type 2) with flags 0x00003001: the decimal128 10, then the keys 1 and 1. The format list (`DataList-904541.iwa`, list type 2), empty in `plain.numbers`, now has one entry:

```
key 1: { 6: { 1: 269, 8: 10, 9: 0, 10: 1 } }
```

## Conclusion

The numeral system format is format kind 269. Field 8 is most likely the base, 10 by default. Fields 9 and 10 are probably the number of places and how negative numbers are shown, which the app's Format inspector offers as options. The cell's value is an ordinary number, so a reader that doesn't know the format can still show 10.

## Confidence

*Likely*: format kind 269 is the numeral system.

*Unknown*: the meaning of fields 8, 9 and 10. Follow-up: change the base and places in the Format inspector.
