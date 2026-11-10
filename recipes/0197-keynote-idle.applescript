-- Experiment 0197: save Keynote presentations with different maximum idle durations.
-- Usage: osascript recipes/0197-keynote-idle.applescript /absolute/folder
-- Writes default.key (unchanged) and idle.key (maximum idle duration 123 seconds).
-- The folder must exist. Keynote opens while the recipe runs.

on run argv
	set d to item 1 of argv
	tell application "Keynote"
		set a to my newKeynote()
		set r to maximum idle duration of a
		save a in POSIX file (d & "/default.key")
		close a saving no
		set b to my newKeynote()
		set maximum idle duration of b to 123
		save b in POSIX file (d & "/idle.key")
		close b saving no
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
