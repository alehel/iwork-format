-- Experiment 0078: save a Numbers spreadsheet with a formula that gives an error: "=1/0" in B2.
-- Usage: osascript recipes/0078-numbers-error.applescript /absolute/path/doc.numbers
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0078-numbers-error.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	tell application "Numbers"
		set theDoc to make new document
		set value of cell "B2" of table 1 of sheet 1 of theDoc to "=1/0"
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
