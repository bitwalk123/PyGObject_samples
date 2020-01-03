import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="トグルボタン")
        self.set_default_size(0, 0)

        vbox = Gtk.VBox()
        self.add(vbox)

        tb1 = Gtk.ToggleButton(label="トグルボタンＡ")
        tb1.connect("clicked", self.on_button_toggled, "Ａ")
        vbox.add(tb1)

        tb2 = Gtk.ToggleButton(label="トグルボタンＢ")
        tb2.connect("clicked", self.on_button_toggled, "Ｂ")
        vbox.add(tb2)

        tb3 = Gtk.ToggleButton(label="トグルボタンＣ")
        tb3.connect("clicked", self.on_button_toggled, "Ｃ")
        vbox.add(tb3)

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "オン"
        else:
            state = "オフ"
        print("トグルボタン" + name + "は「" + state + "」になりました。")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
