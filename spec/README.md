# Specification

The spec is written in layers, each built on the one before. A layer's file is added once its first experiment has run. Every finding links to the experiments that support it, and carries a confidence level (see [CONTRIBUTING.md](../CONTRIBUTING.md#confidence)).

| Layer | Covers | Status |
| --- | --- | --- |
| 1. Container | How a document is packaged: ZIP or folder, its parts, how they're encoded, how objects refer to each other | [Started](container.md): chunks, records and header references confirmed |
| 2. Text | The document's text, paragraphs and breaks | [Started](text.md): the text, its encoding, paragraphs and run tables confirmed; applies to Keynote text too ([0025](../experiments/0025-keynote-title.md)); checked against every sample ([0032](../experiments/0032-reading-all-text.md)) |
| 3. Styles | Paragraph and character styles, fonts, colours | First findings in [text.md](text.md#styles), from experiments 0004, 0007, 0008, 0010–0013, 0033 and 0034, which test how styles combine |
| 4. Objects | Lists, tables and inline images | Lists started in [text.md](text.md#styles), from [0014](../experiments/0014-lists.md) and [0015](../experiments/0015-list-levels.md); tables started in [text.md](text.md#objects-in-the-text), from [0020](../experiments/0020-a-table.md), [0021](../experiments/0021-table-cells.md) [0026](../experiments/0026-numbers-cells.md), [0029](../experiments/0029-numbers-root-to-table.md) to [0031](../experiments/0031-cell-kinds.md) [0035](../experiments/0035-formula-references.md) and [0036](../experiments/0036-more-cell-formats.md); images started in [text.md](text.md#objects-in-the-text) and [container.md](container.md#data-files), from [0023](../experiments/0023-an-image.md) |
| 5. Page layout | Sections, headers, footers, page setup | First findings in [text.md](text.md#headers-and-footers), from [0016](../experiments/0016-header-and-footer.md) to [0019](../experiments/0019-left-and-right-pages.md) and [0040](../experiments/0040-section-break.md); page setup in [text.md](text.md#page-setup), from [0027](../experiments/0027-document-roots.md) and [0028](../experiments/0028-margins.md) |

Layer 1 is confirmed for Keynote and Numbers 15.4 too ([0024](../experiments/0024-keynote-and-numbers.md)), so their own layers can start. Started: [keynote.md](keynote.md) (slides and notes from [0038](../experiments/0038-second-slide.md) and [0039](../experiments/0039-presenter-notes.md)), [numbers.md](numbers.md) (sheets from [0037](../experiments/0037-second-sheet.md)).

## Pages versions observed

| Pages | macOS | First experiment |
| --- | --- | --- |
| 15.4 | 26.5.2 | [0001](../experiments/0001-empty-document.md) |
