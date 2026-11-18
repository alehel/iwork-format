# 0441: Writing right-to-left text

**Status:** run

Pages stores no writing direction for Arabic text set through AppleScript, so a reader was told to lay text out by the Unicode bidirectional rules ([0150](0150-arabic-text.md)). Those rules leave open the paragraph's base direction, which by default comes from its first strong character. This experiment writes Arabic, Latin and mixed text into a body and reads where Pages draws each word.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0002/hello.pages`, with its body (1732539) replaced by each text, in the left-aligned *Brødtekst* |
| Writer | The writer of [0287](0287-rewriting-a-document.md); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh), measured with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift), and each word found with PDFKit |

## Recipe

```bash
mkdir -p samples/0441
O=samples/0441
W=recipes/0287-iwa-writer.py
python3 -I $W samples/0002/hello.pages $O/latin.pages --text 1732539 "Hello world"
python3 -I $W samples/0002/hello.pages $O/arabic.pages --text 1732539 "مرحبا بالعالم"
python3 -I $W samples/0002/hello.pages $O/mixed.pages --text 1732539 "مرحبا ABC بالعالم"
for f in latin arabic mixed; do
  sh recipes/0372-in-app.sh Pages $O/$f.pages "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0319-measure-pdf.swift $O/$f.pdf
done
```

The words' places were read with PDFKit's `findString` on each exported page.

## Observation

| File | Text, in stored order | Ink, left – right | Words, left to right on the page |
| --- | --- | --- | --- |
| `latin.pages` | Hello world | 57.8 – 111.2 | Hello (…), world |
| `arabic.pages` | مرحبا بالعالم | 57.0 – 105.2 | بالعالم (56–80), مرحبا (83–105) |
| `mixed.pages` | مرحبا ABC بالعالم | 58.5 – 131.0 | مرحبا (56–78), ABC (81–103), بالعالم (106–130) |

## Conclusion

Pages applies the bidirectional rules within a paragraph, so a run of Arabic is laid out right to left: the first Arabic word stands to the right of the second. But the paragraph's base direction stays left-to-right, from its style, even when its first strong character is Arabic: the Arabic line starts at the left margin, and in the mixed line the runs follow each other from left to right, with the first Arabic word on the left. A reader should lay out each paragraph with a left-to-right base direction unless its style says otherwise, not detect the direction from the text.

## Confidence

*Confirmed*: Pages lays out Arabic runs right to left within a left-to-right paragraph and doesn't take the paragraph's direction from its text, by writing it. How a right-to-left paragraph is stored, when set in the app, is *unknown*.
