import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ラベル")
        self.set_default_size(0, 0)

        box = Gtk.Box()
        icon1 = Gtk.Image.new_from_icon_name(Gtk.STOCK_YES, Gtk.IconSize.MENU)
        box.pack_start(icon1, True, True, 0)
        icon2 = Gtk.Image.new_from_icon_name(Gtk.STOCK_NO, Gtk.IconSize.MENU)
        box.pack_start(icon2, True, True, 0)
        self.add(box)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
