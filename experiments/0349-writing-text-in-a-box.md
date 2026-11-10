# 0349: Writing a text box's text

**Status:** run

A text box is a shape (type 2011) whose text is a text storage (type 2001) of its own, without field 1 ([0049](0049-text-box.md), [0305](0305-writing-presenter-notes.md)). This experiment writes new text into that storage and reads it back from Pages, and measures it on the exported page.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0049/text-box.pages`: the body `one` and a 250 × 128 text box holding `box`, in text storage 1732650 |
| Writer | The writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0349
cp samples/0049/text-box.pages samples/0349/original.pages
python3 -I recipes/0287-iwa-writer.py samples/0349/original.pages samples/0349/written.pages \
  --text 1732650 "A much longer line of text in the box"
```

Pages opened each file on its own, read the text box's `object text`, `width` and `height` through AppleScript, and exported it as PDF, which was measured with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift).

## Observation

| File | Text box text | Box | Line of ink in the box |
| --- | --- | --- | --- |
| `original.pages` | `box` | 250 × 128 | 170.8 – 188.2 |
| `written.pages` | `A much longer line of text in the box` | 250 × 128 | 169.8 – 347.2 |

The body's `one` stays at 57.2 – 74.8 in both.

## Conclusion

A text box's text is its own text storage's field 3, and writing it changes what the box shows, as for the body. The box keeps its size; the longer text fits on one line here.

## Confidence

*Confirmed*: a text box's text is in its own text storage, by writing it.
