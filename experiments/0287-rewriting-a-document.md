# 0287: Rewriting a document

**Status:** run

Every finding so far was made by reading what the apps write. A stronger test of the container layer is to write a document from the spec and see whether Pages accepts it. This experiment rewrites every `.iwa` part of a document with an encoder written only from [container.md](../spec/container.md), with no content changed, and opens the result in Pages.

## Setup

| | |
| --- | --- |
| Pages | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Input | `samples/0236/plain.pages`, a new document with the body text `One` |
| Writer | [`recipes/0287-iwa-writer.py`](../recipes/0287-iwa-writer.py), standard-library Python |

## Recipe

```bash
mkdir -p samples/0287
cp samples/0236/plain.pages samples/0287/original.pages
python3 -I recipes/0287-iwa-writer.py samples/0287/original.pages samples/0287/rewritten.pages
osascript -e 'tell application "Pages"' \
  -e "set d to open POSIX file \"$PWD/samples/0287/rewritten.pages\"" \
  -e 'set r to body text of d' \
  -e "save d in POSIX file \"$PWD/samples/0287/resaved.pages\"" \
  -e 'close d saving no' -e 'return r' -e 'end tell'
```

For each `.iwa` part, the writer:

1. Decodes the chunks and splits the joined bytes into records.
2. Encodes every record again: header length, header (with each payload's length recomputed into field 2.3), payloads.
3. Encodes the result as chunks of at most 65,536 decoded bytes. Each chunk is a raw Snappy block of literal runs only, which the public Snappy format allows but Pages never writes.

Other files are copied as they are. The ZIP is written uncompressed, as Pages writes it.

## Observation

`rewritten.pages` is 395 kilobytes against the original's 90, because literal-only Snappy doesn't compress. Every part decodes to exactly the same bytes as the original's.

Pages opens it without a warning, reports the body text `One`, and saves it again as `resaved.pages`. That file is 90 kilobytes again, compressed by Pages as usual.

## Conclusion

The chunk and record layers of the spec are complete enough to write: a document whose every `.iwa` part was framed again by an independent encoder opens and saves normally. Pages doesn't need its own Snappy matches. Any valid raw Snappy block is accepted, including one with no compression at all, so a writer can skip compression entirely.

## Confidence

*Confirmed*: re-encoded chunks and records, with header field 2.3 recomputed, are accepted by Pages.
