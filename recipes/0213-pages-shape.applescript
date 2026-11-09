-- Experiments 0213-0216: make a Pages document with the body text "One" and N 100 x 100 shapes on page 1,
-- at x = 300, 450, ... and y = 300, then leave it open for a change through the Arrange menu.
-- Usage: osascript recipes/0213-pages-shape.applescript N
-- The last shape made is left selected. Pages opens while the recipe runs.

on run argv
	set n to (item 1 of argv) as integer
	tell application "Pages"
		set d to make new document
		set body text of d to "One"
		repeat with i from 1 to n
			tell page 1 of d to make new shape with properties {position:{150 + 150 * i, 300}, width:100, height:100}
		end repeat
		return name of d
	end tell
end run
