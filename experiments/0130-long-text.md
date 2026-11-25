# 0130: A long text in a cell

**Status:** run

This experiment puts a long text in a cell, to see whether long strings are split or stored elsewhere.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0130
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0130/longtext.numbers" longtext
```

## Observation

The recipe puts a text of 5000 characters (`abcdefghij` 500 times) in B2. The string table holds it whole, as one 5000-byte entry. The cell's bytes are those of a short text cell.

## Conclusion

Long texts are stored whole in the string table. A cell refers to them by key whatever their length.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `longtext.numbers` | `0024/empty-a.numbers` | `6005 3.3: ×0 → ×1`, `6005 3.3 ~ "abcdefghijabcdefghij"`, `6002 5.6 ~ x"050300000000000008100200010000000500000001000000"`; the string is 5000 bytes | *Likely*: a long text is stored whole, and its cell is like any text cell |

## Confidence

*Likely*: string-table entries aren't split, at least up to 5000 bytes.
