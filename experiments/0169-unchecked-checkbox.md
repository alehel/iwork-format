# 0169: An unchecked checkbox

**Status:** run

[0036](0036-more-cell-formats.md) stored a ticked checkbox as a double 1.0. This experiment stores an unticked one.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0036](0036-more-cell-formats.md), `formats.numbers` |

## Recipe

```bash
mkdir -p samples/0169
osascript recipes/0169-numbers-controls.applescript checkfalse "$PWD/samples/0169/checkfalse.numbers"
```

Cell B2 of table 1 is decoded from `Index/Tables/Tile.iwa` as in [0036](0036-more-cell-formats.md).

## Observation

Cell B2's bytes:

```
05 06 00 00 00 00 20 00 02 14 04 00  00 00 00 00 00 00 00 00  01 00 00 00 06 00 00 00 01 00 00 00
```

Type 6 (boolean) with the same flags as the ticked checkbox, 0x00041402, and the double 0.0. The cell-control list (list type 12) has one entry, whose 12.1 is 8; the format list's entry is 263 (checkbox). Numbers reads the cell back as `false`.

## Conclusion

An unticked checkbox is a boolean cell with the value 0.0, not an empty cell. The cell-control entry's kind 8 is a checkbox.

## Confidence

*Confirmed*: booleans are doubles, 1.0 true and 0.0 false ([0036](0036-more-cell-formats.md) and this experiment).

*Likely*: cell-control kind 8 is a checkbox.
