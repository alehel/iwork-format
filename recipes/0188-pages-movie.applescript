-- Experiment 0188: save a Pages document with a movie on page 1, and a Numbers spreadsheet with a sound on sheet 1.
-- Usage: osascript recipes/0188-pages-movie.applescript /absolute/folder /absolute/path/clip.mov /absolute/path/tone.m4a
-- As in Keynote (0185), "make new image" with a media file adds a movie or sound.
-- The folder must exist. Pages and Numbers open while the recipe runs.

on run argv
	set d to item 1 of argv
	set mov to POSIX file (item 2 of argv)
	set snd to POSIX file (item 3 of argv)
	tell application "Pages"
		set theDoc to make new document
		set body text of theDoc to "one"
		tell page 1 of theDoc to make new image with properties {file:mov}
		save theDoc in POSIX file (d & "/movie.pages")
		close theDoc saving no
	end tell
	tell application "Numbers"
		set theDoc to make new document
		tell sheet 1 of theDoc to make new image with properties {file:snd}
		save theDoc in POSIX file (d & "/sound.numbers")
		close theDoc saving no
	end tell
end run
