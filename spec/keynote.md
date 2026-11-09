# Keynote

What is specific to Keynote documents. The container is the same as Pages' ([container.md](container.md)), and text is stored as in [text.md](text.md). Every finding links to the experiments that support it, with a confidence level as defined in [CONTRIBUTING.md](../CONTRIBUTING.md#confidence).

Observed with Keynote 15.4 on macOS 26.5.2.

## Parts

A new presentation has the seven `.iwa` parts that Pages documents have, without numbers in their names, plus one `Index/Slide-N.iwa` per slide and one `Index/TemplateSlide-N.iwa` per template slide of the theme. N is the ID of the slide record inside. The theme's images, including slide thumbnails, are stored under `Data/`. *Likely* ([0024](../experiments/0024-keynote-and-numbers.md), [0027](../experiments/0027-document-roots.md))

## From the root to a slide's text

| Type | Holds | Part |
| --- | --- | --- |
| 1 | The document root, with the shared document-properties block in field 3 (see [container.md](container.md#following-references)) | `Document.iwa` |
| 2 | The presentation: field 3.2 lists the slide nodes in show order, field 4 is the slide size in points (such as 1920 × 1080, *confirmed* by [0075](../experiments/0075-slide-size.md)), field 5 names the stylesheet ([0038](../experiments/0038-second-slide.md)) | `Document.iwa` |
| 4 | A slide node: field 2 names the slide; fields 10 (thumbnail size) and 16.1 (data ID of the thumbnail image) are optional; field 4 is 1 for a skipped slide ([0070](../experiments/0070-skipped-slide.md)) and field 18 is 1 when the slide's number is shown ([0074](../experiments/0074-slide-numbers.md)) | `Document.iwa` |
| 5 | A slide; field 17 names its layout, a template slide that is itself a type-5 slide named in its field 10 ([0046](../experiments/0046-slide-layout.md)); field 27 names its presenter notes (type 15) | `Slide-N.iwa`, `Slide.iwa`, or `TemplateSlide-N.iwa` for layouts |
| 15 | Presenter notes: field 1 names the notes text, a type-2001 record with field 1 = 4. Every slide has one, empty or not ([0039](../experiments/0039-presenter-notes.md)). | `Slide-N.iwa` |
| 7 | A shape on the slide, such as the title box; fields 2 and 4 name its text record | `Slide-N.iwa` |
| 2001 | The shape's text, as in [text.md](text.md) | `Slide-N.iwa` |

*Likely* ([0025](../experiments/0025-keynote-title.md), [0027](../experiments/0027-document-roots.md))

## Slide contents

Shapes added to a slide (text boxes) are type 2011, images type 3005 and tables types 6000 and 6001, as in Pages and Numbers. Each drawable's field 1.2 names the slide it is on. Placeholders from the layout, such as the title, are type 7. *Likely* ([0068](../experiments/0068-keynote-text-box.md), [0069](../experiments/0069-keynote-image.md), [0073](../experiments/0073-keynote-table.md))

A slide's transition is in its field 4.2.8: the effect's name in field 2 (such as `none` or `apple:dissolve`) and its duration in seconds in field 3. *Likely* ([0071](../experiments/0071-transition.md))

Bulleted body text uses the same text records and list styles as Pages; the theme's default body list style is a bullet (`•` in field 16). *Likely* ([0072](../experiments/0072-keynote-bullets.md))

## Charts

A chart is a drawable of type 5021 on the slide. Its field 10000.7 holds its data: row names in 7.1, column names in 7.2, and one 7.3 per row listing its values as doubles. *Likely* ([0067](../experiments/0067-chart.md))

Field 10000.1 is the chart type and 10000.5 the grouping into series (1 by row, 2 by column); the data grid in 10000.7 is the same whatever the type or grouping. *Likely* ([0079](../experiments/0079-pie-chart.md)–[0086](../experiments/0086-chart-grouped-by-column.md))

| 10000.1 | Type |
| --- | --- |
| 1 | Vertical bar |
| 2 | Horizontal bar |
| 3 | Line |
| 4 | Area |
| 5 | Pie |
| 6 | Stacked vertical bar |
| 9 | Scatter |
| 12 | 3D vertical bar |
