# Accessibility checks

What has been checked on the site, how, and with what result. Rerun these when the layout, colours or builder change, and add a dated section.

## 2026-11-23

**Browser:** the Claude desktop app's built-in browser (Chrome 156 engine) on macOS 26.5.2, light and dark colour schemes. Not tested: Safari, Firefox, and a real screen reader (VoiceOver was not run). The keyboard-scroll fix below matters mostly for Safari, which doesn't make scrolling areas focusable by itself.

**Pages:** the overview, `spec/index`, `spec/text`, `spec/tables`, `spec/styles`, `spec/types`, `spec/releases`, `experiments/index`, experiments 0268 and 0465, and the guides `anatomy` and `numbers-table`.

**Widths:** 320 (the width 400% zoom gives on a 1280-pixel window), 375, 960 and 1400 CSS pixels.

| Check | How | Result |
| --- | --- | --- |
| Text contrast | Computed WCAG ratios for every colour pair in `style.css`, both schemes | All text pairs pass 4.5:1; the lowest are `--mark` on the notice's background, 4.69:1 (light), and `--fg-soft` on code background, 5.67:1 |
| Links told apart from text | Ratio of link colour to text colour, which must reach 3:1 when colour alone marks a link | **Failed**: 2.65:1 light, 1.76:1 dark. Fixed: links in the page's text are underlined |
| Section links (`#`) | Contrast when shown | **Failed**: 1.26:1 light, 1.39:1 dark. Fixed: drawn in `--fg-soft` (6.2:1, 7.1:1) |
| Skip link | Tab from the top, then Enter | First stop; moves focus to the page's text |
| Focus order | Tab through `spec/tables` from the top | Skip link, header, notice, contents, on-this-page list, page. **Found**: on wide screens the on-this-page heading was a Tab stop that folded the list. Fixed: it isn't focusable there |
| Visible focus | Tab through, checking `:focus-visible` styles | Links relied on the browser's default ring. Fixed: one 2-pixel ring in `--accent` for everything focusable |
| Current page | Accessibility tree of the contents | `aria-current="page"` on the current page's link |
| Section links on focus | Tab to a heading's `#` | Shown on focus, named "Link to this section: …" |
| Reflow | Page width against the viewport at 320 pixels, every page above | No page scrolls sideways; wide tables and code scroll inside their own box |
| Scrolling tables and code | Keyboard focus of boxes wider than the page | **Failed** outside Chrome: not focusable. Fixed: a box that overflows gets `tabindex="0"`, `role="region"` and a name ("Table, scrolls sideways"), recomputed on resize |
| Target size | Links and controls outside running text under 24×24 pixels | **Failed**: the release line (20 pixels tall) and `#` links (13–15 pixels wide). Fixed by padding. Links inside sentences are exempt |
| Table headers | Header cells in the built pages | **Failed**: 465 pages (experiment setups) had a header row of 951 empty cells. Fixed: tables written with an empty header row get row headers instead (`<th scope="row">`); other headers get `scope="col"` |
| Figures | Alt text and captions | Every image has a description, but the caption repeated it, so it was read twice. Fixed: the caption is hidden from assistive technology |
| Link names | Links named "here", "this", "more" | None |
| Headings | Skipped levels | None on any page |
| Reduced motion | `prefers-reduced-motion` | Transitions (the fold arrows) are turned off |
| Language | `lang` on every page | `en` |
