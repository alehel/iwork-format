# 0476: Resaving every sample in 16.0 and 14.5

**Status:** run

[0473](0473-every-scripted-sample-in-16-0.md) and [0475](0475-every-scripted-sample-in-14-5.md) remade every sample a recipe makes on its own. The others, made by hand in the apps (comments, tracked changes, pivot tables, highlighting rules, gradients, shadows, masks) or written by the spec's writer, a later release has only read ([0470](0470-opening-15-4-samples-in-16-0.md)), never written. This experiment opens every 15.4 sample in 16.0 and in 14.5 and saves a copy. Saving writes the whole document out again from what the app read, so the copies show how each release writes every feature in the samples.

## Setup

| | |
| --- | --- |
| Apps | Pages, Numbers and Keynote 16.0, installed; and 14.5, run from its disk image while the 16.0 apps weren't running |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-24 |
| Input | Every `.pages`, `.numbers` and `.key` directly under `samples/NNNN/` (0001 to 0460) and `samples/theme/NNNN/`, as in 0470: 1,211 documents. Left out: 0179 and 0180, whose password prompt would hold the run up, and the files written to make an app fail (0379, 0394, 0396, 0424, 0434, 0451) |
| Script | The new [`recipes/0476-resave.py`](../recipes/0476-resave.py), which opens each sample with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh), saves it with `save d in` under `samples/resave/RELEASE/`, checks that the original's modification time didn't change, and compares the copies |

## Recipe

```bash
python3 -I recipes/0476-resave.py 16.0
python3 -I recipes/0476-resave.py 16.0 --compare           # each copy against its 15.4 original
# with the 14.5 apps started from the disk image instead:
python3 -I recipes/0476-resave.py 14.5
python3 -I recipes/0476-resave.py 14.5 --compare
python3 -I recipes/0476-resave.py 16.0 --pair 14.5         # each 16.0 copy against 14.5's
```

`--compare` reuses [`recipes/0473-release-set.py`](../recipes/0473-release-set.py)'s comparison, with each copy against its own original. `--pair` compares the two releases' copies of the same sample with each other, so that whatever saving does in both cancels out.

In 16.0, Pages stopped answering AppleScript once, on five documents of [0402](0402-writing-repeated-header-rows.md) in a row, and then quit; the script stops after five failures in a row. Resumed without 0402, the run finished, and the five documents then saved at the first try, in six seconds. In 14.5, every document saved at the first try. The originals' modification times didn't change.

## Observation

All 1,211 samples were saved by both releases.

**16.0 against 14.5.** 1,208 of the 1,211 pairs are the same, apart from what is already known to differ between 14.5 and 16.0 ([spec/releases.md](../spec/releases.md)). The three others differ in parts that vary from run to run: the calculation engine's locale fields and type-4011 record (`0248/SMALL.numbers`, `theme/0195/line_3d-row.key`) and a view-state record (`0423/table-first.pages`). Saved once more in 16.0, all three came out like 14.5's.

**Each copy against its 15.4 original.** 1,024 of 16.0's copies and 1,025 of 14.5's are the same as their originals, apart from the release's known differences. The about 181 others are the same documents in both releases, so what they differ in is what saving does, in either release:

| What saving changes | Where |
| --- | --- |
| Fields 5 and 16 of the calculation engine's root (type 4000), the locale `nb_NO`, are written | Every document that had been saved only once; 15.4 does the same ([0139](0139-resave.md)'s `resaved.pages`) |
| Slide nodes (type 4) get field 20, and in three presentations field 15 | 92 presentations, mostly those with charts (0195, 0399, 0456 to 0459) and the test-theme reruns; 15.4 wrote field 20 too when a presentation was saved by hand (0296's) |
| Fields the spec's writer added that the app doesn't keep are dropped, such as fields of cell styles (type 6001) and of formula owners (type 4008) | Writing experiments, 0287 to 0459 |
| Data files are renamed to the app's own form, and unused ones left out | 13 documents, such as 0431's non-ASCII name and 0435's unused file |
| `isMultiPage` in `Properties.plist` set to match the document | 15 documents, mostly written with page breaks or section settings (0359, 0361, 0362, 0366) |
| Records counted again, such as section records (types 3047 and 3006) and view-state records | Some of the writing experiments, and documents last shown in another way |

**View-state fields.** [0469](0469-the-16-0-apps.md) took field 49 of Pages' type 10133, fields 34 and 35 of Numbers' type 12026, field 43 of Keynote's type 3 and field 13 of its type 23 to be new in 16.0. 14.5 writes them too, in every copy it saved here, though not in the new documents it made in 0461, 0464 and 0466. No 15.4 sample has them. 16.0 writes them in every document, new or opened.

## Conclusion

The two releases write every feature in the samples the same way, including those only ever made by hand: comments, tracked changes, highlights, pivot tables, categories, filters, highlighting rules, gradients, shadows, masks, media, builds and transitions. Every difference between a copy and its 15.4 original is one both releases make when they save, not one between releases. Since 14.5 and 15.4 differ only in the known details, and 15.4 is no longer installed to be tried, this is as close as can be checked to saying 16.0 writes these features as 15.4 did.

Resaving is a good test of a writer: what the app drops or rewrites shows which written fields it keeps. The fields dropped here are listed by `--compare` per document; which of them the spec describes is for a later experiment to sort out.

The view-state fields aren't a 16.0 change: 14.5 writes them too when it saves a document it opened. When the apps write them is *unknown*, and so is what they hold.

## Published copies

The 182 copies 16.0 changed are kept in `samples/resaved/16.0/` and published with the fixtures under `resaved/16.0/`, each noting its original. The fixtures builder keeps 154. It leaves out the other 28 for the reasons it leaves out their originals: Basic White's photos, Apple's template text, the project owner's contact details in 0408's merge fields, and data files under names it doesn't know as the project's (0395, 0431). One, `0395/original-name.pages`, is new to that list: saving it gave its image a file named after what the writer had called it, `holiday-24.png`. The copies that didn't change aren't published, since they add nothing to their originals.

## Confidence

*Confirmed*: 16.0 and 14.5 write the same structure for all 1,211 samples when they save them again. *Likely*: so did 15.4, as far as its known differences from 14.5 allow.
