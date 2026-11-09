# 0184: A footer row

**Status:** run

The table model's field 11 was thought to be the number of footer rows ([0060](0060-header-rows.md)), but no sample had a footer row. This experiment adds one.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0181/plain.numbers`, a new document |

## Recipe

```bash
mkdir -p samples/0184
osascript recipes/0181-numbers-table-options.applescript footer "$PWD/samples/0184/footer.numbers"
```

The recipe sets `footer row count` of table 1 to 1, then B10 to 7.

## Observation

The table model (type 6001) gains field 11 with the value 1, between fields 10 and 12. The row count (field 6) stays 22. The tile holds B10 as an ordinary number cell.

## Conclusion

Field 11 of the table model is the number of footer rows, and they are counted within the table's rows: here the last of the 22. A new table has no footer rows and leaves the field out.

## Confidence

*Likely*: field 11 is the number of footer rows, part of the row count.
