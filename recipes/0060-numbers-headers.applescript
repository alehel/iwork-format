-- Experiment 0060: save a Numbers spreadsheet whose first table has 2 header rows, 0 header columns and 1 footer row.
-- Usage: osascript recipes/0060-numbers-headers.applescript /absolute/path/doc.numbers
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0060-numbers-headers.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			set header row count to 2
			set header column count to 0
			set footer row count to 1
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
