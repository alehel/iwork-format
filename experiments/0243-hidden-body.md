# 0243: A hidden body placeholder

**Status:** run

[0101](0101-hidden-title.md) found that hiding a slide's title removes a reference from the slide's field 7. This experiment hides the body placeholder instead, to see how the slide lists its placeholders.

## Setup

| | |
| --- | --- |
| Keynote | 15.4 |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0243/body.key`, the same slide with its body shown |

## Recipe

```bash
mkdir -p samples/0243
osascript recipes/0243-keynote-body-showing.applescript "$PWD/samples/0243"
```

The recipe adds a second slide to two new presentations, with the default layout for new slides (*Tittel og punkttegn*, Title & Bullets). In `no-body.key` it sets the slide's `body showing` to false.

## Observation

Both slides have the same records: three type-7 placeholders and one type-2011 shape. In the slide record (type 5) of `body.key`:

| Field | Names |
| --- | --- |
| 5 | 2652480, a type-7 placeholder |
| 6 | 2652511, a type-7 placeholder |
| 7 (repeated) | 2652480, 2652492 (the type-2011 shape), 2652511 |
| 42 (repeated) | 2652480, 2652492, 2652511 |

In `no-body.key`, 2652511 is missing from fields 7 and 42. Field 6 still names it, and the placeholder record is still there.

Rechecking `samples/0101/notitle.key`: there, field 5 names the title placeholder, which is missing from fields 7 and 42, while field 6 names the body placeholder, which is listed in both.

## Conclusion

A slide names its title placeholder in field 5 and its body placeholder in field 6, whether they are shown or not. Fields 7 and 42 list the objects on the slide that are shown, including those placeholders when they are visible. Hiding a placeholder only removes it from those two lists. So the reading of 0101, that field 7 names the title, was too narrow: field 7 lists every shown placeholder. A reader should draw what fields 7 and 42 list. Why there are two lists is unknown, but field 42 is possibly the drawing order.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `body.key` | | `5 6 = present` | *Control*: the slide with its body shown |
| `no-body.key` | `body.key` | `5 7.1: ×47 → ×46`, `5 42.1: ×47 → ×46`, `5 6.1: ×19 → ×19` | *Likely*: a hidden body placeholder is left out of the shown objects in fields 7 and 42, and field 6 still names it |
| `0101/notitle.key` | `0025/hello.key` | `5 7.1: ×44 → ×43`, `5 42.1: ×44 → ×43`, `5 5.1: ×18 → ×18` | *Likely*: the same for a hidden title, which field 5 still names |

## Confidence

*Likely*:

- Slide fields 5 and 6 name the title and body placeholders.
- Fields 7 and 42 list the shown objects.

*Unknown*: the difference between fields 7 and 42.
