-- Experiment 0047: save a Numbers spreadsheet whose first sheet has a second table, named "Second".
-- Usage: osascript recipes/0047-numbers-second-table.applescript /absolute/path/doc.numbers
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0047-numbers-second-table.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	tell application "Numbers"
		set theDoc to make new document
		tell sheet 1 of theDoc to make new table with properties {name:"Second"}
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
