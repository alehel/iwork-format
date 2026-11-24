# 0468: Drawing 15.4 presentations in Keynote 14.5

**Status:** run

Keynote 14.5 opens the 15.4 presentations and reads the same slides from them ([0467](0467-opening-15-4-presentations-in-keynote-14-5.md)). Several Keynote writing experiments kept the PDF that Keynote 15.4 exported next to each presentation. This experiment exports the same presentations again with 14.5 and compares the two drawings pixel by pixel, as [0463](0463-drawing-15-4-documents-in-14-5.md) did for Pages and Numbers.

## Setup

| | |
| --- | --- |
| Keynote | 14.5 (build `M14.5-7045.0.17-4`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-24 |
| Input | Every `samples/NNNN/NAME.pdf` that sits next to a `NAME.key`: 68 presentations from experiments 0381, 0399, 0400, 0414, 0429, 0430, 0440, 0452 and 0456 to 0459 (slide numbers, chart borders, axes, axis names, captions and series styles, bullets, line breaks in titles, dynamic backgrounds and a hidden title), all written from the spec |
| Script | [`recipes/0463-compare-renders.py`](../recipes/0463-compare-renders.py), which now takes the apps to compare as a fourth argument, `Keynote` among them. It exports each presentation with `export d to POSIX file … as PDF`, as the PDFs were made, and compares first pages with [`recipes/0399-pdf-diff.swift`](../recipes/0399-pdf-diff.swift) |

## Recipe

```bash
python3 -I recipes/0463-compare-renders.py samples samples/0468 0466,0467 Keynote
```

Six presentations of 0381 have three slides, so their PDFs have three pages. Pages 2 and 3 of each were split into PDFs of their own with PDFKit and compared with the same tool.

## Observation

| Result | Presentations | Pages |
| --- | --- | --- |
| The same, pixel for pixel | 68 | 80 |
| Different | 0 | 0 |

## Conclusion

Keynote 14.5 draws every slide that Keynote 15.4 drew for these presentations, so how the spec reads every field written in these experiments that shows on a slide holds for 14.5 too: slide numbers, bullets, title breaks, hidden titles, dynamic backgrounds as exported, and chart borders, axes, captions and series styles. With [0466](0466-keynote-14-5.md) and [0467](0467-opening-15-4-presentations-in-keynote-14-5.md), Keynote 14.5 writes, reads and draws the format as the spec describes it for 15.4. The exceptions are the few differences those experiments list, and the radial wipe transition.

## Confidence

*Confirmed*: Keynote 14.5 draws 68 presentations written from the spec, 80 slides, exactly as Keynote 15.4 did.
