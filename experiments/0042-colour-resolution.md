# 0042: Colour and the style rule

**Status:** run

The style rule of [0033](0033-style-resolution.md) was tested for bold, italic, size and font, which Pages reports through the font name. This experiment checks the same rule for text colour (field 11.7, [0013](0013-text-colour.md)), using the `color` that Pages reports for each word.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Documents | `samples/0013/red.pages`, `0013/blue`, `0013/mixed`, `0008/unbold-middle`, `0006/heading-ui` |

## Recipe

Each document was opened in Pages through AppleScript. For each word of the body, `color` was read as three 16-bit components, and the document was closed without saving.

## Observation

| Document | Word | Colour Pages reports | Colour set in 0013 |
| --- | --- | --- | --- |
| 0013/red | one, three | 0, 0, 0 | — |
| | two | 64633, 466, 1797 | 65535, 0, 0 |
| 0013/blue | one, three | 0, 0, 0 | — |
| | two | 7, 114, 65418 | 0, 0, 65535 |
| 0013/mixed | one, three | 0, 0, 0 | — |
| | two | 32767, 16381, 652 | 32768, 16384, 0 |
| 0008/unbold-middle | one, two, three | 0, 0, 0 | — |
| 0006/heading-ui | One, two | 0, 0, 0 | — |

## Conclusion

The rule of 0033 predicts these colours. Only the words whose character style sets field 11.7 have a colour, and every other word gets black from the Body or Heading paragraph style. That includes the bold paragraph of `unbold-middle`, whose unnamed paragraph style sets no colour and inherits Body's.

The colour values don't survive a round trip through AppleScript: pure red comes back as 64633, 466, 1797. The file stores red as (1.0, 0.149, 0.0) ([0013](0013-text-colour.md)). So Pages converts colours both when AppleScript sets them and when it reads them, and the stored components are in a different colour space from AppleScript's. Which one is still unknown.

## Confidence

*Likely*: text colour follows the style rule of 0033.

*Unknown*: the colour space of stored colours. Follow-up: set a colour by its hex value in the Pages colour panel, with full-screen control, or by hand.
