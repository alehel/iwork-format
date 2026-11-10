# 0351: Writing a character style run

**Status:** run

A text's run table 8 attaches character styles (type 2021) to ranges: each entry has a position in field 1 and a style reference in field 2, and an entry without one ends the previous style ([0008](0008-runs-and-shared-styles.md)). This experiment writes such a table and asks Pages.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0002/hello.pages` with its body text replaced by `plain bold`; the template's character style `Framhevet` (Emphasis, record 1731541) sets only 11.1 = 1, bold |
| Writers | The writer of [0287](0287-rewriting-a-document.md) for the text, [`recipes/0351-add-run.py`](../recipes/0351-add-run.py) for the run table |

## Recipe

```bash
mkdir -p samples/0351
python3 -I recipes/0287-iwa-writer.py samples/0002/hello.pages samples/0351/plain.pages --text 1732539 "plain bold"
python3 -I recipes/0351-add-run.py samples/0351/plain.pages samples/0351/bold.pages 1732539 8 0 0 6 1731541
```

The run table gets two entries: position 0 with no style, and position 6 (the start of `bold`) with `Framhevet`. Pages opened each file on its own, read each word's font through AppleScript, exported it as PDF and saved the written file again.

## Observation

| File | Word 1 | Word 2 | Line's ink |
| --- | --- | --- | --- |
| `plain.pages` | HelveticaNeue | HelveticaNeue | 57.8 – 104.2 |
| `bold.pages` | HelveticaNeue | HelveticaNeue-Bold | 57.8 – 105.8 |

Saved again, the run table holds the same two entries.

## Conclusion

A run table entry applies its style from its position to the next entry, and an entry with no style means none. A writer can style part of a text by adding entries, without touching the text or the paragraph runs. A named character style that sets only bold makes the paragraph style's font bold.

## Confidence

*Confirmed*: character style runs (table 8), by writing them.
