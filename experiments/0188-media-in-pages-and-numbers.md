# 0188: Media in Pages and Numbers

**Status:** run

[0185](0185-keynote-audio.md) to [0187](0187-keynote-movie.md) found that Keynote stores sounds and movies as type-3007 records. This experiment adds a movie to a Pages document and a sound to a Numbers sheet, to see whether the other apps store them the same way.

## Setup

| | |
| --- | --- |
| Pages, Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0185](0185-keynote-audio.md) and [0187](0187-keynote-movie.md) |

## Recipe

```bash
mkdir -p samples/0188
osascript recipes/0188-pages-movie.applescript "$PWD/samples/0188" "$PWD/samples/0185/clip.mov" "$PWD/samples/0185/tone.m4a"
```

The recipe puts `clip.mov` from 0187 on page 1 of a Pages document with the body text `one`, and `tone.m4a` from 0185 on sheet 1 of a new spreadsheet. Both go through `make new image`, as in Keynote.

## Observation

`movie.pages` holds `Data/clip-24.mov` and `Data/posterImage-25.png`, and `Document.iwa` has one type-3007 record. Its fields match Keynote's movie: 14 `{ 1: 24 }`, 15 `{ 1: 25 }`, 9 = 0, 23 = 1, a natural size of 64 × 48 in 20 and 21, and `vide` in 29.1.1. Its drawable has no field 1.2, like other objects placed on a Pages page.

`sound.numbers` holds `Data/tone-16.m4a`, and `Document.iwa` has one type-3007 record. Its fields match Keynote's sound: 14 `{ 1: 16 }`, 9 = 1, 23 = 0, sizes of 0 × 0 and `soun` in 29.1.1. Its drawable's field 1.2 names the sheet (904532), as a slide's objects name the slide.

## Conclusion

All three apps store sounds and movies as the same type-3007 record. A reader can handle media once for every app: find the file by the data ID in field 14, and the poster image, if any, in field 15.

## Confidence

*Confirmed*, with 0185 and 0187: sounds and movies are type 3007, naming their file in field 14, in all three apps.
