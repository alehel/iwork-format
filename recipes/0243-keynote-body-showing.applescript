-- Experiment 0243: save two Keynote presentations whose second slide (the default new-slide layout) has its
-- body placeholder shown or hidden.
-- Usage: osascript recipes/0243-keynote-body-showing.applescript /absolute/folder
-- Writes body.key (body shown) and no-body.key (body showing set to false). Returns the layout's name.
-- The folder must exist. Keynote opens while the recipe runs.

on run argv
	set d to item 1 of argv
	tell application "Keynote"
		repeat with nm in {"body", "no-body"}
			set k to my newKeynote()
			set s to make new slide at end of slides of k
			if (contents of nm) is "no-body" then set body showing of s to false
			set r to name of base layout of s
			save k in POSIX file (d & "/" & nm & ".key")
			close k saving no
		end repeat
		return r
	end tell
end run

-- A new Keynote presentation in the theme named in IWORK_KEYNOTE_THEME, such as
-- "iwork-format test" (experiment 0291), or in Keynote's default theme when it is unset.
on newKeynote()
	set t to system attribute "IWORK_KEYNOTE_THEME"
	tell application "Keynote"
		if t is "" then return make new document
		return make new document with properties {document theme:theme t}
	end tell
end newKeynote
