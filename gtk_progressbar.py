import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="プログレスバー")
        self.set_default_size(0, 0)
        self.set_border_width(10)

        pbar = Gtk.ProgressBar()
        self.add(pbar)

        self.timeout_id = GLib.timeout_add(50, self.on_timeout, pbar)
        self.activity_mode = False

    def on_timeout(self, progressbar):
        if self.activity_mode:
            progressbar.pulse()
        else:
            new_value = progressbar.get_fraction() + 0.01

            if new_value > 1:
                new_value = 0

            progressbar.set_fraction(new_value)

        return True


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
