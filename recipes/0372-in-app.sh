#!/bin/sh
# Experiments 0372 onward: open one document in its app, run AppleScript against it, close it unsaved.
#
# Usage: sh recipes/0372-in-app.sh APP FILE 'SCRIPT'
#
# APP is Pages, Numbers or Keynote. FILE is opened through Launch Services (CONTRIBUTING.md), then
# SCRIPT runs inside `tell application ...` with `d` set to that document, found by its file, and
# whatever it returns is printed. Other open documents are left alone. The document is closed
# without saving, but an app may autosave a change a script makes first, so run such scripts on
# copies. Waits up to 30 seconds for the document to open.
#
# The app is "APP Creator Studio" (15.4) when that is installed, and otherwise plain "APP" (such as
# Pages 14.5, from experiment 0461 on). Set IWORK_APP to the full name to choose another.
#
# From experiment 0465 on, it prints to stderr which app it used, its version and build, and a
# warning when Spotlight knows more than one copy of that app, since the system then picks one.
set -eu
if [ -n "${IWORK_APP:-}" ]; then app="$IWORK_APP"
elif [ -d "/Applications/$1 Creator Studio.app" ]; then app="$1 Creator Studio"
else app="$1"; fi
path=$(osascript -e "POSIX path of (path to application \"$app\")" 2>/dev/null || true)
if [ -n "$path" ]; then
  plist="${path%/}/Contents/Info"
  bid=$(defaults read "$plist" CFBundleIdentifier 2>/dev/null || true)
  echo "[in-app: $app $(defaults read "$plist" CFBundleShortVersionString 2>/dev/null) ($(defaults read "$plist" CFBundleVersion 2>/dev/null)) at $path]" >&2
  copies=$(mdfind "kMDItemCFBundleIdentifier == '$bid'" 2>/dev/null | grep -c '\.app$' || true)
  if [ "${copies:-0}" -gt 1 ]; then
    echo "[in-app: warning: $copies copies of $bid are installed; the system may open another one]" >&2
  fi
fi
file=$(cd "$(dirname "$2")" && pwd -P)/$(basename "$2")
inner=$(mktemp -t in-app).applescript
trap 'rm -f "$inner"' EXIT
printf 'on run {docId}\ntell application "%s"\nset d to document id docId\n%s\nend tell\nend run\n' "$app" "$3" > "$inner"
open -a "$app" "$file"
osascript - "$app" "$file" "$inner" <<'EOF'
on run argv
  set appName to item 1 of argv
  set target to item 2 of argv
  set inner to item 3 of argv
  tell application appName
    set d to missing value
    repeat 60 times
      repeat with x in documents
        try
          set p to POSIX path of (file of x as alias)
          if p ends with "/" then set p to text 1 thru -2 of p
          if p is target then set d to contents of x
        end try
      end repeat
      if d is not missing value then exit repeat
      delay 0.5
    end repeat
    if d is missing value then error "document did not open: " & target
  end tell
  set r to ""
  try
    tell application appName to set docId to id of d
    set r to run script (POSIX file inner) with parameters {docId}
    try
      r
    on error
      set r to ""
    end try
  on error e
    set r to "error: " & e
  end try
  tell application appName to close d saving no
  return r
end run
EOF
