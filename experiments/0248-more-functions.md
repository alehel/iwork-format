# 0248: Seventy more functions

**Status:** run

[0223](0223-functions.md) mapped 44 formula functions and found that the numbers up to 168 follow the English names in alphabetical order. This experiment maps 70 more, covering maths, statistics, lookup, information, text, date and financial functions, to fill in the table and test the pattern.

## Setup

| | |
| --- | --- |
| Numbers | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0223](0223-functions.md) |

## Recipe

```bash
mkdir -p samples/0248
while IFS=$'\t' read name formula; do
  osascript recipes/0103-numbers-formula.applescript "$PWD/samples/0248/$name.numbers" "$formula"
done < recipes/0248-functions.tsv
```

Each formula's nodes are decoded as in 0223. Decimal numbers are typed with a comma, as Norwegian Numbers expects.

## Observation

The function number of each formula's outer call:

| Function | Formula | Number |
| --- | --- | --- |
| ACOS | `=ACOS(0)` | 4 |
| ASIN | `=ASIN(0)` | 9 |
| ATAN | `=ATAN(1)` | 11 |
| CEILING | `=CEILING(B2/3;1)` | 17 |
| CHAR | `=CHAR(65)` | 18 |
| CODE | `=CODE("A")` | 21 |
| COLUMN | `=COLUMN()` | 22 |
| COLUMNS | `=COLUMNS(B2:C3)` | 23 |
| COS | `=COS(0)` | 28 |
| COUNTBLANK | `=COUNTBLANK(B2:D2)` | 32 |
| DATEDIF | `=DATEDIF(DATE(2026;1;1);TODAY();"D")` | 40 |
| DEGREES | `=DEGREES(1)` | 44 |
| EDATE | `=EDATE(TODAY();1)` | 47 |
| EVEN | `=EVEN(3)` | 48 |
| EXACT | `=EXACT("a";"a")` | 49 |
| FACT | `=FACT(4)` | 51 |
| FIND | `=FIND("b";"abc")` | 53 |
| FLOOR | `=FLOOR(B2/3;1)` | 55 |
| FV | `=FV(0,05;10;-100)` | 57 |
| GCD | `=GCD(B2;C2)` | 58 |
| HLOOKUP | `=HLOOKUP(B2;B2:C3;1;FALSE())` | 59 |
| HOUR | `=HOUR(NOW())` | 60 |
| TIME | `=TIME(1;2;3)` | 60 |
| ISBLANK | `=ISBLANK(D2)` | 69 |
| ISERROR | `=ISERROR(B2/0)` | 70 |
| ISEVEN | `=ISEVEN(B2)` | 71 |
| ISODD | `=ISODD(B2)` | 72 |
| LARGE | `=LARGE(B2:C2;1)` | 74 |
| LCM | `=LCM(B2;C2)` | 75 |
| LOOKUP | `=LOOKUP(B2;B2:C2)` | 81 |
| MINUTE | `=MINUTE(NOW())` | 90 |
| MODE | `=MODE(B2;B2;C2)` | 93 |
| NPV | `=NPV(0,05;B2;C2)` | 99 |
| ODD | `=ODD(2)` | 100 |
| PMT | `=PMT(0,05;10;1000)` | 105 |
| PROPER | `=PROPER("ab cd")` | 114 |
| PV | `=PV(0,05;10;-100)` | 115 |
| QUOTIENT | `=QUOTIENT(B2;C2)` | 116 |
| RADIANS | `=RADIANS(90)` | 117 |
| RANDBETWEEN | `=RANDBETWEEN(1;6)` | 119 |
| RANK | `=RANK(B2;B2:C2)` | 120 |
| REPLACE | `=REPLACE("abc";2;1;"x")` | 122 |
| REPT | `=REPT("a";3)` | 123 |
| ROW | `=ROW()` | 129 |
| ROWS | `=ROWS(B2:C3)` | 130 |
| SEARCH | `=SEARCH("b";"abc")` | 131 |
| SECOND | `=SECOND(NOW())` | 132 |
| SIN | `=SIN(0)` | 134 |
| SMALL | `=SMALL(B2:C2;1)` | 138 |
| SUBSTITUTE | `=SUBSTITUTE("abc";"b";"x")` | 144 |
| SUMPRODUCT | `=SUMPRODUCT(B2:C2;B2:C2)` | 146 |
| TAN | `=TAN(0)` | 150 |
| TRUNC | `=TRUNC(B2/3)` | 157 |
| VALUE | `=VALUE("3")` | 159 |
| VAR | `=VAR(B2;C2)` | 160 |
| WEEKDAY | `=WEEKDAY(TODAY())` | 166 |
| EOMONTH | `=EOMONTH(TODAY();0)` | 203 |
| WORKDAY | `=WORKDAY(TODAY();5)` | 204 |
| WEEKNUM | `=WEEKNUM(TODAY())` | 206 |
| SUMIFS | `=SUMIFS(B2:C2;B2:C2;">1")` | 231 |
| AVERAGEIFS | `=AVERAGEIFS(B2:C2;B2:C2;">1")` | 232 |
| COUNTIFS | `=COUNTIFS(B2:C2;">1")` | 233 |
| NETWORKDAYS | `=NETWORKDAYS(DATE(2026;1;1);TODAY())` | 260 |
| DAYS360 | `=DAYS360(DATE(2026;1;1);TODAY())` | 261 |
| ISNUMBER | `=ISNUMBER(B2)` | 304 |
| ISTEXT | `=ISTEXT(B2)` | 305 |
| IFS | `=IFS(B2>1;1;TRUE();0)` | 313 |
| TEXTBEFORE | `=TEXTBEFORE("a-b";"-")` | 318 |
| SWITCH | `=SWITCH(B2;4;"a";"b")` | 336 |
| XOR | `=XOR(B2>1;C2>1)` | 382 |

All 70 formulas were accepted and stored.

## Conclusion

The new numbers fit the pattern of 0223 for the functions up to 167, with one correction: SUM is 168, after YEAR (167), so SUM is the one function out of alphabetical order in that range. 0223 wrongly counted it in the order. Every other function numbered up to 167, 117 functions in all, follows the alphabetical order of its English name.

Functions numbered above 168 are later additions, in no alphabetical order: EOMONTH 203, WORKDAY 204, WEEKNUM 206, the `…IFS` family 231–233, NETWORKDAYS 260, DAYS360 261, ISNUMBER 304, ISTEXT 305, IFS 313, TEXTBEFORE 318, SWITCH 336, XOR 382.

One result doesn't fit. `TIME(1;2;3)` is stored as function 60 with 3 arguments, the same number as `HOUR` with 1 argument. Alphabetically, TIME belongs near 151. Numbers reads the formula back as `=TIME(1;2;3)`, so it must tell them apart, perhaps by the number of arguments or by a field the decoder doesn't print.

## Confidence

*Likely*:

- The numbers in the table, each from one sample.
- Numbers 1–167 follow alphabetical order, from 117 functions.

*Unknown*: how TIME and HOUR, both 60, are told apart. Follow-up: dump every field of both call nodes.
