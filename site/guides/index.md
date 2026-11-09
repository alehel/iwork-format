# The iWork file formats

This site specifies the files that Apple's Pages, Keynote and Numbers save: `.pages`, `.key` and `.numbers`. Apple doesn't publish the formats. Everything here was found from the outside, by changing one thing in a document, saving it, and recording what changed in the file. No Apple code was read, disassembled or decompiled.

Each finding links to the experiments that support it and carries a confidence level:

| Level | Meaning |
| --- | --- |
| *Confirmed* | At least two experiments agree |
| *Likely* | One experiment supports it, and nothing contradicts it |
| *Unknown* | Seen in files, but its meaning isn't established yet |

The findings come from Pages, Keynote and Numbers 15.4 on macOS 26.5.

## Where to start

- **[Reading a Pages document](anatomy.md)** takes one small file, a page with the word `hello`, from its ZIP listing down to the bytes that hold the word. Read it first: every other page assumes it.
- **[Reading a Numbers table](numbers-table.md)** follows a spreadsheet's root to its cells and decodes a row byte by byte.
- **[Writing a document](writing.md)** shows that the spec is complete enough to write files the apps accept.
- **[Sample files](samples.md)** lists the documents used on these pages, for download.

## The specification

The specification is written in layers, each built on the one before.

| Page | Covers |
| --- | --- |
| [Container](../../spec/container.md) | How a document is packaged: the ZIP, its parts, the chunk and record encoding, references between objects, password protection |
| [Text](../../spec/text.md) | The text of Pages documents, and the styles, lists, tables, shapes, images and page layout shared with the other apps |
| [Keynote](../../spec/keynote.md) | Slides, layouts, builds, transitions, charts and media |
| [Numbers](../../spec/numbers.md) | Sheets, tables, categories, pivot tables, filters and conditional highlighting |
| [Layer overview](../../spec/README.md) | What each layer covers so far, and the experiments behind it |

## In brief

A document is a ZIP file, stored without compression. Most of it is in `.iwa` parts under `Index/`. Each part is a series of chunks of [Snappy](https://github.com/google/snappy/blob/main/format_description.txt)-compressed data. Once decompressed, a part is a list of records: each is a [Protocol Buffers](https://protobuf.dev/programming-guides/encoding/) header, giving the object's ID, type and length, followed by the object itself as a Protocol Buffers message. Objects refer to each other by ID, and every object can be reached from the root objects.

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
