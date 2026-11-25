# 0417: Writing the objects on a sheet

**Status:** run

A Numbers sheet (type 2) lists its drawables in order in its repeated field 2: tables, text boxes, shapes and images ([0047](0047-second-table.md), [0127](0127-text-box-on-sheet.md)). This experiment reorders the list and drops an entry, and reads the tables through AppleScript and the exported sheet.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0047/two-tables.numbers`: sheet 904532 lists two tables, `Tabell 1` at (0, 28) and `Second` at (0, 548) |
| Writer | [`recipes/0416-reorder.py`](../recipes/0416-reorder.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0417
X=recipes/0416-reorder.py
F=samples/0047/two-tables.numbers
O=samples/0417
cp $F $O/original.numbers
python3 -I $X $F $O/reversed.numbers 904532 2 2,1
python3 -I $X $F $O/first-only.numbers 904532 2 1
for f in original reversed first-only; do
  sh recipes/0372-in-app.sh Numbers $O/$f.numbers "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
set out to {}
repeat with t in tables of sheet 1 of d
  set end of out to {name of t, position of t}
end repeat
return out"
done
```

## Observation

| File | Field 2 written | `tables`, in order | Table names in the PDF |
| --- | --- | --- | --- |
| `original.numbers` | | Tabell 1 (0, 28), Second (0, 548) | Tabell 1, Second |
| `reversed.numbers` | reversed | Second (0, 548), Tabell 1 (0, 28) | Tabell 1, Second |
| `first-only.numbers` | the first only | Tabell 1 (0, 28) | Tabell 1 |

## Conclusion

Field 2 decides which objects are on a sheet and in what order Numbers lists them; each object keeps its own position, so the drawing reads top to bottom the same whichever comes first. The list's order is probably the stacking order, as on a page, which overlapping objects would show. An object left out of the list isn't on the sheet, though its records remain.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.numbers` | `0047/two-tables.numbers` | `same bytes` | *Control* |
| `reversed.numbers` | `original.numbers` | Only `2#904532 2: changed`, the two entries the other way round | *Confirmed*: Numbers lists `Second` first; both tables keep their places |
| `first-only.numbers` | `original.numbers` | Only `2#904532 2: ×2 → ×1`, `2#904532 2.1 ≠ 905254` | *Confirmed*: a table left out of field 2 isn't on the sheet |

## Confidence

*Confirmed*: sheet field 2 as the list of the sheet's objects, in order, by writing it. *Likely*: the order is the stacking order.
