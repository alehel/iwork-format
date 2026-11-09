# 0183: Unfrozen header columns

**Status:** run

[0125](0125-unfrozen-headers.md) found that table-model field 12 says whether header rows are frozen. A new table also has field 13 set to 1. This experiment turns off frozen header columns, to see whether field 13 is their switch.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0181/plain.numbers`, a new document |

## Recipe

```bash
mkdir -p samples/0183
osascript recipes/0181-numbers-table-options.applescript frozencols "$PWD/samples/0183/frozencols.numbers"
```

The recipe sets `header columns frozen` of table 1 to false.

## Observation

In the table model (type 6001), field 13 changes from 1 to 0. Fields 9 and 10 (one header row and one header column) and field 12 (header rows frozen) keep their values.

## Conclusion

Field 13 of the table model says whether header columns are frozen (1) or not (0). It is the column counterpart of field 12. Unlike header rows in 0125, the field is kept with the value 0 rather than dropped.

## Confidence

*Likely*: field 13 is whether header columns are frozen.
