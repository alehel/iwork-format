# 0160: A moved slide

**Status:** run

This experiment moves the third of three slides to the front, to see what changes besides the order.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0038](0038-second-slide.md), `two-slides.key` |

## Recipe

```bash
mkdir -p samples/0160
osascript recipes/0159-keynote-slides.applescript move "$PWD/samples/0160/move.key"
```

## Observation

Field 3.2 of the presentation lists the nodes in the new order: 2652643 (titled `C`), 2652174 (`A`) and 2652520 (`B`). The nodes, slides and text records keep the IDs they'd have had without the move, and each slide stays in its own part.

## Conclusion

Moving a slide changes only the order of the list in field 3.2. Show order comes from that list, not from IDs or part names; here the first slide in the show has the highest ID.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `move.key` | `0038/two-slides.key` | `2 3.2: ×2 → ×3`, `2001 3: absent → "A"`, `2001 3: absent → "B"`, `2001 3: absent → "C"` | *Likely*: three slides are listed in field 3.2, one of them moved |
| `move.key` | `0038/two-slides.key` | `2 3 ~ x"120508e3f3a1011205088ef0a101120508e8f2a101"`, original only: the remake lists its slides in the same order by other IDs | *Likely*: the order of the list in field 3.2 is the order of the show, whatever the IDs |

## Confidence

*Likely*: show order is field 3.2's order alone.
