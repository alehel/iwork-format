# 0377: Writing a tracked change's kind and its author's colour

**Status:** run

A tracked change is a type-2060 record in run table 21 or 22, whose field 1 is 1 for an insertion and 2 for a deletion. Field 2 names a type-2062 record that names the author, a type-212 record with a name (field 1) and a colour (field 2) ([0193](0193-tracked-insertion.md), [0194](0194-tracked-deletion.md)). When Pages exports a document with comments included, it draws tracked changes in the author's markup colour, and strikes deleted text through. This experiment swaps the kinds and changes the author's colour.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/0193/tracked.pages`: `One two` with ` two` a tracked insertion, change record 1732729. `samples/0194/deleted.pages`: `One two` with ` two` a tracked deletion, change record 1732736, author 1732734 with the colour 0.98, 0.94, 0.35 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and drawn with [`recipes/0373-draw-pdf.swift`](../recipes/0373-draw-pdf.swift), which now also marks coloured pixels with `o` |

## Recipe

```bash
mkdir -p samples/0377
R=recipes/0302-set-path.py
O=samples/0377
cp samples/0193/tracked.pages $O/inserted.pages
cp samples/0194/deleted.pages $O/deleted.pages
python3 -I $R $O/deleted.pages $O/deleted-as-insertion.pages 1732736 1 varint 1
python3 -I $R $O/inserted.pages $O/inserted-as-deletion.pages 1732729 1 varint 2
python3 -I $R $O/deleted.pages $O/deleted-blue.pages 1732734 2.3 float 0 2.4 float 0 2.5 float 1
python3 -I $R $O/deleted.pages $O/deleted-red.pages 1732734 2.3 float 1 2.4 float 0 2.5 float 0
python3 -I $R $O/deleted.pages $O/deleted-green.pages 1732734 2.3 float 0 2.4 float 1 2.5 float 0
for f in inserted deleted deleted-as-insertion inserted-as-deletion deleted-blue deleted-red deleted-green; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages \
    "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF with properties {include comments:true}"
  swift recipes/0373-draw-pdf.swift $O/$f.pdf 226 172 14 12 0.25
done
```

With comments included, the page is drawn smaller beside a margin, and `two` sits between x = 226 and 240. The count of coloured pixels in each row of that box was taken from the drawing, and the colour of one pixel on the strike line (232, 177.5) read the same way.

## Observation

AppleScript's `body text` is `One two` for every file. Coloured pixels per row across `two`, from the top of the letters:

| File | Kind written | Coloured pixels per row |
| --- | --- | --- |
| `inserted.pages` | 1 (as made) | 2 3 3 3 3 27 30 31 22 22 22 21 21 21 22 20 21 21 25 24 19 |
| `deleted.pages` | 2 (as made) | 2 3 3 3 3 27 30 31 22 22 22 21 25 **54** 22 20 21 21 25 24 19 |
| `deleted-as-insertion.pages` | 1 | 2 3 3 3 3 27 30 31 22 22 22 21 21 21 22 20 21 21 25 24 19 |
| `inserted-as-deletion.pages` | 2 | 2 3 3 3 3 27 30 31 22 22 22 21 25 **54** 22 20 21 21 25 24 19 |

The row of 54 is the strike line. The colour drawn for each author colour:

| Author colour written (RGB) | Markup drawn |
| --- | --- |
| 0.98, 0.94, 0.35 (as made) | 0.77, 0.64, 0.23 |
| 0, 0, 1 | 0.36, 0.78, 0.69 |
| 1, 0, 0 | 0.98, 0.60, 0.21 |
| 0, 1, 0 | 0.43, 0.76, 0.27 |

## Conclusion

Field 1 of a change record decides how Pages treats it: written as 2, an insertion becomes a deletion and is struck through; written as 1, a deletion becomes an insertion and the strike goes. The text is unchanged either way, so the kind alone decides whether a reader should show the range.

The author's colour does steer the markup, but Pages doesn't draw it as stored: each colour written was drawn as a different colour, nearer some colours than others (red as orange, blue as teal). It seems to pick from a set of its own markup colours. Which set, and how it chooses, is *unknown*; a writer should keep the colours Pages itself gives authors.

## Confidence

*Confirmed*: field 1 of a type-2060 change as its kind, 1 insertion and 2 deletion, by writing it both ways. That the author's colour selects the markup colour is *likely*; how it maps is *unknown*.
