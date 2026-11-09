# 0114: A cleared cell

**Status:** run

This experiment puts text in a cell and clears it again, to see what is left behind.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0114
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0114/cleared.numbers" cleared
```

## Observation

The recipe puts `abc` in B2, then clears B2. The tile has no rows with cells, and the string table has no entries, but its next key is still 2.

## Conclusion

A cleared cell is removed from the tile, and a string no cell uses any more is removed from the string table. Its key isn't handed out again straight away, since the table's next key stays at 2. A reader never sees dangling strings.

## Confidence

*Likely*: unused strings are removed, and the next key isn't reset.
