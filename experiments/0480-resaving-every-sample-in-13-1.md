# 0480: Resaving every sample in 13.1

**Status:** run

[0476](0476-resaving-every-sample.md) opened every 15.4 sample in 16.0 and saved a copy, to see how it writes every feature in the samples, those made by hand included. This experiment does the same in 13.1.

## Setup

| | |
| --- | --- |
| Apps | Pages, Numbers and Keynote 13.1 (build `M13.1-7037.0.101-2`), in Norwegian, run from a read-only disk image |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-24 |
| Input | The same 1,211 documents as 0476 |
| Script | [`recipes/0476-resave.py`](../recipes/0476-resave.py), which now also takes `--apps` to keep to some of the apps |

## Recipe

```bash
export IWORK_APP_DIR=/Volumes/iwork-13-1
python3 -I recipes/0476-resave.py 13.1
python3 -I recipes/0476-resave.py 13.1 --apps Numbers,Keynote
python3 -I recipes/0476-resave.py 13.1 --apps Pages --skip 0262,0273,0274,0336
python3 -I recipes/0476-resave.py 13.1 --compare
python3 -I recipes/0476-resave.py 13.1 --pair 16.0
```

The run wasn't done in one go. Pages stopped at 0262's document, with 13.1's warning that the document was made in a newer version ([0479](0479-drawing-15-4-samples-in-13-1.md)), and the next nine documents couldn't be opened until the window was dismissed. The Numbers and Keynote documents were saved meanwhile, then the rest of Pages' without 0262, 0273, 0274 and 0336, and the nine documents of those four experiments by hand, `save d in` each, after the warning was clicked through. Checksums of every sample taken before the runs still matched.

## Observation

All 1,211 samples were saved by 13.1.

**13.1 against 16.0.** With what is already known to differ between the two set aside, 994 of the 1,211 pairs are the same, and 217 differ. 172 of the 217 differ only in the view state (`ViewState.iwa`: fewer records of types 2002, 3061, 3062 and 6030, and no field 7 on type 10132, which show what was selected), which a reader can ignore. The other 45:

| What differs in 13.1's copy | Documents |
| --- | --- |
| A type-4010 record in the calculation engine, one more than 16.0's | 13 spreadsheets from 0226, 0227, 0279, 0410 and 0411, with categories and pivot tables |
| No field 10 on date fields (type 2034), which the 15.4 originals have and 16.0 keeps, as 0 | 12 Pages documents |
| Fields 7 and 13 of the engine's root (type 4000) and 4, 5 and 9 of formula owners (type 4008), which 16.0's copies lack | 11 spreadsheets, eight from [0409](0409-writing-a-numbers-chart-link.md), and 0030, 0063 and 0225 |
| A record or two more: type 3047 in `Document.iwa`, or types 8 and 153 (a build and its stage) on a slide whose build list the writer took out | 2 Pages documents, 2 presentations |
| Field 5 of the engine's root, where 16.0's copy has field 15 instead: the two copies 16.0 made differently in its two runs in 0476 | 1 spreadsheet (`0248/SMALL.numbers`), 1 presentation (`theme/0195/line_3d-row.key`) |
| No field 14 on drawables (type 6000) | 2 Pages documents |
| Field 1 of the comment author storage (type 213), which the original has too and 16.0 drops | 1 Pages document (`0193/empty-comment.pages`) |

Field 10 of date fields, *unknown* in [0475](0475-every-scripted-sample-in-14-5.md), is therefore not just from a template: 13.1 drops it from documents that have it, and 16.0 keeps it.

**13.1 against the 15.4 originals.** 877 copies are the same as their originals but for 13.1's known differences, 329 differ, and 5 folder packages weren't compared. In the calculation engine and slide nodes they are the changes 0476 found saving makes in 16.0, the slide nodes' field 20 (92 presentations) among them.

## Conclusion

13.1 writes the features in all 1,211 samples as 16.0 does, hand-made ones included, apart from its view state and 45 documents' few fields and records above. What it leaves out is what 13.1 doesn't know, and those are fields a reader doesn't need.

Saving through an older release loses what that release doesn't know: the date fields' field 10 and the drawables' field 14 are gone from 13.1's copies.

## Confidence

*Confirmed*: 13.1 saves all 1,211 samples, and 994 of its copies have the same structure as 16.0's but for what is known to differ. *Likely*: fields absent from its copies and present in the others' are ones 13.1 doesn't know.
