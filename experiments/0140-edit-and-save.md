# 0140: Editing and saving in place

**Status:** run

This experiment edits a document and saves it in place, to see which identifiers survive an ordinary save.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0002](0002-one-word.md), `hello.pages`, copied as `samples/0140/edited.pages` |

## Recipe

```bash
mkdir -p samples/0140
cp samples/0002/hello.pages samples/0140/edited.pages
osascript recipes/0139-pages-container.applescript editsave "$PWD/samples/0140/edited.pages"
```

The recipe opens the copy, sets its body text to `changed`, and saves it in place.

## Observation

- The document UUID in `Properties.plist` and `DocumentIdentifier` changed (`63958141…` against `EF59D734…`).
- As in [0139](0139-resave.md), the view state part is now `ViewState-1732662.iwa`.
- The body record kept its ID.

## Conclusion

Even a save in place gave the copied document a new document UUID. Pages may treat a file whose UUID matches another file's as a duplicate, because the copy had the same UUID as the original. So this experiment can't tell whether an ordinary save keeps the UUID. Object IDs of existing objects survived, as in 0139.

## Confidence

*Likely*: existing object IDs survive a save.

*Unknown*: whether a save in place keeps the document UUID when the file isn't a copy.
