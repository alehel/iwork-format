-- Experiments 0149-0158: save Pages documents that test text and templates.
-- Usage: osascript recipes/0149-pages-text.applescript mode /absolute/path/out.pages
-- Modes:
--   zwj          body "👨‍👩‍👧" and "two" in two paragraphs; paragraph 2 at 20 points
--   rtl          body "مرحبا بالعالم" (Arabic)
--   paras        1000 paragraphs, "p 1" to "p 1000"
--   sizecolour   "one two three"; word 2 at 20 points and red
--   defaultsize  "one two three"; word 2 set to the size it already has
--   replace      "one two three"; word 2 at 20 points; then the body text set to "four five"
--   landscape    a new document from the template "Application/BlankLandscape/ISO"
--   layout       a new document from the template "Application/21_Blank_Layout/ISO"
--   black        a new document from the template "Application/20_Blank_Black/ISO", body "one"
--   essay        a new document from the template "Application/23_Essay/ISO" (unchanged)
-- The folder must exist. Pages opens while the recipe runs.

on run argv
	set mode to item 1 of argv
	set outFile to POSIX file (item 2 of argv)
	tell application "Pages"
		if mode is "landscape" then
			set theDoc to make new document with properties {document template:template id "Application/BlankLandscape/ISO"}
			set body text of theDoc to "one"
		else if mode is "layout" then
			set theDoc to make new document with properties {document template:template id "Application/21_Blank_Layout/ISO"}
		else if mode is "black" then
			set theDoc to make new document with properties {document template:template id "Application/20_Blank_Black/ISO"}
			set body text of theDoc to "one"
		else if mode is "essay" then
			set theDoc to make new document with properties {document template:template id "Application/23_Essay/ISO"}
		else
			set theDoc to make new document
			if mode is "zwj" then
				set body text of theDoc to "👨‍👩‍👧" & linefeed & "two"
				set size of paragraph 2 of body text of theDoc to 20
			else if mode is "rtl" then
				set body text of theDoc to "مرحبا بالعالم"
			else if mode is "paras" then
				set lst to {}
				repeat with i from 1 to 1000
					set end of lst to "p " & i
				end repeat
				set AppleScript's text item delimiters to linefeed
				set body text of theDoc to (lst as text)
				set AppleScript's text item delimiters to ""
			else
				set body text of theDoc to "one two three"
				if mode is "sizecolour" then
					set size of word 2 of body text of theDoc to 20
					set color of word 2 of body text of theDoc to {65535, 0, 0}
				else if mode is "defaultsize" then
					set s to size of word 2 of body text of theDoc
					set size of word 2 of body text of theDoc to s
				else if mode is "replace" then
					set size of word 2 of body text of theDoc to 20
					set body text of theDoc to "four five"
				end if
			end if
		end if
		save theDoc in outFile
		close theDoc saving no
	end tell
end run
