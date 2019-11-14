from gi.repository import GObject, Gedit

class ExampleAppActivatable(GObject.Object, Gedit.AppActivatable):
	app = GObject.property(type=Gedit.App)
	__gtype_name__ = "CustomKeysAppActivatable"

	def do_activate(self):
		#  Uncomment/Comment any of the keyboard shortcuts below and edit as desired
		# "<Primary>" normally corresponds to Ctrl key
		# Additional action names can be found in https://github.com/GNOME/gedit/blob/mainline/gedit/resources/gtk/menus-common.ui

		self.add_keyboard_shortcut("win.redo", "<Primary>Y")
		self.add_keyboard_shortcut("win.goto-line", "<Primary>G")
		#self.add_keyboard_shortcut("app.new-window", "<Primary>N")
		#self.add_keyboard_shortcut("app.quit", "<Primary>Q")
		#self.add_keyboard_shortcut("app.help", "F1")
		#self.add_keyboard_shortcut("win.hamburger-menu", "F10")
		#self.add_keyboard_shortcut("win.open", "<Primary>O")
		#self.add_keyboard_shortcut("win.save", "<Primary>S")
		#self.add_keyboard_shortcut("win.save-as", "<Primary><Shift>S")
		#self.add_keyboard_shortcut("win.save-all", "<Primary><Shift>L")
		#self.add_keyboard_shortcut("win.new-tab", "<Primary>T")
		#self.add_keyboard_shortcut("win.reopen-closed-tab", "<Primary><Shift>T")
		#self.add_keyboard_shortcut("win.close", "<Primary>W")
		#self.add_keyboard_shortcut("win.close-all", "<Primary><Shift>W")
		#self.add_keyboard_shortcut("win.print", "<Primary>P")
		#self.add_keyboard_shortcut("win.find", "<Primary>F")
		#self.add_keyboard_shortcut("win.find-next", "<Primary>G")
		#self.add_keyboard_shortcut("win.find-prev", "<Primary><Shift>G")
		#self.add_keyboard_shortcut("win.replace", "<Primary>H")
		#self.add_keyboard_shortcut("win.clear-highlight", "<Primary><Shift>K")
		#self.add_keyboard_shortcut("win.focus-active-view", "Escape")
		#self.add_keyboard_shortcut("win.side-panel", "F9")
		#self.add_keyboard_shortcut("win.bottom-panel", "<Primary>F9")
		#self.add_keyboard_shortcut("win.fullscreen", "F11")
		#self.add_keyboard_shortcut("win.new-tab-group", "<Primary><Alt>N")
		#self.add_keyboard_shortcut("win.previous-tab-group", "<Primary><Shift><Alt>Page_Up")
		#self.add_keyboard_shortcut("win.next-tab-group", "<Primary><Shift><Alt>Page_Down")
		#self.add_keyboard_shortcut("win.previous-document", "<Primary><Alt>Page_Up")
		#self.add_keyboard_shortcut("win.next-document", "<Primary><Alt>Page_Down")

	def do_deactivate(self):
		self.app.set_accels_for_action("win.redo", ())

	def __init__(self):
		GObject.Object.__init__(self)

	def add_keyboard_shortcut(self, action_name, keyboard_shortcut):
		self.app.remove_accelerator(action_name, None)
		self.app.set_accels_for_action(action_name, [keyboard_shortcut])

