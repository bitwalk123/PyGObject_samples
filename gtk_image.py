import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="イメージ")
        self.set_default_size(0, 0)

        img_list = [Gtk.STOCK_HOME, Gtk.STOCK_COPY, Gtk.STOCK_CUT, Gtk.STOCK_PASTE, Gtk.STOCK_EDIT]
        box = Gtk.Box()
        for img in img_list:
            image = Gtk.Image.new_from_icon_name(img, Gtk.IconSize.MENU)
            box.pack_start(image, True, True, 0)
        self.add(box)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
