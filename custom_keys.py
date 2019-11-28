from gi.repository import GObject, Gedit

class ExampleAppActivatable(GObject.Object, Gedit.AppActivatable):
	app = GObject.property(type=Gedit.App)
	__gtype_name__ = "CustomKeysAppActivatable"

	def do_activate(self):
		#  Uncomment/comment any of the example keyboard shortcuts below and edit as desired
		# "<Primary>" normally corresponds to Ctrl key
		# See README.md for a list of known action names

		self.add_keyboard_shortcut("win.redo", "<Primary>Y")
		self.add_keyboard_shortcut("win.goto-line", "<Primary>G")
		#Examples:
		#self.add_keyboard_shortcut("app.new-window", "<Primary>N")
		#self.add_keyboard_shortcut("app.help", "F1")
		#self.add_keyboard_shortcut("win.save-as", "<Primary><Shift>S")
		#self.add_keyboard_shortcut("win.reopen-closed-tab", "<Primary><Shift>T")
		#self.add_keyboard_shortcut("win.focus-active-view", "Escape")
		#self.add_keyboard_shortcut("win.bottom-panel", "<Primary>F9")
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

