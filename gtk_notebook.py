import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ノートブック")
        self.set_default_size(400, 400)

        notebook = Gtk.Notebook()
        self.add(notebook)

        page1 = Gtk.Box()
        lab1 = Gtk.Label(label="文字列がタイトルのページです。")
        page1.add(lab1)
        notebook.append_page(page1, Gtk.Label(label="文字列"))

        page2 = Gtk.Box()
        lab2 = Gtk.Label(label="イメージがタイトルのページです。")
        page2.add(lab2)
        notebook.append_page(
            page2,
            Gtk.Image.new_from_icon_name("help-about", Gtk.IconSize.MENU)
        )


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
