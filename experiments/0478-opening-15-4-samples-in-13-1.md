# 0478: Opening the 15.4 samples in 13.1

**Status:** run

The 13.1 apps write nearly the same format as 15.4 ([0477](0477-every-scripted-sample-in-13-1.md)). This experiment opens the 15.4 samples in 13.1, as [0470](0470-opening-15-4-samples-in-16-0.md) did in 16.0 and [0462](0462-opening-15-4-documents-in-14-5.md) and [0467](0467-opening-15-4-presentations-in-keynote-14-5.md) in 14.5.

## Setup

| | |
| --- | --- |
| Apps | Pages, Numbers and Keynote 13.1 (build `M13.1-7037.0.101-2`), in Norwegian, run from a read-only disk image |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-24 |
| Input | The same 1,211 documents as 0470: every `.pages` and `.numbers` under `samples/0001` to `samples/0460` and every `.key` under `samples/NNNN/` and `samples/theme/NNNN/` but those 0470 left out, the password-protected ones among them |
| Scripts | [`recipes/0462-open-in-app.py`](../recipes/0462-open-in-app.py) and [`recipes/0467-open-keynote.py`](../recipes/0467-open-keynote.py), unchanged. [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh), which they use, now takes the folder of the apps from `IWORK_APP_DIR`, since it would otherwise choose the installed 16.0 apps |

## Recipe

```bash
export IWORK_APP_DIR=/Volumes/iwork-13-1
for r in "1 178" "181 393" "395 395" "397 423" "425 433" "435 450" "452 460"; do
  python3 -I recipes/0462-open-in-app.py samples $r
done
python3 -I recipes/0467-open-keynote.py samples 0379,0180,0466,0467,0468,0469,theme,release,resave,resaved
python3 -I recipes/0467-open-keynote.py samples/theme 0379,0180,0472,0474
```

## Observation

| Result | Documents |
| --- | --- |
| Pages and Numbers: opened, and the body text agrees with the file (Pages) or the sheets and table were read (Numbers) | 887 |
| Pages: opened, and the body text differs from the file | 1 (`0419/no-body.pages`) |
| Keynote: opened; slide count, titles and notes agree with the file | 323 (244 under `samples/NNNN/`, 79 under `samples/theme/`) |
| Not opened | 0 |

13.1 reports no body text for `0419/no-body.pages`, as every other release did ([0470](0470-opening-15-4-samples-in-16-0.md)).

Afterwards the samples were compared with checksums taken before: opening and closing unsaved left every file as it was.

## Conclusion

The 13.1 apps open every document the 15.4 apps saved in these experiments, and every one written from this spec, and read the same text, tables, slides, titles and notes from them. The password-protected samples weren't tried in 13.1, since each needs its password typed by hand.

## Confidence

*Confirmed*: the 13.1 apps open 1,211 documents from 15.4 and from the spec's writer, and read what 15.4 read.
