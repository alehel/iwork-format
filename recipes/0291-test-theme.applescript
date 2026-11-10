-- Experiment 0291: build the project's test theme from Basic White, with every photo in its
-- masters replaced by a test card from recipes/0291-test-cards.swift.
-- Usage: osascript recipes/0291-test-theme.applescript CARDS_DIR OUT.key
-- The masters are those of Keynote 15.4's default theme, Basic White (Enkel, hvit).
on run argv
	set cards to item 1 of argv
	set outPath to item 2 of argv
	-- master number, image number within the master, card
	set plan to {{2, 1, "photo-f.jpg"}, {3, 1, "photo-a.jpg"}, {6, 1, "photo-b.jpg"}, ¬
		{15, 1, "photo-d.jpg"}, {15, 2, "photo-a.jpg"}, {15, 3, "photo-c.jpg"}, {16, 1, "photo-e.jpg"}}
	tell application "Keynote Creator Studio"
		set d to make new document
		if name of document theme of d is not "Enkel, hvit" then error "expected Basic White as the default theme"
		set report to ""
		repeat with p in plan
			set m to master slide (item 1 of p) of d
			set im to image (item 2 of p) of m
			set oldName to file name of im
			set file name of im to (POSIX file (cards & "/" & item 3 of p))
			set report to report & (item 1 of p) & "." & (item 2 of p) & " " & name of m & ": " & oldName & " -> " & (file name of im) & linefeed
		end repeat
		save d in (POSIX file outPath)
		close d saving no
	end tell
	return report
end run
