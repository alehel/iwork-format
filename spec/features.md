# Features and scope

This page says what full support for Pages, Numbers and Keynote documents means, which smaller profiles measure progress towards it, and which features exist. Each feature has one issue that owns its research. The coverage columns of the inventory are worked out from the experiments each feature cites, so they say what has been shown, not what an issue's closed state might suggest.

## Capabilities

An application can do six things with a feature. Each one is tested on its own, for each app.

| Capability | An application that has it can | Shown by |
| --- | --- | --- |
| Read | Find the feature in a document an app saved, and get its values and meaning | An experiment that changes the feature in the app and records where and how it is stored |
| Edit | Change the feature in a document an app saved, so that the app opens it and shows the change | An experiment that changes the stored values with the project's writer and checks the result in the app |
| Create | Write the feature into a document made without any document an app saved, so that the app opens it and shows the feature | An experiment that builds the document from nothing; none has yet ([#4](https://github.com/alehel/iwork-format/issues/4), [#27](https://github.com/alehel/iwork-format/issues/27), [#35](https://github.com/alehel/iwork-format/issues/35)) |
| Render | Draw the feature as the app draws it | A comparison of an independent drawing with the app's own; none has been made yet |
| Calculate | Work out the values the app works out: formula results, pivot summaries, highlighting and filter results | An experiment comparing computed values with the app's; for features whose Also column names it |
| Play | Run the feature in a presentation as Keynote does: builds, transitions, sound, movies and timing | An experiment comparing playback with Keynote's; for features whose Also column names it |

Saving is not a capability of a single feature: it is the container features below (package, chunks, references, data files, password protection), at the edit or create level, together with the rules for what must be kept or changed when saving ([#6](https://github.com/alehel/iwork-format/issues/6)).

## Profiles

A profile is a capability across every feature of one app. They measure progress; none of them is full support.

- **Read profile**: read for every feature the app has. A reader with it can get all of a document's content and settings, though not draw them.
- **Render profile** (and **calculate** for Numbers, **play** for Keynote): the read profile, plus render (and calculate or play) for every feature that has them.
- **Edit profile**: edit for every feature, and saving a changed document so that every part the application didn't change survives.
- **Create profile**: create for every feature, starting with the smallest document each app opens.
- **Full support** for an app is all of its profiles together, in every release in scope.

A feature counts towards a profile in an app only when its state for that capability is *shown*. *Shown* means at least one experiment shows the capability for some of the feature: it is the evidence a reader can start from, not a claim that the feature is complete. Its owning issue lists what is left.

## States

The inventory gives each capability of each feature one of four states for each app:

| State | Means |
| --- | --- |
| *Shown* | A cited experiment ran in that app and shows the capability for at least part of the feature. The release it ran with is listed with it |
| *Not tested* | The app has the feature, and nothing has shown the capability there yet |
| *Not checked* | The feature is listed for the app with a question mark: whether the app has it at all has not been checked in its interface yet |
| *Doesn't apply* | The app doesn't have the feature, as its interface shows; Numbers has no footnotes, for example |

A field seen in files whose meaning isn't known is not a state of the feature: the chapter that describes it marks it *unknown* (see [CONTRIBUTING.md](../CONTRIBUTING.md#confidence)), and the feature's owner keeps it open. The confidence levels in the chapters and the states here answer different questions: a chapter says how sure a statement is, the inventory says which apps and capabilities have any evidence at all.

## How the coverage is worked out

The site's builder reads the inventory below and, for each cited experiment, the app and release rows of its setup. An experiment counts for each app its setup names. It counts as *edit* evidence when it wrote the document with the project's writer (its setup has a Writer row, or its name begins with *writing*) and as *read* evidence otherwise. An evidence entry can name another capability before the number, such as `create 0480`, once an experiment shows one. An experiment run with the tool alone, such as a regression check, is linked but counts for no app.

The builder stops when a feature cites an experiment that ran in an app its Apps column leaves out, so the applicability and the evidence can't disagree. It also writes the inventory, with every state spelled out, to [features.json](features.json). Each feature there has these fields, which stay stable:

| Field | Holds |
| --- | --- |
| `id` | The feature's ID, `area.name`. An ID never changes or gets reused; a feature that is split keeps its ID for one part |
| `feature` | Its name |
| `owner`, `owner_url` | The number and address of the one issue that owns its research |
| `spec`, `page` | Where the specification describes it, and its row on this page |
| `formats` | For Pages, Numbers and Keynote: `applies` (`yes`, `unverified` or `no`), the `releases` its evidence ran with, and for each capability its `state` and `evidence` |
| `experiments` | Every experiment the feature cites |

## Releases and producers

The specification describes the format as the newest apps write it, Pages, Numbers and Keynote 16.0 for macOS. Most of the evidence comes from 15.4, which writes the same format; the [releases](releases.md) page says how 16.0, 14.5 and 13.1 were checked against it and what differs. The releases each feature's evidence ran with are shown with its states.

| Producer or release | Scope | Why |
| --- | --- | --- |
| Pages, Numbers and Keynote 16.0 for macOS | Current | The release the specification describes. It opens, draws and saves the 15.4 samples as 15.4 wrote them ([0470](../experiments/0470-opening-15-4-samples-in-16-0.md), [0471](../experiments/0471-drawing-15-4-samples-in-16-0.md), [0476](../experiments/0476-resaving-every-sample.md)), and makes new ones with the same structure ([0473](../experiments/0473-every-scripted-sample-in-16-0.md)) |
| The 15.4 apps for macOS | Evidence | The release most experiments ran with, from [0001](../experiments/0001-empty-document.md) to [0460](../experiments/0460-third-regression-check.md) |
| The 13.1 and 14.5 apps for macOS | Checked | Write the same format ([0461](../experiments/0461-new-documents-in-14-5.md), [0466](../experiments/0466-keynote-14-5.md)); every scripted sample was made again with them ([0475](../experiments/0475-every-scripted-sample-in-14-5.md), [0477](../experiments/0477-every-scripted-sample-in-13-1.md)) |
| Other releases of the macOS apps | Not tested | No copy has been run yet; [#23](https://github.com/alehel/iwork-format/issues/23) |
| The iPhone and iPad apps, and iWork for iCloud in a browser | Not tested | They save documents in the same packages, which no experiment has checked yet; [#23](https://github.com/alehel/iwork-format/issues/23) |
| Other applications that save iWork documents | Not tested | Their output may differ from the apps'; [#23](https://github.com/alehel/iwork-format/issues/23) |
| iWork '09 and earlier, which saved XML rather than records | Excluded for now | A different format from the one specified here; reading it would need its own specification. [#23](https://github.com/alehel/iwork-format/issues/23) owns the decision |

A statement that doesn't hold for every release checked carries a version note where it stands; the releases page gathers them.

## Closing a feature issue

An issue that owns features can close when, for each feature it owns and each app that has it:

1. Every capability the feature has is *shown* in the current release, or in 15.4, with experiments cited in the inventory, or the gap is moved to another open issue that the inventory then names as its owner.
2. Every *not checked* entry has been checked in the app's interface and changed to the app or removed.
3. The chapter describing the feature states its rules with a confidence level, and nothing it relies on is left *unknown* without an open issue to settle it.
4. Older releases are shown, or left to [#23](https://github.com/alehel/iwork-format/issues/23) explicitly.

Closing an issue finishes a piece of research; it doesn't mean the format is fully supported. Full support for an app is reached only when every feature in its column is *shown* for every capability it has, which the summary table shows directly. An audit that finds a gap links it to an open owner; it doesn't declare it out of scope.

## Keeping the inventory up to date

- A new experiment is added to the Evidence column of each feature it shows something about. The coverage follows by itself.
- A feature found in an app's interface gets a new row, with a new ID and one owner. When research splits a feature, its ID stays with one part and the other parts get new IDs.
- When an issue is split or its scope moves, the Owner column changes with it, and the roadmaps ([#24](https://github.com/alehel/iwork-format/issues/24) for Numbers, [#25](https://github.com/alehel/iwork-format/issues/25) for Keynote, [#26](https://github.com/alehel/iwork-format/issues/26) for Pages) list the same issues as owners. The owners here are where to look first.
- Applicability comes from what the apps' interfaces offer, never from the names of fields. An app listed with a question mark hasn't been checked yet.

## Inventory

The first table counts, for each app, the features it has (not counting those still to be checked) and those whose capability is *shown*. The second lists every feature.

<!-- feature-inventory -->

| ID | Feature | Apps | Also | Evidence | Owner | Spec |
| --- | --- | --- | --- | --- | --- | --- |
| `container.package` | Packages: ZIP and folder forms, their parts and file names | Pages, Numbers, Keynote | — | 0076, 0144, 0146, 0147, 0394, 0431, 0432, 0434, 0438 | [#3](https://github.com/alehel/iwork-format/issues/3) | [Container](container.md#the-package) |
| `container.chunks` | Chunks, records and their payloads | Pages, Numbers, Keynote | — | 0024, 0141, 0396, 0398, 0433 | [#3](https://github.com/alehel/iwork-format/issues/3) | [Container](container.md#chunks) |
| `container.references` | Object references and the roots of each kind of document | Pages, Numbers, Keynote | — | 0022, 0027, 0029, 0397 | [#3](https://github.com/alehel/iwork-format/issues/3) | [Container](container.md#following-references) |
| `container.data-files` | Data files for images, sounds and movies | Pages, Numbers, Keynote | — | 0142, 0143, 0145, 0148, 0395, 0435 | [#3](https://github.com/alehel/iwork-format/issues/3) | [Container](container.md#data-files) |
| `container.password` | Password protection | Pages, Numbers, Keynote | — | 0179, 0180, 0266 | [#20](https://github.com/alehel/iwork-format/issues/20) | [Container](container.md#password-protection) |
| `container.versions` | The saving release, payload versions and malformed input | Pages, Numbers, Keynote | — | 0461, 0466, 0469, 0481 | [#21](https://github.com/alehel/iwork-format/issues/21) | [Releases](releases.md#telling-which-release-saved-a-document) |
| `container.save-back` | What changes from save to save, and what an editor must keep | Pages, Numbers, Keynote | — | 0139, 0140, 0287 | [#6](https://github.com/alehel/iwork-format/issues/6) | [Container](container.md#ids-and-save-to-save-changes) |
| `container.view-state` | View state: zoom, page view and what was last selected | Pages, Numbers?, Keynote? | — | 0241, 0242 | [#47](https://github.com/alehel/iwork-format/issues/47) | [Container](container.md#view-state) |
| `container.metadata` | Document metadata and collaboration state | Pages, Numbers, Keynote | — | 0465 | [#47](https://github.com/alehel/iwork-format/issues/47) | [Releases](releases.md#telling-which-release-saved-a-document) |
| `container.templates` | Templates, themes and the resources they bring | Pages, Numbers, Keynote | — | 0090, 0155, 0156, 0157, 0158, 0198, 0291, 0294 | [#48](https://github.com/alehel/iwork-format/issues/48) | [Container](container.md#the-package) |
| `document.minimal` | The smallest document each app opens | Pages, Numbers, Keynote | — | 0001, 0024, 0025 | [#4](https://github.com/alehel/iwork-format/issues/4) | [Container](container.md#the-package) |
| `text.body` | Body text, its encoding and paragraphs | Pages, Numbers, Keynote | — | 0002, 0003, 0005, 0025, 0032, 0130, 0149, 0151, 0154, 0164, 0288, 0289, 0451 | [#7](https://github.com/alehel/iwork-format/issues/7) | [Text](text.md#the-body-text) |
| `text.breaks` | Tabs, non-breaking spaces, soft hyphens, and line, column and page breaks | Pages, Numbers?, Keynote | — | 0018, 0058, 0210, 0360, 0369, 0429, 0436 | [#7](https://github.com/alehel/iwork-format/issues/7) | [Text](text.md#the-body-text) |
| `text.character-properties` | Character properties: bold, italic, underline, strikethrough, font, size, colour, highlight, baseline, capitals, spacing and ligatures | Pages, Numbers, Keynote | — | 0007, 0012, 0013, 0053, 0096, 0152, 0200, 0203, 0204, 0205, 0206, 0207, 0208, 0209, 0310, 0322, 0351, 0428 | [#7](https://github.com/alehel/iwork-format/issues/7) | [Styles](styles.md#character-properties) |
| `text.paragraph-properties` | Paragraph properties: alignment, indents, spacing, line spacing, tab stops and borders | Pages, Numbers, Keynote | — | 0010, 0011, 0252, 0253, 0255, 0256, 0262, 0276, 0277, 0281, 0282, 0319, 0320, 0321, 0325, 0336 | [#7](https://github.com/alehel/iwork-format/issues/7) | [Styles](styles.md#paragraph-properties) |
| `text.styles` | Named and unnamed styles, and how they inherit | Pages, Numbers, Keynote | — | 0004, 0008, 0033, 0034, 0042, 0054, 0153, 0311, 0352, 0392, 0393, 0427 | [#7](https://github.com/alehel/iwork-format/issues/7) | [Styles](styles.md#named-and-unnamed-styles) |
| `text.drop-cap` | Drop caps | Pages, Numbers?, Keynote? | — | 0261, 0335 | [#7](https://github.com/alehel/iwork-format/issues/7) | [Text](text.md#runs) |
| `text.document-settings` | Hyphenation and ligatures for the whole document | Pages, Keynote? | — | 0236, 0237, 0420, 0421 | [#7](https://github.com/alehel/iwork-format/issues/7) | [Pages](pages.md#page-setup) |
| `text.lists` | Lists: bullets, numbering, levels and restarts | Pages, Numbers, Keynote | — | 0014, 0015, 0072, 0334, 0353, 0388, 0414 | [#9](https://github.com/alehel/iwork-format/issues/9) | [Styles](styles.md#list-styles) |
| `text.right-to-left` | Right-to-left paragraphs and international text | Pages, Numbers, Keynote | — | 0150, 0441 | [#15](https://github.com/alehel/iwork-format/issues/15) | [Text](text.md#positions-in-the-text) |
| `text.footnotes` | Footnotes and endnotes | Pages | — | 0041, 0356 | [#13](https://github.com/alehel/iwork-format/issues/13) | [Text](text.md#objects-in-the-text) |
| `text.fields` | Page number, page count and date fields | Pages, Keynote? | — | 0048, 0201, 0211, 0357, 0358, 0359 | [#13](https://github.com/alehel/iwork-format/issues/13) | [Text](text.md#objects-in-the-text) |
| `text.table-of-contents` | Tables of contents | Pages | — | 0202, 0407 | [#13](https://github.com/alehel/iwork-format/issues/13) | [Text](text.md#objects-in-the-text) |
| `text.merge-fields` | Merge fields | Pages | — | 0199, 0408 | [#13](https://github.com/alehel/iwork-format/issues/13) | [Text](text.md#objects-in-the-text) |
| `text.placeholders` | Placeholder text and media placeholders | Pages, Keynote? | — | 0212, 0244, 0406 | [#48](https://github.com/alehel/iwork-format/issues/48) | [Text](text.md#objects-in-the-text) |
| `text.links` | Links to web pages, email addresses and phone numbers | Pages, Numbers?, Keynote? | — | 0189, 0190, 0354, 0355 | [#45](https://github.com/alehel/iwork-format/issues/45) | [Text](text.md#runs) |
| `text.bookmarks` | Bookmarks and links to them | Pages | — | 0191, 0192, 0389 | [#45](https://github.com/alehel/iwork-format/issues/45) | [Text](text.md#runs) |
| `text.comments` | Comments and replies | Pages, Numbers?, Keynote? | — | 0249, 0375, 0376, 0443 | [#14](https://github.com/alehel/iwork-format/issues/14) | [Text](text.md#runs) |
| `text.tracked-changes` | Tracked changes: insertions, deletions, accepting, rejecting and pausing | Pages | — | 0193, 0194, 0268, 0269, 0270, 0377 | [#14](https://github.com/alehel/iwork-format/issues/14) | [Text](text.md#runs) |
| `text.equations` | Equations | Pages?, Numbers?, Keynote? | — | — | [#22](https://github.com/alehel/iwork-format/issues/22) | — |
| `text.citations` | Citations and bibliographies | Pages? | — | — | [#22](https://github.com/alehel/iwork-format/issues/22) | — |
| `pages.page-setup` | Paper size, orientation and margins | Pages | — | 0028, 0318, 0326, 0366, 0367 | [#8](https://github.com/alehel/iwork-format/issues/8) | [Pages](pages.md#page-setup) |
| `pages.sections` | Sections, their breaks and backgrounds | Pages | — | 0017, 0040, 0286, 0328, 0361, 0387 | [#8](https://github.com/alehel/iwork-format/issues/8) | [Pages](pages.md#page-setup) |
| `pages.headers-footers` | Headers and footers, first and facing pages | Pages | — | 0016, 0019, 0238, 0239, 0327, 0362, 0386, 0422 | [#8](https://github.com/alehel/iwork-format/issues/8) | [Pages](pages.md#headers-and-footers) |
| `pages.columns` | Text columns | Pages | — | 0254, 0324 | [#8](https://github.com/alehel/iwork-format/issues/8) | [Pages](pages.md#page-setup) |
| `pages.page-layout` | Page layout documents, without body text, and page templates | Pages | — | 0156, 0240, 0419 | [#16](https://github.com/alehel/iwork-format/issues/16) | [Pages](pages.md#page-setup) |
| `pages.floating-objects` | Objects on the page or in the text, text wrap and stacking order | Pages | — | 0052, 0423, 0424, 0425, 0482, 0483, 0484, 0485, 0486, 0487, 0488 | [#12](https://github.com/alehel/iwork-format/issues/12) | [Drawables](drawables.md#on-the-page-or-in-the-text) |
| `tables.cells` | Cell storage: tiles, rows and the kinds of value | Pages, Numbers, Keynote | — | 0020, 0021, 0026, 0030, 0031, 0063, 0113, 0114, 0115, 0116, 0117, 0118, 0131, 0134, 0138, 0174, 0176, 0290, 0306, 0337, 0437 | [#10](https://github.com/alehel/iwork-format/issues/10) | [Tables](tables.md#cells) |
| `tables.size` | Rows and columns: their number, sizes and identity | Pages, Numbers, Keynote | — | 0045, 0059, 0120, 0123, 0182, 0308, 0364, 0365 | [#10](https://github.com/alehel/iwork-format/issues/10) | [Tables](tables.md#the-table-models-storage) |
| `tables.merges` | Merged cells | Pages, Numbers, Keynote? | — | 0044, 0133, 0382, 0426 | [#10](https://github.com/alehel/iwork-format/issues/10) | [Tables](tables.md#merged-cells) |
| `tables.headers` | Header rows and columns, footer rows, freezing and repeating them | Pages, Numbers, Keynote | — | 0060, 0125, 0136, 0183, 0184, 0246, 0301, 0401, 0402 | [#10](https://github.com/alehel/iwork-format/issues/10) | [Tables](tables.md#cells) |
| `tables.formats` | Value formats: number, currency, percentage, date, duration, fraction and others | Pages, Numbers, Keynote | — | 0036, 0137, 0181, 0307, 0323, 0339, 0340, 0341, 0342, 0343 | [#18](https://github.com/alehel/iwork-format/issues/18) | [Tables](tables.md#formats) |
| `tables.formulas` | Formulas: references, operators and functions | Pages, Numbers, Keynote | calculate | 0035, 0064, 0065, 0066, 0078, 0103, 0104, 0105, 0106, 0107, 0108, 0109, 0110, 0111, 0112, 0121, 0132, 0135, 0175, 0223, 0248, 0265, 0315, 0316, 0370, 0371 | [#18](https://github.com/alehel/iwork-format/issues/18) | [Tables](tables.md#formulas) |
| `tables.cell-styles` | Cell fill, text style, alignment and wrap | Pages, Numbers, Keynote | — | 0043, 0061, 0062, 0309, 0313 | [#11](https://github.com/alehel/iwork-format/issues/11) | [Tables](tables.md#cells) |
| `tables.rich-text-cells` | Cells holding text with mixed formatting | Pages, Numbers, Keynote | — | — | [#11](https://github.com/alehel/iwork-format/issues/11) | [Tables](tables.md#cells) |
| `tables.table-styles` | Table names, titles and captions, alternating rows, gridlines and borders | Pages, Numbers, Keynote | — | 0122, 0230, 0231, 0232, 0233, 0234, 0235, 0273, 0274, 0344, 0345 | [#11](https://github.com/alehel/iwork-format/issues/11) | [Tables](tables.md#cells) |
| `tables.controls` | Checkboxes, star ratings, sliders, steppers and pop-up menus | Pages?, Numbers, Keynote? | — | 0169, 0170, 0171, 0172, 0173, 0338 | [#46](https://github.com/alehel/iwork-format/issues/46) | [Tables](tables.md#formats) |
| `tables.sorting-hidden` | Sorting, and hidden rows and columns | Pages?, Numbers, Keynote? | — | 0119 | [#46](https://github.com/alehel/iwork-format/issues/46) | [Tables](tables.md#rows-in-a-tile) |
| `tables.conditional-highlighting` | Conditional highlighting rules | Pages?, Numbers, Keynote? | calculate | 0259, 0267, 0280, 0453, 0454, 0455 | [#30](https://github.com/alehel/iwork-format/issues/30) | [Numbers](numbers.md#conditional-highlighting) |
| `numbers.sheets` | Sheets, the tables and objects on them, and their order | Numbers | — | 0037, 0047, 0124, 0126, 0416, 0417, 0418 | [#28](https://github.com/alehel/iwork-format/issues/28) | [Numbers](numbers.md#from-the-root-to-a-tables-cells) |
| `tables.calculation` | Calculation owners and recalculation | Pages, Numbers, Keynote | calculate | 0293, 0442 | [#29](https://github.com/alehel/iwork-format/issues/29) | [Numbers](numbers.md#the-calculation-engine) |
| `numbers.filters` | Filters | Numbers | calculate | 0258, 0383, 0391 | [#30](https://github.com/alehel/iwork-format/issues/30) | [Numbers](numbers.md#filters) |
| `numbers.categories` | Categories and their summaries | Numbers | calculate | 0226, 0411 | [#31](https://github.com/alehel/iwork-format/issues/31) | [Numbers](numbers.md#categories) |
| `numbers.pivot-tables` | Pivot tables | Numbers | calculate | 0227, 0279, 0410 | [#32](https://github.com/alehel/iwork-format/issues/32) | [Numbers](numbers.md#pivot-tables) |
| `numbers.print` | Print layout, pages and their headers and footers | Numbers | — | — | [#33](https://github.com/alehel/iwork-format/issues/33) | — |
| `keynote.slides` | Slides: their order, copies, skipping and deleting | Keynote | — | 0038, 0070, 0159, 0160, 0161, 0162, 0299, 0378 | [#36](https://github.com/alehel/iwork-format/issues/36) | [Keynote](keynote.md#slides) |
| `keynote.layouts` | Slide layouts, masters, themes and placeholders | Keynote | — | 0046, 0101, 0165, 0168, 0243, 0292, 0312, 0379, 0415, 0452 | [#37](https://github.com/alehel/iwork-format/issues/37) | [Keynote](keynote.md#slides) |
| `keynote.slide-settings` | Slide size, slide numbers and backgrounds | Keynote | — | 0074, 0075, 0314, 0346, 0381 | [#37](https://github.com/alehel/iwork-format/issues/37) | [Keynote](keynote.md#slides) |
| `keynote.notes` | Presenter notes | Keynote | — | 0039, 0163, 0305 | [#41](https://github.com/alehel/iwork-format/issues/41) | [Keynote](keynote.md#slides) |
| `keynote.transitions` | Transitions and Magic Move | Keynote | play | 0071, 0091, 0092, 0093, 0094, 0095, 0196, 0302, 0347 | [#39](https://github.com/alehel/iwork-format/issues/39) | [Keynote](keynote.md#slides) |
| `keynote.builds` | Builds: in, out and actions, their order and timing | Keynote | play | 0257, 0263, 0264, 0368, 0448, 0449, 0450 | [#38](https://github.com/alehel/iwork-format/issues/38) | [Keynote](keynote.md#slide-contents) |
| `keynote.playback` | Presentation playback: autoplay, looping, restarting when idle and self-playing | Keynote | play | 0087, 0088, 0089, 0197, 0272, 0380 | [#41](https://github.com/alehel/iwork-format/issues/41) | [Keynote](keynote.md#parts) |
| `keynote.dynamic-backgrounds` | Dynamic backgrounds | Keynote | play | 0271, 0440 | [#40](https://github.com/alehel/iwork-format/issues/40) | [Keynote](keynote.md#slides) |
| `keynote.print` | Printing, handouts and notes pages | Keynote | — | — | [#49](https://github.com/alehel/iwork-format/issues/49) | — |
| `drawables.geometry` | Position, size, rotation, flips and locking | Pages, Numbers, Keynote | — | 0055, 0056, 0097, 0100, 0213, 0214, 0303, 0373, 0405 | [#17](https://github.com/alehel/iwork-format/issues/17) | [Drawables](drawables.md#geometry) |
| `drawables.images` | Images, masks, adjustments and removed backgrounds | Pages, Numbers, Keynote | — | 0023, 0069, 0128, 0245, 0284, 0285, 0348, 0390, 0412, 0446, 0447 | [#17](https://github.com/alehel/iwork-format/issues/17) | [Drawables](drawables.md#images) |
| `drawables.text-boxes` | Text boxes | Pages, Numbers, Keynote | — | 0049, 0068, 0127, 0349 | [#12](https://github.com/alehel/iwork-format/issues/12) | [Drawables](drawables.md#text-boxes-and-shapes) |
| `drawables.shapes` | Shapes, their paths and the text in them | Pages, Numbers, Keynote | — | 0050, 0129, 0167, 0217, 0218, 0219, 0220, 0221, 0333 | [#17](https://github.com/alehel/iwork-format/issues/17) | [Drawables](drawables.md#text-boxes-and-shapes) |
| `drawables.lines` | Lines | Pages, Numbers?, Keynote | — | 0051, 0166, 0403, 0404, 0439 | [#17](https://github.com/alehel/iwork-format/issues/17) | [Drawables](drawables.md#text-boxes-and-shapes) |
| `drawables.fills-strokes` | Fills, gradients, borders, shadows, reflections, opacity and style presets | Pages, Numbers, Keynote | — | 0057, 0077, 0098, 0099, 0215, 0250, 0251, 0260, 0275, 0278, 0283, 0304, 0330, 0331, 0332, 0384, 0385, 0413, 0444, 0445 | [#17](https://github.com/alehel/iwork-format/issues/17) | [Drawables](drawables.md#text-boxes-and-shapes) |
| `drawables.groups` | Groups | Pages, Numbers?, Keynote? | — | 0216, 0372 | [#17](https://github.com/alehel/iwork-format/issues/17) | [Drawables](drawables.md#groups) |
| `drawables.captions` | Captions and titles of objects | Pages, Numbers, Keynote | — | 0228, 0229, 0374, 0430 | [#17](https://github.com/alehel/iwork-format/issues/17) | [Drawables](drawables.md#images) |
| `drawables.descriptions` | Descriptions of images for accessibility | Pages, Numbers?, Keynote | — | 0102, 0177 | [#45](https://github.com/alehel/iwork-format/issues/45) | [Drawables](drawables.md#images) |
| `drawables.media` | Sounds and movies, their volume and repetition | Pages, Numbers, Keynote | play | 0185, 0186, 0187, 0188, 0363 | [#44](https://github.com/alehel/iwork-format/issues/44) | [Drawables](drawables.md#sounds-and-movies) |
| `charts.types` | Chart types | Pages, Numbers, Keynote | — | 0067, 0079, 0080, 0081, 0082, 0083, 0084, 0085, 0195, 0222, 0224, 0225 | [#19](https://github.com/alehel/iwork-format/issues/19) | [Drawables](drawables.md#charts) |
| `charts.data` | Chart data, its grouping and links to tables | Pages, Numbers, Keynote | — | 0086, 0317, 0350, 0409 | [#19](https://github.com/alehel/iwork-format/issues/19) | [Drawables](drawables.md#charts) |
| `charts.styles` | Chart options, axes and series styles | Pages, Numbers, Keynote | — | 0295, 0296, 0297, 0298, 0399, 0400, 0456, 0457, 0458, 0459 | [#19](https://github.com/alehel/iwork-format/issues/19) | [Drawables](drawables.md#charts) |
