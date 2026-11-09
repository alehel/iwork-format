# 0217: An editable shape

**Status:** run

A shape's outline is in field 1.3 of its drawable ([0049](0049-text-box.md)), but its contents haven't been read. Pages can turn a shape into an editable path (Format → Shapes and Lines → Make Editable). This experiment compares the outline before and after, to read both forms.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0213/plain-shape.pages`, a 100 × 100 shape |

## Recipe

```bash
mkdir -p samples/0217
osascript recipes/0213-pages-shape.applescript 1
```

Then choose Format → Shapes and Lines → Make Editable (*Format → Figurer og linjer → Gjør redigerbar*) and save as `samples/0217/editable.pages`.

## Observation

In the baseline, field 1.3 of the shape (type 2011) is:

```
1: 0,  2: 0
5: { 2: 100 × 100,                         ← the path's natural size
     3: { 1: { 1: 1, 2: (0, 0) }           ← move to
          1: { 1: 2, 2: (100, 0) }         ← line to
          1: { 1: 2, 2: (100, 100) }
          1: { 1: 2, 2: (0, 100) }
          1: { 1: 5 }                      ← close
          1: { 1: 1, 2: (0, 0) } } }       ← move to
```

After Make Editable, field 5 is gone and field 8 holds the outline instead:

```
8: { 1: { 1: { 1: (0, 0),     2: (0, 0),     3: (0, 0),     4: 1 }
          1: { 1: (100, 0),   2: (100, 0),   3: (100, 0),   4: 1 }
          1: { 1: (100, 100), 2: (100, 100), 3: (100, 100), 4: 1 }
          1: { 1: (0, 100),   2: (0, 100),   3: (0, 100),   4: 1 }
          2: 1 },
     2: 100 × 100 }
```

Nothing else in the record changes.

## Conclusion

A shape's outline has two forms:

- **Field 1.3.5, a path:** a natural size (5.2) and a list of elements (5.3.1), each with a kind in field 1 and a point in field 2. The kinds are 1 move to, 2 line to and 5 close the path. Curves are probably 3 and 4.
- **Field 1.3.8, an editable path:** a list of nodes (8.1.1), each with three points, then a flag in field 4, plus a flag in 8.1.2 and the natural size in 8.2. The three points are probably the incoming control point, the node and the outgoing control point. For a sharp corner all three are equal. Field 4 is probably the kind of node (1 sharp), and 8.1.2 = 1 says the outline is closed.

Both are in the shape's own units, here the same as its size. A reader probably scales them from the natural size to the size in 1.1.2.

## Confidence

*Likely*: the two path forms and the element kinds 1, 2 and 5.

*Unknown*: the node flags, and how curves are stored. Follow-up: a shape with a curved edge.
