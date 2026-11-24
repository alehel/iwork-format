# 0473: Every scripted sample in 16.0

**Status:** run

The release experiments so far reran a few dozen recipes in each new release ([0461](0461-new-documents-in-14-5.md), [0464](0464-recipes-rerun-in-14-5.md), [0466](0466-keynote-14-5.md), [0469](0469-the-16-0-apps.md)). This experiment makes a script that reruns every recipe the experiments before 0461 ran, in whatever release is installed, and runs it for 16.0. Each release then has its own set of the samples the apps make from a script alone, for testing readers against more than one release.

## Setup

| | |
| --- | --- |
| Apps | Pages, Numbers and Keynote 16.0 (build `M16.0-7052.0.68-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-24 |
| Theme | Keynote: `iwork-format test` ([0291](0291-test-theme.md)), so the presentations can be published |
| Script | The new [`recipes/0473-release-set.py`](../recipes/0473-release-set.py) |
| Compared with | Each document's namesake from 15.4 under `samples/`, or for Keynote the test-theme one under `samples/theme/` when there is one |

## Recipe

```bash
python3 -I recipes/0473-release-set.py 16.0 --list     # the commands, without running them
python3 -I recipes/0473-release-set.py 16.0            # makes samples/release/16.0/NNNN/...
python3 -I recipes/0473-release-set.py 16.0 --compare
python3 -I fixtures/build.py /tmp/iwork-format-fixtures.zip
osascript recipes/0047-numbers-second-table.applescript "$PWD/samples/0473/0047-two-tables-run4.numbers"
```

The script reads the Recipe section of every experiment before 0461 and collects each `osascript recipes/NNNN-*.applescript` command, with a recipe named as `R=recipes/…` substituted, each `for` or `while` loop around one, and each `cp` of a document that a recipe then opens. It runs them in experiment order with every document path moved from `samples/NNNN/` to `samples/release/16.0/NNNN/`, while input images, sound and movies are still read from `samples/`. A document a recipe opens, such as 0139's input or 0140's copy, is therefore the release's own.

It leaves out what a script can't make alone:

- calls through `osascript -e` or recipes that act on a document already open (0189 to 0287), which were followed by steps in the app;
- the documents of 0146, 0147, 0296 and 0297 that were changed by hand after their recipe and saved under the same name. The script makes them and removes them again;
- 0291, which builds the test theme.

The writing experiments (0287 on), which edit 15.4 documents byte by byte, run no recipe of this kind, so they aren't in the set either.

Two fixes came out of the first run. A path with a space in it, 0144's `rød bilde.png`, was cut at the space, and the recipe placed no image; the script now reads a quoted path to its closing quote. 0140's recipe edits a copy of `0002/hello.pages`, and the copy wasn't made. Both were run again.

The Recipe sections of 0104, 0106 and 0109 to 0112 named their documents differently from the files the experiments kept, such as `nested-functions.numbers` for `nested.numbers`. They now name the files as kept.

## Observation

190 commands from 172 experiments, all run without an error, made 319 documents in 16.0 (323, before the four hand-changed ones were removed).

| `--compare` | Documents |
| --- | --- |
| The same as 15.4 but for what every 16.0 document differs in ([0469](0469-the-16-0-apps.md)) | 313 |
| Different | 0 |
| Not compared: encrypted, so the survey can't decode them | 6 |

The six encrypted documents (0179 and 0180) decrypt with their test passwords in `iwork-probe` and hold the same body text, `one`, as the 15.4 ones.

What `--compare` counts as known: the format version and build history, the view-state fields of 0469, Basic White's and the test theme's master thumbnails, Numbers' *Table Title 1* style, and the calculation engine's owners and lists (types 4008 and 4009), its UUID (type 4000 field 17) and, new here, field 6 of its type-4011 record. That field appeared once, in this run's `0047/two-tables.numbers`, as a list like the type-4009 lists; it wasn't in four other runs of the same recipe in 16.0 (0469's three and `samples/0473/0047-two-tables-run4.numbers`), nor in 15.4's or 14.5's, so it varies with the run as the owners do.

The fixtures builder keeps 316 of the 319, and leaves out 0090, 0158 and 0199 as it does their 15.4 versions, since they hold Apple's template photos or text. The presentations pass its check for media the project didn't make, so every one was made with the test theme.

## Conclusion

Every document the experiments' recipes make, 319 of them across all three apps, comes out of 16.0 with the same structure as from 15.4. This widens [0469](0469-the-16-0-apps.md)'s 43 recipes to all of them: cells, formulas and formats, styles, shapes, images, media, charts, slides, transitions, builds, passwords and the container options.

The set is published with the fixtures under `release/16.0/`. For the next release, the same three commands make and check its set.

## Confidence

*Confirmed*: for 313 documents made by the experiments' recipes, 16.0 writes the same structure as 15.4, apart from the differences every 16.0 document has.
