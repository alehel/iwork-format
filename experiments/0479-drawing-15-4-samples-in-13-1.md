# 0479: Drawing the 15.4 samples in 13.1

**Status:** run

The 13.1 apps open the 15.4 samples and read the same from them ([0478](0478-opening-15-4-samples-in-13-1.md)). This experiment exports, with 13.1, every document whose 15.4 export was kept beside it, and compares the drawings pixel by pixel, as [0463](0463-drawing-15-4-documents-in-14-5.md), [0468](0468-drawing-15-4-presentations-in-keynote-14-5.md) and [0471](0471-drawing-15-4-samples-in-16-0.md) did for 14.5 and 16.0.

## Setup

| | |
| --- | --- |
| Apps | Pages, Numbers and Keynote 13.1 (build `M13.1-7037.0.101-2`), in Norwegian, run from a read-only disk image |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-24 |
| Input | The same 331 Pages and Numbers documents and 68 Keynote presentations as 0471 |
| Script | [`recipes/0463-compare-renders.py`](../recipes/0463-compare-renders.py), unchanged, through [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) with `IWORK_APP_DIR` |

## Recipe

```bash
export IWORK_APP_DIR=/Volumes/iwork-13-1
python3 -I recipes/0463-compare-renders.py samples samples/0479 0383,0391,0402,0409,0410
python3 -I recipes/0463-compare-renders.py samples samples/0479 0466,0467 Keynote
for n in original new-bottom new-all old-bottom old-all; do
  sh recipes/0372-in-app.sh Pages samples/0336/$n.pages "export d to POSIX file \"$PWD/samples/0479/0336-$n.pdf\" as PDF"
  swift recipes/0399-pdf-diff.swift samples/0336/$n.pdf samples/0479/0336-$n.pdf
done
```

The exports of 0336's documents first timed out, all but one, and were made by hand afterwards with the loop above; see *The warning* below. Pages 2 and 3 of 0381's six three-slide presentations were compared as in 0468. The border lines were measured on the pages drawn at 4 pixels per point.

## Observation

| Result | Documents | Pages |
| --- | --- | --- |
| Pages and Numbers: the same, pixel for pixel | 319 | 319 |
| Pages and Numbers: different | 12 | 12 |
| Keynote: the same, pixel for pixel | 68 | 80 |
| Keynote: different | 0 | 0 |

The twelve:

| Documents | Difference | Why |
| --- | --- | --- |
| `0336/original`, `new-bottom`, `new-all`, `old-bottom` and `old-all.pages` | the border's lines are 0.5 points longer at each end, the line below is 0.25 points higher, and the box's lines are up to 0.75 points further in | the same edges, drawn slightly elsewhere; see below |
| `0407/entry-model-text.pages`, `entry-model-roman.pages`, `heading-renamed.pages` | the table of contents: `One 1`, `One 1` and `Six 1`, where 15.4 drew `Written entry 1`, `One I` and `One 1` | 13.1 rebuilds the entries from the headings |
| `0365/thirty-by-nine.numbers` | a `7` in I30 only in 15.4's PDF | that PDF was exported after a script set I30; 13.1's export is the same as 14.5's and 16.0's |
| `0376/comment.pages`, `0376/highlight-with-text.pages` | the commented word on white or yellow | the variation between exports [0463](0463-drawing-15-4-documents-in-14-5.md) found; both are the same as 14.5's and 16.0's |
| `0419/no-body.pages` | 13.1 draws nothing where 15.4 drew `hello` | the body is switched off over its text; 14.5 draws nothing too, and 16.0 draws `hello` |

**Borders.** In every one of 0336's five documents 13.1 draws the edges 15.4 draws: above for 12.15 = 1, below for 2 and a box for 4, whatever 12.45 says.

**Tables of contents.** Four other documents of 0407, `original.pages`, `entry-text.pages`, `page-number.pages` and `entry-model-field2.pages`, were drawn the same as by 15.4. The three that differ are those where a rebuilt table differs from the written entry records.

## The warning

Pages first seemed to hang on 0336's documents, [0262](0262-paragraph-border.md)'s, [0273](0273-border-edges.md)'s and [0274](0274-dashed-border.md)'s: opening them worked, but an export or a save timed out after up to four minutes, and in one case Pages then stopped opening anything. The project owner, at the Mac, saw a window saying that the document had been made in a newer version, and clicked to continue. After that all eleven exports and saves of these documents finished, in 11 seconds at most. The owner thinks the stalls in the documents that came after 0262 were the same window, which fits: those documents all saved at once when retried.

Nothing in those documents' record headers differs from a plain document's, so what makes 13.1 warn about them, and not about others, is *unknown*. Every other document of this run was opened without a warning holding it up.

## Conclusion

13.1 draws 387 of the 399 documents exactly as 15.4 did, and the same borders with lines placed up to 0.75 points differently. Where it differs in substance, it rebuilds tables of contents, as 15.4 doesn't, and draws no body that is switched off, as 14.5 doesn't. The other three differences aren't between releases.

## Evidence

No documents of its own: it draws the samples of earlier experiments in 13.1 and compares the drawings. The one drawn differently because of a body switched off over text:

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `0419/no-body.pages` | `0002/hello.pages` | Only `10012#1732614 1: 1 → 0` | *Confirmed*: 13.1 draws nothing where 15.4 drew the text |

## Confidence

*Confirmed*: 13.1 draws 387 documents written or saved by 15.4 exactly as 15.4 did. *Likely*: it rebuilds tables of contents on opening. *Unknown*: what triggers the newer-version warning.
