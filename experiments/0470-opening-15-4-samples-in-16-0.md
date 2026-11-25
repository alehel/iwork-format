# 0470: Opening the 15.4 samples in 16.0

**Status:** run

The 16.0 apps write the same format as 15.4 ([0469](0469-the-16-0-apps.md)). This experiment opens every sample the 15.4 apps saved or the spec's writer wrote, in all three apps, and checks what 16.0 reads, as [0462](0462-opening-15-4-documents-in-14-5.md) and [0467](0467-opening-15-4-presentations-in-keynote-14-5.md) did for 14.5.

## Setup

| | |
| --- | --- |
| Apps | Pages, Numbers and Keynote 16.0 (build `M16.0-7052.0.68-2`), in Norwegian, the only copies installed |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-24 |
| Input | Every `.pages` and `.numbers` under `samples/0001` to `samples/0460`, and every `.key` under `samples/NNNN/` and `samples/theme/NNNN/`, leaving out what 0462 and 0467 left out: the files written to make the apps fail (0379, 0394, 0396, 0424, 0434 and 0451) and the samples later releases saved (0461 on). Also left out: experiments 0179 and 0180, whose seven password-protected documents would hold up a run nobody watches with their password prompt (with them, 0179's two unprotected documents). 1,211 documents |
| Scripts | [`recipes/0462-open-in-app.py`](../recipes/0462-open-in-app.py) and [`recipes/0467-open-keynote.py`](../recipes/0467-open-keynote.py), unchanged: Pages' body text against the body's text record, Numbers' sheets and first table, and Keynote's slide count, titles and notes against the file |

## Recipe

```bash
for r in "1 178" "181 393" "395 395" "397 423" "425 433" "435 450" "452 460"; do
  python3 -I recipes/0462-open-in-app.py samples $r
done
python3 -I recipes/0467-open-keynote.py samples 0379,0180,0466,0467,0468,0469
python3 -I recipes/0467-open-keynote.py samples/theme 0379,0180
for n in 37 38; do
  sh recipes/0372-in-app.sh Keynote samples/0196/all.key "set p to transition properties of slide $n of d
return transition effect of p"
done
python3 -I recipes/0465-saved-by.py samples
```

## Observation

| Result | Documents |
| --- | --- |
| Pages and Numbers: opened, and the body text agrees with the file (Pages) or the sheets and table were read (Numbers) | 887 |
| Pages: opened, and the body text differs from the file | 1 (`0419/no-body.pages`) |
| Keynote: opened; slide count, titles and notes agree with the file | 323 (244 under `samples/NNNN/`, 79 under `samples/theme/`), 484 slides |
| Not opened | 0 |

No alert was shown. Every reading went through "Keynote Creator Studio" and so on, 16.0.

`0419/no-body.pages` has its body switch written off over the body's text `hello`. 16.0 reports no body text for it, as 15.4 did when it was made ([0419](0419-writing-the-document-body-setting.md)) and as 14.5 did ([0462](0462-opening-15-4-documents-in-14-5.md)): the script compares with the file, not with 15.4.

16.0 reports the transition of 0196's slide 37 as `fade and move` and of slide 38 as `radial wipe`, which 14.5 couldn't report ([0467](0467-opening-15-4-presentations-in-keynote-14-5.md)).

Afterwards, every sample's build history still names the release its experiment names, apart from `0467/resaved.key`, which 14.5 saved over 15.4 on purpose in 0467. Opening and closing unsaved left the files as they were.

### The password-protected samples

A second, attended run opened the nine documents of experiments 0179 and 0180 left out above. The two without a password were read with [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) as above. The seven with one were opened with `open -a`, their test passwords (`pw1234`, and `påss` for `accent.pages`) were typed into 16.0's prompts by hand, not saved in the keychain, and the same script then read the open documents:

```bash
for f in 0179/locked.pages 0179/locked2.pages 0180/accent.pages 0180/image.pages; do
  open -a "Pages Creator Studio" "$PWD/samples/$f"
done
open -a "Numbers Creator Studio" "$PWD/samples/0180/locked.numbers"
open -a "Keynote Creator Studio" "$PWD/samples/0180/locked.key" "$PWD/samples/theme/0180/locked.key"
```

| Document | 16.0 reads | The file holds (`iwork-probe --password`) |
| --- | --- | --- |
| `0179/plain.pages`, `0179/unlocked.pages` (no password) | body `one` | `one` |
| `0179/locked.pages`, `0179/locked2.pages`, `0180/accent.pages`, `0180/image.pages` | body `one` | `one` |
| `0180/locked.numbers` | 1 sheet, first table `Tabell 1` | one sheet, and the name `Tabell 1` |
| `0180/locked.key`, `theme/0180/locked.key` | 1 slide, no title text | one slide part |

Every prompt took its password, and the documents were closed unsaved; their files' modification dates are unchanged.

[0467](0467-opening-15-4-presentations-in-keynote-14-5.md) gave 486 slides for the same 323 presentations, but each presentation's count agreed with the slide nodes its file lists, in that run and in this one, so the totals should be the same. 347 and 137 slides in the two folders add up to 484. The earlier figure can't be checked again, since 14.5 isn't installed.

## Conclusion

The 16.0 apps open every document the 15.4 apps saved in these experiments, the password-protected ones included, and every one written from this spec, and read the same text, tables, slides, titles and notes from them as 15.4 did. Unlike 14.5, Keynote 16.0 knows the radial wipe. Whether 16.0 also draws the samples the same is the next experiment's question.

## Evidence

No documents of its own: it opens the samples of 0001 to 0460 in 16.0.

## Confidence

*Confirmed*: the 16.0 apps open 1,211 documents from 15.4 and from the spec's writer, and read what 15.4 read; and, with the passwords typed by hand, the nine documents of 0179 and 0180, protected or not.
