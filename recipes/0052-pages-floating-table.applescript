-- Experiment 0052: save a Pages document with body text "one" and a 3 x 3 table made through AppleScript.
-- Usage: osascript recipes/0052-pages-floating-table.applescript /absolute/path/doc.pages
-- The folder must exist. Pages opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0052-pages-floating-table.applescript /absolute/path/doc.pages"
	set outFile to POSIX file (item 1 of argv)
	tell application "Pages"
		set theDoc to make new document
		set body text of theDoc to "one"
		tell page 1 of theDoc to make new table with properties {row count:3, column count:3}
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
