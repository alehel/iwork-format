# 0216: A group

**Status:** run

Pages can group objects so they move as one. This experiment groups two shapes, to see how a group holds its members and where their positions are measured from.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0215/blue-style.pages`, the same two shapes ungrouped |

## Recipe

Continuing from experiment [0215](0215-shape-style-preset.md), with both shapes still selected:

1. Choose Arrange → Group (*Ordne → Gruppér*).
2. Save as `samples/0216/group.pages`.

The shapes are 100 × 100, at (300, 300) and (450, 300).

## Observation

`Document.iwa` gains one record, of type 3008, and two of type 3097. The page-level record (type 10015) now lists the body and the group (1732829) instead of the two shapes.

The group:

```
1.1.1: 300, 300        ← position
1.1.2: 250 × 100       ← size: the box around both shapes
1.1.3: 3,  1.1.4: 0
2: { 1: 1732821 }      ← the first shape
2: { 1: 1732823 }      ← the second shape
```

Each shape's drawable field 1.2 now names the group, and its position is measured from the group's corner:

| Shape | 1.1.1 before | 1.1.1 grouped |
| --- | --- | --- |
| 1732821 | 300, 300 | 0, 0 |
| 1732823 | 450, 300 | 150, 0 |

## Conclusion

A group is a type-3008 drawable whose repeated field 2 lists its members. The group has its own geometry, the box around its members. Each member names the group as its parent (field 1.2) and is positioned relative to the group's top-left corner, so a reader must add the group's position (and apply its rotation) to place the members on the page. Only the group is listed on the page.

## Confidence

*Likely*: a group is type 3008 listing its members in field 2, and members are positioned relative to it.

*Unknown*: how a rotated or resized group changes its members' geometry.
