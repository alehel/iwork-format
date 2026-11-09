# Keynote

What is specific to Keynote documents. The container is the same as Pages' ([container.md](container.md)), and text is stored as in [text.md](text.md). Every finding links to the experiments that support it, with a confidence level as defined in [CONTRIBUTING.md](../CONTRIBUTING.md#confidence).

Observed with Keynote 15.4 on macOS 26.5.2.

## Parts

A new presentation has the seven `.iwa` parts that Pages documents have, without numbers in their names, plus one `Index/Slide-N.iwa` per slide and one `Index/TemplateSlide-N.iwa` per template slide of the theme. N is the ID of the slide record inside. The theme's images, including slide thumbnails, are stored under `Data/`. *Likely* ([0024](../experiments/0024-keynote-and-numbers.md), [0027](../experiments/0027-document-roots.md))

## From the root to a slide's text

| Type | Holds | Part |
| --- | --- | --- |
| 1 | The document root, with the shared document-properties block in field 3 (see [container.md](container.md#following-references)) | `Document.iwa` |
| 2 | Probably the presentation: refers to the slide nodes and the stylesheet | `Document.iwa` |
| 4 | A slide node: field 2 names the slide, field 10 a thumbnail size, field 16.1 the data ID of the thumbnail image | `Document.iwa` |
| 5 | A slide | `Slide-N.iwa` |
| 7 | A shape on the slide, such as the title box; fields 2 and 4 name its text record | `Slide-N.iwa` |
| 2001 | The shape's text, as in [text.md](text.md) | `Slide-N.iwa` |

*Likely* ([0025](../experiments/0025-keynote-title.md), [0027](../experiments/0027-document-roots.md))
