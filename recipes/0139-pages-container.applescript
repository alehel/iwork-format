-- Experiments 0139-0145, 0148: save Pages documents that test the container.
-- Usage: osascript recipes/0139-pages-container.applescript mode /absolute/path/out.pages [/absolute/path/input]
-- Modes:
--   resave     open the input document and save it unchanged under a new name
--   editsave   open the input document, change its body text to "changed" and save it in place
--   bigtext    a body of 30000 paragraphs, each "line N"
--   twice      the input image placed twice on page 1
--   image      the input image placed once (for JPEG, odd file names, large images)
--   deleted    the input image placed, then deleted, then the document saved
-- The folder must exist. Pages opens while the recipe runs.

on run argv
	set mode to item 1 of argv
	set outFile to POSIX file (item 2 of argv)
	if (count of argv) > 2 then set img to POSIX file (item 3 of argv)
	tell application "Pages"
		if mode is "resave" then
			set theDoc to open img
			save theDoc in outFile
		else if mode is "editsave" then
			set theDoc to open outFile
			set body text of theDoc to "changed"
			save theDoc
		else
			set theDoc to make new document
			if mode is "bigtext" then
				set lst to {}
				repeat with i from 1 to 30000
					set end of lst to "line " & i
				end repeat
				set AppleScript's text item delimiters to linefeed
				set body text of theDoc to (lst as text)
				set AppleScript's text item delimiters to ""
			else
				set body text of theDoc to "one"
				tell page 1 of theDoc to set i1 to make new image with properties {file:img}
				if mode is "twice" then tell page 1 of theDoc to make new image with properties {file:img}
				if mode is "deleted" then delete i1
			end if
			save theDoc in outFile
		end if
		close theDoc saving no
	end tell
end run
