# 0416: Writing the order of sheets

**Status:** run

A Numbers document root (object 1) lists its sheets in order in field 1 ([0037](0037-second-sheet.md)). Keynote's show order is a similar list, confirmed by writing it ([0378](0378-writing-slide-order.md)). This experiment reorders the sheets and reads them through AppleScript.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0037/two-sheets.numbers`: the sheets `Ark 1` and `Second`, the second active, listed in that order in field 1 of object 1 |
| Writer | The new [`recipes/0416-reorder.py`](../recipes/0416-reorder.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0416
X=recipes/0416-reorder.py
F=samples/0037/two-sheets.numbers
O=samples/0416
cp $F $O/original.numbers
python3 -I $X $F $O/reversed.numbers 1 1 2,1
python3 -I $X $F $O/second-only.numbers 1 1 2
for f in original reversed second-only; do
  sh recipes/0372-in-app.sh Numbers $O/$f.numbers 'set out to {}
repeat with s in sheets of d
  set end of out to name of s
end repeat
return {out, name of active sheet of d}'
done
```

## Observation

| File | Field 1 written | Sheets | Active |
| --- | --- | --- | --- |
| `original.numbers` | | Ark 1, Second | Second |
| `reversed.numbers` | reversed | Second, Ark 1 | Second |
| `second-only.numbers` | `Second` only | Second | Second |

## Conclusion

The order of field 1 is the order of the sheets, and a sheet left out of it isn't part of the document, though its records are still in the file, just as with Keynote's slides. The active sheet is kept by identity, not position: `Second` stayed active when it moved first.

## Confidence

*Confirmed*: field 1 of a Numbers document root as its sheets in order, by writing it.
