# 0186: A looping sound at half volume

**Status:** run

AppleScript can set an audio clip's volume and whether it repeats. This experiment changes both, to find their fields in the type-3007 record from [0185](0185-keynote-audio.md).

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0185](0185-keynote-audio.md), `audio.key` |

## Recipe

```bash
osascript recipes/0185-keynote-media.applescript loop "$PWD/samples/0185/loop.key" "$PWD/samples/0185/tone.m4a"
```

The recipe adds the sound from 0185, then sets its `repetition method` to `loop` and its `clip volume` to 50.

## Observation

Apart from IDs, the type-3007 record differs from 0185's in two fields:

| Field | 0185 | Looping, volume 50 |
| --- | --- | --- |
| 7 | 1.0 | 0.5 |
| 24 | 0 | 1 |

## Conclusion

Field 7 is the volume, as a fraction of full volume: AppleScript's 0–100 scale divided by 100. Field 24 is the repetition: 0 for none and 1 for loop. Loop back and forth is probably 2.

## Confidence

*Likely*: field 7 is the volume and field 24 the repetition.

*Unknown*: the value for loop back and forth.
