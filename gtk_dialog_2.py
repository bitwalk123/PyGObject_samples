# reference
# https://stackoverflow.com/questions/54076575/how-to-pass-return-data-from-gtk-dialog-to-main-application-class
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyDialog(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, title="ダイアログ", parent=parent, flags=0)
        self.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)
        self.add_button(Gtk.STOCK_OK, Gtk.ResponseType.OK)

        self.result = ""
        self.set_default_size(300, 100)
        self.connect("response", self.on_response)
        box = self.get_content_area()

        lab = Gtk.Label(label="何か入力してください。")
        box.pack_start(lab, True, True, 0)

        self.ent = Gtk.Entry()
        box.pack_start(self.ent, True, True, 0)

        self.show_all()

    def on_response(self, widget, response_id):
        self.result = self.ent.get_text()

    def get_result(self):
        return self.result


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="メイン")

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box)

        but = Gtk.Button(label="ダイアログを開く")
        but.connect("clicked", self.on_button_clicked)
        box.pack_start(but, True, True, 0)

        self.lab = Gtk.Label()
        box.pack_start(self.lab, True, True, 0)

    def on_button_clicked(self, widget):
        dialog = MyDialog(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("OK ボタンがクリックされました。")
            self.lab.set_text(dialog.get_result())
            print(dialog.get_result())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel ボタンがクリックされました。")

        dialog.destroy()


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
