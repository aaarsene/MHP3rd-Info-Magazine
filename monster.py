import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MonsterWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="MHP3rd Info Magazine")
        self.set_default_size(480,360)
        self.show_all()

win = MonsterWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
