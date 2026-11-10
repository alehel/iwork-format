# 0309: Writing a cell's background colour, and the colour space

**Status:** run

[0043](0043-cell-styles.md) found a cell's background colour in its cell style (type 6004), field 11.1.1: a colour message with red, green and blue as floats in fields 3, 4 and 5. The spec left the colour space open ([text.md](../spec/text.md#styles)). AppleScript reads a cell's `background color` as three 16-bit numbers. This experiment writes a new colour and compares what Numbers reports with the stored values.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0043/styles.numbers`: F2's background is red, set through AppleScript, in an unnamed cell style, record 905274 |
| Writer | [`recipes/0302-set-path.py`](../recipes/0302-set-path.py) |

## Recipe

```bash
mkdir -p samples/0309
cp samples/0043/styles.numbers samples/0309/original.numbers
python3 -I recipes/0302-set-path.py samples/0309/original.numbers samples/0309/written.numbers 905274 \
  11.1.1.3 float 0.2 11.1.1.4 float 0.4 11.1.1.5 float 0.8
```

The cell style's colour was 1.0, 0.1491, 0.0, with field 1 = 1, field 6 (alpha) = 1, field 12 = 1 and field 13 = 1. The script writes 0.2, 0.4, 0.8. Numbers opened each file on its own and read F2's `background color`, and the written file was saved again. The stored and reported values were then compared, through macOS's own colour conversions, for each pair of the sRGB, Display P3, Generic RGB, device RGB, extended sRGB and Adobe RGB colour spaces.

## Observation

| File | Stored | AppleScript | AppleScript / 65535 |
| --- | --- | --- | --- |
| `original.numbers` | 1.0, 0.1491, 0.0 | 64633, 466, 1797 | 0.986, 0.007, 0.027 |
| `written.numbers` | 0.2, 0.4, 0.8 | 10112, 20062, 49440 | 0.154, 0.306, 0.754 |

Numbers shows the cell in the new blue. The reported numbers aren't the stored ones scaled, so a conversion takes place. Converting the stored values from sRGB to Generic RGB gives 0.154, 0.306, 0.754 and 0.986, 0.007, 0.027: both matches to three decimals. Device RGB and extended sRGB, which equal sRGB here, convert the same way; no other pair matched.

## Conclusion

Colours are stored as sRGB components, and AppleScript reports them converted to Generic RGB. Writing the colour message changes the cell's background. Field 1 = 1 marks an RGB colour. Field 12 = 1 is probably the colour space, sRGB, but no colour with another value has been seen yet.

## Confidence

*Confirmed*: cell style field 11.1.1 is the background colour, by writing it.

*Likely*: colour messages hold sRGB components (two colours matched exactly).
