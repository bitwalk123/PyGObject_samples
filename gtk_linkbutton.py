import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="リンクボタン")
        self.set_default_size(0, 0)

        lb = Gtk.LinkButton(uri="https://pygobject.readthedocs.io/", label="PyGObject サイトへ")
        self.add(lb)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
