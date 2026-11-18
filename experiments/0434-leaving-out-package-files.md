# 0434: Leaving out package files

**Status:** run

Besides its `Index/` parts, a document's ZIP holds `Metadata/Properties.plist`, `Metadata/DocumentIdentifier`, `Metadata/BuildVersionHistory.plist` and three previews ([container.md](../spec/container.md#the-package)). The writer of [0287](0287-rewriting-a-document.md) already left out the previews. This experiment leaves out each of the others, and the view state, and asks whether Pages opens the document.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0002/hello.pages`: seven parts under `Index/`, the three files under `Metadata/`, and `preview.jpg`, `preview-micro.jpg` and `preview-web.jpg` |
| Writer | The new [`recipes/0434-drop-entries.py`](../recipes/0434-drop-entries.py); opened with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0434
X=recipes/0434-drop-entries.py
F=samples/0002/hello.pages
O=samples/0434
python3 -I $X $F $O/no-identifier.pages Metadata/DocumentIdentifier
python3 -I $X $F $O/no-properties.pages Metadata/Properties.plist
python3 -I $X $F $O/no-history.pages Metadata/BuildVersionHistory.plist
python3 -I $X $F $O/no-previews.pages 'preview*'
python3 -I $X $F $O/no-metadata-folder.pages 'Metadata/*'
python3 -I $X $F $O/only-index.pages 'Metadata/*' 'preview*'
python3 -I $X $F $O/no-viewstate.pages Index/ViewState.iwa
for f in no-identifier no-properties no-history no-previews no-metadata-folder only-index no-viewstate; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages 'return {body text of d, font of word 1 of body text of d}'
done
```

## Observation

| File | Left out | Pages |
| --- | --- | --- |
| `no-identifier.pages` | `DocumentIdentifier` | opens: `hello`, HelveticaNeue |
| `no-properties.pages` | `Properties.plist` | opens |
| `no-history.pages` | `BuildVersionHistory.plist` | opens |
| `no-previews.pages` | the three previews | opens |
| `no-metadata-folder.pages` | all of `Metadata/` | opens |
| `only-index.pages` | `Metadata/` and the previews | doesn't open, with no alert |
| `no-viewstate.pages` | `Index/ViewState.iwa` | doesn't open, with no alert |

After either of the last two, Pages opened no other document either, not even ones it had just opened, until it was quit and started again. Each was tried twice, with the same result.

## Conclusion

Pages doesn't need any single file outside `Index/`: each of the three `Metadata/` files, and the previews, can be left out, and so can all of `Metadata/` at once. But a ZIP with nothing outside `Index/` makes Pages stop opening documents altogether, and so does a document without its view state part, which `Metadata.iwa` lists as a component ([0394](0394-renaming-a-part.md)). So a writer should always include `ViewState.iwa` and keep at least one entry besides `Index/`, such as the `Metadata/` files Pages writes. Why the combination matters is *unknown*.

## Confidence

*Confirmed*: Pages opens a document without any one of the `Metadata/` files or the previews, and without all of `Metadata/`, but not without its view state, nor with only `Index/`, by writing them. Why is *unknown*.
