# 0113: The same text twice

**Status:** run

[0021](0021-table-cells.md) found that a text cell holds a key into the table's string table. This experiment puts the same text in two cells, to see whether the string is stored once.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0113
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0113/samestring.numbers" samestring
```

## Observation

The recipe puts `abc` in B2 and C2. Both cells hold string key 1. The string table has one entry, `{1: 1, 2: 2, 3: "abc"}`, and its next key (field 2 of the list) is 2.

## Conclusion

Equal texts share one string-table entry, and the entry's field 2 counts the cells that use it (2 here). So field 3.2 of an entry is a reference count, as 0021 guessed.

## Confidence

*Likely*: string-table entries are shared by equal texts, and field 3.2 counts their users.
