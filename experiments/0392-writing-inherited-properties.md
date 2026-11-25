# 0392: Writing an inherited and a cleared character property

**Status:** run

Field 11 of a character or paragraph style holds the character properties it sets. A property left out is inherited, and one set to 0 is turned off ([0004](0004-larger-word.md), [0007](0007-bold-and-italic.md)). This experiment sets bold and italic on the paragraph style under a word that has a character style, and then clears them in the character style.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0351/bold.pages`: `plain bold` in the paragraph style Body (record 1731511), with `bold` in the character style `Framhevet` (1731541), which sets only 11.1 = 1, bold ([0351](0351-writing-a-character-run.md)) |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0392
R=recipes/0302-set-path.py
B=samples/0351/bold.pages
O=samples/0392
cp $B $O/original.pages
python3 -I $R $B $O/body-bold.pages 1731511 11.1 varint 1
python3 -I $R $O/body-bold.pages $O/body-bold-emph-off.pages 1731541 11.1 varint 0
python3 -I $R $B $O/body-italic.pages 1731511 11.2 varint 1
python3 -I $R $O/body-italic.pages $O/body-italic-emph-off.pages 1731541 11.2 varint 0
for f in original body-bold body-bold-emph-off body-italic body-italic-emph-off; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages \
    'return {font of word 1 of body text of d, font of word 2 of body text of d}'
done
```

## Observation

| File | Body | `Framhevet` | `plain` | `bold` |
| --- | --- | --- | --- | --- |
| `original.pages` | | 11.1 = 1 | HelveticaNeue | HelveticaNeue-Bold |
| `body-bold.pages` | 11.1 = 1 | 11.1 = 1 | HelveticaNeue-Bold | HelveticaNeue-Bold |
| `body-bold-emph-off.pages` | 11.1 = 1 | 11.1 = 0 | HelveticaNeue-Bold | HelveticaNeue |
| `body-italic.pages` | 11.2 = 1 | 11.1 = 1 | HelveticaNeue-Italic | HelveticaNeue-BoldItalic |
| `body-italic-emph-off.pages` | 11.2 = 1 | 11.1 = 1, 11.2 = 0 | HelveticaNeue-Italic | HelveticaNeue-Bold |

## Conclusion

A character style that leaves a property out passes on the paragraph style's value: `Framhevet` sets no italic, so `bold` is bold and italic when Body is italic. A property written as 0 in the character style turns it off over the paragraph style's 1, for bold and for italic alike. So a reader has to tell an absent property from a 0, and look further down the chain only when it is absent.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.pages` | `0351/bold.pages` | `same bytes`, `2021#1731541 11.1 = 1`, `2021#1731541 11.2 = absent` | *Control* |
| `body-bold.pages` | `original.pages` | Only `2022#1731511 11.1: 0 → 1` | *Control*: both words are bold |
| `body-bold-emph-off.pages` | `body-bold.pages` | Only `2021#1731541 11.1: 1 → 0` | *Confirmed*: 0 in the character style turns bold off |
| `body-italic.pages` | `original.pages` | Only `2022#1731511 11.2: 0 → 1` | *Confirmed*: a left-out property is inherited: the second word is bold italic |
| `body-italic-emph-off.pages` | `body-italic.pages` | Only `2021#1731541 11.2: absent → 0` | *Confirmed*: 0 in the character style turns italic off |

## Confidence

*Confirmed*: a left-out character property is inherited and one set to 0 turns it off, by writing them.
