# 0307: Writing a cell format

**Status:** run

Number cells hold a key into the table's format list, whose entries give the kind of format in field 3.6.1: 256 number, 258 percent and so on ([0031](0031-cell-kinds.md), [0036](0036-more-cell-formats.md)). This experiment changes the kind of the format that a table's number cells use, and asks Numbers how the cells look.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0226/plain.numbers`: column B holds 1, 2, 3 and 4, all pointing at format key 2, kind 256 |
| Writer | [`recipes/0307-format-kind.py`](../recipes/0307-format-kind.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0307
cp samples/0226/plain.numbers samples/0307/original.numbers
python3 -I recipes/0307-format-kind.py samples/0307/original.numbers samples/0307/percent.numbers 2 258
```

The format list (type 6005 in `DataList-904541.iwa`) has key 1, kind 260 (text), used by 6 cells, and key 2, kind 256, with 2 = 253 and 4 = 5 = 0, used by 4. The script changes key 2's kind to 258 and leaves its other fields. Numbers opened each file on its own and read B2 through AppleScript, and saved the written file again.

## Observation

| File | B2 value | B2 shown as | B2 format (AppleScript) |
| --- | --- | --- | --- |
| `original.numbers` | 1.0 | `1` | automatic |
| `percent.numbers` | 1.0 | `100 %` | automatic |

Saved again, key 2 has kind 258, with its other fields unchanged.

## Conclusion

The format list's kind decides how a number is shown: with 258 the same value 1 appears as `100 %`. AppleScript still calls the cell's format automatic in both files, so the format list holds the format Numbers resolved for display, not the inspector's choice of Automatic. Where that choice is stored isn't shown by this test.

## Confidence

*Confirmed*: format kind 258 is percent, and number cells show their format-list entry's kind.

*Unknown*: where a cell's Automatic setting is kept.
