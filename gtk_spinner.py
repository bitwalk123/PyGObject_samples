import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="スピナー")
        self.set_default_size(0, 0)

        hbox = Gtk.HBox()
        self.add(hbox)

        but = Gtk.ToggleButton(label="\n開始\n")
        but.set_active(False)
        hbox.add(but)

        spi = Gtk.Spinner()
        hbox.add(spi)

        but.connect("toggled", self.on_button_toggled, spi)

    def on_button_toggled(self, button, spinner):

        if button.get_active():
            spinner.start()
            button.set_label("\n停止\n")
        else:
            spinner.stop()
            button.set_label("\n開始\n")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
