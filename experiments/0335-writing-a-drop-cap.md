# 0335: Writing a drop cap's height, measured on the page

**Status:** run

[0261](0261-drop-cap.md) found drop caps as a text run (field 28) naming a drop-cap style (type 10024), whose 12.1.2 was read as the number of lines the drop cap spans. This experiment changes it and measures the letter.

## Setup

| | |
| --- | --- |
| Pages | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0261/drop-cap.pages`: the word `One` with a drop cap, through `dropcap-style-0` (record 1732137), whose 12.1.2 is 3; the Body style's lines are 12 points apart and the first line's baseline is at 66.2 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0335
cp samples/0261/drop-cap.pages samples/0335/three.pages
python3 -I recipes/0302-set-path.py samples/0335/three.pages samples/0335/six.pages 1732137 12.1.2 varint 6
```

Each file was opened in Pages on its own, exported as PDF and measured with [`recipes/0319-measure-pdf.swift`](../recipes/0319-measure-pdf.swift).

## Observation

| File | The drop cap `O` and `ne`: top – bottom, left – right |
| --- | --- |
| `three.pages` (3) | 57.5 – 90.5, 57.0 – 101.8 |
| `six.pages` (6) | 56.5 – 127.5, 57.0 – 136.2 |

The third line's baseline would be at 66.2 + 2 × 12 = 90.2 and the sixth's at 66.2 + 5 × 12 = 126.2.

## Conclusion

12.1.2 is the number of lines the drop cap spans: the letter is scaled to reach from the top of the first line down to the baseline of the last line it covers, 33 points tall for 3 lines and 71 for 6, and it grows wider in proportion.

## Confidence

*Confirmed*: drop-cap style 12.1.2 is the number of lines, by writing it and measuring.
