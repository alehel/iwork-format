# 0356: Writing a footnote's text

**Status:** run

A footnote's text is a text storage of its own, with field 1 = 2, reached from the body's footnote runs ([0041](0041-footnote.md), [0305](0305-writing-presenter-notes.md)). This experiment writes new text into it and reads the exported page's text with PDFKit.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0041/footnote.pages`: the body `one` with a footnote whose text storage, record 1732708, holds U+FFFC, a space and `note` |
| Writer | The writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0356
cp samples/0041/footnote.pages samples/0356/original.pages
python3 -I recipes/0287-iwa-writer.py samples/0356/original.pages samples/0356/written.pages \
  --text 1732708 "$(printf '\xef\xbf\xbc written footnote text')"
```

The U+FFFC at the start, where Pages draws the footnote's number, is kept. Pages opened each file on its own and exported it as PDF, and PDFKit extracted the first page's text.

## Observation

| File | Page text |
| --- | --- |
| `original.pages` | `one1` / `note 1` |
| `written.pages` | `one1` / `written footnote text 1` |

## Conclusion

A footnote's text is its own text storage's field 3, and writing it changes the footnote. Its first character, U+FFFC, is where the footnote's number is drawn; PDFKit happens to list the number after the text.

## Confidence

*Confirmed*: footnote text, by writing it.
