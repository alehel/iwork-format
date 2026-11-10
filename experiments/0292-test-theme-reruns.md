# 0292: Keynote experiments again, with the test theme

**Status:** run

The Keynote findings so far all come from presentations in Basic White, Keynote's default theme. [0291](0291-test-theme.md) built a test theme from Basic White, with the project's own images in place of Apple's photos. This experiment reruns every Keynote experiment whose recipe needs no clicks with that theme, to see whether anything in the format depends on the theme's images, and whether the resulting files hold only media the project made.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Theme | `iwork-format test`, from [0291](0291-test-theme.md) |
| Compared with | The original samples of each experiment, made with Basic White |

## Recipe

Every Keynote recipe now makes its presentations through one handler, `newKeynote()`. It uses the theme named in the environment variable `IWORK_KEYNOTE_THEME`, or Keynote's default when that is unset, so the original runs are reproduced unchanged. A script collected the recipe commands of the 58 experiments that use only Keynote recipes, and 0024's empty presentations were made the same way. It ran them with every sample path moved under `samples/theme/`:

```bash
export IWORK_KEYNOTE_THEME='iwork-format test'
# the commands of each experiment's Recipe section, with samples/ replaced by samples/theme/
python3 -I recipes/0292-compare-themes.py samples samples/theme
```

[`recipes/0292-compare-themes.py`](../recipes/0292-compare-themes.py) compares each new presentation with its namesake. It checks that every part frames into chunks and records, that every object is reached from the roots through header references, and how many records of each type each holds. It also lists media in `Data/` that isn't the project's own. `iwork-probe text` compared their texts.

The reruns were done twice: first with the test theme's full-size cards, then with the smaller cards it now has ([0291](0291-test-theme.md)). Both runs gave the results below. In the first, 0196, the experiment with every transition, hit an AppleScript timeout once and ran on a second try. 0146 makes a folder package, which the script doesn't read, so it isn't compared.

## Observation

71 presentations from 58 experiments were compared: 0024 and 57 of the 58 rerun, all but 0146.

| Check | Result |
| --- | --- |
| Framing | All parts of all 71 decode |
| Reachability | Every object is reached in all 71 |
| Text | The same texts in all 71, including the masters' placeholder text |
| Media | Only the test cards, their reduced copies, Keynote's thumbnails and the project's own image, sound and movie, except in 0090 |
| Record types | The same counts in all, except for two types |

**0090** sets the presentation's theme on purpose, to theme 2 (Basic Black), so it holds Apple's photos with either default theme.

**Type 11014.** Every Basic White presentation has six type-11014 records in `Metadata.iwa` that the test theme's presentations lack. Each holds a colour: field 1.1 is 1, and fields 1.3 to 1.6 are red, green, blue and alpha as floats. There are as many as there are Basic White photos that are stored only as reduced copies, and the test theme has no such photos.

**Type 4009.** The four presentations with a table (0073, 0134, 0135, 0137) have one or two more type-4009 records with the test theme. Type 4009 records are lists, like Numbers' type 6005, with the kind of list in field 1. In 0073, Basic White's table has lists of kinds 13 and 11 plus one shared with the theme. The test theme's has kinds 14, 5, 12 and 3, plus the shared one.

**Theme photos.** A Basic White photo's entry in the data list (`Metadata.iwa` record 2, field 4) has an empty field 4, so no file is stored. Its field 5 holds a path inside the app (`21_basicwhite/910457886_1434x1669`), and only a reduced copy is in `Data/`, with its own entry. The test theme's cards are stored in full. In every image's entry, field 10.100.1 holds the image's size in pixels, with the width in field 1 and the height in field 2 as floats: 1434 and 1669 for both `910457886_1434x1669` and `photo-a`, 220 and 256 for `photo-a-small`. The reduced copies of the theme's photos also have field 18, the file's size in bytes.

### Experiments that needed clicks

Six more Keynote experiments were redone with the test theme. Four had their clicks made through the accessibility interface: a build in, a build out and an action build on a title ([0257](0257-build.md), [0263](0263-build-out.md), [0264](0264-action-build.md)), and a dynamic background ([0271](0271-dynamic-background.md)), plus their plain baselines. [0180](0180-password-in-other-apps.md)'s password-protected presentation was remade by its recipe, and 0272 is described below. The sidebar showed the same settings as in the original experiments, and each presentation's slide parts hold the same record types as the original's. Compared as above, the only differences are again the six type-11014 records.

The dynamic background's first preset came out with an angle of 33.7°, a scale of 1.42 and a speed of 41.57, against 352.7°, 1.40 and 41.67 the first time, so Keynote varies them. Its still, `motionBackground-N.jpeg`, was byte for byte the same file both times, so the still doesn't follow the settings. [0272](0272-self-playing.md)'s self-playing presentation was redone with screen control, since its setting is a pop-up menu. Its presentation record holds the same values as the original's: field 9 is 1, and fields 10 and 11 are the delays of 5.0 and 2.0 seconds.

## Conclusion

Apart from its photos, the test theme makes presentations that are structurally the same as Basic White's. The objects, references, texts and record types match across 58 experiments. So the Keynote findings don't depend on Basic White's images. These presentations can stand in for the originals as published samples, all except 0090.

A theme's photos can stay inside the app. Keynote then stores only a reduced copy and a path to the full image, and the six type-11014 colours are probably one per such photo. What the extra type-4009 lists mean, and why the test theme's tables have them, was *unknown* here; [0293](0293-calculation-owners.md) found they belong to the calculation engine's owners.

## Confidence

*Likely*:

- Keynote's structure doesn't depend on the theme's images.
- A theme photo can stay in the app, with only a path and a reduced copy in the file.
- An image's data entry holds its size in pixels in field 10.100.1.

*Unknown*: type 11014's link to the photos (since found in [0294](0294-resource-colours.md)); why the type-4009 lists differ.
