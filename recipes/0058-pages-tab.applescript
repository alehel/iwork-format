-- Experiment 0058: save a Pages document whose body text holds a tab and a non-breaking space: "a<TAB>b<NBSP>c".
-- Usage: osascript recipes/0058-pages-tab.applescript /absolute/path/doc.pages
-- The folder must exist. Pages opens while the recipe runs.

on run argv
	if (count of argv) is not 1 then error "usage: osascript 0058-pages-tab.applescript /absolute/path/doc.pages"
	set outFile to POSIX file (item 1 of argv)
	tell application "Pages"
		set theDoc to make new document
		set body text of theDoc to "a" & tab & "b" & (character id 160) & "c"
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
