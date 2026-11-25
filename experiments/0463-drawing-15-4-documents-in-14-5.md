# 0463: Drawing 15.4 documents in 14.5

**Status:** run

Pages and Numbers 14.5 open the 15.4 samples and read the same text from them ([0462](0462-opening-15-4-documents-in-14-5.md)). Many writing experiments kept the PDF that the 15.4 app exported next to each document. This experiment exports the same documents again with 14.5 and compares the two drawings pixel by pixel.

## Setup

| | |
| --- | --- |
| Pages | 14.5, in Norwegian |
| Numbers | 14.5 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-23 |
| Input | Every `samples/NNNN/NAME.pdf` that sits next to a `NAME.pages` or `NAME.numbers`: 331 documents, from experiments 0319 to 0460, most of them written from the spec |
| Script | The new [`recipes/0463-compare-renders.py`](../recipes/0463-compare-renders.py), which exports each document with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh), with comments where the original export had them, and compares the first pages with [`recipes/0399-pdf-diff.swift`](../recipes/0399-pdf-diff.swift) |

## Recipe

```bash
python3 -I recipes/0463-compare-renders.py samples samples/0463 0383,0391,0402,0409,0410
```

Experiments 0383, 0391, 0402, 0409 and 0410 are left out because their PDFs were exported after a script had changed the open document, so the PDF doesn't show the file as saved.

## Observation

| Result | Documents |
| --- | --- |
| The same, pixel for pixel | 327 |
| Different | 4 |

The four:

| Document | Difference | Why |
| --- | --- | --- |
| `0365/thirty-by-nine.numbers` | a `7` in I30 only in 15.4's PDF | that PDF, too, was exported after a script set I30 to 7 ([0365](0365-growing-a-table.md)): not a difference between releases |
| `0376/comment.pages`, `0376/highlight-with-text.pages` | the commented word on a yellow ground in one release's PDF and on white in the other | exported again twice in 14.5, both came out yellow: the shading varies from one export to the next, in either release |
| `0419/no-body.pages` | `hello` drawn by 15.4, nothing by 14.5 | the same in two more exports from 14.5 |

`no-body.pages` is `hello.pages` with document setting field 1, the document body switch, written as 0 and the body's text left in place ([0419](0419-writing-the-document-body-setting.md)).

## Conclusion

14.5 draws what 15.4 drew for every document but one: the reading of every field written in experiments 0319 to 0460 that shows on a page holds for 14.5 too. The exception is a document whose body switch is off while the body still holds text, which a release would never save itself: 15.4 draws that text and 14.5 doesn't. A reader can't rely on either, and a writer should empty the body when it turns the switch off, as both releases do.

When Pages exports comments, the word a comment covers may or may not be shaded, from one export to the next; a comparison of exported pages should allow for it.

## Evidence

No documents of its own: it draws the samples of 0319 to 0460 in 14.5 and compares the drawings. The one that differs because of the release:

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `0419/no-body.pages` | `0002/hello.pages` | Only `10012#1732614 1: 1 → 0` | *Confirmed*: 14.5 draws nothing where 15.4 drew the text |

## Confidence

*Confirmed*: 14.5 draws 327 documents written or saved by 15.4 exactly as 15.4 did, and differs only for a body switched off over text.
