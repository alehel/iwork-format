# 0340: Writing a date format's pattern

**Status:** run

A date format is kind 261 in the format list, with a date pattern among its details ([0031](0031-cell-kinds.md)). In `samples/0031/kinds.numbers`, the date format (key 4) holds only field 1 = 261 and field 14 = `dd.MM.y HH:mm`. This experiment writes a new pattern into field 14 and reads how Numbers shows the date.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0031/kinds.numbers`: E2 holds 2026-01-02 12:00, shown as `02.01.2026 12:00` |
| Writer | [`recipes/0339-format-field.py`](../recipes/0339-format-field.py) |

## Recipe

```bash
mkdir -p samples/0340
cp samples/0031/kinds.numbers samples/0340/original.numbers
python3 -I recipes/0339-format-field.py samples/0340/original.numbers samples/0340/pattern.numbers 4 14 string "yyyy-MM-dd 'kl.' HH.mm"
```

Numbers opened each file on its own and read E2 through AppleScript.

## Observation

| File | E2 shown as |
| --- | --- |
| `original.numbers` | `02.01.2026 12:00` |
| `pattern.numbers` | `2026-01-02 kl. 12.00` |

## Conclusion

Field 14 of a date format is its pattern, in the Unicode date-pattern syntax that Apple's date formatters use: `yyyy`, `MM`, `dd`, `HH` and `mm`, with quoted literal text. Numbers shows any pattern written there, not only those its own menus offer.

## Confidence

*Confirmed*: date format field 14 is the pattern, by writing one.
