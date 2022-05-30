# Description

A plugin for Gedit 3.30 and later that adds some common keyboard shortcuts.

# Installation

Copy `custom_keys.plugin` and `custom_keys.py` to `~/.local/share/gedit/plugins` (Create the directory if it does not exist)

Open gedit and navigate to *Preferences > Plugins* and activate **Custom Keyboard Shortcuts** plugin

# Usage

By default, the following additional keyboard shortcuts are active:

**Ctrl+Y** for **Redo**

**Ctrl+E** for **Delete line(s)**

**Ctrl+G** for **Go to line**

**Ctrl+Tab** for **Next document tab**

**Ctrl+Shift+Tab** for **Previous document tab**

# Customizing

Add or change keyboard shortcuts by uncommenting and editing lines in `~/.local/share/gedit/plugins/custom_keys.py`

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

# Notes

Some shortcuts, such as Ctrl+D for delete line are hard-coded in function `gedit_view_class_init` in `gedit-view.c`

Some shortcuts do not work when added with `add_keyboard_shortcut()`. For example, the following unfortunately has no effect:
```
self.add_keyboard_shortcut("win.previous-document", "<Ctrl><Shift>Tab")
self.add_keyboard_shortcut("win.next-document", "<Ctrl>Tab")
```
(There is a special class, GEdit3TabSwitch, which fixes the tab shortcuts instead)


Additional action names can be found by adding the line below in `custom_keys.py` and run gedit from the command line:

	print(self.app.list_action_descriptions())

Additional action names can be found in https://github.com/GNOME/gedit/blob/master/gedit/resources/gtk/menus-common.ui.
