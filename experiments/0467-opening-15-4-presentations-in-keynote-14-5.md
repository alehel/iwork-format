# 0467: Opening 15.4 presentations in Keynote 14.5

**Status:** run

Keynote 14.5 writes the same format as 15.4 ([0466](0466-keynote-14-5.md)). This experiment opens every Keynote sample of the earlier experiments, made or written with Keynote 15.4, in 14.5, and checks what it reads, as [0462](0462-opening-15-4-documents-in-14-5.md) did for Pages and Numbers.

## Setup

| | |
| --- | --- |
| Keynote | 14.5 (build `M14.5-7045.0.17-4`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-24 |
| Input | Every `.key` under `samples/NNNN/` and `samples/theme/NNNN/` (the test-theme reruns of [0292](0292-test-theme-reruns.md)), except experiment 0466's, which 14.5 saved, those of [0379](0379-writing-a-slide-layout.md), written to make Keynote quit, and `0180/accent.key`, which is password-protected: 323 presentations, from Keynote itself and from the writing experiments |
| Script | The new [`recipes/0467-open-keynote.py`](../recipes/0467-open-keynote.py), which opens each with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh), asks Keynote for the number of slides and each slide's title (when it shows) and presenter notes, and checks that the number matches the slide nodes the presentation lists (type 2, field 3.2) and that every title and note equals a text record in the file's slide parts, as `iwork-probe text` prints it |

## Recipe

```bash
python3 -I recipes/0467-open-keynote.py samples 0379,0180,0466
python3 -I recipes/0467-open-keynote.py samples/theme 0379,0180
mkdir -p samples/0467 && cp samples/0196/all.key samples/0467/all-copy.key
sh recipes/0372-in-app.sh Keynote samples/0196/all.key 'set p to transition properties of slide 37 of d
return transition effect of p'
sh recipes/0372-in-app.sh Keynote samples/0196/all.key 'set p to transition properties of slide 38 of d
return transition effect of p'
sh recipes/0372-in-app.sh Keynote samples/0467/all-copy.key "set t to object text of default title item of slide 38 of d
save d in POSIX file \"$PWD/samples/0467/resaved.key\"
return t"
grep -rl -a "radial wipe" /Applications/Keynote.app/Contents
```

The comparison leaves out white space, control and format characters (such as the soft hyphens in Basic White's prompts) and U+FFFC on both sides.

## Observation

| Result | Presentations |
| --- | --- |
| Opened; slide count, titles and notes agree with the file | 323 (244 under `samples/NNNN/`, 79 under `samples/theme/`), 486 slides |
| Opened, but don't agree | 0 |
| Not opened | 0 |

No alert was shown.

One reading failed outside these checks. [0196](0196-every-transition.md)'s presentation has one slide per transition effect, and 14.5 reports the effect of slides 35 to 37 (`twirl`, `twist`, `fade and move`), but asking for slide 38's effect, `apple:radial wipe`, fails with "AppleEvent handler failed". It reads that slide's title, `radial wipe`. Saved again by 14.5, the presentation still holds `apple:radial wipe` on that slide, and its build history then lists both builds, `M15.4-7051.0.79-2` and `M14.5-7045.0.17-4`. No file in Keynote 14.5's bundle contains the string `radial wipe`, and its AppleScript dictionary has no such effect ([0466](0466-keynote-14-5.md)).

## Conclusion

Keynote 14.5 opens every presentation Keynote 15.4 saved in these experiments, and every one written from this spec, and reads the same slides, titles and notes from them. Nothing 15.4 writes stops it reading a presentation, including slide-node field 32, which 14.5 doesn't write.

The radial wipe transition is new in 15.4. 14.5 keeps its identifier through a save, but doesn't know the effect: its AppleScript can't report it. How 14.5 plays such a slide wasn't tested. A writer that wants a presentation to play the same in 14.5 should avoid `apple:radial wipe`.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `all-copy.key` | `0196/all.key` | `same bytes` | *Control*: opened in 14.5, which can't report the effect of slide 38 |
| `resaved.key` | `all-copy.key` | `11006#2 7: x"1a0400" → x"0e0401"`, `5 4.2.8.2 = "apple:radial wipe"` | *Likely*: 14.5 keeps the radial wipe identifier when it saves |

## Confidence

*Confirmed*: Keynote 14.5 opens 323 presentations from 15.4 and from the spec's writer and reads the same slides, titles and notes. *Likely*: radial wipe is a 15.4 effect that 14.5 keeps but doesn't know.
