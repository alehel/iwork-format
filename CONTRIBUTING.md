# Contributing

This project only works if every statement in the spec can be traced to an experiment, and nothing in it is derived from Apple's code. Please read the rules below before your first pull request.

## Clean-room rules

| Allowed | Not allowed |
| --- | --- |
| Running Pages and saving documents you made yourself | Disassembling, decompiling or reading inside the Pages app bundle (file names and listings only) |
| Scripting Pages through its public AppleScript dictionary | Consulting `.proto` schemas or other material extracted from Apple's binaries |
| Reading public specifications: ZIP, Snappy, Protocol Buffers | Reading or copying the code of other iWork importers, whatever their licence |
| Inspecting the bytes of files you made, on your own machine | Committing files Pages wrote, including thumbnails and previews |
| Writing up findings in your own words | Studying other people's documents, or copying Apple's wording beyond feature names |

If you have already seen extracted schemas or another importer's code, say so in your first pull request. You can still contribute: someone else confirms or redoes your findings independently before they're marked *confirmed*.

In your first pull request, add this line to its description:

> I have followed the clean-room rules in CONTRIBUTING.md for everything in this pull request.

## Adding an experiment

1. Copy [`experiments/TEMPLATE.md`](experiments/TEMPLATE.md) to `experiments/NNNN-short-title.md`, using the next free number.
2. Where you can, write the steps as an AppleScript in `recipes/NNNN-short-title.applescript`, so anyone can rerun them.
3. Save the documents under `samples/NNNN/`. That folder is gitignored: never commit them.
4. Compare the documents with `iwork-probe`, and paste only the part of the output that changed.
5. Record the Pages and macOS versions. The format can change between releases.

## Confidence

Every finding in the spec has one of three levels:

| Level | Means |
| --- | --- |
| *Confirmed* | At least two experiments agree, for example the same field changing again when a different word is made bold |
| *Likely* | One experiment supports it, and nothing contradicts it |
| *Unknown* | Seen in files, but its meaning isn't established yet |

The spec links each finding to the experiments that support it.

## The tool

`iwork-probe` treats every input file as hostile. It must never panic: use checked arithmetic, `get()` instead of indexing, and cap sizes and nesting. Before a pull request, run:

```bash
cargo fmt --all --check && cargo clippy --all-targets -- -D warnings && cargo test
```
