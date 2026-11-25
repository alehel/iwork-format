# 0398: Header versions and extra payloads

**Status:** run

Header field 2.2 holds three packed varints, most often `1 0 5`, and Pages doesn't check it when opening ([0396](0396-writing-record-headers.md)). A few records have more than one payload ([0001](0001-empty-document.md)). This experiment surveys 2.2 and the extra payloads across all samples, and writes the extra payload of a chart.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | Every sample document on this machine for the survey; `samples/0224/donut.pages` for writing: a donut chart, record 1732688 (type 5021), whose 10000.1 is 25 (donut) and which has a second payload |
| Writer | The new [`recipes/0398-payload.py`](../recipes/0398-payload.py) and [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and drawn with [`recipes/0373-draw-pdf.swift`](../recipes/0373-draw-pdf.swift) |

## Recipe

```bash
mkdir -p samples/0398
X=recipes/0398-payload.py
N=recipes/0383-set-nth-path.py
F=samples/0224/donut.pages
O=samples/0398
cp $F $O/donut.pages
python3 -I $X $F $O/donut-no-extra.pages 1732688 2 drop
python3 -I $X $F $O/donut-extra-bar.pages 1732688 2 0801
python3 -I $N $F $O/donut-main-pie.pages 1732688 10000.1 varint 5
python3 -I $N $O/donut-no-extra.pages $O/pie-no-extra.pages 1732688 10000.1 varint 5
for f in donut donut-no-extra donut-extra-bar donut-main-pie pie-no-extra; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0373-draw-pdf.swift $O/$f.pdf 166 129 263 263 14
done
```

The chart is 263 × 263 at (166, 129).

## Observation

**Field 2.2.** Over all payloads of all samples, 2.2 depends only on the record's type:

| 2.2 | Payloads | Types |
| --- | --- | --- |
| 1, 0, 5 | 610,186 | most types |
| 10, 1, 0 | 37,707 | 3097 (placeholders), 633 and 634 (captions and titles) |
| 3, 2, 10 | 8,156 | 4008, 6005, 6001, 6316–6318 (the calculation engine and tables) |
| 2, 4, 0 and 2, 0, 0 | 5,724 each | 6247, the first and second payloads of the same records |
| 11, 2, 4 | 488 | 184 and 185 |
| 1, 1, 0 | 415 | 10016 |
| 65535, 65535, 4294967295 | 905 | type 0, the extra payloads below |

**Extra payloads.** Besides the type-6247 records, two kinds of record have extra payloads of type 0: Numbers' view state (type 12026, with three) and Pages' donut and radar charts (type 5021, with one). An extra payload's header has 2.2 = 65535, 65535, 4294967295, and fields not seen elsewhere: 7 (0), 8 (three varints, such as 2, 3, 4294967295 or 11, 1, 4294967295), 9 (in the charts, `{ 1: [10000] }`, a field path), 10 (10, 1, 28, in the view state) and 11 (2, 0, 25, the main payload's own 2.2). The donut's extra payload is `{ 1: 5 }`, and the radar's `{ 1: 2 }`, while their main payloads have 10000.1 = 25 (donut) and 27 (radar).

**Writing the donut:**

```
donut, donut-no-extra, donut-extra-bar    donut-main-pie, pie-no-extra
..oooo.......oooo..                       ..ooooooooooooooo..
.ooo..........ooo..                       .oooooooooooooooo..
.oo.............oo.                       .ooooooooooooooooo.
ooo.............ooo                       ooooooooooooooooooo
................ooo                       .........oooooooooo
...............ooo.                       ....oooooooooooooo.
..oooo.......oooo..                       ..ooooooooooooooo..
```

(Seven of the thirteen rows drawn; `o` is coloured, `.` white. The white wedge on the pie's left is its palest slice.) All three files on the left drew the same donut, including the one whose extra payload was rewritten as `{ 1: 1 }`. Writing 5 into the main payload's 10000.1 drew a pie, with or without the extra payload.

## Conclusion

Field 2.2 is fixed for each record type, so it reads as the version of that type's layout. It rises for types that changed more often, such as the placeholders at 10, 1, 0. Pages 15.4 doesn't check it ([0396](0396-writing-record-headers.md)).

An extra payload of type 0 is ignored by Pages 15.4. The donut's main payload already holds its type, 25, and the extra one holds 5, a pie: the nearest type that existed before donuts. Its header names a place in the main payload (9, the path 10000) and versions (8 and 11). So it is most likely a fallback for older versions of the apps, which would put 5 into 10000.1 in place of a type they don't know. A reader for current documents can skip payloads of type 0 and read the first payload.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `donut.pages` | `0224/donut.pages` | `same bytes`, `5021#1732688 10000.1 = 25`, `0#1732688 1 = 5`, `header 0#1732688 2 = x"ffff03ffff03ffffffff0f"` | *Control*: a donut, with an extra payload |
| `donut-no-extra.pages` | `donut.pages` | Only `records 0: 1 → 0` | *Confirmed*: Pages ignores the extra payload: the same donut |
| `donut-extra-bar.pages` | `donut.pages` | Only `0#1732688 1: 5 → 1` | *Confirmed*: as above |
| `donut-main-pie.pages` | `donut.pages` | Only `5021#1732688 10000.1: 25 → 5`, `0#1732688 1 = 5` | *Likely*: the main payload's 10000.1 is the type Pages draws: a pie |
| `pie-no-extra.pages` | `donut-no-extra.pages` | Only `5021#1732688 10000.1: 25 → 5`, `records 0: 0 → 0` | *Confirmed*: the extra payload makes no difference: the same pie |

## Confidence

*Confirmed*: 2.2 is the same for every record of a type, across all samples, and Pages 15.4 ignores a type-0 extra payload, by writing it. *Likely*: an extra payload is a fallback for older versions, placed at the path in its field 9.
