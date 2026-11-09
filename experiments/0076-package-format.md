# 0076: The package format

**Status:** run

Every document so far was a ZIP file. Pages can also save a document as a package, a folder, under File → Advanced → Change File Type → Package (*Fil → Avansert → Endre filtype → Pakke*). This experiment saves a document that way and compares the layout.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0020/plain.pages` (the body text `one`, as a ZIP) |

## Recipe

1. AppleScript makes a new document with the body text `one`.
2. In Pages, choose File → Advanced → Change File Type → Package.
3. AppleScript saves the document as `samples/0076/package.pages`.

The first save still wrote a ZIP file. The file type was then changed again on the saved, reopened document, and AppleScript saved it in place (`save front document`). That wrote a folder.

## Observation

`samples/0076/package.pages` is a folder:

```
Index.zip
Metadata/BuildVersionHistory.plist
Metadata/DocumentIdentifier
Metadata/Properties.plist
preview-micro.jpg
preview-web.jpg
preview.jpg
```

`Index.zip` holds the seven `.iwa` parts under `Index/`, with the same names as in a ZIP document, all stored without compression. With `iwork-probe` reading parts inside `Index.zip` (added for this experiment), the text and all 571 objects are found as in a ZIP document. All objects are reachable from objects 1, 2 and 71.

## Conclusion

A Pages document can be a folder as well as a ZIP file. In the folder form:

- the metadata files and previews are files in the folder
- the `.iwa` parts are inside a ZIP file called `Index.zip`, under the same `Index/` names, using the same chunk and record layout

A reader opens either form the same way once it treats `Index.zip` as part of the folder. A document with images would presumably keep its `Data/` folder alongside, but that isn't tested.

AppleScript's `save … in` writes the first save of a new document as a ZIP, whatever file type is chosen. Only a later save in place followed the setting.

## Confidence

*Likely*: the folder form, with `.iwa` parts inside `Index.zip`.

*Unknown*:

- Where data files go in the folder form.
- Whether Keynote and Numbers can save folders too.
