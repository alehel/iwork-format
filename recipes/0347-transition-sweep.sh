#!/bin/zsh
# Experiment 0347: write each transition identifier listed in IDS into a slide's transition and
# read back the effect AppleScript reports. Keynote must be running.
# Usage: zsh recipes/0347-transition-sweep.sh IDS.txt OUT.tsv
# Input: samples/0302/original.key, whose slide 2655467 has a transition in field 4.2.8.
cd "$(dirname $0)/.."
mkdir -p samples/0347/work
while read id; do
  f="$PWD/samples/0347/work/t.key"
  python3 -I recipes/0302-set-path.py samples/0302/original.key "$f" 2655467 4.2.8.2 string "$id" >/dev/null
  osascript -e 'tell application "Keynote Creator Studio" to close every document saving no' >/dev/null 2>&1
  open -a "Keynote Creator Studio" "$f"
  for i in {1..15}; do
    c=$(osascript -e 'tell application "Keynote Creator Studio" to count documents' 2>/dev/null)
    [ "$c" -ge 1 ] 2>/dev/null && break
    sleep 1
  done
  r=$(osascript -e 'tell application "Keynote Creator Studio"' -e 'set tp to transition properties of slide 1 of front document' -e 'return (transition effect of tp) as string' -e 'end tell' 2>&1)
  printf "%s\t%s\n" "$id" "$r" >> "$2"
  rm -f "$f"
done < "$1"
osascript -e 'tell application "Keynote Creator Studio" to close every document saving no' >/dev/null 2>&1
