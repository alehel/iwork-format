# The iWork file formats

This site specifies the files that Apple's Pages, Keynote and Numbers save: `.pages`, `.key` and `.numbers`. Apple doesn't publish the formats. Everything here was found from the outside, by changing one thing in a document, saving it, and recording what changed in the file. No Apple code was read, disassembled or decompiled.

Each finding links to the experiments that support it and carries a confidence level:

| Level | Meaning |
| --- | --- |
| *Confirmed* | At least two experiments agree |
| *Likely* | One experiment supports it, and nothing contradicts it |
| *Unknown* | Seen in files, but its meaning isn't established yet |

The findings come from Pages, Keynote and Numbers 15.4 on macOS 26.5, checked against 14.5 and 16.0, which write the same format with the few differences listed in [releases.md](../../spec/releases.md).

## Where to start

- **[Reading a Pages document](anatomy.md)** takes one small file, a page with the word `hello`, from its ZIP listing down to the bytes that hold the word. Read it first: every other page assumes it.
- **[Reading a Numbers table](numbers-table.md)** follows a spreadsheet's root to its cells and decodes a row byte by byte.
- **[Writing a document](writing.md)** shows that the spec is complete enough to write files the apps accept.
- **[Sample files](samples.md)** lists the documents used on these pages, for download.

## The specification

Five chapters describe what the three apps share, and one chapter per app what is its own.

| Page | Covers |
| --- | --- |
| [1. Container](../../spec/container.md) | How a document is packaged: the ZIP, its parts, the chunk and record encoding, references between objects, password protection |
| [2. Text](../../spec/text.md) | Text storages: the text, paragraphs and breaks, positions, and the run tables that apply styles, links, fields and changes to it |
| [3. Styles](../../spec/styles.md) | Character, paragraph and list styles, their properties, and how they combine |
| [4. Tables](../../spec/tables.md) | Table models, tiles, cells, formats, formulas and merged cells |
| [5. Drawables, media and charts](../../spec/drawables.md) | Images, text boxes, shapes, groups, sounds, movies and charts, and where they are placed |
| [Pages](../../spec/pages.md) | Page setup, sections, headers and footers |
| [Keynote](../../spec/keynote.md) | Slides, layouts, builds, transitions and backgrounds |
| [Numbers](../../spec/numbers.md) | Sheets, the way to a table's cells, categories, pivot tables, filters, conditional highlighting and the calculation engine |
| [Record types](../../spec/types.html) | Every record type the spec names, and where it is described |
| [Experiments by topic](../../experiments/topics.html) | The experiments behind each section of the spec |
| [Search](../../search.html) | The spec, the guides, the record types and the experiments' conclusions, by word, type number or field path |
| [Layers and status](../../spec/README.md) | What each chapter covers so far, and the experiments behind it |

Where to start, after [1. Container](../../spec/container.md):

- **Pages**: [2. Text](../../spec/text.md), [3. Styles](../../spec/styles.md), then [Pages](../../spec/pages.md).
- **Keynote**: [Keynote](../../spec/keynote.md) for the way from the root to each slide, then [2. Text](../../spec/text.md) and [5. Drawables, media and charts](../../spec/drawables.md).
- **Numbers**: [Numbers](../../spec/numbers.md) for the way from the root to each table, then [4. Tables](../../spec/tables.md).

## In brief

A document is a ZIP file, stored without compression. Most of it is in `.iwa` parts under `Index/`. Each part is a series of chunks of [Snappy](https://github.com/google/snappy/blob/main/format_description.txt)-compressed data. Once decompressed, a part is a list of records: each is a [Protocol Buffers](https://protobuf.dev/programming-guides/encoding/) header, giving the object's ID, type and length, followed by the object itself as a Protocol Buffers message. Objects refer to each other by ID. Record headers list the references that lead down the tree, and in documents the apps save every object can be reached from the root objects through them ([container.md](../../spec/container.md#following-references)).

```
document.pages (ZIP)
├── Index/Document.iwa ──► chunks ──► Snappy ──► records ──► objects
├── Index/DocumentStylesheet.iwa
├── …
├── Metadata/Properties.plist
└── preview.jpg
```

There is no schema in the file. Field numbers, types and their meanings are what this specification provides.

## Tools

The repository holds `iwork-probe`, a command-line tool written from this specification, which lists parts, decodes chunks and records, prints messages and follows references. The excerpts on these pages are its output. A small Python writer, using only the standard library, writes documents back ([0287](../../experiments/0287-rewriting-a-document.md)).
