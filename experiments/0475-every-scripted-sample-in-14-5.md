# 0475: Every scripted sample in 14.5

**Status:** run

[0473](0473-every-scripted-sample-in-16-0.md) made a script that remakes every sample the experiments' recipes make on their own, and ran it in 16.0. This experiment runs it in 14.5, whose apps are kept on a disk image, so 14.5 has a set of its own too.

## Setup

| | |
| --- | --- |
| Apps | Pages, Numbers and Keynote 14.5 (build `M14.5-7045.0.17-4`), in Norwegian, run from a read-only disk image while the installed 16.0 apps weren't running |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-24 |
| Theme | Keynote: `iwork-format test` ([0291](0291-test-theme.md)) |
| Script | [`recipes/0473-release-set.py`](../recipes/0473-release-set.py), whose `--compare` now also knows the differences every 14.5 document has (`BY_RELEASE`) |

## Recipe

```bash
hdiutil attach -readonly -nobrowse ~/Desktop/backup/iwork-14-5.dmg
for a in Pages Numbers Keynote; do open -g -a /Volumes/iwork-14-5/$a.app; done
python3 -I recipes/0473-release-set.py 14.5
python3 -I recipes/0473-release-set.py 14.5 --only 0001
sed -e 's/, radial wipe}/}/' -e 's/, "radial wipe"}/}/' recipes/0196-keynote-all-transitions.applescript > /tmp/0196.applescript
IWORK_KEYNOTE_THEME='iwork-format test' osascript /tmp/0196.applescript "$PWD/samples/release/14.5/0196/all.key"
python3 -I recipes/0473-release-set.py 14.5 --compare
```

With the 14.5 apps running, the recipes' `tell application "Pages"` and so on reached them, not the installed 16.0 apps, which share their bundle IDs. 188 of the 190 commands ran at the first try. The first, 0001's `empty-a.pages`, timed out while Pages was still starting, and ran on a second try with `--only 0001`. 0196 doesn't compile in 14.5, which doesn't know `radial wipe`, so it was run without that effect, as in [0466](0466-keynote-14-5.md).

## Observation

319 documents, the same names as the 16.0 set. The 313 that aren't encrypted all end their build history with `M14.5-7045.0.17-4`.

| `--compare` | Documents |
| --- | --- |
| The same as 15.4 but for what every 14.5 document differs in | 308 |
| Different | 5 |
| Not compared: encrypted | 6 |

What every 14.5 document differs in, from [0461](0461-new-documents-in-14-5.md) and [0466](0466-keynote-14-5.md): the one combined flag in `Properties.plist`, no type-4011 record in the calculation engine nor type 4000's field 15 naming it, no field 32 on slide nodes, and Numbers without *Table Title 1*.

The five:

| Document | Difference | Why |
| --- | --- | --- |
| `0196/all.key` | 37 slides, not 38 | made without radial wipe |
| `0090/theme.key` | the blank movie poster stored in the package, one paragraph style more | made from Basic Black, Apple's theme, whose 14.5 copy differs as Basic White's does ([0474](0474-keynote-14-5-with-the-test-theme.md)) |
| `0158/essay.pages`, `0199/letter.pages` | field 10 of the date fields (type 2034), 0 in 15.4, absent in 14.5 | made from Apple's templates; whether the field comes with the template or with the release is *unknown*, since no recipe makes a date field outside them |
| `0024/empty-a.numbers` | 1 record each of types 3061 and 6030 in `ViewState.iwa`, not 5 | how the first document after Numbers started was last shown; `empty-b.numbers`, made right after, has 5 as 15.4 |

The six encrypted documents decrypt with their test passwords in `iwork-probe`, and the Pages ones hold `one`.

## Conclusion

Every document the recipes make comes out of 14.5 with the structure 15.4 gives it, apart from the differences every 14.5 document has, the radial wipe, and three made from Apple's own templates, which differ between releases. 14.5's set is published with the fixtures under `release/14.5/`, beside 16.0's, with the same names, so a reader can be tested on the same content from three releases.

A date field's (type 2034, [text.md](../spec/text.md)) field 10, which 15.4 writes as 0 in the date fields of Apple's essay and letter templates, is new to this experiment; what it holds is *unknown*.

## Confidence

*Confirmed*: for 308 documents made by the experiments' recipes, 14.5 writes the same structure as 15.4, apart from the differences every 14.5 document has.
