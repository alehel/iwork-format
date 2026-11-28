# 0485: The order of objects on one page

**Status:** run

Two objects on the same page share one type-10010 entry, with one field 4 each, in the order they were placed; type 10015 lists them in the same order ([0482](0482-objects-on-later-pages.md)). 10015's order is the stacking order ([0425](0425-writing-stacking-order.md)). This experiment overlaps a red and a blue picture and swaps them in each list in turn, to see whether the order within a 10010 entry matters.

## Setup

| | |
| --- | --- |
| Pages | 16.0 (7052.0.68) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-28 |
| Input | `0482/three-pages.pages`, with the red picture of [0023](0023-an-image.md) and an 8 × 4 blue one placed on page 2 |
| Recipe | [`recipes/0482-blue.py`](../recipes/0482-blue.py) writes the blue picture; [`recipes/0482-place-on-pages.sh`](../recipes/0482-place-on-pages.sh) places them; [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py) writes; [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) exports and saves; [`recipes/0482-red-per-page.swift`](../recipes/0482-red-per-page.swift) gives each colour's box and area |

## Recipe

```bash
mkdir -p samples/0485
S=$PWD/samples/0485
X=recipes/0383-set-nth-path.py
python3 -I recipes/0482-blue.py $S/blue-8x4.png
sh recipes/0482-place-on-pages.sh samples/0482/three-pages.pages $S/tmp-red.pages samples/0482/red-8x4.png 2
sh recipes/0482-place-on-pages.sh $S/tmp-red.pages $S/red-then-blue.pages $S/blue-8x4.png 2
rm $S/tmp-red.pages
python3 -I $X $S/red-then-blue.pages $S/overlap.pages 1732724 1.1.1.1 float 290.8 1.1.1.2 float 399.71
python3 -I $X $S/overlap.pages $S/page-list-swapped.pages 1732278 1.4:1.1.1 varint 1732724 1.4:2.1.1 varint 1732688
python3 -I $X $S/overlap.pages $S/stack-swapped.pages 1732364 1:2.1 varint 1732724 1:3.1 varint 1732688
for f in red-then-blue overlap page-list-swapped stack-swapped; do
  cp $S/$f.pages $S/tmp.pages
  sh recipes/0372-in-app.sh Pages $S/tmp.pages "export d to POSIX file \"$S/$f.pdf\" as PDF
save d in POSIX file \"$S/$f-resaved.pages\""
  swift recipes/0482-red-per-page.swift $S/$f.pdf
done
rm $S/tmp.pages
```

## Observation

Pages placed the red picture, 1732688, at (286.8, 397.71) and the blue one, 1732724, 10 points further right and down. The writer moved the blue one to (290.8, 399.71), so that it covers the red one's lower right corner. Each picture is 8 × 4 points, 32 square points.

| File | 10010 entry for page 2 (field 4) | 10015 field 1 | Red area | Blue area |
| --- | --- | --- | --- | --- |
| `red-then-blue.pages` | red, blue | body, red, blue | apart | apart |
| `overlap.pages` | red, blue | body, red, blue | 25.5 | 35.1 |
| `page-list-swapped.pages` | blue, red | body, red, blue | 25.5 | 35.1 |
| `stack-swapped.pages` | red, blue | body, blue, red | 35.1 | 25.5 |

(The areas are counted at 4 pixels per point, with the pictures' smoothed edges, so a whole picture measures 35.1.) Only swapping type 10015 put red on top.

When Pages saved the files again, the 10010 entry of `page-list-swapped-resaved.pages` was back to red, blue, and that of `stack-swapped-resaved.pages` became blue, red: in both, the order of 10015.

## Conclusion

The order of the objects within a type-10010 entry doesn't change what is drawn: type 10015 alone decides which object is in front. Pages writes each 10010 entry's objects in their 10015 order, back to front, and rewrites them that way when it saves. A reader can ignore the order in field 4; a writer should follow 10015's order.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `red-then-blue.pages` | `0482/three-pages.pages` | `10010#1732278 1.4: absent → present`, `10010#1732278 1.4: ×0 → ×2`, `10015#1732364 1.1 = 1732724` | *Likely*: two pictures on page 2 share an entry |
| `red-then-blue-resaved.pages` | `red-then-blue.pages` | `10010#1732278 1.4: ×2 → ×2` | *Not used*: a saved copy |
| `overlap.pages` | `red-then-blue.pages` | Only `3005#1732724 1.1.1.1: 296.8 → 290.8`, `3005#1732724 1.1.1.2: 407.71 → 399.71` | *Control*: blue over red |
| `overlap-resaved.pages` | `overlap.pages` | `3005#1732724 1.1.1.1 = 290.8` | *Not used*: a saved copy |
| `page-list-swapped.pages` | `overlap.pages` | Only `10010#1732278 1: changed`, the two field-4 entries the other way round | *Likely*: the order in a 10010 entry doesn't change the drawing |
| `page-list-swapped-resaved.pages` | `page-list-swapped.pages` | `10010#1732278 1: changed` | *Likely*: Pages writes the 10015 order back into the entry |
| `stack-swapped.pages` | `overlap.pages` | Only `10015#1732364 1: changed` | *Confirmed*: 10015 decides which object is in front, as in [0425](0425-writing-stacking-order.md) |
| `stack-swapped-resaved.pages` | `stack-swapped.pages` | `10010#1732278 1: changed` | *Likely*: Pages makes the entry follow 10015 |

## Confidence

*Confirmed*: type 10015's order is the stacking order, on any page, by writing it here and in [0425](0425-writing-stacking-order.md).

*Likely*: the order of field 4 in a 10010 entry changes nothing drawn, and Pages writes it in the 10015 order. One writing experiment; a second would swap three objects, or objects on page 1.
