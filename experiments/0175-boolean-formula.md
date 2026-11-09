# 0175: A formula with a boolean result

**Status:** run

[0110](0110-text-result.md) found that a formula cell keeps its last result as a value of the result's type. This experiment uses a comparison, whose result is a boolean.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0066](0066-comparisons-and-if.md) |

## Recipe

```bash
mkdir -p samples/0175
osascript recipes/0169-numbers-controls.applescript boolformula "$PWD/samples/0175/boolformula.numbers"
```

Cell B2 of table 1 is decoded from `Index/Tables/Tile.iwa` as in [0036](0036-more-cell-formats.md).

## Observation

B2's bytes:

```
05 06 00 00 00 00 00 00 02 12 04 00  00 00 00 00 00 00 f0 3f  01 00 00 00 06 00 00 00 02 00 00 00
```

Type 6 (boolean), flags 0x00041202: a double (1.0), a formula key, and two more keys. A checkbox's flags were 0x00041402: the same, but with a cell-control key (0x400) where this has a formula key (0x200). Numbers shows `SANN` (TRUE).

## Conclusion

A formula with a boolean result is a boolean cell holding the result as a double and the formula key. It has the boolean format (flag 0x40000) like a checkbox, but no control, so it shows as TRUE or FALSE, not as a checkbox.

## Confidence

*Likely*: boolean results are stored as type-6 cells with a double, like other formula results.
