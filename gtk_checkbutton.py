import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="チェックボタン")

        self.cbutton = Gtk.CheckButton(label="クリックして下さい")
        self.cbutton.connect("clicked", self.on_button_toggled)
        self.add(self.cbutton)

    def on_button_toggled(self, button):
        if button.get_active():
            state = "オン"
        else:
            state = "オフ"
        print("トグルボタンは「" + state + "」になりました。")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
