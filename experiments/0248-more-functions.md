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

*Corrected 2026-11-25:* the 117 can't be recounted: the tables of this experiment and 0223, with the functions known before, give 103. All of them fit the order. Function 60, which this table has twice, is HOUR ([0265](0265-localised-function-names.md)).

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `ACOS.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 4`, `6005 3.5.1.1.3 = 1` | *Likely*: `=ACOS(0)` calls function 4 |
| `ASIN.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 9`, `6005 3.5.1.1.3 = 1` | *Likely*: `=ASIN(0)` calls function 9 |
| `ATAN.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 11`, `6005 3.5.1.1.3 = 1` | *Likely*: `=ATAN(1)` calls function 11 |
| `CEILING.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 17`, `6005 3.5.1.1.3 = 2` | *Likely*: `=CEILING(B2/3;1)` calls function 17 |
| `CHAR.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 18`, `6005 3.5.1.1.3 = 1` | *Likely*: `=CHAR(65)` calls function 18 |
| `CODE.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 21`, `6005 3.5.1.1.3 = 1` | *Likely*: `=CODE("A")` calls function 21 |
| `COLUMN.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 22`, `6005 3.5.1.1.3 = 0` | *Likely*: `=COLUMN()` calls function 22 |
| `COLUMNS.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 23`, `6005 3.5.1.1.3 = 1` | *Likely*: `=COLUMNS(B2:C3)` calls function 23 |
| `COS.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 28`, `6005 3.5.1.1.3 = 1` | *Likely*: `=COS(0)` calls function 28 |
| `COUNTBLANK.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 32`, `6005 3.5.1.1.3 = 1` | *Likely*: `=COUNTBLANK(B2:D2)` calls function 32 |
| `DATEDIF.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 40`, `6005 3.5.1.1.3 = 3` | *Likely*: `=DATEDIF(DATE(2026;1;1);TODAY();"D")` calls function 40 |
| `DEGREES.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 44`, `6005 3.5.1.1.3 = 1` | *Likely*: `=DEGREES(1)` calls function 44 |
| `EDATE.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 47`, `6005 3.5.1.1.3 = 2` | *Likely*: `=EDATE(TODAY();1)` calls function 47 |
| `EVEN.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 48`, `6005 3.5.1.1.3 = 1` | *Likely*: `=EVEN(3)` calls function 48 |
| `EXACT.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 49`, `6005 3.5.1.1.3 = 2` | *Likely*: `=EXACT("a";"a")` calls function 49 |
| `FACT.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 51`, `6005 3.5.1.1.3 = 1` | *Likely*: `=FACT(4)` calls function 51 |
| `FIND.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 53`, `6005 3.5.1.1.3 = 2` | *Likely*: `=FIND("b";"abc")` calls function 53 |
| `FLOOR.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 55`, `6005 3.5.1.1.3 = 2` | *Likely*: `=FLOOR(B2/3;1)` calls function 55 |
| `FV.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 57`, `6005 3.5.1.1.3 = 3` | *Likely*: `=FV(0,05;10;-100)` calls function 57 |
| `GCD.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 58`, `6005 3.5.1.1.3 = 2` | *Likely*: `=GCD(B2;C2)` calls function 58 |
| `HLOOKUP.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 59`, `6005 3.5.1.1.3 = 4` | *Likely*: `=HLOOKUP(B2;B2:C3;1;FALSE())` calls function 59 |
| `HOUR.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 60`, `6005 3.5.1.1.3 = 1` | *Likely*: `=HOUR(NOW())` calls function 60 |
| `TIME.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 60`, `6005 3.5.1.1.3 = 3` | *Unknown*: why `=TIME(1;2;3)` has function 60, the number of HOUR |
| `ISBLANK.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 69`, `6005 3.5.1.1.3 = 1` | *Likely*: `=ISBLANK(D2)` calls function 69 |
| `ISERROR.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 70`, `6005 3.5.1.1.3 = 1` | *Likely*: `=ISERROR(B2/0)` calls function 70 |
| `ISEVEN.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 71`, `6005 3.5.1.1.3 = 1` | *Likely*: `=ISEVEN(B2)` calls function 71 |
| `ISODD.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 72`, `6005 3.5.1.1.3 = 1` | *Likely*: `=ISODD(B2)` calls function 72 |
| `LARGE.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 74`, `6005 3.5.1.1.3 = 2` | *Likely*: `=LARGE(B2:C2;1)` calls function 74 |
| `LCM.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 75`, `6005 3.5.1.1.3 = 2` | *Likely*: `=LCM(B2;C2)` calls function 75 |
| `LOOKUP.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 81`, `6005 3.5.1.1.3 = 2` | *Likely*: `=LOOKUP(B2;B2:C2)` calls function 81 |
| `MINUTE.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 90`, `6005 3.5.1.1.3 = 1` | *Likely*: `=MINUTE(NOW())` calls function 90 |
| `MODE.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 93`, `6005 3.5.1.1.3 = 3` | *Likely*: `=MODE(B2;B2;C2)` calls function 93 |
| `NPV.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 99`, `6005 3.5.1.1.3 = 3` | *Likely*: `=NPV(0,05;B2;C2)` calls function 99 |
| `ODD.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 100`, `6005 3.5.1.1.3 = 1` | *Likely*: `=ODD(2)` calls function 100 |
| `PMT.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 105`, `6005 3.5.1.1.3 = 3` | *Likely*: `=PMT(0,05;10;1000)` calls function 105 |
| `PROPER.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 114`, `6005 3.5.1.1.3 = 1` | *Likely*: `=PROPER("ab cd")` calls function 114 |
| `PV.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 115`, `6005 3.5.1.1.3 = 3` | *Likely*: `=PV(0,05;10;-100)` calls function 115 |
| `QUOTIENT.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 116`, `6005 3.5.1.1.3 = 2` | *Likely*: `=QUOTIENT(B2;C2)` calls function 116 |
| `RADIANS.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 117`, `6005 3.5.1.1.3 = 1` | *Likely*: `=RADIANS(90)` calls function 117 |
| `RANDBETWEEN.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 119`, `6005 3.5.1.1.3 = 2` | *Likely*: `=RANDBETWEEN(1;6)` calls function 119 |
| `RANK.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 120`, `6005 3.5.1.1.3 = 2` | *Likely*: `=RANK(B2;B2:C2)` calls function 120 |
| `REPLACE.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 122`, `6005 3.5.1.1.3 = 4` | *Likely*: `=REPLACE("abc";2;1;"x")` calls function 122 |
| `REPT.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 123`, `6005 3.5.1.1.3 = 2` | *Likely*: `=REPT("a";3)` calls function 123 |
| `ROW.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 129`, `6005 3.5.1.1.3 = 0` | *Likely*: `=ROW()` calls function 129 |
| `ROWS.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 130`, `6005 3.5.1.1.3 = 1` | *Likely*: `=ROWS(B2:C3)` calls function 130 |
| `SEARCH.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 131`, `6005 3.5.1.1.3 = 2` | *Likely*: `=SEARCH("b";"abc")` calls function 131 |
| `SECOND.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 132`, `6005 3.5.1.1.3 = 1` | *Likely*: `=SECOND(NOW())` calls function 132 |
| `SIN.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 134`, `6005 3.5.1.1.3 = 1` | *Likely*: `=SIN(0)` calls function 134 |
| `SMALL.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 138`, `6005 3.5.1.1.3 = 2` | *Likely*: `=SMALL(B2:C2;1)` calls function 138 |
| `SUBSTITUTE.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 144`, `6005 3.5.1.1.3 = 3` | *Likely*: `=SUBSTITUTE("abc";"b";"x")` calls function 144 |
| `SUMPRODUCT.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 146`, `6005 3.5.1.1.3 = 2` | *Likely*: `=SUMPRODUCT(B2:C2;B2:C2)` calls function 146 |
| `TAN.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 150`, `6005 3.5.1.1.3 = 1` | *Likely*: `=TAN(0)` calls function 150 |
| `TRUNC.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 157`, `6005 3.5.1.1.3 = 1` | *Likely*: `=TRUNC(B2/3)` calls function 157 |
| `VALUE.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 159`, `6005 3.5.1.1.3 = 1` | *Likely*: `=VALUE("3")` calls function 159 |
| `VAR.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 160`, `6005 3.5.1.1.3 = 2` | *Likely*: `=VAR(B2;C2)` calls function 160 |
| `WEEKDAY.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 166`, `6005 3.5.1.1.3 = 1` | *Likely*: `=WEEKDAY(TODAY())` calls function 166 |
| `EOMONTH.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 203`, `6005 3.5.1.1.3 = 2` | *Likely*: `=EOMONTH(TODAY();0)` calls function 203 |
| `WORKDAY.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 204`, `6005 3.5.1.1.3 = 2` | *Likely*: `=WORKDAY(TODAY();5)` calls function 204 |
| `WEEKNUM.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 206`, `6005 3.5.1.1.3 = 1` | *Likely*: `=WEEKNUM(TODAY())` calls function 206 |
| `SUMIFS.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 231`, `6005 3.5.1.1.3 = 3` | *Likely*: `=SUMIFS(B2:C2;B2:C2;">1")` calls function 231 |
| `AVERAGEIFS.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 232`, `6005 3.5.1.1.3 = 3` | *Likely*: `=AVERAGEIFS(B2:C2;B2:C2;">1")` calls function 232 |
| `COUNTIFS.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 233`, `6005 3.5.1.1.3 = 2` | *Likely*: `=COUNTIFS(B2:C2;">1")` calls function 233 |
| `NETWORKDAYS.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 260`, `6005 3.5.1.1.3 = 2` | *Likely*: `=NETWORKDAYS(DATE(2026;1;1);TODAY())` calls function 260 |
| `DAYS360.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 261`, `6005 3.5.1.1.3 = 2` | *Likely*: `=DAYS360(DATE(2026;1;1);TODAY())` calls function 261 |
| `ISNUMBER.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 304`, `6005 3.5.1.1.3 = 1` | *Likely*: `=ISNUMBER(B2)` calls function 304 |
| `ISTEXT.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 305`, `6005 3.5.1.1.3 = 1` | *Likely*: `=ISTEXT(B2)` calls function 305 |
| `IFS.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 313`, `6005 3.5.1.1.3 = 4` | *Likely*: `=IFS(B2>1;1;TRUE();0)` calls function 313 |
| `TEXTBEFORE.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 318`, `6005 3.5.1.1.3 = 2` | *Likely*: `=TEXTBEFORE("a-b";"-")` calls function 318 |
| `SWITCH.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 336`, `6005 3.5.1.1.3 = 4` | *Likely*: `=SWITCH(B2;4;"a";"b")` calls function 336 |
| `XOR.numbers` | `0103/round.numbers` | `6005 3.5.1.1.2: 126 → 382`, `6005 3.5.1.1.3 = 2` | *Likely*: `=XOR(B2>1;C2>1)` calls function 382 |

## Confidence

*Likely*:

- The numbers in the table, each from one sample.
- Numbers 1–167 follow alphabetical order, from 117 functions.

*Unknown*: how TIME and HOUR, both 60, are told apart. Follow-up: dump every field of both call nodes.
