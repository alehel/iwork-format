# 0073: A table in Keynote

**Status:** run

This experiment adds a table to a Keynote slide, to compare it with the tables of Pages and Numbers.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0025](0025-keynote-title.md), `empty.key`; experiment [0052](0052-floating-table.md) |

## Recipe

```bash
mkdir -p samples/0073
osascript recipes/0068-keynote-variants.applescript "$PWD/samples/0073/table.key" table
```

The recipe makes a 3 × 3 table on slide 1.

## Observation

`CalculationEngine.iwa` gained a drawable (type 6000) with the position (95, 215), the size 1730 × 650, and field 1.2 naming the slide. It also gained a table model (type 6001) and the same kinds of supporting records as in Pages and Numbers (types 4004, 4008, 4009 and 6204). The package gained table parts under `Index/Tables/`.

## Conclusion

Keynote's tables are the same as Pages' and Numbers': a drawable (type 6000) and a model (type 6001) in `CalculationEngine.iwa`, with cells in table parts. As with other Keynote drawables, field 1.2 names the slide. A table reader can therefore be shared by all three apps. Only the route to the drawable differs: text attachment or page in Pages, sheet in Numbers, slide in Keynote.

## Confidence

*Likely*: Keynote tables use types 6000 and 6001, as in the other apps.
