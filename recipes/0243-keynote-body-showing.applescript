-- Experiment 0243: save two Keynote presentations whose second slide (the default new-slide layout) has its
-- body placeholder shown or hidden.
-- Usage: osascript recipes/0243-keynote-body-showing.applescript /absolute/folder
-- Writes body.key (body shown) and no-body.key (body showing set to false). Returns the layout's name.
-- The folder must exist. Keynote opens while the recipe runs.

on run argv
	set d to item 1 of argv
	tell application "Keynote"
		repeat with nm in {"body", "no-body"}
			set k to make new document
			set s to make new slide at end of slides of k
			if (contents of nm) is "no-body" then set body showing of s to false
			set r to name of base layout of s
			save k in POSIX file (d & "/" & nm & ".key")
			close k saving no
		end repeat
		return r
	end tell
end run
