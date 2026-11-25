# 0141: A large body text

**Status:** run

[0001](0001-empty-document.md) found a record crossing chunk boundaries in the stylesheet. This experiment writes a body text large enough to need several chunks in `Document.iwa`.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Baseline | Experiment [0002](0002-one-word.md) |

## Recipe

```bash
mkdir -p samples/0141
osascript recipes/0139-pages-container.applescript bigtext "$PWD/samples/0141/big.pages"
```

The recipe sets the body text to 30000 paragraphs, `line 1` to `line 30000`.

## Observation

`Document.iwa` has 8 chunks: seven of 65,536 decoded bytes and a last of 52,618. The body's text record (1732539) has a 497,224-byte payload, which starts at decoded offset 11,892 and crosses all seven boundaries between the eight chunks (first written as eight).

## Conclusion

A single record can span many chunks, so a reader must join the chunks of a part before splitting it into records. That holds for the main text as well as the stylesheet. Chunks of exactly 65,536 decoded bytes, with a shorter last one, were seen again.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `big.pages` | `0002/hello.pages` | `2001 5.1: ×19 → ×30018`; the part is eight chunks, and the body's record is in all of them | *Confirmed*: a record can cross chunk boundaries, and a chunk decodes to at most 65,536 bytes |

## Confidence

*Confirmed*: records can cross chunk boundaries ([0001](0001-empty-document.md) and this experiment), and chunks decode to at most 65,536 bytes.
