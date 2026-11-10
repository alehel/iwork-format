# 0367: Writing the orientation

**Status:** run

In the document root, field 42 is the orientation (0 portrait, 1 landscape), and in a landscape document the paper width and height (fields 30 and 31) are already swapped ([0155](0155-landscape-template.md)). This experiment checks which of the two decides the page Pages draws. It writes the flag alone, the swapped size alone, and both.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0002/hello.pages`: portrait A4, 595.28 × 841.89, field 42 = 0 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py), with the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
mkdir -p samples/0367
R=recipes/0302-set-path.py
B=samples/0002/hello.pages
python3 -I $R $B samples/0367/flag-only.pages 1 42 varint 1
python3 -I $R $B samples/0367/swap-only.pages 1 30 float 841.89 31 float 595.28
python3 -I $R samples/0367/swap-only.pages samples/0367/both.pages 1 42 varint 1
```

Pages opened each file on its own, exported a PDF, and saved a copy (`-resaved`), whose fields were read back.

## Observation

| File | Written: 30 × 31, 42 | PDF page | After Pages saved: 30 × 31, 42 |
| --- | --- | --- | --- |
| `flag-only.pages` | 595.28 × 841.89, 1 | 596 × 842 | 595.28 × 841.89, 1 |
| `swap-only.pages` | 841.89 × 595.28, 0 | 842 × 596 | 841.89 × 595.28, 0 |
| `both.pages` | 841.89 × 595.28, 1 | 842 × 596 | 841.89 × 595.28, 1 |

In each PDF the text starts at the margins, 57 points from the left and 58 from the top.

## Conclusion

The page is drawn from fields 30 and 31 alone. Field 42 doesn't turn the page, and Pages neither corrects it nor the size to match: it saves both as they were written. To make a landscape page, write the swapped size and set 42 = 1, as Pages itself does, so its orientation control agrees.

## Confidence

*Confirmed*: the page size comes from fields 30 and 31, not field 42, by writing them. *Likely*: field 42 only drives the orientation shown in the Document sidebar, which wasn't looked at.
