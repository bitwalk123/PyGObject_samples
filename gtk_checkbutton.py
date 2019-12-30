import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="チェックボタン")
        self.set_default_size(0, 0)

        cb = Gtk.CheckButton(label="クリックして下さい")
        cb.connect("clicked", self.on_button_toggled)
        self.add(cb)

    def on_button_toggled(self, button):
        if button.get_active():
            state = "オン"
        else:
            state = "オフ"
        print("チェックボタンは「" + state + "」になりました。")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
