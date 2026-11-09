-- Experiments 0226-0227: make a Numbers spreadsheet with data to group, ready for the Organise menu.
-- Table 1 gets "kind" and "n" in A1:B1, then a, b, a, b in A2:A5 and 1, 2, 3, 4 in B2:B5.
-- Usage: osascript recipes/0226-numbers-grouping-data.applescript range
-- The given range (such as A2 or A1:B5) is left selected. Numbers opens while the recipe runs,
-- and the document is left open and unsaved.

on run argv
	tell application "Numbers"
		set d to make new document
		tell table 1 of sheet 1 of d
			set value of cell "A1" to "kind"
			set value of cell "B1" to "n"
			set kinds to {"a", "b", "a", "b"}
			repeat with i from 1 to 4
				set value of cell ("A" & (i + 1)) to item i of kinds
				set value of cell ("B" & (i + 1)) to i
			end repeat
			set selection range to range (item 1 of argv)
		end tell
		return name of d
	end tell
end run
