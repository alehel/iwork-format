# 0433: Writing other chunk sizes

**Status:** run

An `.iwa` part is a sequence of chunks, each a raw Snappy block. No chunk Pages writes decodes to more than 65,536 bytes: a larger part is split into chunks of exactly 65,536 decoded bytes and a shorter last one ([0001](0001-empty-document.md), [0141](0141-large-text.md)). This experiment writes the parts with much smaller and much larger chunks.

## Setup

| | |
| --- | --- |
| Pages | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-18 |
| Input | `samples/0002/hello.pages`: seven parts; `DocumentStylesheet.iwa` decodes to 338,982 bytes in six chunks (five of 65,536 and one of 11,302), the others to one chunk each |
| Writer | The new [`recipes/0433-chunk-size.py`](../recipes/0433-chunk-size.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0433
O=samples/0433
for s in 1000 65536 1000000; do
  python3 -I recipes/0433-chunk-size.py samples/0002/hello.pages $O/chunks-$s.pages $s
  sh recipes/0372-in-app.sh Pages $O/chunks-$s.pages 'return {body text of d, font of word 1 of body text of d}'
done
```

## Observation

| File | Chunk size | Largest chunk, decoded | Pages |
| --- | --- | --- | --- |
| `chunks-1000.pages` | 1,000 bytes | 1,000 | opens: `hello`, HelveticaNeue |
| `chunks-65536.pages` | 65,536 bytes, as Pages | 65,536 | opens: `hello`, HelveticaNeue |
| `chunks-1000000.pages` | up to 1,000,000 bytes | 338,982: the whole stylesheet in one chunk | opens: `hello`, HelveticaNeue |

No alert was shown.

## Conclusion

Pages joins a part's chunks before reading it, whatever their size: with 1,000-byte chunks nearly every record is cut across two chunks, and the stylesheet in a single chunk of 338,982 bytes reads as well as in six. The 65,536-byte split is how Pages writes, not something it requires. A reader shouldn't assume a limit on a chunk's decoded size beyond what the 3-byte length allows for the stored block.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `chunks-1000.pages` | `0002/hello.pages` | Only chunks of 1,000 bytes: `same records`, `same parts` | *Confirmed*: Pages reads chunks smaller than 65,536 bytes |
| `chunks-65536.pages` | `0002/hello.pages` | Only written again in chunks of 65,536 bytes: `same records`, `same parts` | *Control*: Pages opens it |
| `chunks-1000000.pages` | `0002/hello.pages` | Only one chunk per part, up to 338,982 bytes: `same records`, `same parts` | *Confirmed*: Pages reads a chunk larger than 65,536 bytes |

## Confidence

*Confirmed*: Pages reads chunks of any decoded size, smaller or larger than 65,536 bytes, by writing them.
