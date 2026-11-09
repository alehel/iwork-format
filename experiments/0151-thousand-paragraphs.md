# 0151: A thousand paragraphs

**Status:** run

[0005](0005-paragraphs.md) found one paragraph-style entry per paragraph. This experiment checks whether that holds for 1000 paragraphs that all have the same style.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | `samples/0020/plain.pages` (the body text `one`) |

## Recipe

```bash
mkdir -p samples/0151
osascript recipes/0149-pages-text.applescript paras "$PWD/samples/0151/paras.pages"
```

## Observation

The body text holds `p 1` to `p 1000`, 5,892 bytes. Field 5 has 1000 entries, 4,978 bytes in all, one at the start of each paragraph. The list-level (field 6) and list-style (field 7) tables still have one entry each.

## Conclusion

Pages writes one paragraph-style entry for every paragraph, even when the style doesn't change. A reader can count paragraphs from field 5. The list tables, though, only record changes.

## Confidence

*Confirmed*: field 5 has one entry per paragraph ([0005](0005-paragraphs.md) and this experiment).
