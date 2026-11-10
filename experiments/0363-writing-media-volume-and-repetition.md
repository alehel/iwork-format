# 0363: Writing a sound's volume and repetition

**Status:** run

A sound or movie is a type-3007 record whose field 7 is the volume, from 0 to 1, and field 24 the repetition, 0 none and 1 loop ([0185](0185-keynote-audio.md)). This experiment writes both into a sound and a movie and reads them back through Keynote's AppleScript properties: `clip volume` and `repetition method` for an audio clip, and `movie volume` and `repetition method` for a movie.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0185/audio.key` and `samples/0185/movie.key`: one slide with a sound or a movie, record 2652476, volume 1.0 and repetition 0 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py), with the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0363
R=recipes/0302-set-path.py
python3 -I $R samples/0185/audio.key samples/0363/quarter-loop.key 2652476 7 float 0.25 24 varint 1
python3 -I $R samples/0185/audio.key samples/0363/back-and-forth.key 2652476 24 varint 2
python3 -I $R samples/0185/movie.key samples/0363/movie-silent.key 2652476 7 float 0 24 varint 2
```

Keynote opened each file on its own and read the properties of the media on slide 1.

## Observation

| File | Field 7 | Field 24 | Volume | Repetition method |
| --- | --- | --- | --- | --- |
| `audio.key` | 1.0 | 0 | 100 | none |
| `quarter-loop.key` | 0.25 | 1 | 25 | loop |
| `back-and-forth.key` | 1.0 | 2 | 100 | loop back and forth |
| `movie.key` | 1.0 | 0 | 100 | none |
| `movie-silent.key` | 0 | 2 | 0 | loop back and forth |

## Conclusion

Field 7 is the volume as a fraction, which AppleScript shows as a percentage. Field 24 is the repetition: 0 none, 1 loop and 2 loop back and forth. The same fields work for a sound and a movie.

## Confidence

*Confirmed*: field 7 as the volume and field 24 as the repetition, with 2 meaning loop back and forth, by writing them.
