# 0378: Writing the slide order

**Status:** run

A presentation's type-2 record lists its slide nodes (type 4) in field 3.2, in show order. Moving a slide in Keynote changes only that list ([0038](0038-second-slide.md), [0160](0160-moved-slide.md)). This experiment rewrites the list and reads the slides back through Keynote's AppleScript.

## Setup

| | |
| --- | --- |
| Keynote | 15.4, in Norwegian |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-17 |
| Input | `samples/theme/0160/move.key`: three slides titled C, A and B, in the test theme. Presentation 2652410 lists the slide nodes 2655739, 2655505 and 2655616 |
| Writer | The new [`recipes/0378-slide-order.py`](../recipes/0378-slide-order.py); read back with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) |

## Recipe

```bash
mkdir -p samples/0378
R=recipes/0378-slide-order.py
F=samples/theme/0160/move.key
cp $F samples/0378/original.key
python3 -I $R $F samples/0378/reversed.key 2652410 3,2,1
python3 -I $R $F samples/0378/rotated.key 2652410 2,3,1
python3 -I $R $F samples/0378/two.key 2652410 3,1
for f in original reversed rotated two; do
  sh recipes/0372-in-app.sh Keynote samples/0378/$f.key 'set out to {}
repeat with s in slides of d
  set end of out to object text of default title item of s
end repeat
return out'
done
```

## Observation

| File | 3.2 written | Slide titles, in order |
| --- | --- | --- |
| `original.key` | 2655739, 2655505, 2655616 | C, A, B |
| `reversed.key` | 2655616, 2655505, 2655739 | B, A, C |
| `rotated.key` | 2655505, 2655616, 2655739 | A, B, C |
| `two.key` | 2655616, 2655739 | B, C |

## Conclusion

The order of field 3.2 is the order Keynote shows the slides in, and nothing else decides it. A slide node left out of the list isn't shown at all, though its records are still in the file, so a reader should list slides from field 3.2 and not from the slide parts it finds.

## Evidence

| File | Compared with | Difference | Shows |
| --- | --- | --- | --- |
| `original.key` | `theme/0160/move.key` | `same bytes`, `2#2652410 3 ~ x"120508fb8ba201120508918aa201120508808ba201"` (2655739, 2655505, 2655616) | *Control*: C, A, B |
| `reversed.key` | `original.key` | Only `2#2652410 3 ~ x"120508808ba201120508918aa201120508fb8ba201"` (2655616, 2655505, 2655739) | *Confirmed*: Keynote shows B, A, C, the order of field 3.2 |
| `rotated.key` | `original.key` | Only `2#2652410 3 ~ x"120508918aa201120508808ba201120508fb8ba201"` (2655505, 2655616, 2655739) | *Confirmed*: Keynote shows A, B, C |
| `two.key` | `original.key` | Only `2#2652410 3.2: ×3 → ×2`, `2#2652410 3.2.1 ≠ 2655505` | *Confirmed*: a slide left out of the list isn't shown: B, C |

## Confidence

*Confirmed*: field 3.2 of the presentation as the show order, and as the list of slides shown, by writing it.
