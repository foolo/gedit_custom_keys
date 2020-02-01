from gi.repository import GObject, Gedit, Gdk

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

	def do_deactivate(self):
		self.app.set_accels_for_action("win.redo", ())

	def __init__(self):
		GObject.Object.__init__(self)

	def add_keyboard_shortcut(self, action_name, keyboard_shortcut):
		self.app.remove_accelerator(action_name, None)
		self.app.set_accels_for_action(action_name, [keyboard_shortcut])


# https://github.com/baxterross/GEdit3TabSwitch
class GEdit3TabSwitch(GObject.Object, Gedit.WindowActivatable):
    window = GObject.property(type=Gedit.Window)

    KEYS_LEFT = ('ISO_Left_Tab', 'Page_Up')
    KEYS_RIGHT = ('Tab', 'Page_Down')
    KEYS = KEYS_LEFT + KEYS_RIGHT

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        handlers = []
        handler_id = self.window.connect('key-press-event', self.on_key_press_event)
        handlers.append(handler_id)
        self.window.GEdit3TabSwitchHandlers = handlers

    def do_deactivate(self):
        handlers = self.window.GEdit3TabSwitchHandlers
        for handler_id in handlers:
            self.window.disconnect(handler_id)

    def do_update_state(self):
        pass

    def on_key_press_event(self, window, event):
        key = Gdk.keyval_name(event.keyval)
        if event.state & Gdk.ModifierType.CONTROL_MASK and key in self.KEYS:
            atab = window.get_active_tab()
            tabs = atab.get_parent().get_children()
            tlen = len(tabs)
            i = 0
            for tab in tabs:
                i += 1
                if tab == atab:
                    break
            if key in self.KEYS_LEFT:
                i -= 2
            if i < 0:
                tab = tabs[tlen-1]
            elif i >= tlen:
                tab = tabs[0]
            else:
                tab = tabs[i]
            window.set_active_tab(tab)
            return True
