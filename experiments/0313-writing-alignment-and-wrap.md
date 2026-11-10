# 0313: Writing a cell's alignment and text wrap

**Status:** run

A cell's horizontal alignment was read as field 12.1 of its text style (type 2022), with Pages' values (0 left, 1 right, 2 centred, [0061](0061-cell-alignment.md)), and its text wrap as field 11.3 of its cell style (type 6004), 0 when off ([0062](0062-text-wrap.md)). AppleScript reads a cell's `alignment` and `text wrap`. This experiment writes both and asks Numbers.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0061/center.numbers`: B2 centred, through text style 905237 with 12.1 = 2; `samples/0062/top-nowrap.numbers`: B2 without wrapping, through cell style 905247 with 11.3 = 0 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0313
cp samples/0061/center.numbers samples/0313/center.numbers
cp samples/0062/top-nowrap.numbers samples/0313/nowrap.numbers
python3 -I recipes/0302-set-path.py samples/0313/center.numbers samples/0313/right.numbers 905237 12.1 varint 1
python3 -I recipes/0302-set-path.py samples/0313/nowrap.numbers samples/0313/wrap.numbers 905247 11.3 varint 1
```

Numbers opened each file on its own and read B2 through AppleScript; the written files were saved again.

## Observation

| File | Alignment | Text wrap |
| --- | --- | --- |
| `center.numbers` | center | true |
| `right.numbers` | right | true |
| `nowrap.numbers` | auto align | false |
| `wrap.numbers` | auto align | true |

## Conclusion

Text style field 12.1 = 1 right-aligns a cell, as in Pages' paragraph styles, and cell style field 11.3 = 1 wraps its text. A cell with no alignment of its own reads as `auto align`.

## Confidence

*Confirmed*: cell alignment 12.1 and text wrap 11.3, by writing them.
