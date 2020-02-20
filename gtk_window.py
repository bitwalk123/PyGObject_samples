import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class SubWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="サブ")
        self.set_default_size(0, 0)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(box)

        self.ent = Gtk.Entry()
        self.ent.set_text("ここは入力欄です。")
        self.ent.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "accessories-text-editor")

        but = Gtk.Button(label="閉じる")
        but.connect("clicked", self.on_button_clicked)

        box.pack_start(self.ent, True, True, 0)
        box.pack_start(but, False, False, 0)

    def get_text(self):
        return self.ent.get_text()

    def on_button_clicked(self, widget):
        print("サブウィンドウを閉じます。")
        self.close()


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="メイン")

        button = Gtk.Button(label="このボタンをクリックすると\nサブウィンドウが開きます。")
        button.connect("clicked", self.on_button_clicked)
        self.add(button)

    def on_button_clicked(self, widget):
        print("サブウィンドウを開きます。")

        subwin = SubWindow()
        subwin.set_transient_for(parent=self)
        subwin.set_modal(True)
        subwin.set_deletable(False)
        subwin.connect("destroy", self.get_text_from_child)
        subwin.show_all()

    def get_text_from_child(self, object):
        print("入力されたエントリの文字列：", object.get_text())
        del object


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
