-- Experiment 0005: save a document whose body text is several paragraphs.
-- Usage: osascript recipes/0005-paragraphs.applescript /absolute/path/doc.pages separator paragraph...
-- separator is "return" (CR), "linefeed" (LF) or "none". Each further argument is one paragraph,
-- joined with the separator. The folder must exist. Pages opens while the recipe runs.

on run argv
	if (count of argv) < 3 then error "usage: osascript 0005-paragraphs.applescript /absolute/path/doc.pages separator paragraph..."
	set outFile to POSIX file (item 1 of argv)
	set sepName to item 2 of argv
	if sepName is "return" then
		set sep to return
	else if sepName is "linefeed" then
		set sep to linefeed
	else
		set sep to ""
	end if
	set theText to item 3 of argv
	repeat with i from 4 to count of argv
		set theText to theText & sep & item i of argv
	end repeat
	tell application "Pages"
		set theDoc to make new document
		set body text of theDoc to theText
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
