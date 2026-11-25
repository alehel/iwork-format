# 0428: Writing a font name with a weight

**Status:** run

A style's font is in 11.5, and its bold and italic in 11.1 and 11.2. A font name may already include a weight, such as `HelveticaNeue-Bold`, which Pages wrote in some styles ([styles.md](../spec/styles.md)). This experiment writes font names with weights into the body's style, with and without the bold flag.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0002/hello.pages`: the body `hello` in *Brødtekst* (1731511), which sets 11.5 = `HelveticaNeue` and 11.1 = 0 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and compared with [`recipes/0399-pdf-diff.swift`](../recipes/0399-pdf-diff.swift) |

## Recipe

```bash
mkdir -p samples/0428
R=recipes/0302-set-path.py
F=samples/0002/hello.pages
O=samples/0428
cp $F $O/original.pages
python3 -I $R $F $O/font-bold-name.pages 1731511 11.5 string HelveticaNeue-Bold
python3 -I $R $F $O/font-bold-name-and-flag.pages 1731511 11.5 string HelveticaNeue-Bold 11.1 varint 1
python3 -I $R $F $O/font-light-name-and-flag.pages 1731511 11.5 string HelveticaNeue-Light 11.1 varint 1
python3 -I $R $F $O/font-italic-name.pages 1731511 11.5 string HelveticaNeue-Italic
for f in original font-bold-name font-bold-name-and-flag font-light-name-and-flag font-italic-name; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF
return font of word 1 of body text of d"
done
swift recipes/0399-pdf-diff.swift $O/font-bold-name.pdf $O/font-bold-name-and-flag.pdf
```

## Observation

| File | 11.5 | 11.1 | Font of `hello` |
| --- | --- | --- | --- |
| `original.pages` | HelveticaNeue | 0 | HelveticaNeue |
| `font-bold-name.pages` | HelveticaNeue-Bold | 0 | HelveticaNeue |
| `font-bold-name-and-flag.pages` | HelveticaNeue-Bold | 1 | HelveticaNeue-Bold |
| `font-light-name-and-flag.pages` | HelveticaNeue-Light | 1 | HelveticaNeue-Bold |
| `font-italic-name.pages` | HelveticaNeue-Italic | 0 | HelveticaNeue |

`font-bold-name.pdf` and `font-bold-name-and-flag.pdf` differ in the word's 562 pixels: the first is drawn regular.

## Conclusion

Pages takes the font's family from 11.5 and its weight and slant from the bold and italic flags, not from the name. A name with a weight or slant in it is drawn without that weight when the style's flag is 0, and a light face with bold set is drawn in the family's bold. So a reader should reduce the name in 11.5 to its family and apply 11.1 and 11.2, as the rule for combining styles already does with the flags. In the styles Pages writes, a name with `-Bold` comes with bold set, so either reading gives the same result there.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0002/hello.pages` | `same bytes`, `2022#1731511 11.5 = "HelveticaNeue"`, `2022#1731511 11.1 = 0` | *Control* |
| `font-bold-name.pages` | `original.pages` | Only `2022#1731511 11.5: "HelveticaNeue" → "HelveticaNeue-Bold"` | *Confirmed*: a bold name with the flag at 0 is drawn regular |
| `font-bold-name-and-flag.pages` | `original.pages` | Only `2022#1731511 11.5: "HelveticaNeue" → "HelveticaNeue-Bold"`, `2022#1731511 11.1: 0 → 1` | *Confirmed*: with the flag at 1 it is bold |
| `font-light-name-and-flag.pages` | `original.pages` | Only `2022#1731511 11.5: "HelveticaNeue" → "HelveticaNeue-Light"`, `2022#1731511 11.1: 0 → 1` | *Confirmed*: a light name with the flag at 1 is drawn in the family's bold |
| `font-italic-name.pages` | `original.pages` | Only `2022#1731511 11.5: "HelveticaNeue" → "HelveticaNeue-Italic"` | *Confirmed*: an italic name without the flag is drawn upright |

## Confidence

*Confirmed*: the bold and italic flags decide the face, over a weight or slant in the font's name, by writing them.
