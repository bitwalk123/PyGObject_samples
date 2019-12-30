import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="スイッチ")
        self.set_default_size(0, 0)

        hbox = Gtk.Box()
        self.add(hbox)

        sw = Gtk.Switch()
        sw.connect("notify::active", self.on_switch_activated)
        hbox.pack_end(sw, False, True, 0)

    def on_switch_activated(self, switch, gparam):
        if switch.get_active():
            state = "オン"
        else:
            state = "オフ"
        print(f"スイッチが「{state}」になりました。")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
