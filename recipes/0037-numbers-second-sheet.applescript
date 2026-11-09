-- Experiment 0037: save a Numbers spreadsheet with a second sheet named "Second".
-- Usage: osascript recipes/0037-numbers-second-sheet.applescript /absolute/path/doc.numbers
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0037-numbers-second-sheet.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	tell application "Numbers"
		set theDoc to make new document
		tell theDoc to make new sheet with properties {name:"Second"}
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
