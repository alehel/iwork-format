# 0338: Writing a checkbox cell

**Status:** run

A boolean cell (type 6) was read as holding a double after its flags (flag 0x2): 1.0 for true and 0.0 for false, for a checkbox or a formula's result ([0036](0036-more-cell-formats.md), [0169](0169-unchecked-checkbox.md)). This experiment writes a checked box's value as 0.0 and asks Numbers.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0036/formats.numbers`: B2 is a checked checkbox, shown as `SANN` (true) |
| Writer | [`recipes/0338-cell-double.py`](../recipes/0338-cell-double.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0338
cp samples/0036/formats.numbers samples/0338/original.numbers
python3 -I recipes/0338-cell-double.py samples/0338/original.numbers samples/0338/unchecked.numbers 1 1 0
```

The script finds B2 (row 1, column 1 from 0) and replaces the double after its prefix, 1.0, with 0.0. Numbers opened each file on its own and read B2 through AppleScript.

## Observation

| File | B2 shown as | AppleScript value |
| --- | --- | --- |
| `original.numbers` | `SANN` | true |
| `unchecked.numbers` | `USANN` | false |

## Conclusion

A boolean cell's value is the double after its prefix: 0.0 is false, and Numbers shows the checkbox unchecked. Nothing else in the cell or its control changes between the two.

## Confidence

*Confirmed*: boolean cell values, by writing one.
