# 0170: A rating of zero

**Status:** run

This experiment stores a rating of 0 stars, to see whether it differs from an empty cell.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0036](0036-more-cell-formats.md), `formats.numbers` |

## Recipe

```bash
mkdir -p samples/0170
osascript recipes/0169-numbers-controls.applescript rating0 "$PWD/samples/0170/rating0.numbers"
```

Cell B2 of table 1 is decoded from `Index/Tables/Tile.iwa` as in [0036](0036-more-cell-formats.md).

## Observation

B2 is a number cell (type 2) with flags 0x00003401 and the decimal128 0. The cell-control entry (list type 12) is:

```
12: { 1: 6, 3: 0.0, 4: 5.0, 5: 1.0 }
```

and the format list's entry is 267 (rating).

## Conclusion

A rating is a number with a control: kind 6, from 0 (field 3) to 5 (field 4) in steps of 1 (field 5). Zero stars is the number 0, so it isn't empty.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `rating0.numbers` | `0036/formats.numbers` | `6002 5.6 = x"05020000000001000134000000000000000000000000000000004030010000000100000001000000"`, `6005 3.12.1 = 6`, `6005 3.12.3 = 0.0`, `6005 3.12.4 = 5.0` | *Likely*: control kind 6 is a rating, from 0 to 5, and zero stars is the number 0 |

## Confidence

*Likely*: cell-control kind 6 is a rating, with its minimum, maximum and step in fields 3, 4 and 5.
