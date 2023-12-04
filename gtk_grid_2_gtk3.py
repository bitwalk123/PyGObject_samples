import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title='Grid 2')
        self.set_default_size(0, 0)

        grid = Gtk.Grid(column_spacing=5)
        self.add(grid)

        y = 0
        for msg in ['あいうえお', 'けこ', 'すせそ']:
            lab = Gtk.Label(label=msg)
            lab.set_hexpand(False)
            lab.set_halign(Gtk.Align.END)
            ent = Gtk.Entry()
            ent.set_hexpand(True)
            ent.set_editable(False)
            ent.set_can_focus(False)
            grid.attach(lab, 0, y, 1, 1)
            grid.attach(ent, 1, y, 1, 1)
            y += 1


win = MyWindow()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()
