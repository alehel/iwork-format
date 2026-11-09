-- Experiments 0096-0102: save a Keynote presentation with one object property changed.
-- Usage: osascript recipes/0096-keynote-objects.applescript /absolute/path/doc.key mode [/absolute/path/image.png]
-- Modes:
--   textstyle   a text item "box" whose text is Georgia, 40 points, red
--   rotation    a shape rotated 45 degrees
--   opacity     a shape at 50 percent opacity
--   reflection  the image with a reflection of 40 percent
--   locked      the image locked
--   notitle     slide 1's title hidden
--   description the image with the accessibility description "red bar"
-- The folder must exist. Keynote opens while the recipe runs.

on run argv
	if (count of argv) < 2 then error "usage: osascript 0096-keynote-objects.applescript doc.key mode [image]"
	set outFile to POSIX file (item 1 of argv)
	set mode to item 2 of argv
	tell application "Keynote"
		set theDoc to make new document
		set s to slide 1 of theDoc
		if mode is "textstyle" then
			tell s to set t to make new text item with properties {object text:"box"}
			set font of object text of t to "Georgia"
			set size of object text of t to 40
			set color of object text of t to {65535, 0, 0}
		else if mode is "rotation" then
			tell s to set sh to make new shape
			set rotation of sh to 45
		else if mode is "opacity" then
			tell s to set sh to make new shape
			set opacity of sh to 50
		else
			tell s to set img to make new image with properties {file:POSIX file (item 3 of argv)}
			if mode is "reflection" then
				set reflection showing of img to true
				set reflection value of img to 40
			else if mode is "locked" then
				set locked of img to true
			else if mode is "description" then
				set description of img to "red bar"
			else if mode is "notitle" then
				delete img
				set title showing of s to false
			end if
		end if
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
