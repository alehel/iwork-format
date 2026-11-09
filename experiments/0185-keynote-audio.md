# 0185: A sound in Keynote

**Status:** run

This experiment puts a sound on a slide, to see how Keynote stores media.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0168/untouched.key`, a new presentation |

## Recipe

```bash
mkdir -p samples/0185
cd samples/0185
python3 -c "import wave,struct,math; w=wave.open('tone.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(8000); w.writeframes(b''.join(struct.pack('<h',int(8000*math.sin(2*math.pi*440*i/8000))) for i in range(8000))); w.close()"
afconvert -f m4af -d aac tone.wav tone.m4a
cd ../..
osascript recipes/0185-keynote-media.applescript audio "$PWD/samples/0185/audio.key" "$PWD/samples/0185/tone.m4a"
```

`tone.m4a` is a one-second, 440 Hz AAC tone. Making an `audio clip` through AppleScript adds nothing: the slide's count of audio clips stays 0. Making an `image` from the sound file adds an audio clip instead, so the recipe does that.

## Observation

`tone.m4a` is stored unchanged as `Data/tone-9076.m4a`. The slide's part gains one record of type 3007:

```
1:  drawable: 1.1 geometry, 1.2 { 1: 2652175 } (the slide)
3:  0.0
4:  1.0
5:  0.0
7:  1.0
9:  1
14: { 1: 9076 }           ← the data ID of the sound file
20: { 1: 0.0, 2: 0.0 }
21: { 1: 0.0, 2: 0.0 }
23: 0
24: 0
29: { 1: { 1: "soun", 2: 1, 3: 1445, 4: "1c14dd8a…", 8: 8000, 9: 8000, …, 19: "und" }, 2: 01 00 00 }
```

The drawable is at (960, 540), the middle of the slide, with a size of 0 × 0. The hex text in 29.1.4 is not the SHA-1 of the file.

## Conclusion

A sound is stored as a type-3007 record, the same type as a movie ([0187](0187-keynote-movie.md)). Its field 14 names the media file by data ID, as an image names its file. Field 29 describes the media's first track: its kind (`soun`), its time scale (8000, the sample rate) and its language (`und`, undetermined). Fields 3–5 are probably the start, end and poster times in seconds, with the end at the one-second length. Field 9 is 1 for a sound with no picture.

## Confidence

*Likely*: a sound is a type-3007 record that names its file in field 14.

*Unknown*: fields 3–5, 29.1.3 and 29.1.4.
