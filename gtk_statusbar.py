import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ステータスバー")
        self.set_default_size(0, 0)

        lab = Gtk.Label(label="　何かキーを押下、または　")
        but = Gtk.Button(label="ここをクリック")
        but.connect("clicked", self.button_clicked)

        self.status = Gtk.Statusbar()
        self.context_id = self.status.get_context_id("example")
        self.status.push(self.context_id, "何かするのを待っています…")

        grid = Gtk.Grid()
        grid.attach(lab, 0, 0, 1, 1)
        grid.attach_next_to(but, lab, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach(self.status, 0, 1, 2, 1)
        self.add(grid)

    def button_clicked(self, button):
        self.status.push(self.context_id, "ボタンをクリックしました。")

    def do_key_press_event(self, event):
        self.status.push(self.context_id, Gdk.keyval_name(event.keyval) + " キーを押しました。")
        return True


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
