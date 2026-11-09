-- Experiment 0001: save a new, empty Pages document.
-- Usage: osascript recipes/0001-empty-document.applescript /absolute/path/empty.pages
-- The folder must exist. Pages opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0001-empty-document.applescript /absolute/path/empty.pages"
	set outFile to POSIX file (item 1 of argv)
	tell application "Pages"
		set theDoc to make new document
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
