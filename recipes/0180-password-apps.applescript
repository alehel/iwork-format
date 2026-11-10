-- Experiment 0180: password-protected documents in Keynote and Numbers, a non-ASCII password, and an image.
-- Usage: osascript recipes/0180-password-apps.applescript /absolute/folder /absolute/path/image.png
-- Writes locked.key (password "pw1234"), locked.numbers (password "pw1234"),
-- accent.pages (password "påss", body "one") and image.pages (password "pw1234", body "one", one image).
-- The folder must exist. The apps open while the recipe runs.

on run argv
	set d to item 1 of argv
	set img to POSIX file (item 2 of argv)
	tell application "Keynote"
		set k to my newKeynote()
		set password "pw1234" to k hint "test" saving in keychain no
		save k in POSIX file (d & "/locked.key")
		close k saving no
	end tell
	tell application "Numbers"
		set n to make new document
		set password "pw1234" to n hint "test" saving in keychain no
		save n in POSIX file (d & "/locked.numbers")
		close n saving no
	end tell
	tell application "Pages"
		set a to make new document
		set body text of a to "one"
		set password "påss" to a hint "test" saving in keychain no
		save a in POSIX file (d & "/accent.pages")
		close a saving no
		set b to make new document
		set body text of b to "one"
		tell page 1 of b to make new image with properties {file:img}
		set password "pw1234" to b hint "test" saving in keychain no
		save b in POSIX file (d & "/image.pages")
		close b saving no
	end tell
end run

-- A new Keynote presentation in the theme named in IWORK_KEYNOTE_THEME, such as
-- "iwork-format test" (experiment 0291), or in Keynote's default theme when it is unset.
on newKeynote()
	set t to system attribute "IWORK_KEYNOTE_THEME"
	tell application "Keynote"
		if t is "" then return make new document
		return make new document with properties {document theme:theme t}
	end tell
end newKeynote
