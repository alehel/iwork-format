# 0418: Writing a Numbers table's position

**Status:** run

A Numbers table's drawable (type 6000) holds its position in 1.1.1, and its stored y was 28 points less than the y Numbers reports ([0126](0126-table-at-origin.md)). This experiment writes positions and reads them back through AppleScript.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0226/plain.numbers`: one table, drawable 904769, stored at (0, 0.32), which AppleScript reports at (0, 28). Its name, `Tabell 1`, is shown above it: table model 904595 has field 22 = 1 ([0345](0345-writing-gridlines-and-title.md)) |
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
python3 -I $R $F $O/no-name.numbers 904595 22 varint 0
python3 -I $R $O/no-name.numbers $O/no-name-y-100.numbers 904769 1.1.1.2 float 100
for f in original y-100 x-50-y-0 y-minus-28 no-name no-name-y-100; do
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
| `no-name.numbers` | 0, 0.32, name hidden (22 = 0) | 0, 0 |
| `no-name-y-100.numbers` | 0, 100, name hidden | 0, 100 |

## Conclusion

The stored position is the top-left corner of the whole table object, including the name shown above it. AppleScript reports where the table's body starts: 28 points lower while the name is shown, and the stored position itself when the name is hidden. x is the same either way. So a reader placing a table should start its body 28 points below the stored y when field 22 shows the name, which is where the name is drawn.

## Confidence

*Confirmed*: the stored position as the table object's corner, with the body 28 points lower while the name is shown, by writing the position and the name's visibility.
