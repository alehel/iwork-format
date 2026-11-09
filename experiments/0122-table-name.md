# 0122: Renaming a table

**Status:** run

This experiment renames a table.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` |

## Recipe

```bash
mkdir -p samples/0122
osascript recipes/0113-numbers-variants.applescript "$PWD/samples/0122/tablename.numbers" tablename
```

## Observation

The recipe sets the table's name to `Budget`. Model field 8 changed from `Tabell 1` to `Budget`, and nothing else changed.

## Conclusion

Model field 8 is the table's name.

## Confidence

*Confirmed*: model field 8 is the name ([0020](0020-a-table.md) and this experiment).
