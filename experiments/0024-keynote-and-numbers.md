# 0024: Keynote and Numbers

**Status:** run

The README has said since the start that Keynote and Numbers documents appear to share a container with Pages. This experiment checks it. It saves new, empty documents from both apps and runs every container finding so far over them: the package, chunks, records, header references and roots.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0001](0001-empty-document.md), `empty-a.pages` |

## Recipe

```bash
mkdir -p samples/0024
R=recipes/0024-empty-iwork-document.applescript
osascript $R Keynote "$PWD/samples/0024/empty-a.key"
osascript $R Numbers "$PWD/samples/0024/empty-a.numbers"
osascript $R Keynote "$PWD/samples/0024/empty-b.key"
osascript $R Numbers "$PWD/samples/0024/empty-b.numbers"
```

The recipe makes a new document in the named app with the app's defaults and saves it. Keynote used the theme *Basic White* (`21_BasicWhite`), and Numbers the *Blank* template. Every `.iwa` part was then checked with `iwork-probe chunks`, `records` and `refs`, as in [0022](0022-header-references.md).

## Observation

### The package

| | Pages (0001) | Keynote | Numbers |
| --- | --- | --- | --- |
| Package | ZIP, 13 parts | ZIP, 54 parts | ZIP, 43 parts |
| Parts stored with ZIP compression | 0 | 0 | 0 |
| `Metadata/` and `preview*.jpg` | yes | yes | yes |
| `fileFormatVersion` in `Properties.plist` | `26.4.0` | `26.4.0` | `26.4.0` |
| Template in `BuildVersionHistory.plist` | `Blank` | `21_BasicWhite` | `Blank` |

Part names under `Index/`:

- **Keynote:** `AnnotationAuthorStorage`, `CalculationEngine`, `Document`, `DocumentMetadata`, `DocumentStylesheet`, `Metadata`, `ViewState`, one `Slide-N` and 17 `TemplateSlide-N`.
- **Numbers:** the seven shared names, plus 30 parts under `Index/Tables/`, named as in [0020](0020-a-table.md). A new Numbers document already holds an empty table.

Unlike in Pages, `AnnotationAuthorStorage` and `CalculationEngine` have no number in their names here.

The Keynote file also has 23 images under `Data/`, the theme's pictures for the template slides. Pages' Blank template had none.

Two empty saves from the same app had the same part names.

### Chunks, records and references

| | Keynote | Numbers |
| --- | --- | --- |
| `.iwa` parts | 26 | 37 |
| Parts where the chunk and record layout failed | 0 | 0 |
| Chunks with a type other than 0 | 0 | 0 |
| Objects | 962 | 627 |
| Reached from objects 1, 2 and 71 through header references | 962 | 627 |
| Header references to objects that don't exist | 0 | 0 |

### The roots

| Root | Part | Pages | Keynote | Numbers |
| --- | --- | --- | --- | --- |
| 1 | `Document.iwa` | type 10000 | type 1 | type 1 |
| 2 | `Metadata.iwa` | type 11006 | type 11006 | type 11006 |
| 71 | `DocumentMetadata.iwa` | type 11011 | type 11011 | type 11011 |

## Conclusion

Keynote and Numbers 15.4 write the same container as Pages 15.4. They use ZIP files without compression, the same metadata files, and `.iwa` parts with the same chunk and record layout. Header references reach every object from the same three roots, and the metadata roots (2 and 71) have the same types. So the container layer of the spec applies to all three apps. A reader can decode any of them up to the level of records and references.

The apps differ in their document root, object 1. In Pages it is type 10000, and in both Keynote and Numbers it is type 1. Whether Keynote's and Numbers' type 1 is the same kind of object, or whether type numbers are only unique within one app, is still open. The parts each app adds also differ: slides for Keynote, tables for Numbers. Those, and what lies below object 1, are where each app needs its own layers.

## Confidence

*Confirmed* for all three apps: the ZIP package, the chunk and record layout, and header references. Each was already confirmed for Pages and held without exception here.

*Likely*:

- Every object in a Keynote or Numbers document can be reached from objects 1, 2 and 71.
- The metadata objects 2 and 71 are shared between the apps.

*Unknown*: whether type numbers mean the same thing across apps. Follow-up: compare the payload of type 1 in Keynote with type 1 in Numbers.
