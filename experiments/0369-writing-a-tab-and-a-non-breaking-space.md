# 0369: Writing a tab and a non-breaking space

**Status:** run

A tab (U+0009) and a non-breaking space (U+00A0) are plain characters in the text with no runs of their own ([0058](0058-tab-and-nbsp.md)). Tab stops fall every 36 points from the margin unless set ([0325](0325-writing-tab-stops.md)). This experiment writes each into a body and checks the layout on the exported page.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0002/hello.pages`, with a left margin of 56.69 points |
| Writer | The writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0369
W=recipes/0287-iwa-writer.py
T=$(python3 -c "print(' '.join(f'w{i:02d}' for i in range(1,61)), end='')")
python3 -I $W samples/0002/hello.pages samples/0369/spaces.pages --text 1732539 "$T"
python3 -I $W samples/0002/hello.pages samples/0369/nbsp.pages --text 1732539 \
  "$(python3 -c "import sys; print(sys.argv[1].replace('w20 w21','w20 w21'), end='')" "$T")"
python3 -I $W samples/0002/hello.pages samples/0369/tab.pages --text 1732539 "$(printf 'w01\tw02 w03')"
python3 -I $W samples/0002/hello.pages samples/0369/no-tab.pages --text 1732539 "w01 w02 w03"
```

`spaces.pages` showed where the first line wraps. In `nbsp.pages` the space at that point, between w20 and w21, is a non-breaking space. Pages opened each file on its own and exported it as PDF. The lines were read with PDFKit and the ink measured with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift).

## Observation

| File | First line | Second line starts |
| --- | --- | --- |
| `spaces.pages` | w01 … w20 | w21 |
| `nbsp.pages` | w01 … w19 | w20 w21 |

| File | Ink pieces on the line, in points from the left edge |
| --- | --- |
| `no-tab.pages` | 57.2–124.2 |
| `tab.pages` | 57.2–75.2 (w01), 93.2–136.5 (w02 w03) |

Pages counted 11 characters in both short bodies, so the tab is one character.

## Conclusion

A non-breaking space keeps its two words on one line: the line breaks before w20 instead of after it. A tab moves the text after it to the next stop, 56.69 + 36 = 92.69 points, where w02's ink starts. Neither needs anything but the character.

## Confidence

*Confirmed*: U+0009 as a tab and U+00A0 as a non-breaking space, by writing them.
