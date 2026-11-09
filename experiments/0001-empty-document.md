# 0001: An empty document

**Status:** planned

The baseline for every later experiment: what Pages writes for a new document with nothing in it. It answers the first container questions. Is the file a ZIP or a folder? Which parts does it hold? And how are the parts encoded?

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | |
| Date | |
| Baseline | New document |

## Recipe

```bash
mkdir -p samples/0001
osascript recipes/0001-empty-document.applescript "$PWD/samples/0001/empty-a.pages"
osascript recipes/0001-empty-document.applescript "$PWD/samples/0001/empty-b.pages"
cargo run --release -- list samples/0001/empty-a.pages
```

Saving two empty documents shows which bytes change between saves of the same content, such as IDs, timestamps or random values. Later experiments then know to ignore those.

## Observation

Not run yet.

## Conclusion

Not run yet.

## Confidence

Not run yet.
