# 0139: Saving an existing document again

**Status:** run

[0001](0001-empty-document.md) left open whether a document keeps its IDs when it is saved again, rather than made anew. This experiment opens a saved document and saves it, unchanged, under a new name.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0002](0002-one-word.md), `hello.pages` |

## Recipe

```bash
mkdir -p samples/0139
osascript recipes/0139-pages-container.applescript resave "$PWD/samples/0139/resaved.pages" "$PWD/samples/0002/hello.pages"
```

## Observation

- `Properties.plist` and `DocumentIdentifier` have a new document UUID (`16DE3765…` against `EF59D734…`), and new private and version UUIDs.
- The part `Index/ViewState.iwa` is now called `Index/ViewState-1732662.iwa`, after the ID of its first record, which is new.
- The other parts keep their names, and the body's text record keeps its ID (1732539).
- `CalculationEngine` has a different set of records, and `Metadata.iwa` record 2 grew by 19 bytes.
- All 571 objects are reachable from objects 1, 2 and 71.

## Conclusion

Objects that already existed keep their IDs when a document is saved again, but objects Pages makes afresh, such as the view state, get new IDs. A part's name can change between saves: `ViewState.iwa` became `ViewState-1732662.iwa`. So a reader must list a package's parts rather than expect fixed names.

Saving under a new name gives the document a new document UUID. It is a new document as far as the metadata goes.

## Confidence

*Likely*:

- Existing objects keep their IDs.
- Part names can change between saves.
- Saving under a new name gives a new document UUID.
