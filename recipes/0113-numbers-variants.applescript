-- Experiments 0113-0130: save a Numbers spreadsheet with one change to its first table or sheet.
-- Usage: osascript recipes/0113-numbers-variants.applescript /absolute/path/doc.numbers mode [/absolute/path/image.png]
-- Modes (cells are in table 1 of sheet 1):
--   samestring  "abc" in B2 and C2           cleared   "abc" in B2, then B2 cleared
--   newline     "one" & linefeed & "two" in B2  extremes  1E+20 in B2, 0.000001 in C2
--   dateonly    the date 2026-01-02 (midnight) in B2      emoji  "hi🙂" in B2
--   sort        3, 1, 2 in B2:B4, sorted ascending by column B
--   fewerrows   row count set to 5            emptyref  =C3 in B2, with C3 empty
--   tablename   table renamed "Budget"         fewercols column count set to 3
--   sheetname   sheet renamed "Data"           unfrozen  header rows not frozen
--   origin      table moved to (0, 0)          textbox   a text item "note" on sheet 1
--   image       the image on sheet 1           shape     a shape on sheet 1
--   longtext    a 5000-character text in B2
-- The folder must exist. Numbers opens while the recipe runs.

on run argv
	if (count of argv) < 2 then error "usage: osascript 0113-numbers-variants.applescript doc.numbers mode [image]"
	set outFile to POSIX file (item 1 of argv)
	set mode to item 2 of argv
	tell application "Numbers"
		set theDoc to make new document
		set sh to sheet 1 of theDoc
		set t to table 1 of sh
		if mode is "samestring" then
			set value of cell "B2" of t to "abc"
			set value of cell "C2" of t to "abc"
		else if mode is "cleared" then
			set value of cell "B2" of t to "abc"
			clear cell "B2" of t
		else if mode is "newline" then
			set value of cell "B2" of t to "one" & linefeed & "two"
		else if mode is "extremes" then
			set value of cell "B2" of t to 1.0E+20
			set value of cell "C2" of t to 1.0E-6
		else if mode is "dateonly" then
			set d to current date
			set year of d to 2026
			set month of d to 1
			set day of d to 2
			set time of d to 0
			set value of cell "B2" of t to d
		else if mode is "emoji" then
			set value of cell "B2" of t to "hi🙂"
		else if mode is "sort" then
			set value of cell "B2" of t to 3
			set value of cell "B3" of t to 1
			set value of cell "B4" of t to 2
			sort t by column 2 of t direction ascending
		else if mode is "fewerrows" then
			set row count of t to 5
		else if mode is "emptyref" then
			set value of cell "B2" of t to "=C3"
		else if mode is "tablename" then
			set name of t to "Budget"
		else if mode is "fewercols" then
			set column count of t to 3
		else if mode is "sheetname" then
			set name of sh to "Data"
		else if mode is "unfrozen" then
			set header rows frozen of t to false
		else if mode is "origin" then
			set position of t to {0, 0}
		else if mode is "textbox" then
			tell sh to make new text item with properties {object text:"note"}
		else if mode is "image" then
			tell sh to make new image with properties {file:POSIX file (item 3 of argv)}
		else if mode is "shape" then
			tell sh to make new shape
		else if mode is "longtext" then
			set s to ""
			repeat 500 times
				set s to s & "abcdefghij"
			end repeat
			set value of cell "B2" of t to s
		end if
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
