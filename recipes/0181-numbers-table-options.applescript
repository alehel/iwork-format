-- Experiments 0181-0184: save a Numbers spreadsheet after one change to table 1 of sheet 1.
-- Usage: osascript recipes/0181-numbers-table-options.applescript mode /absolute/path/out.numbers
-- Modes:
--   numeral    B2 is 10, with the numeral system format
--   transpose  B2 is 1, C2 is 2, B3 is 3, then the table is transposed
--   frozencols header columns not frozen (a new table has one frozen header column)
--   footer     one footer row, with 7 in B10 (the default table has 10 rows)
--   plain      no change, for comparison
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	set mode to item 1 of argv
	set outFile to POSIX file (item 2 of argv)
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			if mode is "numeral" then
				set format of cell "B2" to numeral system
				set value of cell "B2" to 10
			else if mode is "transpose" then
				set value of cell "B2" to 1
				set value of cell "C2" to 2
				set value of cell "B3" to 3
				transpose
			else if mode is "frozencols" then
				set header columns frozen to false
			else if mode is "footer" then
				set footer row count to 1
				set value of cell "B10" to 7
			end if
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
