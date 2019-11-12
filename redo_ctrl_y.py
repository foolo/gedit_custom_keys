from gi.repository import GObject, Gtk, Gedit, Gio

class ExampleAppActivatable(GObject.Object, Gedit.AppActivatable):
    app = GObject.property(type=Gedit.App)
    window = GObject.property(type=Gedit.Window)
    __gtype_name__ = "RedoCtrlYAppActivatable"

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        self.app.set_accels_for_action("win.redo", ("<Primary>Y", None))

    def do_deactivate(self):
        self.app.set_accels_for_action("win.redo", ())
