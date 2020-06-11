import gi
import os
import pathlib

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class file_chooser():
    basedir = ''

    @classmethod
    def get(cls, parent):
        dialog = Gtk.FileChooserDialog(
            title='ファイルの選択',
            parent=parent,
            action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(Gtk.STOCK_CANCEL,
                           Gtk.ResponseType.CANCEL,
                           Gtk.STOCK_OPEN,
                           Gtk.ResponseType.OK)
        # specify basedir to open in the dialog
        if os.path.exists(cls.basedir):
            dialog.set_current_folder(str(cls.basedir))

        cls.add_filters(cls, dialog)
        response = dialog.run()
        filename = dialog.get_filename()
        dialog.destroy()

        if response == Gtk.ResponseType.OK:
            # update basedir
            p = pathlib.Path(filename)
            cls.basedir = os.path.dirname(p)
            return filename
        elif response == Gtk.ResponseType.CANCEL:
            return ''

    def add_filters(self, dialog):
        filter_any = Gtk.FileFilter()
        filter_any.set_name("全てのファイル")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="ファイル選択用ダイアログ")
        self.set_default_size(400, 0)

        box = Gtk.Box()
        self.add(box)

        but = Gtk.Button(label="ファイル選択")
        but.connect("clicked", self.on_file_clicked)
        box.add(but)

    def on_file_clicked(self, widget):
        filename = file_chooser.get(parent=self)
        if len(filename) > 0:
            print("ファイル「" + filename + "」が選択されました。")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
