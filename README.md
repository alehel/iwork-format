# iwork-format

An open description of the file format that Apple Pages writes. It's built from black-box experiments and written in our own words, so anyone can use it to read Pages documents.

Pages, Keynote and Numbers are trademarks of Apple Inc. This project isn't affiliated with or endorsed by Apple.

## Status

Early. Two hundred and twenty-seven [experiments](experiments/) have been run, all with the 15.4 apps on macOS 26.5.2. Each layer's status is in [`spec/README.md`](spec/README.md). In short:

- **Container** ([`spec/container.md`](spec/container.md)): how the parts are compressed and split into records is *confirmed*, and so is the fact that record headers list references. So is the fact that every object can be reached from three roots through those references (four when a chart adds `ObjectContainer.iwa`), checked against all 203 sample documents, and the folder form of a document, with its parts inside `Index.zip`, in all three apps. How a password-protected document is encrypted is *confirmed* for all three apps. How data files are named, shared and dropped, and that part names can change between saves, are *likely*.
- **Text** ([`spec/text.md`](spec/text.md)): where the body text lives, its encoding (UTF-8, with positions in UTF-16 units), paragraph breaks, and the run tables that attach styles to ranges are *confirmed*. So are the language and autocorrection runs that typing adds. Line, page and section breaks, footnotes, page number fields and template fields (placeholder text, dates and the author's name) are *likely*.
- **Styles**: character and paragraph styles are partly mapped. Bold, italic, size, font, colour, underline, strikethrough and alignment are *likely*. So is how character and paragraph styles and their parents combine, tested against Pages' own reading of each word.
- **Lists and page layout**: list styles, list levels, where header and footer text is stored, and some section and document switches are *likely*.
- **Tables**: how number and text cells are stored is *confirmed*, and Numbers stores them identically. How a table is anchored in the text, and where its size and name are, is *likely*. How dates, currency, percentages, checkboxes, ratings, sliders, steppers and formulas are stored, and how cells point at their formats, is *likely*. So are how formulas refer to cells and ranges, how a cell's text style and background are attached, where merged cells are recorded, and where row heights and column widths are kept.
- **Images and shapes**: how an image file is stored and found, and an image's position, size, rotation and opacity, are *likely*; its description is *confirmed*. So are text boxes, shapes and lines, which share one type, and the difference between objects in the text and objects on the page.
- **Keynote and Numbers**: their documents use the same container as Pages, *confirmed* for the package, chunks, records and header references. Keynote stores slide text, shapes, images and tables the same way as Pages. Its slides, their order, layouts, notes, transitions and chart data are mapped in [`spec/keynote.md`](spec/keynote.md). Numbers' sheets and tables, from its root to a table's cells, are in [`spec/numbers.md`](spec/numbers.md). Both are *likely*.
- **Page setup**: Pages' paper size, orientation, margins, header and footer distances, the template a document came from, and what marks a page-layout document are *likely*.

## Why

Apple publishes no specification for the Pages format. Projects that want to open Pages documents have two options today: rely on material derived from Apple's binaries, or use importers whose licences don't suit them. This project builds a third option: a specification that anyone can check, because every statement in it links to an experiment that anyone with a Mac and Pages can rerun.

Keynote and Numbers documents share a container with Pages, as [experiment 0024](experiments/0024-keynote-and-numbers.md) confirmed. That's why the repository is named for iWork, not just Pages.

## How it's made

Every finding comes from comparing files that Pages writes for documents we make ourselves, one change at a time:

1. Start from a baseline document saved in Pages.
2. Make one change: type a word, make it bold, add a table row.
3. Save it as a new file.
4. Decode both files with [`iwork-probe`](tool/) and compare them.
5. Record what changed, what we conclude, and how sure we are, in [`experiments/`](experiments/).
6. Fold confirmed findings into [`spec/`](spec/), then pick the next change.

The clean-room rules are in [CONTRIBUTING.md](CONTRIBUTING.md). Every contributor has to follow them.

## Layout

| Path | Holds |
| --- | --- |
| [`spec/`](spec/) | The specification, one file per layer |
| [`experiments/`](experiments/) | One file per experiment, numbered |
| [`recipes/`](recipes/) | AppleScript that reproduces each experiment's documents |
| [`tool/`](tool/) | `iwork-probe`, the Rust tool for inspecting files |
| `samples/` | Gitignored. Files Pages wrote, kept on your own machine only |

## Using iwork-probe

```bash
cargo run --release -- list path/to/document.pages
```

| Command | What it does |
| --- | --- |
| `list <file>` | Lists the parts of a document, whether it's a ZIP file or a folder package, including the parts inside a package's `Index.zip` |
| `hex <file> <part> [--offset N] [--len N]` | Shows the bytes of one part in hexadecimal |
| `proto <file> <part> [--offset N] [--len N]` | Decodes bytes as a Protocol Buffers message and prints the fields as a tree |
| `chunks <file> <part>` | Lists the Snappy-compressed chunks of an `.iwa` part |
| `records <file> <part>` | Splits an `.iwa` part's decoded bytes into records and lists each payload's offset, length, ID, type and version |
| `refs <file> <part>` | Lists the object IDs each record's header says it refers to |
| `text <file>` | Prints the text of every text record (type 2001) in a document, in any of the three apps |

Add `--decoded` to `hex` or `proto` to read an `.iwa` part's decoded bytes. The offsets `records` prints are offsets into those bytes, so `proto <file> <part> --decoded --offset <payload> --len <len>` shows one payload.

The decoders only use public specifications: ZIP, Snappy and the Protocol Buffers wire format. What the tool knows about Pages' own structures comes from experiments: `chunks` and `records` follow the layout [experiment 0001](experiments/0001-empty-document.md) found. Commands that need more than that, such as `dump` and `diff`, are added once experiments have established those structures.

## Licences

- **Specification and experiment write-ups** (`spec/`, `experiments/`, this README): [CC-BY-4.0](LICENSE-SPEC).
- **Tool and recipes** (`tool/`, `recipes/`): [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE), at your option.
