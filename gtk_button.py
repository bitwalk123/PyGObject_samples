import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title = "ボタン")

        self.button = Gtk.Button.new_with_label("クリックして下さい。")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked (self, button):
        print("ボタンがクリックされました。")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
