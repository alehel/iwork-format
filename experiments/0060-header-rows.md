# 0060: Header and footer rows

**Status:** run

This experiment changes a Numbers table's header rows, header columns and footer rows, to find where their counts are kept.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0024](0024-keynote-and-numbers.md), `empty-a.numbers` (1 header row, 1 header column, no footer row) |

## Recipe

```bash
mkdir -p samples/0060
osascript recipes/0060-numbers-headers.applescript "$PWD/samples/0060/headers.numbers"
```

The recipe sets the first table's `header row count` to 2, `header column count` to 0 and `footer row count` to 1.

## Observation

Of the table model's (type 6001) top-level numeric fields, only these changed:

| Field | Empty | After |
| --- | --- | --- |
| 9 | 1 | 2 |
| 10 | 1 | absent |
| 11 | absent | 1 |

## Conclusion

Table model field 9 is the number of header rows, field 10 the number of header columns, and field 11 the number of footer rows. A field left out means 0. In Pages' table of [0020](0020-a-table.md), field 9 was 1, which fits its single header row.

## Confidence

*Likely*: table model fields 9, 10 and 11 are the header row, header column and footer row counts.
