import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="テキストビュー")
        self.set_default_size(200, 200)

        tv = Gtk.TextView()
        tv.set_wrap_mode(wrap_mode=Gtk.WrapMode.WORD)
        self.add(tv)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
