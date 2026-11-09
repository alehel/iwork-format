-- Experiment 0045: save a Numbers spreadsheet whose column B is 200 points wide and row 3 is 50 points high.
-- Usage: osascript recipes/0045-numbers-sizes.applescript /absolute/path/doc.numbers
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0045-numbers-sizes.applescript /absolute/path/doc.numbers"
	set outFile to POSIX file (item 1 of argv)
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			set width of column 2 to 200
			set height of row 3 to 50
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
