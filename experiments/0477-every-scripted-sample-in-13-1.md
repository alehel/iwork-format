# 0477: Every scripted sample in 13.1

**Status:** run

[0473](0473-every-scripted-sample-in-16-0.md) and [0475](0475-every-scripted-sample-in-14-5.md) made every sample a recipe makes on its own again in 16.0 and 14.5. The 13.1 apps are kept on a disk image too, so this experiment does the same in 13.1, the oldest release tried.

## Setup

| | |
| --- | --- |
| Apps | Pages, Numbers and Keynote 13.1 (build `M13.1-7037.0.101-2`), in Norwegian, run from a read-only disk image while the installed 16.0 apps weren't running |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-24 |
| Theme | Keynote: `iwork-format test v2` ([0291](0291-test-theme.md)), the theme as it is in `theme/`, which 13.1 lists among its themes |
| Script | [`recipes/0473-release-set.py`](../recipes/0473-release-set.py), whose `--compare` now also knows the differences every 13.1 document has (`BY_RELEASE`) |

## Recipe

```bash
hdiutil attach -readonly -nobrowse ~/Desktop/backup/iwork-13-1.dmg
for a in Pages Numbers Keynote; do open -g -a /Volumes/iwork-13-1/$a.app; done
python3 -I recipes/0473-release-set.py 13.1
sed -e 's/, radial wipe}/}/' -e 's/, "radial wipe"}/}/' recipes/0196-keynote-all-transitions.applescript > /tmp/0196.applescript
IWORK_KEYNOTE_THEME='iwork-format test v2' osascript /tmp/0196.applescript "$PWD/samples/release/13.1/0196/all.key"
python3 -I recipes/0473-release-set.py 13.1 --compare
```

189 of the 190 commands ran at the first try. 0196 doesn't compile in 13.1, which doesn't know `radial wipe`, so it was run without that effect, as in 14.5.

## Observation

319 documents, the same names as the 14.5 and 16.0 sets. Those that aren't encrypted end their build history with `M13.1-7037.0.101-2`; new Pages and Numbers documents name their templates `Template: Blank (13.1)` and `Template: Blank (11.2)`. Their `fileFormatVersion` is `13.1.2`.

| `--compare` | Documents |
| --- | --- |
| The same as 15.4 but for what every 13.1 document differs in | 306 |
| Different | 7 |
| Not compared: encrypted | 6 |

What every 13.1 document differs in:

| | 15.4 | 13.1 |
| --- | --- | --- |
| `Properties.plist` | `hasExternalReferenceOrMissingData` and `hasUnmaterializedRemoteData` | neither, nor 14.5's one combined flag |
| `CalculationEngine.iwa` | the empty type-4011 record, named by type 4000's field 15 | neither, as in 14.5 |
| Formula owners (type 4008) | field 16, empty | no field 16; 14.5 has it |
| Table models (type 6001) | field 93 | no field 93; 14.5 has it |
| Slide nodes (type 4) | field 32 | no field 32, as in 14.5 |
| Pages' view state (type 10133) | field 47, naming two objects | field 29, naming two objects the same way. 14.5 uses 47 |
| Text records (type 2001) whose text a recipe set | no field 19 | field 19, the language `nb`, in 49 of 63 Pages documents, 15 of 74 presentations and 1 of 182 spreadsheets. No 14.5 or 16.0 document of the sets has one |

The last is where 13.1 differs in what it records rather than in how: text set through AppleScript gets the language entry that 15.4 gives only text typed or rewritten in the app ([0006](0006-typing-in-pages.md)).

The seven:

| Document | Difference | Why |
| --- | --- | --- |
| `0196/all.key` | 37 slides, not 38 | made without radial wipe |
| `0090/theme.key` | two template slides fewer, one paragraph style more | made from Basic Black, Apple's theme, which differs between releases |
| `0158/essay.pages`, `0199/letter.pages` | no field 10 on the date fields (type 2034), which 15.4 writes as 0; the essay has one paragraph style fewer | made from Apple's templates. 14.5 lacks field 10 too ([0475](0475-every-scripted-sample-in-14-5.md)), and whether it comes with the template or the release is *unknown* |
| `0223/INDEX.numbers`, `0248/COLUMNS.numbers`, `0248/ROWS.numbers` | a type-4010 record in the calculation engine | 13.1 keeps one for formulas whose functions read a whole range; none in 14.5's, 15.4's or 16.0's copies |

The type-4010 record's field 1 is the number of the owner (6 in all three) and field 2 holds a cell and a range of rows and columns. That is bookkeeping about which cells a formula depends on, kept with the owners a reader can skip ([numbers.md](../spec/numbers.md#the-calculation-engine)).

The six encrypted documents were made too; the four Pages ones decrypt with their test passwords in `iwork-probe` and hold `one`.

## Conclusion

Every document the recipes make comes out of 13.1 with the structure 15.4 gives it, apart from a short list of fields, the radial wipe, and Apple's own templates. 13.1 lacks everything 14.5 lacks, and two fields more (4008.16 and 6001.93). What it has that 15.4 lacks is a language on scripted text, another number for one view-state field, and type-4010 records for some formulas.

A reader of 15.4 documents needs to change nothing to read a 13.1 document, except to accept a missing field 93 on a table model and field 16 on an owner, and a language entry on text 15.4 leaves without one. A choice of 13.1's set, enough to hold every field path the set holds, is published with the fixtures under `release/13.1/` ([`fixtures/SELECTED.txt`](../fixtures/SELECTED.txt)).

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `release/13.1/**` | | `11006#2 7 = x"0d0102"` in every one | *Confirmed*: 306 documents made in 13.1 have 15.4's structure, but for what every 13.1 document differs in; the recipe compares them |

## Confidence

*Confirmed*: for 306 documents made by the experiments' recipes, 13.1 writes the same structure as 15.4, apart from the differences every 13.1 document has. *Likely*: that 13.1 keeps type-4010 records for formulas over a range.
