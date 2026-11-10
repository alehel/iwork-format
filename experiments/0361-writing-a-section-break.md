# 0361: Writing a section break

**Status:** run

A section break (Insert → Section Break) is U+0004 in the text. In a file Pages saved, the body's section runs (field 17) gain an entry at the character after it, pointing at a new section record ([0040](0040-section-break.md)). This experiment writes the character in two ways and checks the sections, the pages and what Pages writes when it saves the file again:

1. The character alone, leaving one section run.
2. The character plus a second section run at the next character, pointing at the existing section record.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0002/hello.pages`, whose body (text storage 1732539) has one section run, pointing at section record 1732296 |
| Writer | The writer of [0287](0287-rewriting-a-document.md) and [`recipes/0351-add-run.py`](../recipes/0351-add-run.py) |

## Recipe

```bash
mkdir -p samples/0361
python3 -I recipes/0287-iwa-writer.py samples/0002/hello.pages samples/0361/char-only.pages \
  --text 1732539 "$(printf 'first\x04second')"
python3 -I recipes/0351-add-run.py samples/0361/char-only.pages samples/0361/with-run.pages \
  1732539 17 0 1732296 6 1732296
```

Pages opened each file on its own and counted the sections and the body's paragraphs through AppleScript. It then exported a PDF, read with PDFKit, and saved a copy (`-resaved`).

## Observation

| File | Sections | Paragraphs | PDF pages | Section runs as written | Section runs after Pages saved |
| --- | --- | --- | --- | --- | --- |
| `char-only.pages` | 2 | 2 | 2: "first", "second" | 0 → 1732296 | 0 → 1732660, 6 → 1732682 (both new) |
| `with-run.pages` | 2 | 2 | 2: "first", "second" | 0 → 1732296, 6 → 1732296 | unchanged |

For comparison, `samples/0040/section-break.pages` has 0 → 1732296 and 4 → 1732696.

## Conclusion

The U+0004 character alone makes the section break: Pages shows two sections, the second starting on a new page. The section runs only need to follow when the sections should differ. With one run, Pages makes the missing section on opening and writes two new section records when it saves. Two runs pointing at the same record are kept as they are, so a section record can be shared.

## Confidence

*Confirmed*: U+0004 as a section break, by writing it. *Likely*: two sections may share one section record, since Pages kept the shared record on saving.
