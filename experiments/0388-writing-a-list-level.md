# 0388: Writing a list level

**Status:** run

A list paragraph's level is in run table 6 of its text: entries at paragraph starts whose field 2 is the level, 0 for the first ([0015](0015-list-levels.md)). This experiment writes other levels and measures where Pages draws the paragraphs.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/0015/nested-list.pages`: the dash list `One`, `Two`, `three` in text 1732539. Table 6 has an entry at 0 with level 0 and one at 4, the start of `Two`, with level 1, which also covers `three` |
| Writer | [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and measured with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift) |

## Recipe

```bash
mkdir -p samples/0388
N=recipes/0383-set-nth-path.py
F=samples/0015/nested-list.pages
O=samples/0388
cp $F $O/original.pages
for v in 0 2 4; do
  python3 -I $N $F $O/level-$v.pages 1732539 6.1:2.2 varint $v
done
for f in original level-0 level-2 level-4; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
done
swift recipes/0319-measure-pdf.swift $O/*.pdf
```

## Observation

The left edge of the ink on each line, marker included, in points:

| File | Level written at 4 | `One` | `Two` | `three` |
| --- | --- | --- | --- | --- |
| `level-0.pages` | 0 | 57.5 | 57.5 | 57.5 |
| `original.pages` | 1 | 57.5 | 69.5 | 69.5 |
| `level-2.pages` | 2 | 57.5 | 81.5 | 81.5 |
| `level-4.pages` | 4 | 57.5 | 105.5 | 105.5 |

## Conclusion

Field 2 of a table-6 entry is the list level of the paragraphs from that position to the next entry. Each level indents the paragraph, marker and all, a further 12 points in the Dash list style, so level 4 is 48 points in from level 0. A level the document never used before (2 and 4 here) is drawn too, so the list style holds settings for every level.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0015/nested-list.pages` | `same bytes`, `2001#1732539 6.1.2 = 1` | *Control*: level 1 is drawn 12 points further in than level 0 |
| `level-0.pages` | `original.pages` | Only `2001#1732539 6.1.2 ≠ 1` | *Confirmed*: level 0: all three paragraphs have the same left edge |
| `level-2.pages` | `original.pages` | Only `2001#1732539 6.1.2: 1 → 2` | *Confirmed*: level 2 is drawn 24 points in |
| `level-4.pages` | `original.pages` | Only `2001#1732539 6.1.2: 1 → 4` | *Confirmed*: level 4 is drawn 48 points in |

## Confidence

*Confirmed*: run table 6's field 2 as the list level, by writing it.
