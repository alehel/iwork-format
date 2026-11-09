# 0171: A slider

**Status:** run

This experiment gives a cell the slider format.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0036](0036-more-cell-formats.md), `formats.numbers` |

## Recipe

```bash
mkdir -p samples/0171
osascript recipes/0169-numbers-controls.applescript slider "$PWD/samples/0171/slider.numbers"
```

Cell B2 of table 1 is decoded from `Index/Tables/Tile.iwa` as in [0036](0036-more-cell-formats.md).

## Observation

B2 is a number cell with flags 0x00003401, like the rating, holding the decimal128 50. The cell-control entry is:

```
12: { 1: 5, 3: 1.0, 4: 100.0, 5: 1.0 }
```

and the format list's entry is 256 (number), with a field 6.2 of 253.

## Conclusion

A slider is a number with control kind 5, ranging here from 1 to 100 in steps of 1. Unlike a rating, its number format is an ordinary one. The cell's flags are the same as for a rating, so only the control entry tells them apart.

## Confidence

*Likely*: cell-control kind 5 is a slider.
