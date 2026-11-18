# 0453: Writing a highlighting rule's style

**Status:** run

A conditional highlighting rule names a cell style (type 6004) and a text style (type 2022) to apply to the cells it matches ([0259](0259-conditional-highlighting.md)); the value it compares with was confirmed by writing it ([0391](0391-writing-a-rule-value.md)). This experiment writes the two styles' colours.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0259/highlight.numbers`: `n` 1, 2, 3, 4 in B2:B5 with the rule *greater than 2* and the preset *Grønt fyll* (green fill); rule 905589 names cell style 905591, whose fill is 0.69, 0.89, 0.54 in 11.1.1, and text style 905590, black in 11.7 and 11.46.1 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh), read with [`recipes/0384-pdf-colours.swift`](../recipes/0384-pdf-colours.swift) and drawn with [`recipes/0373-draw-pdf.swift`](../recipes/0373-draw-pdf.swift) |

## Recipe

```bash
mkdir -p samples/0453
R=recipes/0302-set-path.py
F=samples/0259/highlight.numbers
O=samples/0453
cp $F $O/original.numbers
python3 -I $R $F $O/fill-blue.numbers 905591 11.1.1.3 float 0 11.1.1.4 float 0 11.1.1.5 float 1 11.1.1.6 float 1
python3 -I $R $F $O/text-red.numbers 905590 11.7.3 float 1 11.46.1.3 float 1
for f in original fill-blue text-red; do
  sh recipes/0372-in-app.sh Numbers $O/$f.numbers "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0384-pdf-colours.swift $O/$f.pdf 220,130 220,170
  swift recipes/0373-draw-pdf.swift $O/$f.pdf 240 164 28 12 0.5
done
```

(220, 130) is in B2, which doesn't match, and (220, 170) in B4, which does; the box at (240, 164) holds B4's digit.

## Observation

| File | B2's fill | B4's fill | B4's digit |
| --- | --- | --- | --- |
| `original.numbers` | white | 0.72, 0.90, 0.58 | dark (64 dark samples) |
| `fill-blue.numbers` | white | 0, 0, 1 | |
| `text-red.numbers` | white | 0.72, 0.90, 0.58 | red (78 coloured samples, none dark) |

## Conclusion

A highlighting rule's cell style gives matched cells their fill and its text style their text colour, as written; cells the rule doesn't match keep their own look. The fill is drawn in its colour without the style's alpha of 0.9 showing against white. A reader can draw highlighted cells by applying the rule's two styles over the cell's own.

## Confidence

*Confirmed*: the fill of a rule's cell style and the colour of its text style, by writing them.
