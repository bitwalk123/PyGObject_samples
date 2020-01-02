import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="チェックボタン")
        self.set_default_size(0, 0)

        vbox = Gtk.VBox()
        self.add(vbox)

        cb1 = Gtk.CheckButton(label="チェックボタンＡ")
        cb1.connect("clicked", self.on_button_toggled, "Ａ")
        vbox.pack_start(cb1, True, True, 0)

        cb2 = Gtk.CheckButton(label="チェックボタンＢ")
        cb2.connect("clicked", self.on_button_toggled, "Ｂ")
        vbox.pack_start(cb2, True, True, 0)

        cb3 = Gtk.CheckButton(label="チェックボタンＣ")
        cb3.connect("clicked", self.on_button_toggled, "Ｃ")
        vbox.pack_start(cb3, True, True, 0)

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "オン"
        else:
            state = "オフ"
        print("チェックボタン" + name + "は「" + state + "」になりました。")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
