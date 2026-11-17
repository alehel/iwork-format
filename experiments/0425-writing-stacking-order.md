# 0425: Writing the stacking order of the page

**Status:** run

A type-10015 record lists what is drawn on the page in its field 1, the body's text among them; reordering a shape that didn't overlap anything changed nothing visible ([0424](0424-writing-the-page-objects-list.md)). This experiment moves a blue square over the body's first word and puts it after and before the body in the list.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0213/plain-shape.pages`: the body `One` and square 1732647; record 1732364 lists the body's text, then the square |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) and [`recipes/0416-reorder.py`](../recipes/0416-reorder.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and drawn with [`recipes/0373-draw-pdf.swift`](../recipes/0373-draw-pdf.swift) |

## Recipe

```bash
mkdir -p samples/0425
O=samples/0425
python3 -I recipes/0302-set-path.py samples/0213/plain-shape.pages $O/over-text.pages 1732647 \
  1.1.1.1.1 float 40 1.1.1.1.2 float 40 1.2.1 varint 1731554
python3 -I recipes/0416-reorder.py $O/over-text.pages $O/shape-first.pages 1732364 1 2,1
for f in over-text shape-first; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0373-draw-pdf.swift $O/$f.pdf 54 56 26 12 1
done
```

The square is moved to (40, 40), over where `One` starts (57, 58), and given the blue preset style (`shape-1-shapestyle`, [0413](0413-writing-a-shape-style-preset.md)). PDFKit gave each file's position of `One`.

## Observation

| File | Field 1 | Where `One` is drawn | At (54–80, 56–68) |
| --- | --- | --- | --- |
| `over-text.pages` | body, square | x = 152, right of the square | blue: the square |
| `shape-first.pages` | square, body | x = 56, where it was | the black word over the blue square |

The square is 100 points wide, from x = 40 to 140.

## Conclusion

The list is the stacking order from back to front, and where the body's text stands in it matters. A shape listed after the body is in front of the text, and the text wraps around it, so `One` moved to the right of the square. A shape listed before the body is behind the text: the text is drawn over it and doesn't wrap. A reader should draw the page's objects in the list's order and wrap the body's text only around objects that come after it.

## Confidence

*Confirmed*: type 10015's field 1 as the stacking order, back to front, with text wrapping only around objects in front of the body, by writing it.
