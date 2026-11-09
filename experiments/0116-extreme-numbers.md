# 0116: Very large and very small numbers

**Status:** run

[0021](0021-table-cells.md) found numbers stored as decimal128. This experiment stores a very large and a very small number, to check the exponent.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0116
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0116/extremes.numbers" extremes
```

## Observation

The recipe puts 1E+20 in B2 and 0.000001 in C2. The cells' decimal128 values:

```
B2: coefficient 0x5AF3107A4000 = 100000000000000 (10^14), exponent field 0x304C → 6 → 10^14 × 10^6
C2: coefficient 0x038D7EA4C68000 = 1000000000000000 (10^15), exponent field 0x3016 → −21 → 10^15 × 10^−21
```

The exponent is the top bits of the last two bytes, shifted right by one, minus the bias 6176.

## Conclusion

Numbers keeps any number as a decimal128 with a coefficient of up to about 16 digits and an exponent. Both values here came from AppleScript doubles and were normalised to 15 significant digits, so a reader should decode the coefficient and exponent generally rather than expect a fixed scale.

## Confidence

*Confirmed*: numbers are decimal128 ([0021](0021-table-cells.md), [0026](0026-numbers-cells.md) and this experiment).
