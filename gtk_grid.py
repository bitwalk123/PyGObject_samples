import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Grid")
        self.set_default_size(0, 0)

        grid = Gtk.Grid()
        self.add(grid)

        but0 = Gtk.Button(label="0")
        but1 = Gtk.Button(label="1")
        but2 = Gtk.Button(label="2")
        but3 = Gtk.Button(label="3")
        but4 = Gtk.Button(label="4")
        but5 = Gtk.Button(label="5")
        but6 = Gtk.Button(label="6")
        but7 = Gtk.Button(label="7")
        but8 = Gtk.Button(label="8")
        but9 = Gtk.Button(label="9")

        grid.attach(but0, 0, 0, 1, 1)
        grid.attach(but1, 1, 0, 1, 1)
        grid.attach(but2, 2, 0, 1, 1)
        grid.attach(but3, 3, 0, 1, 1)

        grid.attach(but4, 0, 1, 1, 1)
        grid.attach(but5, 1, 1, 1, 1)
        grid.attach(but6, 2, 1, 1, 1)
        grid.attach(but7, 3, 1, 1, 2)

        grid.attach(but8, 0, 2, 2, 1)
        grid.attach(but9, 2, 2, 1, 1)


win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
