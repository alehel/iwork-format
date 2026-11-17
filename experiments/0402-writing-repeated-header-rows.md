# 0402: Writing repeated header rows

**Status:** run

A table model's field 29 is 1 when header rows repeat on each page; a new table in Pages has it, and turning the option off removes the field ([0246](0246-repeated-header-rows.md)). This experiment writes it both ways, then makes each table long enough to cross pages and counts the pages that show the header.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0246/plain-table.pages`: a new table with a header row, model 1732684, with field 29 = 1. `samples/0246/no-repeat.pages`: the same with the option turned off, model 1732707, without field 29 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) and [`recipes/0300-set-field.py`](../recipes/0300-set-field.py); then [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0402
O=samples/0402
cp samples/0246/plain-table.pages samples/0246/no-repeat.pages $O/
python3 -I recipes/0302-set-path.py $O/no-repeat.pages $O/repeat-written.pages 1732707 29 varint 1
python3 -I recipes/0300-set-field.py $O/plain-table.pages $O/repeat-off-written.pages 6001 29=0
for f in plain-table no-repeat repeat-written repeat-off-written; do
  cp $O/$f.pages $O/$f-grown.pages
  sh recipes/0372-in-app.sh Pages $O/$f-grown.pages "set t to table 1 of d
set row count of t to 70
set value of cell \"A1\" of t to \"HEAD\"
export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0374-pdf-text.swift $O/$f.pdf | grep -c HEAD
done
```

Growing the table and labelling its header cell are done through AppleScript after the file is opened, on a copy, since Pages may save such a change into the file.

## Observation

| File | Field 29 | Pages in the PDF | Pages showing `HEAD` |
| --- | --- | --- | --- |
| `plain-table.pages` | 1 (as made) | 3 | 3 |
| `no-repeat.pages` | absent (as made) | 3 | 1 |
| `repeat-written.pages` | 1, written | 3 | 3 |
| `repeat-off-written.pages` | 0, written | 3 | 1 |

## Conclusion

Field 29 = 1 makes a table's header rows repeat at the top of each page it reaches; written as 0, or absent, they appear only on the first. A reader laying out a long table over pages should repeat the header rows when the field is 1.

## Confidence

*Confirmed*: table model field 29 as repeating the header rows on each page, by writing it both ways.
