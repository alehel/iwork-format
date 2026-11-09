# 0126: A table at the origin

**Status:** run

[0059](0059-table-geometry.md) found a table's stored y 28 points less than the y Numbers reports. This experiment moves a table to (0, 0), to see whether the difference is a constant.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0126
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0126/origin.numbers" origin
```

## Observation

The recipe sets the table's position to (0, 0). The drawable's position (field 1.1.1) is (0, −28).

## Conclusion

The stored y of a Numbers table is 28 points less than the y Numbers reports, here as in 0059. The difference is constant, so it is probably room above the table for its name. A reader that places a table by its stored position should add 28 to y when the name is shown, though when exactly that applies isn't tested.

## Confidence

*Likely*: a table's stored y is 28 points less than its reported y.

*Unknown*: whether the offset depends on the table name being shown.
