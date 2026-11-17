# 0410: Writing a pivot table's summary function

**Status:** run

A pivot table's value fields are in field 5 of its type-6370 record, with the summary function in 5.1.3: 2 for Sum and 18 for Average. The pivot table's own cells hold the current summary, and a label table holds the function's name in the app's language ([0227](0227-pivot-table.md), [0279](0279-pivot-average.md)). This experiment writes the function and asks when Numbers applies it.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0279/sum.numbers`: `kind` a, b, a, b and `n` 1, 2, 3, 4, with a pivot summing `n` by `kind`; record 905722 has 5.1.3 = 2. Numbers' own average version: `samples/0279/average.numbers` |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py); exported with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) and read with [`recipes/0374-pdf-text.swift`](../recipes/0374-pdf-text.swift) |

## Recipe

```bash
mkdir -p samples/0410
O=samples/0410
cp samples/0279/sum.numbers $O/sum.numbers
cp samples/0279/average.numbers $O/numbers-average.numbers
python3 -I recipes/0302-set-path.py $O/sum.numbers $O/written-average.numbers 905722 5.1.3 varint 18
for f in sum numbers-average written-average; do
  sh recipes/0372-in-app.sh Numbers $O/$f.numbers "export d to POSIX file \"$PWD/$O/$f.pdf\" as PDF"
  swift recipes/0374-pdf-text.swift $O/$f.pdf
done
```

Copies of `sum` and `written-average` were also exported after setting the source's B2 from 1 to 5 through AppleScript.

## Observation

The pivot table in each exported sheet:

| File | Label | a | b | Total |
| --- | --- | --- | --- | --- |
| `sum.pdf` | (Summer) | 4 | 6 | 10 |
| `numbers-average.pdf` | (Gjennomsnitt) | 2 | 3 | 2,5 |
| `written-average.pdf` | (Summer) | 4 | 6 | 10 |
| `sum-edited.pdf`, B2 = 5 | (Summer) | 4 | 6 | 10 |
| `written-average-edited.pdf`, B2 = 5 | (Summer) | 4 | 6 | 10 |

`written-average.pdf` is pixel for pixel the same as `sum.pdf`.

## Conclusion

Numbers shows a pivot table's stored cells and label as they are. It doesn't recompute the pivot when it opens the document, so the written function has no visible effect yet. It doesn't recompute it when the source changes either: after B2 became 5 the pivot still said a = 4, until it is refreshed in the app. So a reader is right to show a pivot table's cells as they are, and a writer that changes a pivot's definition must also write the cells and labels it should show. Whether Numbers then reads 5.1.3 as Average when refreshing wasn't tested, since refreshing has no AppleScript command.

## Confidence

*Confirmed*: Numbers shows a pivot table's stored cells and doesn't recompute them on opening or when the source changes. The summary codes stay *likely*.
