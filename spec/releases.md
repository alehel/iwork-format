# Releases

The specification describes the file format as the 15.4 apps write it. Other releases checked against it write the same format, with the few differences listed below; a statement that holds for some releases only carries a mark such as [release: 15.4 only] where it stands in the spec.

## Releases checked

| Release | Apps | macOS | `fileFormatVersion` | Build |
| --- | --- | --- | --- | --- |
| 15.4 | Pages, Keynote, Numbers | 26.5.2 | `26.4.0` | `M15.4-7051.0.79-2` |
| 16.0 | Pages, Keynote, Numbers | 26.5.2 | `27.0.1` | `M16.0-7052.0.68-2` |
| 14.5 | Pages, Keynote, Numbers | 26.5.2 | `14.4.1` | `M14.5-7045.0.17-4` |

- **15.4** is the release the spec describes, from [0001](../experiments/0001-empty-document.md) on. Its apps are named "Pages Creator Studio" and so on.
- **14.5** writes the same format ([0461](../experiments/0461-new-documents-in-14-5.md), [0464](../experiments/0464-recipes-rerun-in-14-5.md)), opens and reads the 15.4 samples ([0462](../experiments/0462-opening-15-4-documents-in-14-5.md)) and draws them the same ([0463](../experiments/0463-drawing-15-4-documents-in-14-5.md)).
- **16.0** writes the same format too ([0469](../experiments/0469-the-16-0-apps.md)), and where 14.5 and 15.4 differ it sides with 15.4, apart from Numbers' *Table Title 1* style, which it leaves out as 14.5 does. What is new is one more field in each app's view-state record, which a reader can ignore. It opens the 15.4 samples and reads the same text, tables, slides and notes from them, the radial wipe included ([0470](../experiments/0470-opening-15-4-samples-in-16-0.md)), and draws them as 15.4 did, a body switched off over text included ([0471](../experiments/0471-drawing-15-4-samples-in-16-0.md)). Its apps are named "Pages Creator Studio" and so on, as 15.4's were, and they replaced both 15.4 and 14.5 on the Mac the experiments run on, so documents can't be taken back to those releases.
- **Keynote 14.5** writes the same format too ([0466](../experiments/0466-keynote-14-5.md)), apart from a slide-node field, a resource and its Basic White template; it opens and reads the 15.4 presentations ([0467](../experiments/0467-opening-15-4-presentations-in-keynote-14-5.md)) and draws them the same ([0468](../experiments/0468-drawing-15-4-presentations-in-keynote-14-5.md)). It doesn't know the radial wipe transition.

## Telling which release saved a document

`Metadata/Properties.plist` holds the file format version in `fileFormatVersion`, and `Metadata/BuildVersionHistory.plist` lists the template and the build of the app that saved it, such as `M14.5-7045.0.17-4`. The format version doesn't follow the app's version: 14.5 writes `14.4.1`, 15.4 writes `26.4.0` and 16.0 writes `27.0.1` ([0461](../experiments/0461-new-documents-in-14-5.md)). A reader doesn't need either to read a document, but they say which differences below can apply. Every sample document's build was checked against the release its experiment names, and all matched ([0465](../experiments/0465-which-release-saved-each-sample.md)).

## Differences

Every statement in the spec marked as holding for some releases only, gathered from where it stands:

<!-- release-differences -->

## Releases that change the format

When a release writes a format that differs in more than a few details, the spec moves on to describe it, and the spec as it stood is kept for documents the earlier release wrote: `python3 -I site/archive.py RELEASE` freezes it in `spec/versions/RELEASE/`, and the site shows a *Spec version* menu to switch between them. No release has needed that yet.
