# For more info visit the article https://theawless.github.io/How-to-write-plugins-for-gedit/

# This file needs to be placed like ~/.local/share/gedit/plugins/example/__init__.py
# or renamed like ~/.local/share/gedit/plugins/example.py depending on .plugin file

from gi.repository import GObject, Gtk, Gedit, PeasGtk, Gio


# For our example application, this class is not exactly required.
# But we had to make it because we needed the app menu extension to show the menu.
class ExampleAppActivatable(GObject.Object, Gedit.AppActivatable):
    app = GObject.property(type=Gedit.App)
    __gtype_name__ = "ExampleAppActivatable"

    def __init__(self):
        GObject.Object.__init__(self)
        self.menu_ext = None
        self.menu_item = None

    def do_activate(self):
        self._build_menu()

    def _build_menu(self):
        # Get the extension from tools menu        
        self.menu_ext = self.extend_menu("tools-section")
        # This is the submenu which is added to a menu item and then inserted in tools menu.        
        sub_menu = Gio.Menu()
        sub_menu_item = Gio.MenuItem.new("Clear Document", 'win.clear_document')
        sub_menu.append_item(sub_menu_item)
        self.menu_item = Gio.MenuItem.new_submenu("Example", sub_menu)
        self.menu_ext.append_menu_item(self.menu_item)
        # Setting accelerators, now our action is called when Ctrl+Alt+1 is pressed.
        self.app.set_accels_for_action("win.clear_document", ("<Primary><Alt>1", None))

    def do_deactivate(self):
        self._remove_menu()

    def _remove_menu(self):
        # removing accelerator and destroying menu items
        self.app.set_accels_for_action("win.dictonator_start", ())
        self.menu_ext = None
        self.menu_item = None


class ExampleWindowActivatable(GObject.Object, Gedit.WindowActivatable, PeasGtk.Configurable):
    window = GObject.property(type=Gedit.Window)
    __gtype_name__ = "ExampleWindowActivatable"

    def __init__(self):
        GObject.Object.__init__(self)
        # This is the attachment we will make to bottom panel.
        self.bottom_bar = Gtk.Box()
    
    #this is called every time the gui is updated
    def do_update_state(self):
        # if there is no document in sight, we disable the action, so we don't get NoneException
        if self.window.get_active_view() is not None:
            self.window.lookup_action('clear_document').set_enabled(true)

    def do_activate(self):
        # Defining the action which was set earlier in AppActivatable.
        self._connect_menu()
        self._insert_bottom_panel()

    def _connect_menu(self):
        action = Gio.SimpleAction(name='clear_document')
        action.connect('activate', self.action_cb)
        self.window.add_action(action)

    def action_cb(self, action, data):
        # On action clear the document.
        doc = self.window.get_active_document()
        doc.set_text("")

    def _insert_bottom_panel(self):
        # Add elements to panel.
        self.bottom_bar.add(Gtk.Label("Hello There!"))
        # Get bottom bar (A Gtk.Stack) and add our bar.        
        panel = self.window.get_bottom_panel()
        panel.add_titled(self.bottom_bar, 'example', "Example")
        # Make sure everything shows up.
        panel.show()
        self.bottom_bar.show_all()
        panel.set_visible_child(self.bottom_bar)

    def do_deactivate(self):
        self._remove_bottom_panel()

    def _remove_bottom_panel(self):
        panel = self.window.get_bottom_panel()
        panel.remove(self.bottom_bar)

    def do_create_configure_widget(self):
        # Just return your box, PeasGtk will automatically pack it into a box and show it.
        box=Gtk.Box()
        box.add(Gtk.Label("Settings Here!"))
        return box
