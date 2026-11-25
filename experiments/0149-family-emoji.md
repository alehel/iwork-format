# 0149: A family emoji

**Status:** run

[0003](0003-non-ascii-word.md) found that positions count UTF-16 code units. This experiment uses an emoji made of several code points joined by zero-width joiners, and gives the paragraph after it its own size.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0020/plain.pages` (the body text `one`) |

## Recipe

```bash
mkdir -p samples/0149
osascript recipes/0149-pages-text.applescript zwj "$PWD/samples/0149/zwj.pages"
```

## Observation

The body text is `👨‍👩‍👧`, a line feed, and `two`: 18 UTF-8 bytes for the emoji, which is three emoji joined by two U+200D characters. That's 8 UTF-16 code units.

The paragraph-style runs (field 5) have two entries: Body (1731511) from 0, and a new style 1732647 from 9. There are no character-style runs (field 8).

Style 1732647 is a paragraph style (type 2022) in `DocumentStylesheet.iwa`. Its parent (1.3) is Body, and its field 11 sets only the size, 20.

## Conclusion

The second paragraph starts at 9: the emoji's 8 UTF-16 units plus the line feed. A joined emoji is not one position, and not one per emoji either: every code unit counts, joiners included.

Setting the size of a whole paragraph through AppleScript made an unnamed paragraph style, as Pages did in [0008](0008-runs-and-shared-styles.md), not a character style.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `zwj.pages` | `0020/plain.pages` | `2001 3 ~ x"f09f91a8e2808df09f91a9e2808df09f91a70a74776f"`, `2001 5.1.1: absent → 9` | *Confirmed*: positions count UTF-16 code units, eight for this joined emoji |
| `zwj.pages` | `0020/plain.pages` | `records 2022: 242 → 243`, `2022 11.3: absent → 20.0`, `2001 8: ×0 → ×0` | *Likely*: formatting a whole paragraph makes a paragraph style |

## Confidence

*Confirmed*: positions count UTF-16 code units, here for a joined emoji.

*Likely*: formatting a whole paragraph makes a paragraph style based on the old one.
