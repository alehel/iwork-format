# 0301: Writing a table's header and footer rows

**Status:** run

The table model's fields 9 to 13 were read as the numbers of header rows, header columns and footer rows, and whether header rows and columns are frozen ([0120](0120-fewer-rows.md), [0125](0125-unfrozen-headers.md), [0183](0183-unfrozen-header-columns.md), [0184](0184-footer-row.md)). Numbers' AppleScript can read all five. This experiment writes new values into a file and asks Numbers.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0226/plain.numbers`: one table of 22 rows and 7 columns, with one header row and one header column, both frozen |
| Writer | [`recipes/0300-set-field.py`](../recipes/0300-set-field.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0301
python3 -I recipes/0300-set-field.py samples/0226/plain.numbers samples/0301/headers.numbers 6001 9=2 10=0 11=1 12=0
```

The table model (type 6001) had fields 9 = 1, 10 = 1 and 12 = 1, and no field 11. The script sets 2 header rows, 0 header columns, 1 footer row and unfrozen header rows, leaving field 13 (header columns frozen) at 1. Numbers then opened each file on its own, read the table's properties through AppleScript, and saved the written file again.

The first attempt opened the original first and then the written file: Numbers said the written file couldn't be opened at the moment, because the operation wasn't permitted, while the original was still open. The written file is a copy of the original and shares its document ID ([container.md](../spec/container.md#the-package)). Opened alone, it worked.

## Observation

| | Original | Written |
| --- | --- | --- |
| header row count | 1 | 2 |
| header column count | 1 | 0 |
| footer row count | 0 | 1 |
| header rows frozen | true | false |
| header columns frozen | true | true |
| row count | 22 | 22 |

Saved again by Numbers, the model has fields 9 = 2, 11 = 1 and 13 = 1, and no fields 10 and 12: Numbers leaves out the fields that are 0.

## Conclusion

Fields 9, 10, 11 and 12 of the table model are what they were read as: header rows, header columns, footer rows, and whether header rows are frozen. Numbers writes a 0 in them by leaving the field out, so a reader must take an absent field as 0.

The apps seemed to refuse to open a document while another with the same document ID was open. [0302](0302-writing-a-transition.md) found refusals with no other document open, and that opening files through Launch Services (`open -a`) avoids them, so that explanation was wrong.

## Confidence

*Confirmed*: table model fields 9 to 12, by writing them.

The explanation of the refusals was withdrawn in [0302](0302-writing-a-transition.md).
