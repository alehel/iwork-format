# 0018: A page break and a left-page header

**Status:** run

[0017](0017-section-switches.md) found the *Facing pages* switch but couldn't say what a section's other two header-and-footer sets (fields 23 and 24) are for. This experiment turns facing pages on and adds a second page, which is a left-hand page. Then it types into that page's header, to see whether a left page uses a set of its own. Adding the page also shows how a page break is stored.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`), with a Norwegian (nb) user interface and default autocorrection |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0016](0016-header-and-footer.md), `header.pages` (text in the left header of a one-page document) |

## Recipe

1. AppleScript makes a new document and sets its body text to `one`.
2. In the Pages window, Document tab of the sidebar: turn on *Motstående sider* (Facing pages).
3. Click at the end of `one`, then choose Insert → Page Break (*Sett inn → Sideskift*) and type `two`. Pages capitalised it to `Two` on the new page.
4. View → Show Layout, then click the left box of the second page's header and type `left`.
5. Pages offered `Left` in a suggestion that blocked AppleScript. It was dismissed with its close button. It appeared only once the save had started, so it can't be cleared beforehand.
6. AppleScript saves the document as `left-page-header.pages`.

With facing pages on, Pages showed the first page on the right of a spread and the second page as the left page of the next spread.

## Observation

### The page break

The body's text:

```
3: bytes (7) 6f 6e 65 05 54 77 6f        "one", U+0005, "Two"
```

The page break is the single character U+0005. `iwork-probe` shows the field as bytes, not text, because it treats control characters that way.

The paragraph-style runs (field 5) have a second entry at 4, the position after U+0005. The section runs (field 17) still have one entry, pointing at section 1732296.

### The left page's header

The text `left` went into record 1732234. That is the same record that took the left header text on the single page in 0016, and it's in the header-and-footer set the section names in field 25. The section and its three sets are unchanged:

```
section 1732296: 17: 1, 18–21: 0, 22: 1, 23 → 1732380, 24 → 1732482, 25 → 1732544, 28: 0
set 1732544: header 1732234 ("left"), 1732385, 1732428; footer 1732501, 1732440, 1732492
```

## Conclusion

A page break is the character U+0005 in the text, and it also ends a paragraph: the paragraph after it gets its own entry in the paragraph-style runs.

Facing pages on its own doesn't give left pages their own headers. The left page used the same header text record as the right page, from the set in section field 25. So the sets in fields 23 and 24 belong to some option that is still off. Pages has a switch for different left and right pages in other versions. If 15.4 has one, it may only show in the Section tab once facing pages is on, and this experiment didn't look there.

## Confidence

*Likely*:

- A page break is U+0005 and also starts a paragraph.
- With facing pages on and no other switch, left and right pages share the set in section field 25.

*Unknown*: what the sets in fields 23 and 24 are for. Follow-up: with facing pages on, look in the Section tab for a left-and-right-pages switch, turn it on, and type into a left page's header.
