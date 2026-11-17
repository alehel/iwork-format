# 0418: Writing a Numbers table's position

**Status:** run

A Numbers table's drawable (type 6000) holds its position in 1.1.1, and its stored y was 28 points less than the y Numbers reports ([0126](0126-table-at-origin.md)). This experiment writes positions and reads them back through AppleScript.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0226/plain.numbers`: one table, drawable 904769, stored at (0, 0.32), which AppleScript reports at (0, 28) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0418
R=recipes/0302-set-path.py
F=samples/0226/plain.numbers
O=samples/0418
cp $F $O/original.numbers
python3 -I $R $F $O/y-100.numbers 904769 1.1.1.2 float 100
python3 -I $R $F $O/x-50-y-0.numbers 904769 1.1.1.1 float 50 1.1.1.2 float 0
python3 -I $R $F $O/y-minus-28.numbers 904769 1.1.1.2 float -28
for f in original y-100 x-50-y-0 y-minus-28; do
  sh recipes/0372-in-app.sh Numbers $O/$f.numbers 'return position of table 1 of sheet 1 of d'
done
```

## Observation

| File | Stored x, y | Reported x, y |
| --- | --- | --- |
| `original.numbers` | 0, 0.32 | 0, 28 |
| `y-100.numbers` | 0, 100 | 0, 128 |
| `x-50-y-0.numbers` | 50, 0 | 50, 28 |
| `y-minus-28.numbers` | 0, −28 | 0, 0 |

## Conclusion

AppleScript reports a Numbers table's position as the stored one moved down by 28 points, whatever the stored value, while x is reported as stored. The stored position is probably that of the table's body and the reported one that of the whole object with its name above it, which is shown in this table; or the reverse. Either way, a reader placing a table on a sheet should use the stored position consistently and remember the 28-point difference when comparing with AppleScript.

## Confidence

*Confirmed*: the reported y is the stored y plus 28, by writing it. *Unknown*: what the 28 points are.
