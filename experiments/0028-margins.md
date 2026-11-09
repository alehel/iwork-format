# 0028: Margins

**Status:** run

[0027](0027-document-roots.md) found the page margins in fields 32–35 of Pages' document root, but all four were 2 cm, so it couldn't say which field is which margin. This experiment sets four different margins.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0027](0027-document-roots.md): the root of `samples/0002/hello.pages` (all margins 2 cm) |

## Recipe

1. AppleScript makes a new document and sets its body text to `one`.
2. In the Pages window, Document tab of the sidebar, under *Dokumentmarger*: set *Øverst* (top) to 1 cm, *Venstre* (left) to 3 cm and *Høyre* (right) to 4 cm. *Nederst* (bottom) stays at 2 cm.
3. AppleScript saves the document as `samples/0028/margins.pages`.

## Observation

Fields 30–38 of the document root (object 1, type 10000):

```
30: 595.28      31: 841.89
32: 85.03937    33: 113.385826    34: 28.346457    35: 56.692917
36: 35.43307    37: 42.519684     38: 1.0
```

In points (1 cm = 72 / 2.54 points), the four margins are 28.35 (1 cm), 56.69 (2 cm), 85.04 (3 cm) and 113.39 (4 cm).

## Conclusion

| Field | Margin |
| --- | --- |
| 32 | Left |
| 33 | Right |
| 34 | Top |
| 35 | Bottom |

All are in points, as floats. The other page-setup fields kept the values of 0027.

## Confidence

*Likely*: fields 32–35 of Pages' document root are the left, right, top and bottom margins, in points.

*Unknown*: whether the left and right fields become inner and outer margins when facing pages is on. With facing pages on, the sidebar labels them *Innvendig* (inside) and *Utvendig* (outside), as seen in [0017](0017-section-switches.md).
