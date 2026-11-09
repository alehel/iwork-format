-- Experiments 0244-0245: make a Pages document with the body text "One" and the 8 x 4 red PNG from
-- experiment 0023 on page 1, at (300, 300) and 200 x 100 points. The new image is left selected and the
-- document open and unsaved.
-- Usage: osascript recipes/0244-pages-image.applescript /absolute/path/image.png

on run argv
	tell application "Pages"
		set d to make new document
		set body text of d to "One"
		tell page 1 of d to make new image with properties {file:POSIX file (item 1 of argv), position:{300, 300}, width:200, height:100}
		return name of d
	end tell
end run
