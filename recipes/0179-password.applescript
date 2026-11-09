-- Experiment 0179: save Pages documents with and without a password.
-- Usage: osascript recipes/0179-password.applescript /absolute/folder
-- Writes plain.pages (body "one"), locked.pages (same, password "pw1234", hint "test"),
-- locked2.pages (a second save with the same password) and unlocked.pages (password set, then removed).
-- The folder must exist. Pages opens while the recipe runs.

on run argv
	set d to item 1 of argv
	tell application "Pages"
		repeat with nmRef in {"plain", "locked", "locked2", "unlocked"}
			set nm to contents of nmRef
			set theDoc to make new document
			set body text of theDoc to "one"
			if nm is not "plain" then set password "pw1234" to theDoc hint "test" saving in keychain no
			if nm is "unlocked" then remove password "pw1234" from theDoc
			save theDoc in POSIX file (d & "/" & nm & ".pages")
			close theDoc saving no
		end repeat
	end tell
end run
