# 0178: Checking every sample

**Status:** run

After 177 experiments, this experiment checks that every sample saved so far can be framed, walked and read with what the spec says.

## Setup

| | |
| --- | --- |
| Pages, Keynote, Numbers | 15.4 (build `M15.4-7051.0.79-2`) |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-09 |
| Documents | All 203 documents in `samples/`, from experiments 0001–0177 |

## Recipe

Three checks were run over every document in `samples/` with `iwork-probe` and a throwaway script:

```bash
for f in samples/*/*.pages samples/*/*.key samples/*/*.numbers; do
  for p in $(target/release/iwork-probe list "$f" | awk '{print $NF}' | grep '\.iwa$'); do
    target/release/iwork-probe records "$f" "$p" > /dev/null || echo "framing failed: $f $p"
  done
  target/release/iwork-probe text "$f" > /dev/null || echo "text failed: $f"
done
```

1. **Framing.** Split every `.iwa` part into chunks and records, as in [container.md](../spec/container.md).
2. **Reachability.** Start at objects 1, 2 and 71, and at 61 in documents with a chart, and follow only the IDs listed in record headers (fields 2.5 and 2.4.4). Count which objects are reached and which listed IDs don't exist.
3. **Text.** Extract every text record.

## Observation

| | |
| --- | --- |
| Documents | 203: 89 Pages, 55 Keynote, 59 Numbers, 3 of them folder packages |
| `.iwa` parts | 4,692, all framed without error |
| Objects | 142,258, all reached from the roots |
| References to missing objects | none |
| Text extraction | no errors |

The only listed ID that didn't exist was root 61, in the documents without a chart.

## Conclusion

Everything the spec says about the container holds for every document saved so far, from all three apps and in both the ZIP and folder forms: chunk framing, record headers, reference lists, the four roots, data files and UTF-8 entry names. No part or object is left that a reader following the spec couldn't reach.

## Confidence

*Confirmed*: the container layer ([container.md](../spec/container.md)) holds for all 203 samples.
