-- Experiment 0197: save Keynote presentations with different maximum idle durations.
-- Usage: osascript recipes/0197-keynote-idle.applescript /absolute/folder
-- Writes default.key (unchanged) and idle.key (maximum idle duration 123 seconds).
-- The folder must exist. Keynote opens while the recipe runs.

on run argv
	set d to item 1 of argv
	tell application "Keynote"
		set a to make new document
		set r to maximum idle duration of a
		save a in POSIX file (d & "/default.key")
		close a saving no
		set b to make new document
		set maximum idle duration of b to 123
		save b in POSIX file (d & "/idle.key")
		close b saving no
		return r
	end tell
end run
