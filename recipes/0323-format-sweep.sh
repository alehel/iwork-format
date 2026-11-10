#!/bin/zsh
# Experiment 0323: write every format kind from FIRST to LAST into the format that column B's
# numbers use, and read how Numbers shows B2 (the value 1).
# Usage: zsh recipes/0323-format-sweep.sh FIRST LAST OUT.tsv
cd "$(dirname $0)/.."
mkdir -p samples/0323/work
for n in $(seq $1 $2); do
  f="$PWD/samples/0323/work/k$n.numbers"
  python3 -I recipes/0307-format-kind.py samples/0226/plain.numbers "$f" 2 $n >/dev/null
  osascript -e 'tell application "Numbers Creator Studio" to close every document saving no' >/dev/null 2>&1
  open -a "Numbers Creator Studio" "$f"
  for i in {1..15}; do
    c=$(osascript -e 'tell application "Numbers Creator Studio" to count documents' 2>/dev/null)
    [ "$c" -ge 1 ] 2>/dev/null && break
    sleep 1
  done
  r=$(osascript -e 'tell application "Numbers Creator Studio"
    tell table 1 of sheet 1 of front document
      return (formatted value of cell "B2") & tab & (format of cell "B2" as string) & tab & (value of cell "B2" as string)
    end tell
  end tell' 2>&1 | tr '\n' ' ')
  printf "%s\t%s\n" "$n" "$r" >> "$3"
  rm -f "$f"
done
osascript -e 'tell application "Numbers Creator Studio" to close every document saving no' >/dev/null 2>&1
