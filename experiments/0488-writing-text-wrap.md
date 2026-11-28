# 0488: Writing a drawable's text wrap

**Status:** run

A picture placed on the page has a message in drawable field 1.3, `{ 1: 4, 2: 2, 3: 1, 4: 12.0, 5: 0.5, 6: 0 }`, in every document so far ([0023](0023-an-image.md), [0482](0482-objects-on-later-pages.md)). The Arrange sidebar shows the same picture's text wrap as *Automatic*, a spacing of 12 pt, an alpha of 50 % and the second of two *Text Fit* buttons ([0487](0487-move-with-text.md)), so 1.3 looks like the wrap settings. This experiment writes each field into a picture in the middle of a page of text and measures where the lines break around it.

## Setup

| | |
| --- | --- |
| Pages | 16.0 (7052.0.68) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-28 |
| Input | `words.pages`: `samples/0002/hello.pages` with the body written as `word` 1,200 times, two pages of 12-point lines from 57.2 to 523.8 points across |
| Writer | [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py); [`recipes/0482-place-on-pages.sh`](../recipes/0482-place-on-pages.sh) places the picture; exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and measured with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift), which lists each line of dark ink with the pieces it is broken into |

## Recipe

```bash
mkdir -p samples/0488
S=$PWD/samples/0488
X=recipes/0383-set-nth-path.py
python3 -I recipes/0287-iwa-writer.py samples/0002/hello.pages $S/words.pages --text 1732539 \
  "$(python3 -c "print(' '.join(['word']*1200), end='')")"
sh recipes/0482-place-on-pages.sh $S/words.pages $S/small-picture.pages samples/0482/red-8x4.png 1
python3 -I $X $S/small-picture.pages $S/base.pages 1732688 1.1.2.1 float 80 1.1.2.2 float 40 4.1 float 80 4.2 float 40
B=$S/base.pages; I=1732688
python3 -I $X $B $S/gap-30.pages $I 1.3.4 float 30
for v in 0 1 2 3 5; do python3 -I $X $B $S/type-$v.pages $I 1.3.1 varint $v; done
for v in 0 1; do python3 -I $X $B $S/sides-$v.pages $I 1.3.2 varint $v; done
for t in 1 3; do for v in 0 1; do
  python3 -I $X $B $S/type-$t-sides-$v.pages $I 1.3.1 varint $t 1.3.2 varint $v
done; done
python3 -I $X $B $S/type-2-gap-30.pages $I 1.3.1 varint 2 1.3.4 float 30
python3 -I $X $B $S/fit-0.pages $I 1.3.3 varint 0
python3 -I $X $B $S/field6-1.pages $I 1.3.6 varint 1
for f in base gap-30 type-0 type-1 type-2 type-3 type-5 sides-0 sides-1 type-1-sides-0 type-1-sides-1 \
         type-3-sides-0 type-3-sides-1 type-2-gap-30 fit-0 field6-1; do
  cp $S/$f.pages $S/tmp.pages
  sh recipes/0372-in-app.sh Pages $S/tmp.pages "export d to POSIX file \"$S/$f.pdf\" as PDF"
  swift recipes/0319-measure-pdf.swift $S/$f.pdf
done
rm $S/tmp.pages
```

The picture, 1732688, is 80 × 40 points at (286.8, 397.71), so it covers 286.8–366.8 across and 397.7–437.7 down. Its 1.3 is as above.

## Observation

Lines are 12 points apart; the table gives, for the lines from 382 to 450 points down, where the text is.

| File | Written in 1.3 | Lines beside the picture | Text above and below |
| --- | --- | --- | --- |
| `base.pages` | as Pages made it | 57.2–246.8 and 379.2–513.5; at 382 and 442, 57.2–274.5 and 378.0–512.2 | lines at 370 and 454 run full width |
| `gap-30.pages` | 4: 30.0 | right side from 397.2; seven more lines narrowed, from 358 to 466 | |
| `type-0.pages` | 1: 0 | full width; the picture hides the text under it | |
| `type-5.pages` | 1: 5 | as `type-0.pages` | |
| `type-1.pages` | 1: 1 | as `base.pages` | |
| `type-2.pages` | 1: 2 | none: no line between 378 and 451 | last line above ends at 378.2, next starts at 451.2 |
| `type-2-gap-30.pages` | 1: 2, 4: 30.0 | none | next line starts at 469.2 |
| `type-3.pages` | 1: 3 | left side only, 57.2–246.8 | |
| `sides-0.pages`, `sides-1.pages` | 2: 0, 2: 1 | as `base.pages` | |
| `type-1-sides-0.pages` | 1: 1, 2: 0 | left side only | |
| `type-1-sides-1.pages` | 1: 1, 2: 1 | right side only, from 378.0 | |
| `type-3-sides-0.pages`, `type-3-sides-1.pages` | 1: 3, 2: 0 or 1 | left side only | |
| `fit-0.pages` | 3: 0 | as `base.pages`, but the lines at 382 and 442 also stop at 246.8 and start at 379.2 | |
| `field6-1.pages` | 6: 1 | as `base.pages` | |

The right side of the text starts 12.4 points after the picture's right edge in `base.pages` (366.8 to 379.2) and 30.4 points after it in `gap-30.pages`. With type 2, the text resumes 12 points below the picture's bottom edge (437.7 + 12 = 449.7, the top of the line drawn from 451.2), or 30 points below it with the spacing written as 30.

