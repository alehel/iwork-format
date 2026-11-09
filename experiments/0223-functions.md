# 0223: Forty-four functions

**Status:** run

Formula function calls are node type 16, with the function as a number in field 2 ([0064](0064-operators-and-functions.md)). Nine functions have been mapped so far. This experiment maps 44 more, one spreadsheet each, to give readers a usable table and to look for a pattern in the numbers.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiments [0064](0064-operators-and-functions.md) and [0103](0103-round.md)–[0112](0112-unary-minus.md) |

## Recipe

```bash
mkdir -p samples/0223
while IFS=$'\t' read name formula; do
  osascript recipes/0103-numbers-formula.applescript "$PWD/samples/0223/$name.numbers" "$formula"
done < recipes/0223-functions.tsv
```

`recipes/0223-functions.tsv` lists each function's name and a formula that uses it, with B2 = 4 and C2 = 2 as in 0103. Each formula's nodes are decoded from the formula list as in 0103.

Bare `TRUE` and `FALSE` aren't accepted as arguments through AppleScript: the cell is left empty. Written as `TRUE()` and `FALSE()`, they are function calls.

## Observation

The function number in field 2 of each formula's last type-16 node:

| Function | Formula | Number |
| --- | --- | --- |
| ABS | `=ABS(B2)` | 1 |
| AND | `=AND(B2>1;C2>1)` | 7 |
| CHOOSE | `=CHOOSE(1;B2;C2)` | 19 |
| CONCATENATE | `=CONCATENATE(B2;C2)` | 25 |
| COUNTA | `=COUNTA(B2:C2)` | 31 |
| COUNTIF | `=COUNTIF(B2:C2;">1")` | 33 |
| DATE | `=DATE(2026;11;9)` | 39 |
| DAY | `=DAY(TODAY())` | 41 |
| EXP | `=EXP(C2)` | 50 |
| FALSE | `=FALSE()` | 52 |
| INDEX | `=INDEX(B2:C3;1;2)` | 63 |
| INT | `=INT(B2/3)` | 65 |
| LEFT | `=LEFT("abc";1)` | 76 |
| LN | `=LN(B2)` | 78 |
| LOG10 | `=LOG10(B2)` | 80 |
| LOWER | `=LOWER("ABC")` | 82 |
| MATCH | `=MATCH(B2;B2:B3;0)` | 83 |
| MEDIAN | `=MEDIAN(B2;C2)` | 86 |
| MID | `=MID("abc";2;1)` | 87 |
| MOD | `=MOD(B2;3)` | 92 |
| MONTH | `=MONTH(TODAY())` | 94 |
| NOT | `=NOT(B2>1)` | 96 |
| NOW | `=NOW()` | 97 |
| OR | `=OR(B2>1;C2>1)` | 102 |
| PI | `=PI()` | 104 |
| POWER | `=POWER(B2;C2)` | 107 |
| PRODUCT | `=PRODUCT(B2;C2)` | 113 |
| RAND | `=RAND()` | 118 |
| RIGHT | `=RIGHT("abc";1)` | 124 |
| ROUNDDOWN | `=ROUNDDOWN(B2/3;1)` | 127 |
| ROUNDUP | `=ROUNDUP(B2/3;1)` | 128 |
| SIGN | `=SIGN(B2)` | 133 |
| SQRT | `=SQRT(B2)` | 139 |
| STDEV | `=STDEV(B2;C2)` | 140 |
| SUMIF | `=SUMIF(B2:C2;">1")` | 145 |
| TRIM | `=TRIM(" a ")` | 155 |
| TRUE | `=TRUE()` | 156 |
| UPPER | `=UPPER("abc")` | 158 |
| VLOOKUP | `=VLOOKUP(B2;B2:C3;2;FALSE())` | 165 |
| YEAR | `=YEAR(TODAY())` | 167 |
| AVERAGEIF | `=AVERAGEIF(B2:C2;">1")` | 234 |
| IFERROR | `=IFERROR(B2/C2;0)` | 235 |
| XLOOKUP | `=XLOOKUP(B2;B2:B3;C2:C3)` | 314 |
| TEXTJOIN | `=TEXTJOIN(",";TRUE();B2;C2)` | 328 |

Other nodes behave as already described:

- Each argument appears before the call.
- The number of arguments is in field 3.
- `CHOOSE` brackets each choice in nodes 34 and 35, like `IF` ([0066](0066-comparisons-and-if.md)).
- `IFERROR` doesn't bracket its arguments.

## Conclusion

Together with the earlier nine (15 AVERAGE, 30 COUNT, 62 IF, 77 LEN, 84 MAX, 88 MIN, 126 ROUND, 154 TODAY, 168 SUM), the numbers from 1 to 168 follow the functions' English names in alphabetical order: ABS 1, AND 7, AVERAGE 15, … TRUE 156, UPPER 158, VLOOKUP 165, YEAR 167. This is probably the original function list. Functions added later have numbers beyond it, outside the alphabetical order: AVERAGEIF 234, IFERROR 235, XLOOKUP 314, TEXTJOIN 328. A reader can use this table to print formulas. For other numbers, the alphabetical pattern narrows the range but can't name a function with certainty.

`TRUE()` and `FALSE()` are functions (156 and 52), not literals.

## Confidence

*Likely*: the numbers in the table, each from one sample.

*Likely*: numbers up to 168 are in alphabetical order, from 53 functions that all fit it.
