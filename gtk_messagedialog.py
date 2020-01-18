import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="メッセージダイアログ")
        self.set_default_size(0, 0)

        box = Gtk.HBox(spacing=0)
        self.add(box)

        button1 = Gtk.Button(label="情報 (Information)")
        button1.connect("clicked", self.on_info_clicked)
        box.add(button1)

        button2 = Gtk.Button(label="エラー (Error)")
        button2.connect("clicked", self.on_error_clicked)
        box.add(button2)

        button3 = Gtk.Button(label="警告 (Warning)")
        button3.connect("clicked", self.on_warn_clicked)
        box.add(button3)

        button4 = Gtk.Button(label="質問 (Question)")
        button4.connect("clicked", self.on_question_clicked)
        box.add(button4)

    def on_info_clicked(self, widget):
        dialog = Gtk.MessageDialog(parent=self,
                                   flags=0,
                                   message_type=Gtk.MessageType.INFO,
                                   buttons=Gtk.ButtonsType.OK,
                                   text="メッセージタイプは INFO です。")
        dialog.format_secondary_text("二行目のメッセージ欄です。")
        dialog.run()
        print("INFO ダイアログが閉じられました。")

        dialog.destroy()

    def on_error_clicked(self, widget):
        dialog = Gtk.MessageDialog(parent=self,
                                   flags=0,
                                   message_type=Gtk.MessageType.ERROR,
                                   buttons=Gtk.ButtonsType.CANCEL,
                                   text="メッセージタイプは ERROR です。")
        dialog.format_secondary_text("二行目のメッセージ欄です。")
        dialog.run()
        print("ERROR ダイアログが閉じられました。")

        dialog.destroy()

    def on_warn_clicked(self, widget):
        dialog = Gtk.MessageDialog(parent=self,
                                   flags=0,
                                   message_type=Gtk.MessageType.WARNING,
                                   buttons=Gtk.ButtonsType.OK_CANCEL,
                                   text="メッセージタイプは WARNING です。")
        dialog.format_secondary_text("二行目のメッセージ欄です。")
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("WARN ダイアログが OK ボタンで閉じられました。")
        elif response == Gtk.ResponseType.CANCEL:
            print("WARN ダイアログが CENCEL ボタンで閉じられました。")

        dialog.destroy()

    def on_question_clicked(self, widget):
        dialog = Gtk.MessageDialog(parent=self,
                                   flags=0,
                                   message_type=Gtk.MessageType.QUESTION,
                                   buttons=Gtk.ButtonsType.YES_NO,
                                   text="メッセージタイプは QUESTION です。")
        dialog.format_secondary_text("二行目のメッセージ欄です。")
        response = dialog.run()
        if response == Gtk.ResponseType.YES:
            print("QUESTION ダイアログが YES ボタンで閉じられました。")
        elif response == Gtk.ResponseType.NO:
            print("QUESTION ダイアログが NO ボタンで閉じられました。")

        dialog.destroy()


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
