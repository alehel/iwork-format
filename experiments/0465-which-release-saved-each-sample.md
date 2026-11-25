# 0465: Which release saved each sample

**Status:** run

With more than one release of the apps on the same Mac, a run can open or save a document in another copy than the one meant: the copies share a bundle ID, so `open -a Pages` and AppleScript's `tell application "Pages"` let the system choose. Each document an app saves records the app's build in `Metadata/BuildVersionHistory.plist` ([0461](0461-new-documents-in-14-5.md)). This experiment checks every sample's builds against the release its experiment says it used, and lists the copies of the apps installed.

## Setup

| | |
| --- | --- |
| Apps | Pages and Numbers 14.5 installed in `/Applications`; no Keynote there |
| macOS | 26.5.2 (25F84) |
| Date | 2026-11-23 |
| Input | Every `.pages`, `.key` and `.numbers` in `samples/`, including `samples/theme/`: 1,299 documents |
| Script | The new [`recipes/0465-saved-by.py`](../recipes/0465-saved-by.py), which reads each document's build history and compares its last build's release with the releases its experiment's setup names, as the site reads them |

## Recipe

```bash
python3 -I recipes/0465-saved-by.py samples
for id in com.apple.iWork.Pages com.apple.iWork.Numbers com.apple.iWork.Keynote; do
  mdfind "kMDItemCFBundleIdentifier == '$id'"
done
```

## Observation

| Documents | Saved by |
| --- | --- |
| 574 `.pages`, 360 `.numbers`, 328 `.key` | 15.4 only (`M15.4-7051.0.79-2`) |
| 10 `.pages`, 17 `.numbers` | 14.5 only (`M14.5-7045.0.17-4`), all from 0461 and 0464 |
| 10 | unreadable: encrypted, so their build history is too |

No document was saved by more than one release, and none by a release its experiment doesn't name. No other build appears in any document.

Spotlight knows these copies of the apps:

| App | Copies |
| --- | --- |
| Pages | `/Applications/Pages.app` (14.5), `~/Desktop/backup/13.1/Pages.app` (13.1) |
| Numbers | `/Applications/Numbers.app` (14.5), `~/Desktop/backup/13.1/Numbers.app` (13.1) |
| Keynote | `~/Desktop/backup/13.1/Keynote.app` (13.1) |

## Conclusion

Every document an app saved in these experiments was saved by the release its experiment names: the 15.4 apps up to 0460, including all 328 Keynote presentations, and 14.5 in 0461 and 0464. No saved document came from the 13.1 copies or from an update.

Runs that only opened a document, to read from it or export it, leave no record in the file, and an exported PDF names only the app, not its version. From 0372 to 0460, [`recipes/0372-in-app.sh`](../recipes/0372-in-app.sh) addressed the 15.4 apps by their own names ("Pages Creator Studio" and so on), which no other copy has. In 0462 and 0463 each document had to open in the copy AppleScript addressed, `/Applications/Pages.app` or `/Applications/Numbers.app`, or the run would have reported it as not opened. Readings in Keynote before 0372 that saved nothing can't be checked from their files; rerunning them is the way to check them.

Since a second copy of an app makes the choice the system's, the helper now prints to stderr which app, version and build it used, and warns when Spotlight knows more than one copy of it.

## Evidence

No documents of its own: it reads the build history of every sample.

## Confidence

*Confirmed*: the release that saved each of 1,289 documents matches its experiment. *Unknown*: which copy performed reads that saved nothing before 0372.
