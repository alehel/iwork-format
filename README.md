# iwork-format

An open description of the file format that Apple Pages writes. It's built from black-box experiments and written in our own words, so anyone can use it to read Pages documents.

Pages, Keynote and Numbers are trademarks of Apple Inc. This project isn't affiliated with or endorsed by Apple.

## Status

Just started. Nothing in [`spec/`](spec/) is confirmed yet. The first experiment, [0001: an empty document](experiments/0001-empty-document.md), is planned but hasn't been run.

## Why

Apple publishes no specification for the Pages format. Projects that want to open Pages documents have two options today: rely on material derived from Apple's binaries, or use importers whose licences don't suit them. This project builds a third option: a specification that anyone can check, because every statement in it links to an experiment that anyone with a Mac and Pages can rerun.

Keynote and Numbers documents appear to share a container with Pages. That's why the repository is named for iWork, not just Pages. Whether the container really is shared is something experiments will confirm.

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
| `list <file>` | Lists the parts of a document, whether it's a ZIP file or a folder package |
| `hex <file> <part> [--offset N] [--len N]` | Shows the bytes of one part in hexadecimal |
| `proto <file> <part> [--offset N] [--len N]` | Decodes bytes as a Protocol Buffers message and prints the fields as a tree |

The tool only uses public specifications: ZIP and the Protocol Buffers wire format. Commands that understand Pages' own structures (`dump` and `diff`) are added once experiments have established those structures.

## Licences

- **Specification and experiment write-ups** (`spec/`, `experiments/`, this README): [CC-BY-4.0](LICENSE-SPEC).
- **Tool and recipes** (`tool/`, `recipes/`): [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE), at your option.
