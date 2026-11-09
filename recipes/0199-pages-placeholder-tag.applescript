-- Experiment 0199: save a document from the Classic Letter template and list its placeholders' tags.
-- Usage: osascript recipes/0199-pages-placeholder-tag.applescript /absolute/folder
-- Writes letter.pages, unchanged. Setting a placeholder's tag fails with error -10000, so the recipe only reads them.
-- Returns each placeholder's tag. The folder must exist. Pages opens while the recipe runs.

on run argv
	set d to item 1 of argv
	tell application "Pages"
		set t to template id "Application/23_Classic_Letter/ISO"
		set a to make new document with properties {document template:t}
		set r to {}
		repeat with i from 1 to count of placeholder texts of a
			try
				set end of r to tag of placeholder text i of a
			on error
				set end of r to "(no tag)"
			end try
		end repeat
		save a in POSIX file (d & "/letter.pages")
		close a saving no
		return r
	end tell
end run
