# Specification

The spec is written in layers, each built on the one before. A layer's file is added once its first experiment has run. Every finding links to the experiments that support it, and carries a confidence level (see [CONTRIBUTING.md](../CONTRIBUTING.md#confidence)).

| Layer | Covers | Status |
| --- | --- | --- |
| 1. Container | How a document is packaged: ZIP or folder, its parts, how they're encoded, how objects refer to each other | Not started |
| 2. Text | The document's text, paragraphs and breaks | Not started |
| 3. Styles | Paragraph and character styles, fonts, colours | Not started |
| 4. Objects | Lists, tables and inline images | Not started |
| 5. Page layout | Sections, headers, footers, page setup | Not started |

Keynote and Numbers layers can start once layer 1 is confirmed.

## Pages versions observed

| Pages | macOS | First experiment |
| --- | --- | --- |
| 15.4 | | [0001](../experiments/0001-empty-document.md) (planned) |
