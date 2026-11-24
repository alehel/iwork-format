# 0474: Keynote 14.5 with the test theme

**Status:** run

Keynote 14.5's presentations in [0466](0466-keynote-14-5.md) were made with Basic White, so none can be published. 14.5 was replaced by 16.0 since, but is kept on a disk image. This experiment runs Keynote 14.5 from that image, beside the installed 16.0, and remakes 0466's presentations with the project's test theme, as [0472](0472-keynote-16-0-with-the-test-theme.md) did for 16.0.

## Setup

| | |
| --- | --- |
| Keynote | 14.5 (build `M14.5-7045.0.17-4`), in Norwegian, run from a read-only disk image (`/Volumes/iwork-14-5/Keynote.app`) while Keynote 16.0 stayed installed but wasn't running |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-24 |
| Theme | `iwork-format test` ([0291](0291-test-theme.md)), which 14.5 lists among its themes |
| Recipes | The 14 Keynote recipes of 0466, through [`recipes/0472-keynote-test-theme-rerun.sh`](../recipes/0472-keynote-test-theme-rerun.sh); 0196 without radial wipe, as in 0466 |
| Compared with | Each recipe's test-theme presentation from 15.4, under `samples/theme/` ([0292](0292-test-theme-reruns.md)) |

## Recipe

```bash
hdiutil attach -readonly -nobrowse ~/Desktop/backup/iwork-14-5.dmg
osascript -e 'tell application "Keynote Creator Studio" to quit'
open -a /Volumes/iwork-14-5/Keynote.app
osascript -e 'tell application "Keynote" to get version'     # 14.5
bash recipes/0472-keynote-test-theme-rerun.sh samples/theme/0474
sed -e 's/, radial wipe}/}/' -e 's/, "radial wipe"}/}/' recipes/0196-keynote-all-transitions.applescript > /tmp/0196.applescript
IWORK_KEYNOTE_THEME='iwork-format test' osascript /tmp/0196.applescript "$PWD/samples/theme/0474/0196-all.key"
python3 -I recipes/0461-compare-structure.py samples/theme/0196/all.key samples/theme/0474/0196-all.key
```

With 14.5 running, AppleScript's `tell application "Keynote"`, as the recipes say it, reached 14.5, not the installed 16.0 ("Keynote Creator Studio", the same bundle ID). Every presentation's build history ends with `M14.5-7045.0.17-4`, after the theme's own `M15.4-7051.0.79-2`, as in 0472.

## Observation

Every recipe ran but 0196, whose script doesn't compile in 14.5 because of `radial wipe`; without that effect it made 37 slides instead of 38.

In all 16 pairs, the differences from 15.4 are those 0466 found between 14.5 and 15.4 with Basic White, and no others:

| | 15.4 | 14.5 |
| --- | --- | --- |
| `Properties.plist` | the two flags | the one combined flag |
| `CalculationEngine.iwa` | the empty type-4011 record, named by type 4000's field 15 | neither |
| Slide nodes (type 4) | field 32 | no field 32 |
| Master thumbnails | 16 | 16, with other UUIDs |
| `0196-all.key` | 38 slides | 37: no radial wipe slide |

Two of 0466's differences don't appear: 14.5 has the same paragraph styles as 15.4 here, without the unnamed 56-point *Liten infotekst* variation, and it doesn't store `blankMoviePosterImage` in the package. Both come with 14.5's own Basic White template; the test theme, made from 15.4's Basic White, brings 15.4's styles and resources with it.

The fixtures builder keeps all 16.

## Conclusion

With the test theme, Keynote 14.5 writes the presentations of these recipes with the same structure as 15.4 and 16.0, apart from the flag, the type-4011 record and slide-node field 32 that every 14.5 document lacks. The paragraph style and stored poster image that 0466 found are differences in 14.5's Basic White, not in how it writes. They are published with the fixtures under `keynote/0474/`, the first presentations from 14.5 there.

## Confidence

*Confirmed*: for these 16 presentations, Keynote 14.5 with the test theme differs from 15.4 only as every 14.5 document does. *Likely*: the extra paragraph style and stored poster image of 0466 belong to 14.5's Basic White.
