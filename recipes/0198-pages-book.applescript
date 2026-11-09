-- Experiment 0198: save a Pages document made from the blank portrait book template.
-- Usage: osascript recipes/0198-pages-book.applescript /absolute/path/out.pages
-- The folder must exist. Pages opens while the recipe runs.

on run argv
	set outFile to POSIX file (item 1 of argv)
	tell application "Pages"
		set theDoc to make new document with properties {document template:template id "Application/00B_Blank_Portrait/ISO"}
		set body text of theDoc to "one"
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
