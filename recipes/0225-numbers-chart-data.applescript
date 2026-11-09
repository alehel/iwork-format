-- Experiment 0225: make a Numbers spreadsheet with a small table of chart data, selected, ready for
-- Insert → Chart. Table 1 gets x and y in B1:C1, r1 and r2 in A2:A3 and the values 1, 2, 3, 4 in B2:C3.
-- Usage: osascript recipes/0225-numbers-chart-data.applescript
-- Numbers opens while the recipe runs, and the document is left open and unsaved.

tell application "Numbers"
	set d to make new document
	tell table 1 of sheet 1 of d
		set value of cell "B1" to "x"
		set value of cell "C1" to "y"
		set value of cell "A2" to "r1"
		set value of cell "A3" to "r2"
		set value of cell "B2" to 1
		set value of cell "C2" to 2
		set value of cell "B3" to 3
		set value of cell "C3" to 4
		set selection range to range "A1:C3"
	end tell
	return name of d
end tell
