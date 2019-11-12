from gi.repository import GObject, Gedit

class ExampleAppActivatable(GObject.Object, Gedit.AppActivatable):
    app = GObject.property(type=Gedit.App)
    __gtype_name__ = "RedoCtrlYAppActivatable"

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        self.app.set_accels_for_action("win.redo", ("<Primary>Y", None))

    def do_deactivate(self):
        self.app.set_accels_for_action("win.redo", ())
