import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="エントリ")
        self.set_default_size(0, 0)

        ent = Gtk.Entry()
        ent.set_text("ここは入力欄です。")
        ent.set_max_length(32)
        ent.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "accessories-text-editor")
        ent.connect("activate", self.on_entry_activate)
        self.add(ent)

    def on_entry_activate(self, entry):
        print(entry.get_text())


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
