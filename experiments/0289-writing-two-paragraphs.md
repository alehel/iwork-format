# 0289: Writing two paragraphs

**Status:** run

[0288](0288-writing-new-text.md) changed a one-paragraph body by rewriting its text alone. The spec says the paragraph run table (field 5) has one entry per paragraph ([0005](0005-paragraphs.md)). This experiment writes a two-paragraph body twice, once with a second paragraph entry and once without, to see whether Pages needs the entry.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Input | `samples/0287/original.pages`, one paragraph `One` in the Body style |
| Writer | [`recipes/0289-two-paragraphs.py`](../recipes/0289-two-paragraphs.py), using the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0289
python3 -I recipes/0289-two-paragraphs.py samples/0287/original.pages \
  samples/0289/with-run.pages samples/0289/without-run.pages
```

Both files get the body text `One` U+000A `Two`:

- `with-run.pages` also gets a second field-5 entry, `{ 1: 4 }`, with no style, as Pages wrote two paragraphs in 0005.
- `without-run.pages` keeps the single entry at 0.

Each file was opened in Pages through AppleScript, its paragraphs counted, and saved with `-resaved` added to its name.

## Observation

Pages opens both and counts two paragraphs, the second being `Two`.

| Resaved file | Field 5 |
| --- | --- |
| `with-run-resaved` | 0 → 1731511 (Body), 4 → no style: as written |
| `without-run-resaved` | 0 → 1731490, 4 → no style |

Record 1731490 is the paragraph style named `Standard`, with the identifier `paragraph-style-default`. AppleScript reports its font size as 12, against Body's 11.

## Conclusion

The paragraph run table needs one entry per paragraph. When a writer supplies them, Pages keeps them as written. An entry without a style continues the previous paragraph's style, here Body. When one is missing, Pages rebuilds the table on open, putting a run at each paragraph start. It then gives every paragraph the stylesheet's default style rather than the one the writer named, so the written style is lost. A writer must therefore add an entry at the start of every paragraph.

## Confidence

*Likely*:

- Field 5 must have an entry per paragraph.
- A missing entry makes Pages fall back on `paragraph-style-default`.
- An entry with no style continues the previous style.
