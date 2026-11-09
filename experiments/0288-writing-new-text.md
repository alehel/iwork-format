# 0288: Writing new text

**Status:** run

[0287](0287-rewriting-a-document.md) rewrote a document without changing it. This experiment uses the same writer to change the body text, to a string of a different length, and checks how Pages reads and saves the result.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Input | `samples/0287/original.pages`, the body text `One` |
| Writer | [`recipes/0287-iwa-writer.py`](../recipes/0287-iwa-writer.py) |

## Recipe

```bash
mkdir -p samples/0288
python3 -I recipes/0287-iwa-writer.py samples/0287/original.pages samples/0288/hello.pages \
  --text 1732539 "Hello, written world" --plain
```

The writer replaces field 3 of record 1732539, the body text (type 2001), with `Hello, written world`, and re-serialises the payload and its header. Nothing else changes: the run tables still have their single entries at position 0. `--plain` also leaves the previews out.

The document is then opened in Pages through AppleScript, its body text, words and paragraphs read, and it is saved as `hello-resaved.pages`.

## Observation

Pages opens the file without a warning and reports the body text `Hello, written world`: three words in one paragraph. The missing previews cause no complaint.

In `hello-resaved.pages`, the body text record is identical to the one the writer produced.

## Conclusion

Field 3 of the body text is all a writer has to change to change the text, as long as every run table's entries stay within the new length. Here every table starts at 0 and applies to the whole text. Pages reads the length from the field itself, finds the record through header references the writer didn't touch, and accepts a document without previews. Saving again doesn't rewrite the record, so Pages found nothing in it to correct.

## Confidence

*Likely*: replacing a body text's field 3 is enough to change a single-paragraph text, and previews are optional.

Follow-up: write two paragraphs, which needs a second entry in the paragraph runs (field 5).
