# Releases

The specification describes the files the newest apps write, Pages, Keynote and Numbers 16.0. Older releases write the same format with a few differences. Each is noted where it matters in the chapters: [since: 15.4] means 15.4 was the first release checked to have something, and [until: 14.5] means 14.5 was the last one checked to do something the newest no longer does. This page gathers the notes.

Only the releases below have been checked. Something new since 15.4 is in 15.4 and not in 14.5; which release between them added it is *unknown*. A statement without a note holds for every release it has been checked in, and things the oldest one already had get no note.

## Releases checked

| Release | `fileFormatVersion` | Build | Samples |
| --- | --- | --- | --- |
| 16.0 | `27.0.1` | `M16.0-7052.0.68-2` | Every scripted sample made again ([0473](../experiments/0473-every-scripted-sample-in-16-0.md)), every sample saved again ([0476](../experiments/0476-resaving-every-sample.md)) |
| 15.4 | `26.4.0` | `M15.4-7051.0.79-2` | The originals of experiments [0001](../experiments/0001-empty-document.md) to [0460](../experiments/0460-third-regression-check.md) |
| 14.5 | `14.4.1` | `M14.5-7045.0.17-4` | Every scripted sample made again ([0475](../experiments/0475-every-scripted-sample-in-14-5.md)) |
| 13.1 | `13.1.2` | `M13.1-7037.0.101-2` | Every scripted sample made again ([0477](../experiments/0477-every-scripted-sample-in-13-1.md)), every sample saved again ([0480](../experiments/0480-resaving-every-sample-in-13-1.md)) |

All three apps of each release, on macOS 26.5.2. The 15.4 and 16.0 apps are named "Pages Creator Studio" and so on.

## Telling which release saved a document

`Metadata/BuildVersionHistory.plist` lists the template and the build of each release that saved the document; the last build is the release that saved it last. `Metadata/Properties.plist` holds the file format version in `fileFormatVersion`, and `Metadata.iwa` repeats it ([data files](container.md#data-files)). The format version doesn't follow the app's version ([0461](../experiments/0461-new-documents-in-14-5.md), [0481](../experiments/0481-the-format-version-in-metadata.md)). A reader doesn't need either to read a document, but they say which of the notes apply. Every sample was saved by the release its experiment names ([0465](../experiments/0465-which-release-saved-each-sample.md), [0481](../experiments/0481-the-format-version-in-metadata.md)).

## What each release changed

Every statement with a version note, newest release first, gathered from where it stands:

<!-- release-history -->

## Templates

Apple's own templates and themes change between releases. A document takes its styles, images and layouts from the template it was made from, so these differences are in what was copied, not in how the format works. Readers find styles and data by reference and need nothing for them.

| Template | Difference |
| --- | --- |
| Keynote's Basic White, master thumbnails | `mt-UUID-N.jpg` has one set of UUIDs in 16.0, another in 15.4 and a third in 14.5 ([0466](../experiments/0466-keynote-14-5.md), [0469](../experiments/0469-the-16-0-apps.md)) |
| Keynote's Basic White, paragraph styles | In 16.0 and 15.4, 26 empty texts on its template slides use the *Brødtekst* (Body) style. In 14.5, 17 of them use an unnamed variation of *Liten infotekst* (Caption Small) at 56 points, one more type-2022 style ([0466](../experiments/0466-keynote-14-5.md), [0469](../experiments/0469-the-16-0-apps.md)) |
| Keynote's Basic White, movie poster | 16.0 and 15.4 keep `blankMoviePosterImage.png` as an app resource, with a colour. 14.5 stores it in the package as `Data/blankMoviePosterImage-N.png`, without one ([0466](../experiments/0466-keynote-14-5.md), [0469](../experiments/0469-the-16-0-apps.md)) |
| Numbers' blank template | 15.4 has one paragraph style the others lack, `text-12-paragraphstyle-Table Title 1` ([0464](../experiments/0464-recipes-rerun-in-14-5.md), [0469](../experiments/0469-the-16-0-apps.md)) |

Presentations made in 14.5 and 16.0 from the project's test theme, which 15.4 saved, have 15.4's styles and resources, so the Basic White differences are the template's ([0472](../experiments/0472-keynote-16-0-with-the-test-theme.md), [0474](../experiments/0474-keynote-14-5-with-the-test-theme.md)).

## What was checked

Most experiments ran with 15.4. The others were checked against it:

| Release | New documents | Opens the 15.4 samples | Draws them the same | Saves them again |
| --- | --- | --- | --- | --- |
| 16.0 | 313 of the 319 documents the recipes make compared, all with 15.4's structure but for the notes ([0473](../experiments/0473-every-scripted-sample-in-16-0.md), [0469](../experiments/0469-the-16-0-apps.md)) | All 1,211, and reads the same from them; also nine documents of the password experiments ([0470](../experiments/0470-opening-15-4-samples-in-16-0.md)) | 396 of 399, the other three for reasons other than the release ([0471](../experiments/0471-drawing-15-4-samples-in-16-0.md)) | All 1,211, hand-made features included ([0476](../experiments/0476-resaving-every-sample.md)) |
| 14.5 | 309 documents with 15.4's structure but for the notes ([0475](../experiments/0475-every-scripted-sample-in-14-5.md), [0461](../experiments/0461-new-documents-in-14-5.md), [0464](../experiments/0464-recipes-rerun-in-14-5.md), [0466](../experiments/0466-keynote-14-5.md)) | 893 of 895 Pages and Numbers documents, the other two for want of a password, and 323 presentations ([0462](../experiments/0462-opening-15-4-documents-in-14-5.md), [0467](../experiments/0467-opening-15-4-presentations-in-keynote-14-5.md)) | Yes, but for a body switched off over text ([0463](../experiments/0463-drawing-15-4-documents-in-14-5.md), [0468](../experiments/0468-drawing-15-4-presentations-in-keynote-14-5.md)) | Not tested |
| 13.1 | 306 documents with 15.4's structure but for the notes ([0477](../experiments/0477-every-scripted-sample-in-13-1.md)) | All 1,211 ([0478](../experiments/0478-opening-15-4-samples-in-13-1.md)) | 387 of 399; what differs in substance is tables of contents and a body switched off over text ([0479](../experiments/0479-drawing-15-4-samples-in-13-1.md)) | All 1,211, 994 with 16.0's structure ([0480](../experiments/0480-resaving-every-sample-in-13-1.md)) |

The structure compared is the parts, the record types with their versions and counts, and the top-level fields each type uses, plus which nested fields occur ([0481](../experiments/0481-the-format-version-in-metadata.md)); not every value. Opening an older document in a newer release works; the other way, 13.1 sometimes first warns that a document was made in a newer version, and what triggers that is *unknown* ([0479](../experiments/0479-drawing-15-4-samples-in-13-1.md)).

## When a new release comes

1. Make the set of every sample the recipes make on their own, `python3 -I recipes/0473-release-set.py RELEASE` and `--compare`, and open, draw and save the earlier samples, as for the releases above.
2. Add the release at the front of `RELEASES` in `site/build.py`, which then shows it as the one described.
3. Change each statement the new release makes untrue: say what the newest does, with [since: 16.0] as the note for what is new, or a note ending what it no longer does.
