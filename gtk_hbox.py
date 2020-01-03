import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="HBox")
        self.set_default_size(0, 0)

        hbox = Gtk.HBox()
        self.add(hbox)

        but1 = Gtk.Button(label="1")
        hbox.add(but1)

        but2 = Gtk.Button(label="2")
        hbox.add(but2)

        but3 = Gtk.Button(label="3")
        hbox.add(but3)

        but4 = Gtk.Button(label="4")
        hbox.add(but4)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
