# 0323: A sweep of format kinds

**Status:** run

The format list's kinds were read one at a time: 256 number, 257 currency, 258 percent, 259 scientific, 260 text, 261 date, 262 fraction, 263 checkbox, 267 rating, 268 duration and 269 numeral system ([0036](0036-more-cell-formats.md), [0181](0181-numeral-system.md)), and [0307](0307-writing-a-format.md) confirmed 258 by writing it. This experiment writes every kind from 250 to 280 into one format and reads how Numbers shows the value 1.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, started in English |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0226/plain.numbers`: B2 holds 1 and uses format key 2, whose other fields are 2 = 253, 4 = 0 and 5 = 0 |
| Script | [`recipes/0323-format-sweep.sh`](../recipes/0323-format-sweep.sh), using [`recipes/0307-format-kind.py`](../recipes/0307-format-kind.py) |

## Recipe

```bash
mkdir -p samples/0323
zsh recipes/0323-format-sweep.sh 250 280 "$PWD/samples/0323/kinds.tsv"
```

For each kind, the script writes it into format key 2, opens the file in Numbers through Launch Services and reads B2's `formatted value`, `format` and `value`. The results are in [`recipes/0323-format-kinds.tsv`](../recipes/0323-format-kinds.tsv).

## Observation

| Kind | B2 shown as |
| --- | --- |
| 258 | `100 %` |
| 259 | `1E+00` |
| 262 | `2` |
| 267 | `1 ★` |
| 269 | `1E+00` |
| All others, 250–257, 260, 261, 263–266, 268, 270–280 | `1` |

The value stayed 1, and AppleScript's `format` stayed `automatic`, in every case.

## Conclusion

The kinds that need nothing but the kind show themselves: 258 percent, 259 scientific and 267 rating. Currency, date, duration, checkbox and the others need settings of their own, such as a currency code or a date pattern, which this format doesn't have, so they fall back to showing the plain number. Kind 262 showing `2` and 269 showing scientific notation are probably the fraction and numeral-system formats misreading this format's fields, which belong to a number format, but that wasn't tested. Kinds outside 256 to 269 aren't formats Numbers knows.

## Confidence

*Confirmed*: 258 percent, 259 scientific and 267 rating, by writing them.

*Unknown*: what 262 and 269 make of a number format's settings.
