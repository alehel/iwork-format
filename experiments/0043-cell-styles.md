# 0043: Cell styles

**Status:** run

[0031](0031-cell-kinds.md) and [0036](0036-more-cell-formats.md) decoded a cell's flag bits for values and formats, but never changed a cell's appearance. This experiment gives five cells the same value and different font size, font, text colour and background, to find where cell formatting is kept.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0031](0031-cell-kinds.md), cell G2 (a plain 42) |

## Recipe

```bash
mkdir -p samples/0043
osascript recipes/0043-numbers-cell-style.applescript "$PWD/samples/0043/styles.numbers"
```

All five cells hold 42. Numbers' AppleScript then sets C2's `font size` to 20, D2's `font name` to `Helvetica-Bold`, E2's `text color` to red, and F2's `background color` to red.

## Observation

| Cell | Change | Flags | Keys, in order |
| --- | --- | --- | --- |
| B2 | none | 0x3001 | 1, 1 |
| C2 | font size 20 | 0x3041 | 1, 1, 1 |
| D2 | font Helvetica-Bold | 0x3041 | 2, 1, 1 |
| E2 | text colour red | 0x3041 | 3, 1, 1 |
| F2 | background red | 0x3021 | 4, 1, 1 |

Data list 904534 (list type 4) gained four entries, keys 1 to 4. Each names a record in `DocumentStylesheet.iwa`:

| Key | Record | Type | Parent (1.3) | Field 10 | Field 11 |
| --- | --- | --- | --- | --- | --- |
| 1 | 905249 | 2022 | 903892 | 1 | 3: 20.0 |
| 2 | 905256 | 2022 | 903892 | 2 | 1: 1, 5: `Helvetica-Bold` |
| 3 | 905265 | 2022 | 903892 | 1 | 7: (1.0, 0.149, 0.0, alpha 1.0) |
| 4 | 905274 | 6004 | 904075 | 1 | 1.1: (1.0, 0.149, 0.0, alpha 1.0) |

## Conclusion

Two more flag bits each add a key into the style list (list type 4) of the table model:

| Flag bit | Followed by |
| --- | --- |
| 0x0020 | A cell style: a type-6004 record whose field 11.1.1 is the background colour |
| 0x0040 | A text style: an unnamed paragraph style (type 2022) that changes the cell text's character properties |

The keys come first, before the 0x1000 and 0x2000 keys, which matches ordering by bit value.

A cell's text formatting therefore uses the same paragraph styles, properties and parents as text in Pages. The text style's parent (903892) is presumably the table's default paragraph style, so the rule of [0033](0033-style-resolution.md) should apply to cells too.

Setting the font to `Helvetica-Bold` set two properties, the font name and bold, and field 10 is 2. That fits field 10 counting the properties a style sets.

The red stored here, (1.0, 0.149, 0.0), is the same as for text coloured red through Pages' AppleScript in 0013. So both apps convert AppleScript colours the same way.

## Confidence

*Likely*:

- Flag 0x40 is a text-style key and 0x20 a cell-style key, both into list type 4.
- Cell text styles are unnamed paragraph styles.
- Cell styles are type 6004 with the fill colour in 11.1.1.

*Unknown*:

- Flag 0x1000, which stayed 1 in every cell here.
- Objects 903892 and 904075.
