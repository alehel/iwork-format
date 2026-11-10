# 0342: Writing a negative number, and the format's negative style and thousands separator

**Status:** run

A negative decimal128 has its sign bit set ([0112](0112-unary-minus.md), [0174](0174-negative-number.md)), and number formats have fields 4 and 5 whose meaning [0341](0341-writing-decimal-places.md) couldn't see on a small positive value. This experiment writes −12345 into a number cell, then sets each field on its format.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0226/plain.numbers`: B2 holds 1, in format key 2 (kind 256, 2 = 253, 4 = 0, 5 = 0) |
| Writers | [`recipes/0342-cell-number.py`](../recipes/0342-cell-number.py) for the value, [`recipes/0339-format-field.py`](../recipes/0339-format-field.py) for the format |

## Recipe

```bash
mkdir -p samples/0342
python3 -I recipes/0342-cell-number.py samples/0226/plain.numbers samples/0342/negative.numbers 1 1 -12345
R=recipes/0339-format-field.py
python3 -I $R samples/0342/negative.numbers samples/0342/f4.numbers 2 4 varint 1
python3 -I $R samples/0342/negative.numbers samples/0342/f5.numbers 2 5 varint 1
python3 -I $R samples/0342/negative.numbers samples/0342/f5-2.numbers 2 5 varint 2
```

The value is written as a coefficient of 12345 with exponent 0 and the sign bit, as bytes `… 40 B0`. Numbers opened each file on its own and read B2 through AppleScript.

## Observation

| File | B2 shown as | AppleScript value |
| --- | --- | --- |
| `negative.numbers` | `−12345` | −12345 |
| `f4.numbers` (4 = 1) | `12345` | −12345 |
| `f5.numbers` (5 = 1) | `−12 345` | −12345 |
| `f5-2.numbers` (5 = 2) | `−12 345` | −12345 |

## Conclusion

The sign bit makes a decimal128 negative, and Numbers reads −12345 as written. Field 4 of a number format is the negative-number style: 1 drops the minus sign, which fits Numbers' style that shows negatives in red without one; the colour can't be read through AppleScript. Field 5 turns on the thousands separator, and any non-zero value does.

## Confidence

*Confirmed*: negative decimal128s, and field 5 as the thousands separator, by writing them.

*Likely*: field 4 is the negative style, 1 being red without a sign (the colour not seen).
