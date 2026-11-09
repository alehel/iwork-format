-- Experiments 0230-0232: make a new Numbers spreadsheet with cell B2 of table 1 selected, so the Format
-- sidebar shows the table's options. The document is left open and unsaved.
-- Usage: osascript recipes/0230-numbers-blank.applescript

tell application "Numbers"
	set d to make new document
	tell table 1 of sheet 1 of d to set selection range to range "B2"
	return name of d
end tell
