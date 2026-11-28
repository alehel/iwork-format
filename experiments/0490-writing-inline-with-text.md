# 0490: Writing Inline with Text

**Status:** run

Choosing Inline with Text for a picture that moves with the text set its wrap type, drawable field 1.3.1, to 0 and took it out of type 10015, leaving the attachment as it was ([0489](0489-the-text-wrap-menu.md)). This experiment writes each of the two changes on its own, and writes an inline picture back to wrap 5, to see which one makes the picture inline.

## Setup

| | |
| --- | --- |
| Pages | 16.0 (7052.0.68) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-28 |
| Input | `0489/move-around.pages`: picture 1732688, Move with Text, anchored at the end of a two-line paragraph through type-2003 record 1732925, wrap Around (1.3.1 = 1), listed in type 10015; and `0489/inline.pages`, the same picture after Pages made it inline |
| Writer | [`recipes/0383-set-nth-path.py`](../recipes/0383-set-nth-path.py) and [`recipes/0416-reorder.py`](../recipes/0416-reorder.py); exported and saved again with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh), measured with [`recipes/0482-red-per-page.swift`](../recipes/0482-red-per-page.swift) and [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift) |

## Recipe

```bash
mkdir -p samples/0490
S=$PWD/samples/0490
M=samples/0489/move-around.pages
X=recipes/0383-set-nth-path.py
python3 -I $X $M $S/tmp.pages 1732688 1.3.1 varint 0
python3 -I recipes/0416-reorder.py $S/tmp.pages $S/inline-written.pages 1732364 1 1
rm $S/tmp.pages
python3 -I $X $M $S/wrap-0-listed.pages 1732688 1.3.1 varint 0
python3 -I $X samples/0489/inline.pages $S/inline-wrap-5.pages 1732688 1.3.1 varint 5
for f in samples/0489/inline samples/0489/move-around $S/inline-written $S/wrap-0-listed $S/inline-wrap-5; do
  b=$(basename $f)
  cp $f.pages $S/tmp.pages
  sh recipes/0372-in-app.sh Pages $S/tmp.pages "export d to POSIX file \"$S/$b.pdf\" as PDF
save d in POSIX file \"$S/$b-resaved.pages\""
  swift recipes/0482-red-per-page.swift $S/$b.pdf
  swift recipes/0319-measure-pdf.swift $S/$b.pdf
done
rm $S/tmp.pages $S/inline-resaved.pages $S/move-around-resaved.pages
```

## Observation

| File | 1.3.1 | In 10015 | Red drawn at | Second line of text |
| --- | --- | --- | --- | --- |
| `0489/move-around.pages` | 1 | yes | (286.8, 397.2)–(367.0, 437.5) | 70.2–80.2 |
| `0489/inline.pages` | 0 | no | (198.8, 68.5)–(279.0, 108.8) | 100.8–110.8 |
| `inline-written.pages` | 0 | no | (198.8, 68.5)–(279.0, 108.8) | 100.8–110.8 |
| `wrap-0-listed.pages` | 0 | yes | (198.8, 68.5)–(279.0, 108.8) | 100.8–110.8 |
| `inline-wrap-5.pages` | 5 | no | (286.8, 397.2)–(367.0, 437.5) | 70.2–80.2 |

Inline, the picture follows `once.`, which ends at 198 points, and stands on the line: its bottom (108.8) is the baseline the line's text sits on, and the line moved down by the picture's height less the text's, from 70.2 to 100.8. Both written files draw it exactly as Pages' own `inline.pages` does, whether or not the picture is in type 10015.

`inline-wrap-5.pages` is drawn as a floating picture again, at the anchor plus the 2003 offset (56.69 + 230.11 across, 80.69 + 316.91 down), and the paragraph is back to two plain lines, though the picture is in neither type 10015 nor type 10010.

Pages saved each file as it was written: `inline-written-resaved.pages` and `inline-wrap-5-resaved.pages` keep 10015 with the body's text alone, `wrap-0-listed-resaved.pages` keeps the picture in it, and 1.3.1 is unchanged in all three.

## Conclusion

An object attached to the text (U+FFFC, attachment run, type 2003, parent in 1.2) is inline when its wrap type 1.3.1 is 0, and floats at the 2003 offset otherwise. Inline, it is drawn in the line like a character, after the text before the U+FFFC, with its bottom on the line's baseline, and the line is made tall enough to hold it; its 1.1.1 and the 2003 offset aren't used. Whether the object is in type 10015 doesn't change how an attached object is drawn: Pages leaves an inline object out of the list, but a reader shouldn't rely on that to tell inline from floating. On an object placed on the page, wrap 0 has no line to sit in, and is drawn as no wrap ([0488](0488-writing-text-wrap.md)).

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `inline-written.pages` | `0489/move-around.pages` | Only `3005#1732688 1.3.1: 1 → 0`, `10015#1732364 1: ×2 → ×1` | *Confirmed*: wrap 0 and leaving 10015, as Pages does, draw the picture inline |
| `inline-written-resaved.pages` | `inline-written.pages` | `3005#1732688 1.3.1 = 0`, `10015#1732364 1: ×1 → ×1` | *Not used*: a saved copy |
| `wrap-0-listed.pages` | `0489/move-around.pages` | Only `3005#1732688 1.3.1: 1 → 0` | *Confirmed*: wrap 0 alone makes an attached object inline |
| `wrap-0-listed-resaved.pages` | `wrap-0-listed.pages` | `10015#1732364 1: ×2 → ×2`, `3005#1732688 1.3.1 = 0` | *Likely*: Pages keeps an inline object in 10015 when it is written there |
| `inline-wrap-5.pages` | `0489/inline.pages` | Only `3005#1732688 1.3.1: 0 → 5` | *Confirmed*: any other wrap floats the object at its 2003 offset, without a 10015 entry |
| `inline-wrap-5-resaved.pages` | `inline-wrap-5.pages` | `3005#1732688 1.3.1 = 5`, `10015#1732364 1: ×1 → ×1` | *Likely*: Pages doesn't add it back to 10015 |

## Confidence

*Confirmed* by writing, with [0489](0489-the-text-wrap-menu.md): an attached object with wrap type 0 is Inline with Text, drawn in its line; with any other wrap it floats at the 2003 offset; its place in type 10015 doesn't decide either.

*Likely*: an inline object's bottom sits on the line's baseline (one picture, one line; a picture in the middle of a line would show it more clearly).
