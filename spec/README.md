# Specification

The spec is written in layers, each built on the one before. A layer's file is added once its first experiment has run. Every finding links to the experiments that support it, and carries a confidence level (see [CONTRIBUTING.md](../CONTRIBUTING.md#confidence)).

| Layer | Covers | Status |
| --- | --- | --- |
| 1. Container | How a document is packaged: ZIP or folder, its parts, how they're encoded, how objects refer to each other | [Started](container.md): chunks, records and header references confirmed |
| 2. Text | The document's text, paragraphs and breaks | [Started](text.md): the text, its encoding, paragraphs and run tables confirmed; footnotes and page number fields from [0041](../experiments/0041-footnote.md) and [0048](../experiments/0048-page-number.md); applies to Keynote text too ([0025](../experiments/0025-keynote-title.md)); checked against every sample ([0032](../experiments/0032-reading-all-text.md)) |
| 3. Styles | Paragraph and character styles, fonts, colours | First findings in [text.md](text.md#styles), from experiments 0004, 0007, 0008, 0010–0013, 0033, 0034 and 0042, which test how styles combine |
| 4. Objects | Lists, tables and inline images | Lists started in [text.md](text.md#styles), from [0014](../experiments/0014-lists.md) and [0015](../experiments/0015-list-levels.md); tables started in [text.md](text.md#objects-in-the-text), from [0020](../experiments/0020-a-table.md), [0021](../experiments/0021-table-cells.md) [0026](../experiments/0026-numbers-cells.md), [0029](../experiments/0029-numbers-root-to-table.md) to [0031](../experiments/0031-cell-kinds.md) [0035](../experiments/0035-formula-references.md), [0036](../experiments/0036-more-cell-formats.md), [0043](../experiments/0043-cell-styles.md) to [0045](../experiments/0045-row-and-column-sizes.md); text boxes, shapes and lines from [0049](../experiments/0049-text-box.md) to [0051](../experiments/0051-line.md); images started in [text.md](text.md#objects-in-the-text) and [container.md](container.md#data-files), from [0023](../experiments/0023-an-image.md) |
| 5. Page layout | Sections, headers, footers, page setup | First findings in [text.md](text.md#headers-and-footers), from [0016](../experiments/0016-header-and-footer.md) to [0019](../experiments/0019-left-and-right-pages.md) and [0040](../experiments/0040-section-break.md); page setup in [text.md](text.md#page-setup), from [0027](../experiments/0027-document-roots.md) and [0028](../experiments/0028-margins.md) |

Layer 1 is confirmed for Keynote and Numbers 15.4 too ([0024](../experiments/0024-keynote-and-numbers.md)), so their own layers can start. Started: [keynote.md](keynote.md) (slides, notes and layouts from [0038](../experiments/0038-second-slide.md), [0039](../experiments/0039-presenter-notes.md) and [0046](../experiments/0046-slide-layout.md)), [numbers.md](numbers.md) (sheets and tables from [0037](../experiments/0037-second-sheet.md) and [0047](../experiments/0047-second-table.md)).

## Pages versions observed

| Pages | macOS | First experiment |
| --- | --- | --- |
| 15.4 | 26.5.2 | [0001](../experiments/0001-empty-document.md) |