## Conclusion

Drawable field 1.3 is the object's text wrap:

| Field | Holds | Values seen |
| --- | --- | --- |
| 1.3.1 | How text wraps | 0 none: the text runs under the object, which is drawn over it; 1 around, on the sides 1.3.2 chooses; 2 above and below, nothing beside; 3 on one side only, the left here, where there is more room (and 1.3.2 is ignored); 4 the sidebar's *Automatic*, Pages' default, here on both sides, and 1.3.2 is ignored. 5 drew as 0 |
| 1.3.2 | Which sides, for wrap 1 | 0 left, 1 right, 2 both (Pages' default) |
| 1.3.3 | Text fit | Pages' default is 1; 0 keeps the full spacing on lines that only partly reach the object's top or bottom edge, which 1 lets closer, so 0 is most likely the sidebar's box fit and 1 its outline (alpha) fit |
| 1.3.4 | The spacing between the text and the object, in points, on every side | 12.0 by default, the sidebar's 12 pt |
| 1.3.5 | Most likely the alpha threshold for outline fit, from 0 to 1 | 0.5, the sidebar's 50 %; not tested, since the picture is opaque |
| 1.3.6 | Unknown | 0; 1 changed nothing drawn |

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `words.pages` | `0002/hello.pages` | Only `2001#1732539 3: changed`, `2001#1732539 3 ~ "word word"` | *Control*: two pages of text |
| `small-picture.pages` | `words.pages` | `3005#1732688 1.3.1 = 4`, `3005#1732688 1.3.4 = 12.0`, `3005#1732688 1.3.5 = 0.5`, `10010#1732278 1.1 = 0` | *Control*: Pages' default wrap |
| `base.pages` | `small-picture.pages` | Only `3005#1732688 1.1.2.1: 8.0 → 80.0`, `3005#1732688 1.1.2.2: 4.0 → 40.0`, `3005#1732688 4.1: 8.0 → 80.0`, `3005#1732688 4.2: 4.0 → 40.0` | *Control*: an 80 × 40 picture in the text |
| `gap-30.pages` | `base.pages` | Only `3005#1732688 1.3.4: 12.0 → 30.0` | *Confirmed*: 1.3.4 is the spacing in points |
| `type-2-gap-30.pages` | `base.pages` | Only `3005#1732688 1.3.1: 4 → 2`, `3005#1732688 1.3.4: 12.0 → 30.0` | *Confirmed*: the spacing applies above and below too |
| `type-0.pages` | `base.pages` | Only `3005#1732688 1.3.1: 4 → 0` | *Likely*: 0 is no wrap |
| `type-1.pages` | `base.pages` | Only `3005#1732688 1.3.1: 4 → 1` | *Likely*: 1 wraps around, on both sides with 1.3.2 = 2 |
| `type-2.pages` | `base.pages` | Only `3005#1732688 1.3.1: 4 → 2` | *Likely*: 2 is above and below |
| `type-3.pages` | `base.pages` | Only `3005#1732688 1.3.1: 4 → 3` | *Likely*: 3 wraps on one side |
| `type-5.pages` | `base.pages` | Only `3005#1732688 1.3.1: 4 → 5` | *Unknown*: 5 draws as no wrap |
| `sides-0.pages` | `base.pages` | Only `3005#1732688 1.3.2: 2 → 0` | *Likely*: with wrap 4 the sides are ignored |
| `sides-1.pages` | `base.pages` | Only `3005#1732688 1.3.2: 2 → 1` | *Likely*: with wrap 4 the sides are ignored |
| `type-1-sides-0.pages` | `base.pages` | Only `3005#1732688 1.3.1: 4 → 1`, `3005#1732688 1.3.2: 2 → 0` | *Likely*: side 0 is the left |
| `type-1-sides-1.pages` | `base.pages` | Only `3005#1732688 1.3.1: 4 → 1`, `3005#1732688 1.3.2: 2 → 1` | *Likely*: side 1 is the right |
| `type-3-sides-0.pages` | `base.pages` | Only `3005#1732688 1.3.1: 4 → 3`, `3005#1732688 1.3.2: 2 → 0` | *Likely*: with wrap 3 the sides are ignored |
| `type-3-sides-1.pages` | `base.pages` | Only `3005#1732688 1.3.1: 4 → 3`, `3005#1732688 1.3.2: 2 → 1` | *Likely*: with wrap 3 the sides are ignored |
| `fit-0.pages` | `base.pages` | Only `3005#1732688 1.3.3: 1 → 0` | *Likely*: 1.3.3 is the text fit |
| `field6-1.pages` | `base.pages` | Only `3005#1732688 1.3.6: 0 → 1` | *Unknown*: changes nothing drawn |

## Confidence

*Confirmed* by writing: 1.3.4 is the gap between the text and the object, in points, beside and above and below it.

*Likely*: the meanings of 1.3.1 (0 none, 1 around, 2 above and below, 3 one side, 4 automatic), 1.3.2 (0 left, 1 right, 2 both, for wrap 1) and 1.3.3 (text fit). Which side wrap 3 and wrap 4 choose, and the names Pages gives them, need the sidebar's pop-up, which couldn't be used in the background: a follow-up should choose each wrap there and compare.

*Unknown*: 1.3.5, most likely the alpha threshold (a picture with transparency would show it), 1.3.6, and wrap type 5.
