import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Horizontal Box")
        self.set_default_size(0, 0)

        box = Gtk.Box()
        self.add(box)

        but1 = Gtk.Button(label="1")
        box.pack_start(but1, True, True, 0)

        but2 = Gtk.Button(label="2")
        box.pack_start(but2, True, True, 0)

        but3 = Gtk.Button(label="3")
        box.pack_start(but3, True, True, 0)

        but4 = Gtk.Button(label="4")
        box.pack_start(but4, True, True, 0)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
