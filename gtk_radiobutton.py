import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ラジオボタン")
        self.set_default_size(0, 0)

        vbox = Gtk.VBox()
        self.add(vbox)

        rb1 = Gtk.RadioButton.new_with_label_from_widget(None, "ラジオボタンＡ")
        rb1.connect("toggled", self.on_button_toggled, "Ａ")
        vbox.add(rb1)

        rb2 = Gtk.RadioButton.new_with_mnemonic_from_widget(rb1, "ラジオボタンＢ")
        rb2.connect("toggled", self.on_button_toggled, "Ｂ")
        vbox.add(rb2)

        rb3 = Gtk.RadioButton.new_with_mnemonic_from_widget(rb1, "ラジオボタンＣ")
        rb3.connect("toggled", self.on_button_toggled, "Ｃ")
        vbox.add(rb3)

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "オン"
        else:
            state = "オフ"
        print("ラジオボタン" + name + "が「" + state + "」になりました。")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
