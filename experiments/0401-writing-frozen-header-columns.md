# 0401: Writing frozen header columns

**Status:** run

A table model's field 13 says whether its header columns are frozen ([0183](0183-unfrozen-header-columns.md)). Fields 9 to 12 were confirmed by writing them, while field 13 was left at 1 ([0301](0301-writing-header-rows.md)). Numbers' AppleScript has `header columns frozen`. This experiment writes field 13.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0226/plain.numbers`: one table, model 904595, with one header row and one header column, both frozen (fields 9, 10, 12 and 13 all 1) |
| Writer | [`recipes/0300-set-field.py`](../recipes/0300-set-field.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0401
O=samples/0401
cp samples/0226/plain.numbers $O/original.numbers
python3 -I recipes/0300-set-field.py samples/0226/plain.numbers $O/columns-unfrozen.numbers 6001 13=0
python3 -I recipes/0300-set-field.py samples/0226/plain.numbers $O/two-columns-unfrozen.numbers 6001 10=2 13=0
for f in original columns-unfrozen two-columns-unfrozen; do
  sh recipes/0372-in-app.sh Numbers $O/$f.numbers 'set t to table 1 of sheet 1 of d
return {header column count of t, header columns frozen of t, header row count of t, header rows frozen of t}'
done
```

## Observation

| File | Fields written | Header columns | Frozen | Header rows | Frozen |
| --- | --- | --- | --- | --- | --- |
| `original.numbers` | | 1 | true | 1 | true |
| `columns-unfrozen.numbers` | 13 = 0 | 1 | false | 1 | true |
| `two-columns-unfrozen.numbers` | 10 = 2, 13 = 0 | 2 | false | 1 | true |

## Conclusion

Field 13 of the table model is whether the header columns are frozen, 1 for frozen, independently of field 12 for the header rows.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.numbers` | `0226/plain.numbers` | `same bytes`, `6001#904595 13 = 1` | *Control*: AppleScript says the header columns are frozen |
| `columns-unfrozen.numbers` | `original.numbers` | Only `6001#904595 13: 1 → 0` | *Confirmed*: field 13 is whether the header columns are frozen |
| `two-columns-unfrozen.numbers` | `original.numbers` | Only `6001#904595 10: 1 → 2`, `6001#904595 13: 1 → 0` | *Confirmed*: the same with two header columns |

## Confidence

*Confirmed*: table model field 13 as header columns frozen, by writing it.
