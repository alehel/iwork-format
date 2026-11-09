# 0187: A movie in Keynote

**Status:** run

[0185](0185-keynote-audio.md) found that a sound is a type-3007 record. This experiment adds a movie, to see how pictures change it.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0185](0185-keynote-audio.md), `audio.key` |

## Recipe

```bash
cd samples/0185
ffmpeg -f lavfi -i color=c=red:s=64x48:d=1 -c:v libx264 -pix_fmt yuv420p clip.mov
cd ../..
osascript recipes/0185-keynote-media.applescript movie "$PWD/samples/0185/movie.key" "$PWD/samples/0185/clip.mov"
```

`clip.mov` is a one-second, 64 × 48 red H.264 movie. As with the sound, the recipe adds it through `make new image`.

## Observation

The package gains `Data/clip-9076.mov`, the movie unchanged, and `Data/posterImage-9077.png`, a 64 × 48 PNG. The slide's part has one type-3007 record, which differs from the sound's in:

| Field | Sound (0185) | Movie |
| --- | --- | --- |
| 1.1, geometry | (960, 540), 0 × 0 | (928, 516), 64 × 48 |
| 9 | 1 | 0 |
| 15 | absent | `{ 1: 9077 }`, the poster image |
| 20, 21 | 0 × 0 | 64 × 48 |
| 23 | 0 | 1 |
| 29.1.1 | `soun` | `vide` |
| 29.1.8, 29.1.9 | 8000 | 1000 |

The movie's position, (928, 516), puts its centre at (960, 540), the middle of the 1920 × 1080 slide.

## Conclusion

A movie is the same type-3007 record as a sound. Field 14 names the movie file and field 15 a poster image that Keynote makes from its first frame. A reader that can't play the movie can show that image instead. Fields 20 and 21 are the movie's natural size; field 23 is 1 when it has pictures, and field 9 is 1 when it has only sound. Field 29 describes the first track, here `vide` with a time scale of 1000.

## Confidence

*Likely*:

- A movie is type 3007, with its file in field 14 and its poster image in field 15.
- Fields 9 and 23 tell sound from pictures, and 20 and 21 hold the natural size.
