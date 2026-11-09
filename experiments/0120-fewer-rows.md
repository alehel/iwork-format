# 0120: Fewer rows

**Status:** run

[0020](0020-a-table.md) read the number of rows from table model field 6. This experiment changes it.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0120
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0120/fewerrows.numbers" fewerrows
```

## Observation

The recipe sets the table's row count to 5. Model field 6 changed from 22 to 5. The drawable's size (494 × 231) didn't change.

## Conclusion

Model field 6 is the number of rows. As in [0059](0059-table-geometry.md), the drawable's stored size wasn't updated.

## Confidence

*Confirmed*: model field 6 is the row count ([0020](0020-a-table.md) and this experiment).
