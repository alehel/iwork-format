# 0484: Writing an object's page

**Status:** run

Type 10010 lists the pages that have objects placed on them: each field-1 entry holds a page number from 0 in 1.1 and the objects on that page in 1.4 ([0482](0482-objects-on-later-pages.md)). This experiment writes the page numbers, and leaves an object out, to see which page Pages draws each object on.

## Setup

| | |
| --- | --- |
| Pages | 16.0 (7052.0.68) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-28 |
| Input | `0482/on-2-and-3.pages`: three pages; record 1732278 (type 10010) lists picture 1732688 on page 1 (the second page) and picture 1732695 on page 2 |
| Writer | [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py) and [`recipes/0416-reorder.py`](../recipes/0416-reorder.py); exported and saved again with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh), checked with [`recipes/0482-red-per-page.swift`](../recipes/0482-red-per-page.swift) |

## Recipe

```bash
mkdir -p samples/0484
S=$PWD/samples/0484
F=samples/0482/on-2-and-3.pages
X=recipes/0383-set-nth-path.py
python3 -I $X $F $S/first-to-page-1.pages 1732278 1:1.1 varint 0
python3 -I $X $F $S/second-to-page-1.pages 1732278 1:2.1 varint 0
python3 -I $X $F $S/second-to-page-4.pages 1732278 1:2.1 varint 3
python3 -I $X $F $S/second-to-page-9.pages 1732278 1:2.1 varint 8
python3 -I recipes/0416-reorder.py $F $S/second-unlisted.pages 1732278 1 1
for f in first-to-page-1 second-to-page-1 second-to-page-4 second-to-page-9 second-unlisted; do
  cp $S/$f.pages $S/tmp.pages
  sh recipes/0372-in-app.sh Pages $S/tmp.pages "set n to count of pages of d
export d to POSIX file \"$S/$f.pdf\" as PDF
save d in POSIX file \"$S/$f-resaved.pages\"
return {n, count of images of d}"
  swift recipes/0482-red-per-page.swift $S/$f.pdf
done
rm $S/tmp.pages
```

The page names below count from 1, as Pages shows them; the numbers written count from 0.

## Observation

| File | Written | Pages, images | Red drawn on | 10010 field 1 after Pages saved it |
| --- | --- | --- | --- | --- |
| `0482/on-2-and-3.pages` | 1 → 1732688, 2 → 1732695 | 3, 2 | pages 2 and 3 | |
| `first-to-page-1.pages` | 0 → 1732688, 2 → 1732695 | 3, 2 | pages 1 and 3 | as written |
| `second-to-page-1.pages` | 1 → 1732688, 0 → 1732695 | 3, 2 | pages 1 and 2 | 0 → 1732695, 1 → 1732688 |
| `second-to-page-4.pages` | 1 → 1732688, 3 → 1732695 | 3, 2 | page 2 only | as written |
| `second-to-page-9.pages` | 1 → 1732688, 8 → 1732695 | 3, 2 | page 2 only | as written |
| `second-unlisted.pages` | 1 → 1732688 | 3, 1 | page 2 only | as written |

Each picture moved to the page written, at the same place on that page: (286.8, 397.5) on page 1 in `first-to-page-1.pages`, for example, where it had been on page 2. Pages kept every entry it could, and put the entries of `second-to-page-1.pages` back in page order when it saved.

In `second-to-page-4.pages` and `second-to-page-9.pages`, Pages added no pages and drew the picture nowhere, but kept it: AppleScript counted two images, and the saved copy keeps the entry with page 3 or 8 and the picture in type 10015. In `second-unlisted.pages`, the picture is still in type 10015 but not drawn, and AppleScript counted one image.

## Conclusion

The page an object placed on the page is drawn on is the page number of the 10010 entry that lists it, counted from 0 at the start of the document. Its position in drawable field 1.1.1 is from that page's top-left corner, so changing the page number alone moves the object to the same spot on another page. Entries out of page order are read correctly, and Pages sorts them when it saves.

A page number past the last page doesn't add pages or move the object to the last page. Pages keeps the object, and the number, but doesn't draw it. An object in type 10015 but in no 10010 entry isn't drawn either, and AppleScript doesn't count it as an image; it is the same as an object left out of 10015 ([0424](0424-writing-the-page-objects-list.md)). A writer must list every placed object in both records.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `first-to-page-1.pages` | `0482/on-2-and-3.pages` | Only `10010#1732278 1.1: 1 → 0` | *Confirmed*: the entry's page number decides the page, counted from 0 |
| `first-to-page-1-resaved.pages` | `first-to-page-1.pages` | `10010#1732278 1.1 = 0`, `10010#1732278 1.1 = 2` | *Control*: Pages keeps the written page |
| `second-to-page-1.pages` | `0482/on-2-and-3.pages` | Only `10010#1732278 1.1: 2 → 0` | *Confirmed*: entries out of page order are read correctly |
| `second-to-page-1-resaved.pages` | `second-to-page-1.pages` | `10010#1732278 1: changed` | *Likely*: Pages puts the entries in page order |
| `second-to-page-4.pages` | `0482/on-2-and-3.pages` | Only `10010#1732278 1.1: 2 → 3` | *Confirmed*: past the last page, the object isn't drawn and no page is added |
| `second-to-page-4-resaved.pages` | `second-to-page-4.pages` | `10010#1732278 1.1 = 3` | *Likely*: Pages keeps the number |
| `second-to-page-9.pages` | `0482/on-2-and-3.pages` | Only `10010#1732278 1.1: 2 → 8` | *Confirmed*: as for one page past the end |
| `second-to-page-9-resaved.pages` | `second-to-page-9.pages` | `10010#1732278 1.1 = 8` | *Likely*: Pages keeps the number |
| `second-unlisted.pages` | `0482/on-2-and-3.pages` | Only `10010#1732278 1: ×2 → ×1` | *Confirmed*: an object in no 10010 entry isn't drawn |
| `second-unlisted-resaved.pages` | `second-unlisted.pages` | `10010#1732278 1: ×1 → ×1`, `10015#1732364 1.1 = 1732695` | *Likely*: Pages leaves it in 10015 and out of 10010 |

## Confidence

*Confirmed* by writing: type 10010's field 1.1 is the page an object is drawn on, from 0, and its position is from that page's corner; an object needs a 10010 entry to be drawn; a page number past the last page draws nothing and adds no page.

*Likely*: Pages sorts the entries and keeps numbers past the end when it saves.
