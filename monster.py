import gi
from database import MHP3DB

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MonsterInfoWindow(Gtk.Window):
    def __init__(self, monster):
        Gtk.Window.__init__(self, title="MHP3rd Info Magazine")
        self.set_default_size(480, 360)
        self.db = MHP3DB('mhp3rd.db')
        self.damage_table = self.db.get_damages(monster)

        self.liststore = Gtk.ListStore(str, int, int, int, int,
                                       int, int, int, int)

        for body_part in self.damage_table:
            self.liststore.append(body_part)

        treeview = Gtk.TreeView(model=self.liststore)

        renderer_text = Gtk.CellRendererText()
        colum_part = Gtk.TreeViewColumn("Body Part", renderer_text, text=0)
        treeview.append_column(colum_part)

        damage_types = self.db.get_damage_type()
        columns = []
        renderer_columns = []
        for damage_type in damage_types:
            renderer_columns.append(Gtk.CellRendererText())
            columns.append(Gtk.TreeViewColumn(damage_type[0],
                           renderer_columns[-1],
                           text=damage_types.index(damage_type) + 1))

            treeview.append_column(columns[-1])

        self.add(treeview)


class MonstersWindow(Gtk.Window):
    def __init__(self, monsters):
        Gtk.Window.__init__(self, title="MHP3rd Info Magazine")
        self.set_default_size(480, 360)
        self.liststore = Gtk.ListStore(int, str)
        for monster in monsters:
            self.liststore.append(monster)

        treeview = Gtk.TreeView(model=self.liststore)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("#", renderer_text, text=0)
        treeview.append_column(column_text)

        renderer_editabletext = Gtk.CellRendererText()
        column_editabletext = Gtk.TreeViewColumn("Name",
                                                 renderer_editabletext, text=1)
        treeview.append_column(column_editabletext)

        self.add(treeview)


if __name__ == '__main__':
    win = MonsterInfoWindow(1)
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
