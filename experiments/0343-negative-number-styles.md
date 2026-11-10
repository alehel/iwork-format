# 0343: The negative-number styles

**Status:** run

[0342](0342-negative-numbers-and-thousands.md) found that a number format's field 4 = 1 shows a negative number without its minus sign, probably in red, which AppleScript can't show. This experiment writes each value from 0 to 3 and checks both the text and, on an exported PDF, the colour.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0342/negative.numbers`: B2 holds −12345 in format key 2 |
| Writer | [`recipes/0339-format-field.py`](../recipes/0339-format-field.py) |

## Recipe

```bash
mkdir -p samples/0343
for v in 0 1 2 3; do
  python3 -I recipes/0339-format-field.py samples/0342/negative.numbers samples/0343/neg$v.numbers 2 4 varint $v
done
```

Numbers opened each file on its own, read B2 through AppleScript, and exported the sheet as PDF. The PDF's page was drawn and its clearly red pixels (red above 0.6, green and blue below 0.35) counted.

## Observation

| Field 4 | B2 shown as | Red pixels |
| --- | --- | --- |
| 0 | `−12345` | 0 |
| 1 | `12345` | 619 |
| 2 | `(12345)` | 0 |
| 3 | `(12345)` | 771 |

## Conclusion

Field 4 of a number format is its negative style, Numbers' four choices: 0 a minus sign, 1 red without a sign, 2 in parentheses, 3 red in parentheses.

## Confidence

*Confirmed*: the four negative styles, by writing them.
