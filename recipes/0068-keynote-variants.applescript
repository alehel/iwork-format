-- Experiments 0068-0075: save a Keynote presentation with one change to a new presentation.
-- Usage: osascript recipes/0068-keynote-variants.applescript /absolute/path/doc.key mode [/absolute/path/image.png]
-- Modes:
--   textbox      a text item reading "box" on slide 1
--   image        the given image on slide 1
--   skipped      slide 1 skipped
--   transition   slide 1's transition set to dissolve, 2 seconds
--   bullets      a "Title & Bullets" slide whose body is "one", "two" (indented) and "three"
--   table        a 3 x 3 table on slide 1
--   slidenumbers slide numbers shown (a document setting)
--   size         the presentation's size set to 1024 x 768
-- The folder must exist. Keynote opens while the recipe runs.

on run argv
	if (count of argv) < 2 then error "usage: osascript 0068-keynote-variants.applescript doc.key mode [image]"
	set outFile to POSIX file (item 1 of argv)
	set mode to item 2 of argv
	tell application "Keynote"
		set theDoc to make new document
		set s to slide 1 of theDoc
		if mode is "textbox" then
			tell s to make new text item with properties {object text:"box"}
		else if mode is "image" then
			tell s to make new image with properties {file:POSIX file (item 3 of argv)}
		else if mode is "skipped" then
			set skipped of s to true
		else if mode is "transition" then
			set transition properties of s to {transition effect:dissolve, transition duration:2.0}
		else if mode is "bullets" then
			set base slide of s to master slide "Tittel og punkttegn" of theDoc
			set object text of default body item of s to "one" & return & tab & "two" & return & "three"
		else if mode is "table" then
			tell s to make new table with properties {row count:3, column count:3}
		else if mode is "slidenumbers" then
			set slide numbers showing of theDoc to true
		else if mode is "size" then
			set width of theDoc to 1024
			set height of theDoc to 768
		end if
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
