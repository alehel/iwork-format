# 0471: Drawing the 15.4 samples in 16.0

**Status:** run

The 16.0 apps open the 15.4 samples and read the same from them ([0470](0470-opening-15-4-samples-in-16-0.md)). This experiment exports, with 16.0, every document whose 15.4 export was kept beside it, and compares the drawings pixel by pixel, as [0463](0463-drawing-15-4-documents-in-14-5.md) and [0468](0468-drawing-15-4-presentations-in-keynote-14-5.md) did for 14.5.

## Setup

| | |
| --- | --- |
| Apps | Pages, Numbers and Keynote 16.0 (build `M16.0-7052.0.68-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-24 |
| Input | Every `samples/NNNN/NAME.pdf` that sits next to a `NAME.pages`, `NAME.numbers` or `NAME.key`: 331 Pages and Numbers documents from experiments 0319 to 0460, and 68 Keynote presentations, most of them written from the spec. The same as 0463 and 0468, leaving out what they left out |
| Script | [`recipes/0463-compare-renders.py`](../recipes/0463-compare-renders.py), unchanged, which exports each document with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) (with comments where the original export had them) and compares first pages with [`recipes/0399-pdf-diff.swift`](../recipes/0399-pdf-diff.swift) |

## Recipe

```bash
python3 -I recipes/0463-compare-renders.py samples samples/0471 0383,0391,0402,0409,0410
python3 -I recipes/0463-compare-renders.py samples samples/0471 0466,0467 Keynote
for n in comment highlight-with-text; do
  for i in 2 3; do
    sh recipes/0372-in-app.sh Pages samples/0376/$n.pages \
      "export d to POSIX file \"$PWD/samples/0471/again-$n-$i.pdf\" as PDF with properties {include comments:true}"
  done
  swift recipes/0399-pdf-diff.swift samples/0376/$n.pdf samples/0471/0376-$n.pdf samples/0471/again-$n-*.pdf
done
swift recipes/0399-pdf-diff.swift samples/0463/0365-thirty-by-nine.pdf samples/0471/0365-thirty-by-nine.pdf
```

As in 0468, pages 2 and 3 of the six three-slide presentations of 0381 were split into PDFs of their own with PDFKit and compared with the same tool. The colour of the commented word in 0376's exports was read as the average over the box the tool reported.

## Observation

| Result | Documents | Pages |
| --- | --- | --- |
| Pages and Numbers: the same, pixel for pixel | 328 | 328 |
| Pages and Numbers: different | 3 | 3 |
| Keynote: the same, pixel for pixel | 68 | 80 |
| Keynote: different | 0 | 0 |

The three:

| Document | Difference | Why |
| --- | --- | --- |
| `0365/thirty-by-nine.numbers` | a `7` in I30 only in 15.4's PDF | that PDF was exported after a script set I30 to 7 ([0365](0365-growing-a-table.md)). 16.0's export is the same as 14.5's ([0463](0463-drawing-15-4-documents-in-14-5.md)) |
| `0376/comment.pages` | the commented word on white in 16.0's export, yellow in 15.4's | two more exports from 16.0 came out yellow, the same as 15.4's |
| `0376/highlight-with-text.pages` | the commented word yellow in 16.0's export, white in 15.4's | yellow in two more exports too, as in all of 14.5's |

Across the releases, the commented word has come out yellow in most exports and white in one export each from 15.4, 14.5 and 16.0, always in a different document. This is the variation 0463 found, not a difference between releases.

`0419/no-body.pages`, `hello.pages` with the body switch written off over its text ([0419](0419-writing-the-document-body-setting.md)), is drawn the same as 15.4 drew it: with `hello`. 14.5 drew nothing.

## Conclusion

The 16.0 apps draw every document written or saved by 15.4 in these experiments as 15.4 did: every field written in experiments 0319 to 0460 that shows on a page or slide reads the same in 16.0. Where 14.5 differed from 15.4, with a body switched off over text, 16.0 draws as 15.4 does.

With [0469](0469-the-16-0-apps.md) and [0470](0470-opening-15-4-samples-in-16-0.md), the 16.0 apps write, read and draw the format as 15.4 did. The spec holds for 16.0 as written, with the release marks noting its few differences.

## Confidence

*Confirmed*: 16.0 draws 396 documents written or saved by 15.4 exactly as 15.4 did; the other three differ for reasons that have nothing to do with the release.
