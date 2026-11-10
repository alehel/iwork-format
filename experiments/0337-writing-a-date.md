# 0337: Writing a date cell

**Status:** run

A date cell's value was read as a little-endian double after the cell's flags (flag 0x4): seconds since 2001-01-01 00:00, with the shown clock time counted as UTC ([0031](0031-cell-kinds.md)). This experiment writes a new date into a cell's bytes and asks Numbers.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84), in a time zone one hour ahead of UTC in winter |
| Date | 2026-11-10 |
| Input | `samples/0031/kinds.numbers`: E2 (row 1, column 4 from 0) shows `02.01.2026 12:00`, stored as 789048000 |
| Writer | [`recipes/0337-cell-date.py`](../recipes/0337-cell-date.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0337
cp samples/0031/kinds.numbers samples/0337/original.numbers
python3 -I recipes/0337-cell-date.py samples/0337/original.numbers samples/0337/written.numbers 1 4 920277000
```

920277000 seconds after 2001-01-01 00:00 is 2030-03-01 08:30. The script finds the cell's bytes through the row's offsets and replaces the double after the cell's 12-byte prefix. Numbers opened each file on its own and read E2 through AppleScript; the written file was saved again.

## Observation

| File | E2 shown as | AppleScript value |
| --- | --- | --- |
| `original.numbers` | `02.01.2026 12:00` | Friday 2 January 2026 12:00:00 |
| `written.numbers` | `01.03.2030 08:30` | Friday 1 March 2030 08:30:00 |

789048000 seconds is 2026-01-02 12:00 exactly, as shown.

## Conclusion

A date cell's value is the double after its prefix, in seconds since 2001-01-01 00:00. The clock time shown is that count read as UTC, with no shift for the Mac's time zone, so a writer stores the wall-clock time it wants to show.

## Confidence

*Confirmed*: date cells, by writing one.
