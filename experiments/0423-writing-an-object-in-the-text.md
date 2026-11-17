# 0423: Writing an object's place in the text

**Status:** run

An object placed in the text, such as a table, is the character U+FFFC in the text with an entry in the attachment runs (field 9) at that position ([0020](0020-a-table.md)). This experiment moves the character and the entry, together and apart.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0020/table.pages`: the body (1732539) is `one` and U+FFFC, with one attachment entry at position 3 naming the table; Pages draws `one` and the table below it |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) and [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and measured with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift) |

## Recipe

```bash
mkdir -p samples/0423
R=recipes/0302-set-path.py
N=recipes/0383-set-nth-path.py
F=samples/0020/table.pages
O=samples/0423
cp $F $O/original.pages
python3 -I $R $F $O/x.pages 1732539 3 string "$(printf '\xef\xbf\xbcone')"
python3 -I $N $O/x.pages $O/table-first.pages 1732539 9.1:1.1 varint 0
rm $O/x.pages
python3 -I $R $F $O/char-moved-only.pages 1732539 3 string "$(printf '\xef\xbf\xbcone')"
python3 -I $N $F $O/entry-moved-only.pages 1732539 9.1:1.1 varint 0
for f in original table-first char-moved-only entry-moved-only; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
return {body text of d, count of tables of d}"
  swift recipes/0319-measure-pdf.swift $O/$f.pdf
done
```

## Observation

| File | Text | Entry at | `body text`, tables | `one` drawn at | Table drawn |
| --- | --- | --- | --- | --- | --- |
| `original.pages` | `one` U+FFFC | 3 | one, 1 | 60–66 | below `one` (bottom edge at 92.5) |
| `table-first.pages` | U+FFFC `one` | 0 | U+FFFC one, 1 | 175–181 | above `one` (from 79) |
| `char-moved-only.pages` | U+FFFC `one` | 3 | one, 1 | 60–66 | no |
| `entry-moved-only.pages` | `one` U+FFFC | 0 | one, 1 | 60–66 | no |

## Conclusion

An object in the text sits where its U+FFFC is, and only when an attachment entry sits at the same position: moving both put the table before the word, and moving either alone left the table undrawn, though Pages still counted it. In the mismatched files AppleScript's `body text` leaves the U+FFFC out, so Pages treats an unattached U+FFFC as nothing. A reader must pair each U+FFFC with the attachment entry at its position, and a writer must keep the two together.

## Confidence

*Confirmed*: an object in the text as a U+FFFC with an attachment entry at the same position, by writing them.
