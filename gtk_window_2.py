import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ChildWindow(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title="サブ")
        self.set_transient_for(parent=parent)
        self.set_modal(True)
        self.set_deletable(False)
        self.connect("destroy", Gtk.Widget.destroy)

        button = Gtk.Button(label="このボタンをクリックするとウィンドウを閉じます。")
        button.connect("clicked", self.on_button_clicked)
        self.add(button)

    def on_button_clicked(self, widget):
        print("ウィンドウを閉じます。")
        self.close()

    def run(self):
        self.show_all()


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="メイン")

        button = Gtk.Button(label="このボタンをクリックすると、子ウィンドウが開きます。")
        button.connect("clicked", self.on_button_clicked)
        self.add(button)

    def on_button_clicked(self, widget):
        print("クリックされました。")

        child = ChildWindow(self)
        child.run()

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
