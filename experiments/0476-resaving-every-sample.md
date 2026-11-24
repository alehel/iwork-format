# 0476: Resaving every sample in 16.0

**Status:** run

**Correction ([0481](0481-the-format-version-in-metadata.md)):** this experiment was meant to compare 16.0 with 14.5, and said it had. The copies it called 14.5's were saved by 16.0 too: their build history ends in `M16.0-7052.0.68-2`, because the helper script opens the installed Creator Studio apps whatever else is running. They are a second run in 16.0, and nothing here says how 14.5 saves a document it opens. The text below is corrected.

[0473](0473-every-scripted-sample-in-16-0.md) and [0475](0475-every-scripted-sample-in-14-5.md) remade every sample a recipe makes on its own. The others, made by hand in the apps (comments, tracked changes, pivot tables, highlighting rules, gradients, shadows, masks) or written by the spec's writer, a later release has only read ([0470](0470-opening-15-4-samples-in-16-0.md)), never written. This experiment opens every 15.4 sample in 16.0 and saves a copy, twice. Saving writes the whole document out again from what the app read, so the copies show how 16.0 writes every feature in the samples.

## Setup

| | |
| --- | --- |
| Apps | Pages, Numbers and Keynote 16.0, installed |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-24 |
| Input | Every `.pages`, `.numbers` and `.key` directly under `samples/NNNN/` (0001 to 0460) and `samples/theme/NNNN/`, as in 0470: 1,211 documents. Left out: 0179 and 0180, whose password prompt would hold the run up, and the files written to make an app fail (0379, 0394, 0396, 0424, 0434, 0451) |
| Script | The new [`recipes/0476-resave.py`](../recipes/0476-resave.py), which opens each sample with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh), saves it with `save d in` under `samples/resave/RELEASE/`, checks that the original's modification time didn't change, and compares the copies |

## Recipe

```bash
python3 -I recipes/0476-resave.py 16.0
python3 -I recipes/0476-resave.py 16.0 --compare           # each copy against its 15.4 original
# the second run, meant for 14.5 and saved by 16.0:
python3 -I recipes/0476-resave.py 14.5
python3 -I recipes/0476-resave.py 14.5 --compare
python3 -I recipes/0476-resave.py 16.0 --pair 14.5         # each copy against the second run's
```

`--compare` reuses [`recipes/0473-release-set.py`](../recipes/0473-release-set.py)'s comparison, with each copy against its own original. `--pair` compares two runs' copies of the same sample with each other, so that whatever saving does in both cancels out. Since 0481 the script counts a copy as failed when the release that saved it isn't the one named, so the second run as given above now stops at once.

In 16.0, Pages stopped answering AppleScript once, on five documents of [0402](0402-writing-repeated-header-rows.md) in a row, and then quit; the script stops after five failures in a row. Resumed without 0402, the run finished, and the five documents then saved at the first try, in six seconds. In the second run, every document saved at the first try. The originals' modification times didn't change.

## Observation

All 1,211 samples were saved in both runs.

**The first run against the second.** 1,208 of the 1,211 pairs are the same in structure. The three others differ in parts that vary from run to run: the calculation engine's locale fields and type-4011 record (`0248/SMALL.numbers`, `theme/0195/line_3d-row.key`) and a view-state record (`0423/table-first.pages`). Saved once more, all three came out like the second run's.

**Each copy against its 15.4 original.** 1,024 of the first run's copies and 1,025 of the second's are the same as their originals, apart from 16.0's known differences. The about 181 others are the same documents in both runs, so what they differ in is what saving in 16.0 does:

| What saving changes | Where |
| --- | --- |
| Fields 5 and 16 of the calculation engine's root (type 4000), the locale `nb_NO`, are written | Every document that had been saved only once; 15.4 does the same ([0139](0139-resave.md)'s `resaved.pages`) |
| Slide nodes (type 4) get field 20, and in three presentations field 15 | 92 presentations, mostly those with charts (0195, 0399, 0456 to 0459) and the test-theme reruns; 15.4 wrote field 20 too when a presentation was saved by hand (0296's) |
| Fields the spec's writer added that the app doesn't keep are dropped, such as fields of table models (type 6001; first written here as cell styles) and of formula owners (type 4008) | Writing experiments, 0287 to 0459 |
| Data files are renamed to the app's own form, and unused ones left out | 13 documents, such as 0431's non-ASCII name and 0435's unused file |
| `isMultiPage` in `Properties.plist` set to match the document | 15 documents, mostly written with page breaks or section settings (0359, 0361, 0362, 0366) |
| Records counted again, such as records of types 3047 and 3006 (first written here as section records; 3006 is an image mask, [drawables.md](../spec/drawables.md), and 3047 isn't identified) and view-state records | Some of the writing experiments, and documents last shown in another way |

**View-state fields.** 16.0 writes field 49 of Pages' type 10133, fields 34 and 35 of Numbers' type 12026, field 43 of Keynote's type 3 and field 13 of its type 23, new in 16.0 ([0469](0469-the-16-0-apps.md)), in the documents it opens as well as in new ones.

## Conclusion

16.0 writes every feature in the samples with the structure 15.4 gave it, including those only ever made by hand: comments, tracked changes, highlights, pivot tables, categories, filters, highlighting rules, gradients, shadows, masks, media, builds and transitions. Where a copy differs from its 15.4 original, it is in the ways listed above, the same in both runs. Whether 15.4 changed the same things when it saved is shown only where its own samples were saved again; it is no longer installed to be tried.

Resaving is a good test of a writer: what the app drops or rewrites shows which written fields it keeps. The fields dropped here are listed by `--compare` per document; which of them the spec describes is for a later experiment to sort out.

Two runs of the same release differ in three documents of 1,211, so a difference of that kind and size between releases says nothing.

## Published copies

`fixtures/select.py` chooses copies to publish under `resaved/16.0/`, each noting its original: of the 182 that 16.0 changed, enough to hold every field path they hold, and of the rest, those that hold a path no document of [0473](0473-every-scripted-sample-in-16-0.md)'s set holds, such as features only made by hand. Left out are copies whose originals are left out: Basic White's photos, Apple's template text, the project owner's contact details in 0408's merge fields, and data files under names the builder doesn't know as the project's (0395, 0431).

## Confidence

*Confirmed*: 16.0 saves all 1,211 samples and, in two runs, keeps the structure of 1,024 and 1,025 of them but for its known differences. *Unknown*: how 14.5 saves a document it opens.
