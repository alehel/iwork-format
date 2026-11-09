# Specification

The spec is written in layers, each built on the one before. A layer's file is added once its first experiment has run. Every finding links to the experiments that support it, and carries a confidence level (see [CONTRIBUTING.md](../CONTRIBUTING.md#confidence)).

| Layer | Covers | Status |
| --- | --- | --- |
| 1. Container | How a document is packaged: ZIP or folder, its parts, how they're encoded, how objects refer to each other | [Started](container.md): chunks and records confirmed |
| 2. Text | The document's text, paragraphs and breaks | [Started](text.md): the text, its encoding, paragraphs and run tables confirmed |
| 3. Styles | Paragraph and character styles, fonts, colours | First findings in [text.md](text.md#styles), from experiments 0004, 0007, 0008 and 0010–0013 |
| 4. Objects | Lists, tables and inline images | Lists started in [text.md](text.md#styles), from [0014](../experiments/0014-lists.md) and [0015](../experiments/0015-list-levels.md); tables and images not started |
| 5. Page layout | Sections, headers, footers, page setup | First findings in [text.md](text.md#headers-and-footers), from [0016](../experiments/0016-header-and-footer.md) to [0018](../experiments/0018-page-break-and-left-page.md) |

Keynote and Numbers layers can start once layer 1 is confirmed.

## Pages versions observed

| Pages | macOS | First experiment |
| --- | --- | --- |
| 15.4 | 26.5.2 | [0001](../experiments/0001-empty-document.md) |
