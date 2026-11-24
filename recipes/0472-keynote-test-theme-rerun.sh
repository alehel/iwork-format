#!/bin/bash
# Experiment 0472: rerun the Keynote recipes of experiments 0466 and 0469 with the project's test
# theme in the installed Keynote, and compare each presentation with the test-theme one 15.4 made
# from the same recipe (experiment 0292, under samples/theme/).
#
# Usage: bash recipes/0472-keynote-test-theme-rerun.sh [OUT]
#
# OUT defaults to samples/theme/0472. Run from the repository root. The theme must be installed in
# Keynote as "iwork-format test v2" (theme/README.md). Each pair is compared with
# recipes/0461-compare-structure.py; UUIDs, the build history, the format version and record counts
# that agree are left out of what it prints.
set -u
export IWORK_KEYNOTE_THEME='iwork-format test v2'  # the theme in theme/; see recipes/0473-release-set.py
out=${1:-samples/theme/0472}
# 0197 and 0243 save into a folder; their files are moved up as 0197-default.key and so on
# afterwards, since fixtures/build.py reads only files directly under samples/theme/NNNN/.
mkdir -p "$out/0197" "$out/0243"
P=$(cd "$out" && pwd -P)
osascript recipes/0024-empty-iwork-document.applescript Keynote "$P/0024-empty-a.key"
osascript recipes/0025-keynote-title.applescript "$P/0025-hello.key"
osascript recipes/0038-keynote-two-slides.applescript "$P/0038-two-slides.key"
osascript recipes/0039-keynote-notes.applescript "$P/0039-notes.key"
osascript recipes/0046-keynote-layout.applescript "$P/0046-blank-layout.key" Tom
osascript recipes/0067-keynote-chart.applescript "$P/0067-chart.key"
osascript recipes/0068-keynote-variants.applescript "$P/0068-textbox.key" textbox
osascript recipes/0087-keynote-document-settings.applescript "$P/0087-autoplay.key" autoplay
osascript recipes/0091-keynote-transitions.applescript "$P/0091-movein.key" movein
osascript recipes/0096-keynote-objects.applescript "$P/0096-textstyle.key" textstyle
osascript recipes/0159-keynote-slides.applescript dup "$P/0159-dup.key"
osascript recipes/0196-keynote-all-transitions.applescript "$P/0196-all.key" || echo "FAILED 0196"
osascript recipes/0197-keynote-idle.applescript "$P/0197"
osascript recipes/0243-keynote-body-showing.applescript "$P/0243"
for f in 0197/default 0197/idle 0243/body 0243/no-body; do mv "$P/$f.key" "$P/${f/\//-}.key"; done
rmdir "$P/0197" "$P/0243"
for pair in "0024/empty-a.key 0024-empty-a.key" "0025/hello.key 0025-hello.key" \
  "0038/two-slides.key 0038-two-slides.key" "0039/notes.key 0039-notes.key" \
  "0046/blank-layout.key 0046-blank-layout.key" "0067/chart.key 0067-chart.key" \
  "0068/textbox.key 0068-textbox.key" "0087/autoplay.key 0087-autoplay.key" \
  "0091/movein.key 0091-movein.key" "0096/textstyle.key 0096-textstyle.key" \
  "0159/dup.key 0159-dup.key" "0196/all.key 0196-all.key" \
  "0197/default.key 0197-default.key" "0197/idle.key 0197-idle.key" \
  "0243/body.key 0243-body.key" "0243/no-body.key 0243-no-body.key"; do
  set -- $pair
  echo "=== theme/$1"
  python3 -I recipes/0461-compare-structure.py "samples/theme/$1" "$P/$2" \
    | grep -vE "UUID|revision|BuildVersionHistory|fileFormatVersion|-> [0-9]+ records$"
done
