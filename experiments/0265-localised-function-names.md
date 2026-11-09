# 0265: Localised function names

**Status:** run

[0248](0248-more-functions.md) found that `TIME(1;2;3)` and `HOUR(NOW())` were both stored as function 60, although TIME should fall near 151 in the alphabetical order of function numbers. This experiment tests whether the language the formulas are typed in explains it: the apps run in Norwegian, where function names are translated.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0248](0248-more-functions.md) |

## Recipe

```bash
mkdir -p samples/0265
while IFS=$'\t' read name formula; do
  osascript recipes/0103-numbers-formula.applescript "$PWD/samples/0265/$name.numbers" "$formula"
done < recipes/0265-functions.tsv
```

`recipes/0265-functions.tsv` holds four formulas: `TID` (Norwegian for TIME), `SUMMER` (SUM), `MINUTT` (MINUTE) and the English `TIMEVALUE`. Separately, a formula `=HOUR(NOW())` was set through AppleScript and its `formula` read back.

## Observation

| Formula | Function number |
| --- | --- |
| `=TID(1;2;3)` | 152, with 3 arguments |
| `=SUMMER(B2;C2)` | 168, as for `SUM` |
| `=MINUTT(NOW())` | 90, as for `MINUTE` |
| `=TIMEVALUE("1:00")` | 153 |

`=HOUR(NOW())` is read back as `=TIME(NÅ())`.

The full node of 0248's `TIME(1;2;3)` is `{ 1: 16, 2: 60, 3: 3 }`, the same as HOUR's apart from the argument count.

## Conclusion

Numbers parses formulas in the app's language. It accepts English names too, unless an English name is also a Norwegian one. `TIME` is the Norwegian name of HOUR, so 0248's `=TIME(1;2;3)` was stored as HOUR (60) called with three arguments, a formula Numbers would show as an error. English TIME is 152, between TEXT and TIMEVALUE (153), as the alphabetical order of 0223 predicts.

The file stores only the number, never a name. So formulas are portable between languages, and a reader must print function names from a table such as this spec's, in the language it wants. The TIME row of 0248 is wrong and should read HOUR with three arguments.

## Confidence

*Likely*: formulas set through AppleScript are parsed in the app's language, and the file stores language-independent function numbers.

*Likely*: TIME is 152.
