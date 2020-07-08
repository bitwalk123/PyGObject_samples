import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ヘッダーバー")
        self.set_border_width(10)
        self.set_default_size(400, 200)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "ヘッダーバー"
        self.set_titlebar(hb)

        but1 = Gtk.Button(label="1")
        hb.pack_start(but1)

        but2 = Gtk.Button(label="2")
        hb.pack_start(but2)

        but3 = Gtk.Button(label="3")
        hb.pack_start(but3)

        but4 = Gtk.Button(label="4")
        hb.pack_start(but4)

        but5 = Gtk.Button(label="5")
        hb.pack_start(but5)

        but6 = Gtk.Button(label="6")
        hb.pack_start(but6)

        but7 = Gtk.Button(label="7")
        hb.pack_start(but7)

        but8 = Gtk.Button(label="8")
        hb.pack_start(but8)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
