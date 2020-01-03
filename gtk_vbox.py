import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="HBox")
        self.set_default_size(0, 0)

        vbox = Gtk.VBox()
        self.add(vbox)

        but1 = Gtk.Button(label="1")
        vbox.add(but1)

        but2 = Gtk.Button(label="2")
        vbox.add(but2)

        but3 = Gtk.Button(label="3")
        vbox.add(but3)

        but4 = Gtk.Button(label="4")
        vbox.add(but4)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
