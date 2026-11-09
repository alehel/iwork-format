# 0066: Comparisons and IF

**Status:** run

In [0064](0064-operators-and-functions.md), an IF formula written with commas was rejected. This experiment writes it with semicolons, as Norwegian Numbers expects, together with each comparison operator.

## Setup

| | |
| --- | --- |
| Numbers | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0064](0064-operators-and-functions.md) |

## Recipe

```bash
mkdir -p samples/0066
osascript recipes/0066-numbers-if.applescript "$PWD/samples/0066/if.numbers"
```

The recipe sets B2 to 4 and writes six formulas in E2 to E7.

## Observation

| Cell | Formula | Shown | Nodes |
| --- | --- | --- | --- |
| E2 | `=IF(B2>1;1;0)` | 1 | 36 17(1) **7** **34** 17(1) **35** **34** 17(0) **35** 16(function **62**, 3) |
| E3 | `=B2<1` | USANN (false) | 36 17(1) **9** |
| E4 | `=B2=4` | SANN (true) | 36 17(4) **11** |
| E5 | `=B2>=4` | SANN | 36 17(4) **8** |
| E6 | `=B2<=4` | SANN | 36 17(4) **10** |
| E7 | `=B2<>4` | USANN | 36 17(4) **12** |

## Conclusion

The comparison nodes are 7 `>`, 8 `>=`, 9 `<`, 10 `<=`, 11 `=` and 12 `<>`. IF is function 62, which fits the alphabetical numbering of [0064](0064-operators-and-functions.md). Its second and third arguments are each wrapped in a node 34 before and a node 35 after. Those probably mark arguments to be evaluated only when needed, since IF uses only one of them. The first argument, the condition, isn't wrapped.

Formulas typed in a Norwegian Numbers separate arguments with `;`, but the stored form has no separators, so it doesn't depend on the language.

## Confidence

*Likely*:

- The comparison nodes 7–12.
- IF is function 62.
- Nodes 34 and 35 bracket arguments that IF evaluates only when needed.
