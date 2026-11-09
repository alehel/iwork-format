-- Experiments 0169-0176: save a Numbers spreadsheet with one cell of table 1 set in B2.
-- Usage: osascript recipes/0169-numbers-controls.applescript mode /absolute/path/out.numbers
-- Modes:
--   checkfalse  format checkbox, value false     rating0   format rating, value 0
--   slider      format slider, value 50          stepper   format stepper, value 5
--   popup       format pop up menu, value "x"    negative  the number -5
--   boolformula the formula =1=1                 numtext   the text "123" set as a string
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	set mode to item 1 of argv
	set outFile to POSIX file (item 2 of argv)
	tell application "Numbers"
		set theDoc to make new document
		tell table 1 of sheet 1 of theDoc
			if mode is "checkfalse" then
				set format of cell "B2" to checkbox
				set value of cell "B2" to false
			else if mode is "rating0" then
				set format of cell "B2" to rating
				set value of cell "B2" to 0
			else if mode is "slider" then
				set format of cell "B2" to slider
				set value of cell "B2" to 50
			else if mode is "stepper" then
				set format of cell "B2" to stepper
				set value of cell "B2" to 5
			else if mode is "popup" then
				set format of cell "B2" to pop up menu
				set value of cell "B2" to "x"
			else if mode is "negative" then
				set value of cell "B2" to -5
			else if mode is "boolformula" then
				set value of cell "B2" to "=1=1"
			else if mode is "numtext" then
				set value of cell "B2" to "123"
			end if
		end tell
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
