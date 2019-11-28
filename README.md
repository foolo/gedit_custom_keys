# Installation

Copy `custom_keys.plugin` and `custom_keys.py` to `~/.local/share/gedit/plugins`

Open gedit and navigate to *Preferences > Plugins* and Activate **Custom Keyboard Shortcuts** plugin

# Usage

Add or change keyboard shortcuts by uncommenting and editing lines in `~/.local/share/gedit/plugins/custom_keys.py`

By default, two keyboard shortcut settings are active:

**Ctrl+Y** for **Redo**

**Ctrl+G** for **Go to line**

Known action names:

```
app.help
app.new-window
app.quit
move-to-new-window
win.auto-indent
win.bottom-panel
win.check-spell
win.clear-highlight
win.close
win.close-all
win.copy
win.cut
win.delete
win.display-right-margin
win.find
win.find-next
win.find-prev
win.focus-active-view
win.fullscreen
win.goto-line
win.hamburger-menu
win.highlight-current-line
win.highlight-mode
win.move-to-new-window
win.new-tab
win.new-tab-group
win.next-document
win.next-tab-group
win.open
win.overwrite-mode
win.paste
win.previous-document
win.previous-tab-group
win.print
win.redo
win.reopen-closed-tab
win.replace
win.revert
win.save
win.save-all
win.save-as
win.select-all
win.show-line-numbers
win.side-panel
win.tab-width
win.undo
win.use-spaces
win.wrap-mode
```

# Reference

	https://developer.gnome.org/gtk3/stable/GtkApplication.html
	https://developer.gnome.org/gtk3/stable/gtk3-Keyboard-Accelerators.html
