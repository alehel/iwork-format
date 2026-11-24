# Specification

Five chapters describe what Pages, Keynote and Numbers documents share, each built on the one before, and one chapter per app describes what is its own. Every finding links to the experiments that support it, and carries a confidence level (see [CONTRIBUTING.md](../CONTRIBUTING.md#confidence)). The [experiments by topic](../experiments/topics.html) list the evidence behind each section.

| Chapter | Covers | What is known so far |
| --- | --- | --- |
| [1. Container](container.md) | How a document is packaged: ZIP or folder, its parts, how they're encoded, how objects refer to each other | Chunks, records, references, part and data file lists and password protection are *confirmed*, and so is writing documents back. What the view state holds is mostly open |
| [2. Text](text.md) | The document's text, paragraphs and breaks, and the runs that apply styles, links, fields and changes | Text, positions, breaks, run tables, links, comments, fields and tracked changes are *confirmed*. Right-to-left paragraphs set in the app are *unknown* |
| [3. Styles](styles.md) | Paragraph, character and list styles, fonts, colours | Most properties and how styles inherit are *confirmed* by writing them; underline, strikethrough and some line spacing are *likely* |
| [4. Tables](tables.md) | Table models, tiles, cells, formats, formulas, merged cells | Cells, formats, formulas and every function number, merges, sizes and headers are *confirmed*; control settings and parts of formulas are *likely* |
| [5. Drawables, media and charts](drawables.md) | Images, text boxes, shapes, groups, sounds, movies, charts | Geometry, borders, fills, groups, masks, captions, media and chart data and options are *confirmed*; some outline forms and gradients are open |
| [Pages](pages.md) | Page setup, sections, headers and footers | Paper, margins, sections, headers and footers are *confirmed*; page-layout documents are *likely* |
| [Keynote](keynote.md) | Slides, layouts, notes, builds, transitions, backgrounds | Slides and their order, layouts, notes, transitions, builds and presentation settings are mapped, many *confirmed* by writing them |
| [Numbers](numbers.md) | Sheets, the way to a table's cells, categories, pivot tables, filters, highlighting, the calculation engine | Sheets and tables are *confirmed*; categories, pivot tables, filters and highlighting in part; what the engine's owners are for is *likely* |

Every write so far changes a document the apps saved; making one from nothing is not yet shown.

## App releases

The spec describes the format as the newest apps write it, Pages, Numbers and Keynote 16.0. A version note stands where something doesn't hold for every release checked; [releases.md](releases.md) lists the releases, how to tell which one saved a document, and everything each one changed.

## Features and scope

[features.md](features.md) defines what full support for each app means: the read, edit, create, render, calculate and play capabilities, the profiles built from them, and the releases and producers in scope. It lists every feature with one owning issue, and shows for each app which capabilities its experiments have shown, worked out from the experiments themselves. Its coverage is also published as [features.json](features.json).

## Corrected claims and where they hold

Some earlier statements in the spec and guides said more than their experiments showed, or contradicted each other. Each was corrected in place. This table records what each correction rests on in each app, in 15.4 unless a release is named. *Shown* means an experiment in that app supports the corrected statement; *not tested* means nothing has checked it there yet, so the statement is not claimed for that app, even where the type numbers match.

| Corrected claim | Pages | Numbers | Keynote |
| --- | --- | --- | --- |
| Text run table 28 holds drop caps; a body without one has a single entry with no style, not an unknown entry of zeros ([text.md](text.md#runs)) | Shown ([0261](../experiments/0261-drop-cap.md), [0335](../experiments/0335-writing-a-drop-cap.md)) | Not tested | Not tested |
| 65,536 decoded bytes is the chunk size the apps write, not a limit a reader can assume ([container.md](container.md#chunks)) | Shown: written at 65,536 ([0141](../experiments/0141-large-text.md)), read at 1,000 and 338,982 ([0433](../experiments/0433-writing-chunk-sizes.md)) | Chunk layout shown ([0024](../experiments/0024-keynote-and-numbers.md)); larger chunks not tested | Chunk layout shown ([0024](../experiments/0024-keynote-and-numbers.md)); larger chunks not tested |
| Header references list only downward references, and an accepted document can lack them; reaching every object from the roots is a property of the apps' output ([container.md](container.md#following-references)) | Shown ([0022](../experiments/0022-header-references.md), [0396](../experiments/0396-writing-record-headers.md), [0460](../experiments/0460-third-regression-check.md)) | Reachability shown ([0024](../experiments/0024-keynote-and-numbers.md), [0460](../experiments/0460-third-regression-check.md)); opening without header lists not tested | Reachability shown ([0024](../experiments/0024-keynote-and-numbers.md), [0460](../experiments/0460-third-regression-check.md)); opening without header lists not tested |
| A table's size is the count of row and column UUIDs in its type-6267 record; model fields 6 and 7 are copies ([tables.md](tables.md), [numbers.md](numbers.md)) | Has type-6267 records; which one sets the size not tested | Shown ([0364](../experiments/0364-writing-names-and-table-size.md), [0365](../experiments/0365-growing-a-table.md)) | Not tested |
| A paragraph's base direction doesn't come from its text; left-to-right shown for one style only, and how an app-set right-to-left paragraph is stored is unknown ([text.md](text.md#positions-in-the-text)) | Shown for the left-aligned Body style ([0441](../experiments/0441-writing-right-to-left-text.md)) | Not tested | Not tested |
| Every write so far changes a document an app saved; making one without a saved document to start from is not yet shown ([writing guide](../site/guides/writing.md)) | Not shown | Not shown | Not shown |
| Cells and formulas are stored the same way in all three apps; merges and header counts only shown for Pages and Numbers ([tables.md](tables.md)) | Shown ([0131](../experiments/0131-pages-table-cells.md), [0133](../experiments/0133-pages-merge.md), [0136](../experiments/0136-pages-header-rows.md)) | Shown ([0021](../experiments/0021-table-cells.md), [0026](../experiments/0026-numbers-cells.md)) | Cells and formulas shown ([0134](../experiments/0134-keynote-table-cells.md), [0135](../experiments/0135-keynote-table-formula.md)); merges and header counts not tested |
| Slide nodes get field 20 on some presentations when saved again, not on all ([keynote.md](keynote.md)) | Doesn't apply | Doesn't apply | Shown in 13.1 and 16.0 ([0476](../experiments/0476-resaving-every-sample.md), [0480](../experiments/0480-resaving-every-sample-in-13-1.md)) |
