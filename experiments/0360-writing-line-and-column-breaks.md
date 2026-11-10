# 0360: Writing a line break and a column break

**Status:** run

A line break (Shift-Return) is U+2028 in the text and stays within its paragraph, and a column break is U+000C, which also starts a new paragraph ([0006](0006-typing-in-pages.md), [0210](0210-column-break.md)). This experiment writes each into a body and checks the paragraphs through AppleScript and the lines on the exported page with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift).

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0002/hello.pages`, and `samples/0324/two.pages`, whose body is in two columns, each 228.9 points wide with a 24.1-point gap |
| Writer | The writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0360
python3 -I recipes/0287-iwa-writer.py samples/0002/hello.pages samples/0360/line-break.pages \
  --text 1732539 "$(printf 'first line\xe2\x80\xa8second line')"
python3 -I recipes/0287-iwa-writer.py samples/0324/two.pages samples/0360/column-break.pages \
  --text 1732539 "$(printf 'left column\x0cright column')"
```

Pages opened each file on its own, counted the body's paragraphs through AppleScript, and exported it as PDF.

## Observation

| File | Paragraphs | Lines of ink: top, pieces |
| --- | --- | --- |
| `line-break.pages` | 1 | 58.2, 57.0 – 94.8; 70.2, 57.2 – 112.8 |
| `column-break.pages` | 2 | 59.2, 57.8 – 115.2 and 310.8 – 376.0 |

The second column starts at 56.69 + 228.9 + 24.1 = 309.7.

## Conclusion

U+2028 breaks the line and keeps one paragraph. U+000C ends the paragraph and sends the text after it to the top of the next column, here the right-hand one. Neither needs anything but the character.

## Confidence

*Confirmed*: U+2028 as a line break and U+000C as a column break, by writing them.
