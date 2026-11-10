# 0310: Writing a cell's font, size and text colour

**Status:** run

[0043](0043-cell-styles.md) found a cell's text formatting in an unnamed paragraph style (type 2022), with character properties in field 11: 11.3 the size, 11.5 the font and 11.7 the text colour ([text.md](../spec/text.md#styles)). AppleScript reads a cell's `font size`, `font name` and `text color`. This experiment writes each and asks Numbers.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0043/styles.numbers`: C2 has size 20 (style 905249), D2 the font Helvetica-Bold (905256, which also has 11.1 = 1) and E2 red text (905265, which has the colour in 11.7 and again in 11.46.1) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0310
cp samples/0043/styles.numbers samples/0310/original.numbers
python3 -I recipes/0302-set-path.py samples/0310/original.numbers samples/0310/s1.numbers 905249 11.3 float 33
python3 -I recipes/0302-set-path.py samples/0310/s1.numbers samples/0310/s2.numbers 905256 11.5 string Courier
python3 -I recipes/0302-set-path.py samples/0310/s2.numbers samples/0310/written.numbers 905265 \
  11.7.3 float 0.0 11.7.4 float 0.5 11.7.5 float 1.0
rm samples/0310/s1.numbers samples/0310/s2.numbers
python3 -I recipes/0302-set-path.py samples/0310/written.numbers samples/0310/written2.numbers 905265 \
  11.46.1.3 float 0.0 11.46.1.4 float 0.5 11.46.1.5 float 1.0
python3 -I recipes/0302-set-path.py samples/0310/original.numbers samples/0310/only46.numbers 905265 \
  11.46.1.3 float 0.0 11.46.1.4 float 0.5 11.46.1.5 float 1.0
```

Numbers opened each file on its own and read the three cells through AppleScript; `only46.numbers` was saved again.

## Observation

| File | C2 size | D2 font | E2 colour |
| --- | --- | --- | --- |
| `original.numbers` | 20 | Helvetica-Bold | 64633, 466, 1797 (red) |
| `written.numbers` (11.7 blue) | 33 | Courier-Bold | 64633, 466, 1797 (red) |
| `written2.numbers` (11.7 and 11.46 blue) | | | 2915, 26156, 65429 |
| `only46.numbers` (11.46 blue) | | | 2915, 26156, 65429 |

The blue written, 0, 0.5, 1 in sRGB, converts to exactly 2915, 26156, 65429 in Generic RGB, as in [0309](0309-writing-a-cell-colour.md). Saved again, `only46.numbers` has the blue in both 11.46.1 and 11.7.

## Conclusion

11.3 is the font size and 11.5 the font, by its PostScript name. The font name holds the family's face, and 11.1 = 1 (bold) is applied on top, so Courier with bold set shows as Courier-Bold. The text colour that counts is 11.46.1, a fill holding a colour. 11.7 is a copy, which Numbers rewrites from 11.46 when it saves, so a writer should set both. This is a third sRGB colour converted exactly to what AppleScript reports.

## Confidence

*Confirmed*: 11.3 the size, 11.5 the font, 11.46.1 the text colour, by writing them; 11.7 is a copy rewritten from 11.46 on saving.
