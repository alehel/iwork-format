# Keynote

What is specific to Keynote documents. The container is the same as Pages' ([container.md](container.md)), and text is stored as in [text.md](text.md). Every finding links to the experiments that support it, with a confidence level as defined in [CONTRIBUTING.md](../CONTRIBUTING.md#confidence).

Observed with Keynote 15.4 on macOS 26.5.2.

## Parts

A new presentation has the seven `.iwa` parts that Pages documents have, without numbers in their names, plus one `Index/Slide-N.iwa` per slide and one `Index/TemplateSlide-N.iwa` per template slide of the theme. N is the ID of the slide record inside. The theme's images, including slide thumbnails, are stored under `Data/`. *Likely* ([0024](../experiments/0024-keynote-and-numbers.md), [0027](../experiments/0027-document-roots.md))

## From the root to a slide's text

| Type | Holds | Part |
| --- | --- | --- |
| 1 | The document root, with the shared document-properties block in field 3 (see [container.md](container.md#following-references)) | `Document.iwa` |
| 2 | The presentation: field 3.2 lists the slide nodes in show order, field 4 is the slide size in points (such as 1920 × 1080), field 5 names the stylesheet ([0038](../experiments/0038-second-slide.md)) | `Document.iwa` |
| 4 | A slide node: field 2 names the slide; fields 10 (thumbnail size) and 16.1 (data ID of the thumbnail image) are optional | `Document.iwa` |
| 5 | A slide; field 17 names its layout, a template slide that is itself a type-5 slide named in its field 10 ([0046](../experiments/0046-slide-layout.md)); field 27 names its presenter notes (type 15) | `Slide-N.iwa`, `Slide.iwa`, or `TemplateSlide-N.iwa` for layouts |
| 15 | Presenter notes: field 1 names the notes text, a type-2001 record with field 1 = 4. Every slide has one, empty or not ([0039](../experiments/0039-presenter-notes.md)). | `Slide-N.iwa` |
| 7 | A shape on the slide, such as the title box; fields 2 and 4 name its text record | `Slide-N.iwa` |
| 2001 | The shape's text, as in [text.md](text.md) | `Slide-N.iwa` |

*Likely* ([0025](../experiments/0025-keynote-title.md), [0027](../experiments/0027-document-roots.md))

## Charts

A chart is a drawable of type 5021 on the slide. Its field 10000.7 holds its data: row names in 7.1, column names in 7.2, and one 7.3 per row listing its values as doubles. *Likely* ([0067](../experiments/0067-chart.md))
