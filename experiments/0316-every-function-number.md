# 0316: Every function number

**Status:** run

Earlier experiments mapped function numbers one function at a time: 123 of them, set through AppleScript and read from the file ([0223](0223-functions.md), [0248](0248-more-functions.md)). [0315](0315-writing-a-formula-function.md) showed that writing a number into a formula's function-call node makes Numbers show that function. This experiment does it for every number from 1 to 400 and reads each formula back, giving the whole table from the app itself.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, started in English (`open -a "Numbers Creator Studio" --args -AppleLanguages "(en)"`) so that formulas show English names |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-10 |
| Input | `samples/0104/nested.numbers`: E2 = ROUND(AVERAGE(B2:C2) × 1.5; 0), whose formula list (record 904540) calls function 15 once |
| Script | [`recipes/0316-function-sweep.sh`](../recipes/0316-function-sweep.sh), using [`recipes/0315-formula-function.py`](../recipes/0315-formula-function.py) |

## Recipe

```bash
mkdir -p samples/0316
zsh recipes/0316-function-sweep.sh 1 400 "$PWD/samples/0316/functions.tsv"
```

For each number, the script writes it in place of function 15, opens the file in Numbers through Launch Services, reads E2's `formula` and `value` through AppleScript, and closes it. The resulting table is [`recipes/0316-functions.tsv`](../recipes/0316-functions.tsv). Numbers was then restarted in the user's language.

## Observation

Of the 400 numbers, 399 gave a formula; number 337 gave none. In order:

| Numbers | What Numbers shows |
| --- | --- |
| 1–167 | Function names in English alphabetical order, ABS to YEAR |
| 168 | SUM |
| 169–184 | Operators: `*`, `/`, `^`, `%`, `+`, `-`, `(null)` (175), `+`, `-`, `&`, `<`, `>`, `<=`, `>=`, `=`, `<>` |
| 185–278, 280, 285–306, 309–325, 328–336, 338, 341–391 | More function names, in no alphabetical order, such as 185 NORMDIST, 193 YIELDMAT, 204 MONTHNAME and 338 SEQUENCE |
| 279 | `:` |
| 326, 327 | `(null)` |
| 339, 340 | `@` and `#` |
| 281–284, 307, 308, 392–400 | `Unsupported` |

363 numbers are function names. Every function in earlier experiments has the number found there, including 60 HOUR, 152 TIME and 168 SUM. Values were recalculated: `ABS` of a range gave 6, and functions that don't take a single range gave no value.

## Conclusion

Function numbers 1 to 167 are Numbers' original functions in alphabetical order, 168 is SUM, and 169 to 184 are the operators, which formulas also use as nodes. The later functions were added in the order Apple added them, up to 391. The full table is in `recipes/0316-functions.tsv`, so a reader can name any function a formula calls without keeping its own list.

## Confidence

*Confirmed*: the number of every function from 1 to 391, read from Numbers itself.
