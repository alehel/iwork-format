# 0036: More cell formats

**Status:** run

[0031](0031-cell-kinds.md) decoded number, currency, percent, date and formula cells. Its boolean became the number 1, because AppleScript set the value without a checkbox format. This experiment sets six more formats explicitly through Numbers' AppleScript: checkbox, rating, fraction, scientific, text and duration.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0031](0031-cell-kinds.md) |

## Recipe

```bash
mkdir -p samples/0036
osascript recipes/0036-numbers-formats.applescript "$PWD/samples/0036/formats.numbers"
```

The recipe sets each cell's `format` first, then its value. Numbers' dictionary calls the star rating format `rating`. Reading the cells back through AppleScript gave:

| Cell | Format set | Value set | Shown | Format read back |
| --- | --- | --- | --- | --- |
| B2 | checkbox | true | `SANN` (true) | checkbox |
| C2 | rating | 3 | `3 ★` | rating |
| D2 | fraction | 0.5 | `1/2` | fraction |
| E2 | scientific | 1234.5 | `1,2345E+03` | scientific |
| F2 | text | "042" | `042` | text |
| G2 | duration | 90 | `90` | automatic |

## Observation

### The cells

Cells split by the byte offsets in tile field 5.7, as in 0031. Bytes 0–1 are the version and type, bytes 6–7 a 16-bit value, and bytes 8–11 the flags:

| Cell | Type | Bytes 6–7 | Flags | Value | Keys, in order |
| --- | --- | --- | --- | --- | --- |
| B2 | 6 | 0x0020 | 0x00041402 | double 1.0 | 1, 6, 1 |
| C2 | 2 | 0x0001 | 0x00003401 | decimal128 3 | 2, 1, 2 |
| D2 | 2 | 0x0001 | 0x00003001 | decimal128 5 × 10⁻¹ | 1, 3 |
| E2 | 2 | 0x0001 | 0x00003001 | decimal128 12345 × 10⁻¹ | 1, 4 |
| F2 | 3 | 0x0080 | 0x00021008 | — | 1, 5, 5 |
| G2 | 2 | 0x0004 | 0x00013001 | decimal128 90 | 1, 7, 6 |

### The format list

The table model's format list (`DataList-904541.iwa`, list type 2) has seven entries. Their field 1:

| Key | Field 1 | Other fields |
| --- | --- | --- |
| 1 | 263 | |
| 2 | 267 | |
| 3 | 262 | 11: −3 |
| 4 | 259 | 2: 253 |
| 5 | 260 | |
| 6 | 268 | 7: 1, 15: 4, 16: 16, 40: 1 |
| 7 | 256 | 2: 253 |

### A list of controls

`DataList-904554.iwa` (list type 12), empty in 0031, has two entries:

```
key 1: { 1: 8 }
key 2: { 1: 6, 3: 0.0, 4: 5.0, 5: 1.0 }
```

## Conclusion

Taking each cell's keys in order of its flag bits, every key but one fits a list:

| Flag bit | Followed by |
| --- | --- |
| 0x00002 | A double. A checkbox's value: 1.0 for true. |
| 0x00008 | A string key ([0021](0021-table-cells.md)) |
| 0x00400 | A key into the control list (list type 12): B2 → 1 (the checkbox), C2 → 2 (a rating from 0 to 5 in steps of 1) |
| 0x01000 | Still unidentified: 6, 1, 1, 1, 5 and 1 here |
| 0x02000 | Number format: C2 → 2 (rating), D2 → 3 (fraction), E2 → 4 (scientific), G2 → 7 (number) |
| 0x10000 | Duration format: G2 → 6 |
| 0x20000 | Text format: F2 → 5 |
| 0x40000 | Boolean format: B2 → 1 (checkbox) |

That adds to the format kinds of 0031 (256 number, 257 currency, 258 percent, 261 date): 259 scientific, 260 text, 262 fraction, 263 checkbox, 267 rating and 268 duration. Cell type 6 is a boolean.

G2 carries a duration format key, but Numbers reported its format as automatic and showed `90`. A cell can keep formats for several kinds side by side, here a number format (key 7) and a duration format (key 6). Which one applies probably depends on the value's kind, so the number format won for a plain number.

Bytes 6–7 differ by format: 0x0020 for the checkbox, 0x0080 for text, 0x0004 for the duration and 0x0001 for the others. In 0031 they were 0x0802 for currency and 0x0001 for percent. They may record which format the user chose, but that isn't established.

## Confidence

*Likely*: the flag bits and format kinds listed above, cell type 6 as a boolean, and list type 12 as cell controls.

*Unknown*:

- Flag bit 0x1000 and its list.
- Bytes 6–7.
- Why the duration format wasn't applied.
