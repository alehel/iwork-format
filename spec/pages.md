# Pages

What is specific to Pages documents: page setup, sections, and headers and footers. The container is described in [1. Container](container.md) and the body text in [2. Text](text.md). Every finding links to the experiments that support it, with a confidence level as defined in [CONTRIBUTING.md](../CONTRIBUTING.md#confidence).

Observed with Pages 15.4 on macOS 26.5.2.

## Page setup

Pages keeps its page setup in the document root (object 1, type 10000). All lengths are in points, as floats. *Likely* ([0027](../experiments/0027-document-roots.md), [0028](../experiments/0028-margins.md))

| Field | Holds |
| --- | --- |
| 30, 31 | Paper width and height (*confirmed* by writing them, [0318](../experiments/0318-writing-paper-size-and-margin.md)) |
| 32, 33, 34, 35 | Left, right, top and bottom margins (*confirmed* by writing them, [0318](../experiments/0318-writing-paper-size-and-margin.md), [0326](../experiments/0326-writing-top-and-right-margins.md), [0366](../experiments/0366-writing-bottom-margin-and-header-distances.md)) |
| 36, 37 | Header and footer distance from the page edge (*confirmed* by writing them, [0366](../experiments/0366-writing-bottom-margin-and-header-distances.md)). A header or footer that reaches past the margin pushes the body away from it |
| 43 | Printer name |
| 40 | Change tracking: 1 while it is on. Fields 16 and 17 then name the current editing session, a type-2062 record ([0269](../experiments/0269-rejected-insertion.md)) |
| 42 | Orientation: 0 portrait, 1 landscape; 30 and 31 are already swapped ([0155](../experiments/0155-landscape-template.md)). The page is drawn from 30 and 31 alone: writing 42 doesn't turn it, and Pages doesn't make the two agree (*confirmed* by writing, [0367](../experiments/0367-writing-orientation.md)) |
| 44 | Paper name, such as `iso-a4`; empty for a custom size, as in the book templates, which make ordinary documents ([0198](../experiments/0198-book-template.md)) |
| 15.9 | The identifier of the template the document came from, such as `Application/Blank/ISO` ([0155](../experiments/0155-landscape-template.md)) |
| 48 | Only in page-layout documents: names a page template (type 10017). Their body text record is empty. ([0156](../experiments/0156-page-layout-template.md)) |

## Headers and footers

Header and footer text is in type-2001 records, like the body. They are reached through the body's section runs (field 17), which point at a section (type 10011). Fields 23, 24 and 25 of a section each name a set of headers and footers (type 10143). In a set, field 1 lists the header and field 2 the footer, each as three text records in the order left, centre, right (*confirmed* by writing text into them, [0327](../experiments/0327-writing-headers-and-footers.md); an empty one has no field 3). A plain document uses the set in field 25. When section field 19 is 1, left-hand pages use the set in field 24 instead, *confirmed* by writing it ([0016](../experiments/0016-header-and-footer.md), [0018](../experiments/0018-page-break-and-left-page.md), [0019](../experiments/0019-left-and-right-pages.md), [0386](../experiments/0386-writing-left-and-right-pages.md)). When section field 18 is 1, the section's first page uses the set in field 23, *confirmed* by writing ([0362](../experiments/0362-writing-first-page-headers.md)).

Other section fields hold switches from the Section tab of Pages' Document sidebar. *Likely* ([0017](../experiments/0017-section-switches.md))

| Section field | Switch | Values |
| --- | --- | --- |
| 17 | Same as previous section: when on, the section's pages use the previous section's headers and footers and its own sets are ignored | 1 on (default), 0 off; *confirmed* by writing ([0387](../experiments/0387-writing-same-as-previous-section.md)) |
| 18 | First page uses its own header-and-footer set (field 23) | 0 off (default), 1 on; *confirmed* by writing ([0362](../experiments/0362-writing-first-page-headers.md)) |
| 19 | Left and right pages are different: odd pages use the set in field 25 and even pages the set in field 24. Pages shows the switch only with facing pages on, but it applies with facing pages off too | 0 off (default), 1 on ([0019](../experiments/0019-left-and-right-pages.md)); *confirmed* by writing ([0386](../experiments/0386-writing-left-and-right-pages.md)) |
| 28 | Hide header and footer on the section's first page | 0 off (default), 1 on; *confirmed* by writing ([0362](../experiments/0362-writing-first-page-headers.md)) |
| 30 | The background of the section's pages, a fill like a shape's (a colour in field 1), drawn out to the page's edges ([0286](../experiments/0286-section-background.md); *confirmed* by writing it, [0328](../experiments/0328-writing-a-page-background.md)) | message |

The document-wide *Facing pages* setting is field 34 of the type-10012 record, which also holds the creation time and template name and is probably the document's settings. *Confirmed* by writing it ([0017](../experiments/0017-section-switches.md), [0300](../experiments/0300-writing-document-settings.md))

Other fields of the type-10012 document settings:

| Type-10012 field | Setting |
| --- | --- |
| 1 | Document body: 1 word processing (default), 0 page layout ([0240](../experiments/0240-no-document-body.md); *confirmed* by writing it both ways, [0419](../experiments/0419-writing-the-document-body-setting.md)). Pages empties the body when it turns this off. [release: 15.4 and 14.5 differ] Written 0 over a body that still holds text, the text is drawn by Pages 15.4 and 16.0 and not by 14.5 ([0419](../experiments/0419-writing-the-document-body-setting.md), [0463](../experiments/0463-drawing-15-4-documents-in-14-5.md), [0471](../experiments/0471-drawing-15-4-samples-in-16-0.md)). |
| 2 | Show headers, 1 on (default) ([0238](../experiments/0238-no-header.md)); writing 0 alone turns the sidebar's checkbox off but doesn't hide headers that have text: Pages hides headers by also replacing their texts with empty ones ([0327](../experiments/0327-writing-headers-and-footers.md)) |
| 3 | Show footers, 1 on (default) ([0239](../experiments/0239-no-footer.md)). Written alone, 0 doesn't hide a footer with text either; with fields 2 and 3 both 0, Pages draws no header or footer even when they hold text (*confirmed* by writing them, [0422](../experiments/0422-writing-header-and-footer-switches.md)) |
| 9 | Hyphenate the whole document, 1 on ([0236](../experiments/0236-hyphenation.md); *confirmed* by writing it, [0420](../experiments/0420-writing-hyphenation.md)) |
| 10 | Use ligatures, 1 on (default) ([0237](../experiments/0237-document-ligatures.md); *confirmed* by writing it, [0421](../experiments/0421-writing-document-ligatures.md)) |
