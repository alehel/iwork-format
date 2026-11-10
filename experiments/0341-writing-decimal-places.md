# 0341: Writing a format's decimal places

**Status:** run

Number and percent formats in the format list share a layout: kind in field 1, field 2 = 253, and fields 4 and 5 = 0 ([0031](0031-cell-kinds.md)). [0339](0339-writing-a-currency-format.md) found field 2 to be a currency format's decimal places. This experiment writes fields 2, 4 and 5 of a percent format and reads how Numbers shows its cell.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0031/kinds.numbers`: C2 holds 0.25, shown as `25 %` through format key 3: kind 258, 2 = 253, 4 = 0, 5 = 0 |
| Writer | [`recipes/0339-format-field.py`](../recipes/0339-format-field.py) |

## Recipe

```bash
mkdir -p samples/0341
cp samples/0031/kinds.numbers samples/0341/original.numbers
R=recipes/0339-format-field.py
python3 -I $R samples/0341/original.numbers samples/0341/pct2.numbers 3 2 varint 2
python3 -I $R samples/0341/original.numbers samples/0341/pct-f4.numbers 3 4 varint 1
python3 -I $R samples/0341/original.numbers samples/0341/pct-f5.numbers 3 5 varint 1
```

Numbers opened each file on its own and read C2 through AppleScript.

## Observation

| File | C2 shown as |
| --- | --- |
| `original.numbers` (2 = 253) | `25 %` |
| `pct2.numbers` (2 = 2) | `25,00 %` |
| `pct-f4.numbers` (4 = 1) | `25 %` |
| `pct-f5.numbers` (5 = 1) | `25 %` |

## Conclusion

Field 2 is the number of decimal places in number-like formats too, and 253 means automatic: as many as the value needs. Fields 4 and 5 had no visible effect on a small positive value; they may control negative numbers or the thousands separator, which this value can't show.

## Confidence

*Confirmed*: field 2 is the decimal places, 253 automatic.

*Unknown*: fields 4 and 5, since found to be the negative style and the thousands separator ([0342](0342-negative-numbers-and-thousands.md)).
