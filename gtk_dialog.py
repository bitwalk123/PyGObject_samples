import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyDialog(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "ダイアログ")
        self.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)
        self.add_button(Gtk.STOCK_OK, Gtk.ResponseType.OK)
        self.set_default_size(0, 0)
        self.set_resizable(False)
        self.set_modal(True)

        msg = Gtk.TextBuffer()
        msg.set_text("このウィンドウは、追加情報を表示するためのダイアログです。")
        tv = Gtk.TextView()
        tv.set_wrap_mode(wrap_mode=Gtk.WrapMode.WORD)
        tv.set_editable(False)
        tv.set_buffer(msg)

        content = self.get_content_area()
        content.add(tv)

        self.show_all()


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="メイン")
        self.set_default_size(0, 0)

        but = Gtk.Button(label="ダイアログを開く")
        but.connect("clicked", self.on_button_clicked)

        self.add(but)

    def on_button_clicked(self, widget):
        dialog = MyDialog(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("「OK」ボタンがクリックされました。")
        elif response == Gtk.ResponseType.CANCEL:
            print("「Cancel」ボタンがクリックされました。")

        dialog.destroy()


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
