# 0339: Writing a currency format

**Status:** run

The format list's entries give the kind of format in field 3.6.1 and its details after it, such as a currency code ([0031](0031-cell-kinds.md)). A currency format (kind 257) had fields 2 = 2, 3 = `NOK`, and 4, 5 and 6 = 0. This experiment writes field 3 and field 2 and reads how Numbers shows the cells.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0031/kinds.numbers`: B2 (42) and F2 (84, a formula) use format key 2, kind 257 |
| Writer | [`recipes/0339-format-field.py`](../recipes/0339-format-field.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0339
cp samples/0031/kinds.numbers samples/0339/original.numbers
python3 -I recipes/0339-format-field.py samples/0339/original.numbers samples/0339/usd.numbers 2 3 string USD
python3 -I recipes/0339-format-field.py samples/0339/original.numbers samples/0339/places0.numbers 2 2 varint 0
```

Numbers opened each file on its own and read B2 and F2 through AppleScript.

## Observation

| File | B2 | F2 |
| --- | --- | --- |
| `original.numbers` | `42,00 kr` | `84,00 kr` |
| `usd.numbers` (3 = `USD`) | `42,00 USD` | `84,00 USD` |
| `places0.numbers` (2 = 0) | `42 kr` | `84 kr` |

## Conclusion

In a currency format, field 3 is the ISO 4217 currency code and field 2 the number of decimal places. Numbers formats the code in the user's locale, so `NOK` appears as `kr` in Norwegian and `USD` as `USD`. Both cells use the same format entry, so one change reformats both.

## Confidence

*Confirmed*: currency format fields 2 (decimal places) and 3 (currency code), by writing them.
