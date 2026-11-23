# 0460: Third regression check

**Status:** run

[0178](0178-regression-check.md) and [0247](0247-second-regression-check.md) checked every sample against three rules: that each `.iwa` part frames into chunks and records, that every object can be reached from the roots through the IDs in record headers, and that every text record can be read. Since then the samples have grown by the writing experiments, many of them deliberately unusual. This experiment runs the three checks again over all of them, with the tool as it stands, and runs the tool's own checks.

## Setup

| | |
| --- | --- |
| Tool | `iwork-probe` at this commit, built with Rust 1.99 (`cargo build --release`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-23 |
| Input | Every `.pages`, `.key` and `.numbers` in `samples/`, including `samples/theme/`: 1,272 documents from experiments 0001 to 0459 |
| Script | The new [`recipes/0460-regression-check.py`](../recipes/0460-regression-check.py), which runs `iwork-probe list`, `records` and `text` on each document and follows header references with the writer of [0287](0287-rewriting-a-document.md) |

## Recipe

```bash
cargo fmt --all --check && cargo clippy --all-targets -- -D warnings && cargo test
cargo build --release
python3 -I recipes/0460-regression-check.py samples/ target/release/iwork-probe
```

Reachability starts at objects 1, 2 and 71, and 61 where a document has it, and follows header fields 2.5 and 2.4.4 ([container.md](../spec/container.md#following-references)). It covers ZIP documents and leaves out the folder packages and the password-protected documents, which 0076 and 0266 checked; the framing and text checks cover every document.

## Observation

`cargo fmt`, `clippy` and the 39 tests all pass.

| Check | Documents | Failures |
| --- | --- | --- |
| Framing, every `.iwa` part | 1,272 | 0 |
| Text | 1,272 | 0 |
| Reachability | 1,260, with 875,522 objects | 1 |

The one failure is `0396/text-refs-none.pages`, whose body text record had its header field 2.5 removed on purpose ([0396](0396-writing-record-headers.md)): 25 of its 571 objects, the header and footer texts and what they refer to, can't be reached without those references. Pages opened that document normally.

The checked documents include the deliberately unusual ones: parts under other names (0394), changed header types and versions (0396), chunks of 1,000 and 338,982 decoded bytes (0433), Deflate-compressed entries (0432), a name with the UTF-8 flag cleared (0431) and missing package files (0434).

## Conclusion

The tool still frames and reads every sample, including every file the writing experiments produced, and the rule that headers lead to every object holds for all 1,259 documents Pages or Keynote or Numbers wrote or opened unchanged. The only exception is a file written without the references, which shows that a tool that walks the object tree by headers depends on writers keeping them, even though Pages doesn't.

## Confidence

*Confirmed*: framing, text and reachability across all 1,272 samples, apart from the one file written without its references.
