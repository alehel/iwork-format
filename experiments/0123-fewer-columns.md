# 0123: Fewer columns

**Status:** run

This experiment changes the number of columns.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0123
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0123/fewercols.numbers" fewercols
```

## Observation

The recipe sets the column count to 3. Model field 7 changed from 7 to 3.

## Conclusion

Model field 7 is the number of columns.

## Confidence

*Confirmed*: model field 7 is the column count ([0020](0020-a-table.md) and this experiment).
