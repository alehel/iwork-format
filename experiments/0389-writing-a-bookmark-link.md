# 0389: Writing a bookmark and a link to it

**Status:** run

A bookmark is a type-2035 record placed by run table 15, identified by the UUID in its field 1.1. A link to it is a type-2039 smart field whose field 2 is `#` and that UUID ([0191](0191-bookmark.md), [0192](0192-link-to-bookmark.md)). Pages exports such a link to PDF as a link annotation that goes to a point on a page. This experiment moves the bookmark, changes the UUIDs, and reads the annotation's target.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/0192/bookmark-link.pages`: `one two` in text 1732539, with `one` linked (record 1732745) to a bookmark on `two` (record 1732700, placed at position 4 by run table 15) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) and [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift), which now prints a link's target |

## Recipe

```bash
mkdir -p samples/0389
R=recipes/0302-set-path.py
N=recipes/0383-set-nth-path.py
F=samples/0192/bookmark-link.pages
O=samples/0389
U=11111111-2222-3333-4444-555555555555
cp $F $O/original.pages
python3 -I $N $F $O/moved.pages 1732539 15.1:2.1 varint 2
python3 -I $R $F $O/link-elsewhere.pages 1732745 2 string "#$U"
python3 -I $R $O/link-elsewhere.pages $O/both-renamed.pages 1732700 1.1 string "$U"
for f in original moved link-elsewhere both-renamed; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
```

## Observation

Each PDF has one link annotation over `one` (57, 774, 18 × 12, from the page's bottom-left corner):

| File | Written | Link goes to |
| --- | --- | --- |
| `original.pages` | nothing | page 1 at 78, 785 (the start of `two`) |
| `moved.pages` | bookmark entry at position 2 instead of 4 | page 1 at 69, 785 (the `e` of `one`) |
| `link-elsewhere.pages` | link field 2 = `#` and a UUID no bookmark has | nowhere |
| `both-renamed.pages` | that UUID in the link and in bookmark field 1.1 | page 1 at 78, 785 |

## Conclusion

The bookmark is where its run-table-15 entry puts it: moving the entry moves the link's destination with it. The link finds its bookmark only by the UUID after the `#`: with no bookmark of that UUID it goes nowhere, and when both are renamed alike it works as before, so the UUID needn't be one Pages made.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0192/bookmark-link.pages` | `same bytes` | *Control*: the link goes to the start of the second word |
| `moved.pages` | `original.pages` | Only `2001#1732539 15.1.1: 4 → 2` | *Confirmed*: run table 15 places the bookmark: the link's destination moves with it |
| `link-elsewhere.pages` | `original.pages` | Only `2039#1732745 2: "#B3EA9C7C-BDCF-41C7-9E6B-E441FE2FEF95" → "#11111111-2222-3333-4444-555555555555"` | *Confirmed*: a link with a UUID no bookmark has goes nowhere |
| `both-renamed.pages` | `link-elsewhere.pages` | Only `2035#1732700 1.1: "B3EA9C7C-BDCF-41C7-9E6B-E441FE2FEF95" → "11111111-2222-3333-4444-555555555555"` | *Confirmed*: the UUIDs join a link to its bookmark: it works again |

## Confidence

*Confirmed*: run table 15 as a bookmark's position, bookmark field 1.1 as its UUID, and link field 2 as `#` and that UUID, by writing them.
