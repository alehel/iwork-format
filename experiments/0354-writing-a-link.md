# 0354: Writing a link's address

**Status:** run

A web link is a smart field over a range of text (run table 11): a type-2032 record whose field 2 holds the address ([0189](0189-web-link.md)). AppleScript can't read links, but Pages exports them to PDF as link annotations. This experiment writes a new address and reads the exported PDF's links with PDFKit.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0189/link.pages`: a word linked to `http://www.apple.com/no` through record 1732708 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0354
cp samples/0189/link.pages samples/0354/original.pages
python3 -I recipes/0302-set-path.py samples/0354/original.pages samples/0354/written.pages 1732708 2 string "https://example.org/written-link"
```

Pages opened each file on its own and exported it as PDF; PDFKit then listed each page's annotations and their URLs. A first search for `/URI` in the raw PDF found nothing, because the annotations are in compressed object streams.

## Observation

| File | Link annotations in the PDF |
| --- | --- |
| `original.pages` | `http://www.apple.com/no` |
| `written.pages` | `https://example.org/written-link` |

## Conclusion

Field 2 of a type-2032 link is its address, used as written, and Pages carries it into exported PDFs as a link annotation.

## Confidence

*Confirmed*: link field 2, by writing it.
