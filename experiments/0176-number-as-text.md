# 0176: A number typed as text

**Status:** run

This experiment sets a cell to the string `"123"` through AppleScript, to see whether Numbers keeps it as text.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0026](0026-numbers-cells.md) |

## Recipe

```bash
mkdir -p samples/0176
osascript recipes/0169-numbers-controls.applescript numtext "$PWD/samples/0176/numtext.numbers"
```

Cell B2 of table 1 is decoded from `Index/Tables/Tile.iwa` as in [0036](0036-more-cell-formats.md).

## Observation

B2 is a number cell (type 2), flags 0x00003001, holding the decimal128 123. Numbers reads it back as the number 123 with the format `automatic`. No string was added to the string table.

## Conclusion

Numbers converts text that looks like a number into a number, as when a user types it. A cell keeps digits as text only when its format is text, as in [0036](0036-more-cell-formats.md)'s F2 (`042`).

## Confidence

*Likely*: numeric-looking text in an automatic-format cell is stored as a number.
