#!/bin/zsh
# Experiment 0316: write every function number from FIRST to LAST into a formula and read the
# formula back from Numbers, which must already be running (in English, for standard names).
# Usage: zsh recipes/0316-function-sweep.sh FIRST LAST OUT.tsv
# Input: samples/0104/nested.numbers, whose formula list 904540 calls function 15 once.
cd "$(dirname $0)/.."
first=$1; last=$2; out=$3
mkdir -p samples/0316/work
for n in $(seq $first $last); do
  f="$PWD/samples/0316/work/f$n.numbers"
  python3 -I recipes/0315-formula-function.py samples/0104/nested.numbers "$f" 904540 15 $n >/dev/null
  osascript -e 'tell application "Numbers Creator Studio" to close every document saving no' >/dev/null 2>&1
  open -a "Numbers Creator Studio" "$f"
  for i in {1..15}; do
    c=$(osascript -e 'tell application "Numbers Creator Studio" to count documents' 2>/dev/null)
    [ "$c" -ge 1 ] 2>/dev/null && break
    sleep 1
  done
  r=$(osascript -e 'tell application "Numbers Creator Studio"
    tell table 1 of sheet 1 of front document
      set v to value of cell "E2"
      return (formula of cell "E2") & tab & (v as string)
    end tell
  end tell' 2>&1 | tr '\n' ' ')
  printf "%s\t%s\n" "$n" "$r" >> "$out"
  rm -f "$f"
done
osascript -e 'tell application "Numbers Creator Studio" to close every document saving no' >/dev/null 2>&1
