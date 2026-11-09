-- Experiments 0055-0057: save a Pages document with body text "one" and an image whose properties are changed.
-- Usage: osascript recipes/0055-pages-image-property.applescript /absolute/path/doc.pages /absolute/path/image.png size|rotation|opacity
-- size sets width 80 and height 40; rotation sets 30 degrees; opacity sets 50 percent.
-- The folder must exist. Pages opens while the recipe runs.

on run argv
	if (count of argv) is not 3 then error "usage: osascript 0055-pages-image-property.applescript doc.pages image.png size|rotation|opacity"
	set outFile to POSIX file (item 1 of argv)
	set imageFile to POSIX file (item 2 of argv)
	set what to item 3 of argv
	tell application "Pages"
		set theDoc to make new document
		set body text of theDoc to "one"
		tell page 1 of theDoc to set img to make new image with properties {file:imageFile}
		if what is "size" then
			set width of img to 80
			set height of img to 40
		else if what is "rotation" then
			set rotation of img to 30
		else if what is "opacity" then
			set opacity of img to 50
		end if
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
