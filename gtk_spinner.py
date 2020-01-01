import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="スピナー")
        self.set_default_size(0, 0)
        self.set_border_width(3)
        #self.connect("destroy", Gtk.main_quit)

        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(hbox)

        button = Gtk.ToggleButton("開始")
        button.set_active(False)
        hbox.pack_start(button, True, True, 0)

        spinner = Gtk.Spinner()
        hbox.pack_start(spinner, True, True, 0)

        button.connect("toggled", self.on_button_toggled, spinner)

        #self.table = Gtk.Table(3, 2, True)
        #self.table.attach(self.button, 0, 2, 0, 1)
        #self.table.attach(self.spinner, 0, 2, 2, 3)

        #self.add(self.table)
        #self.show_all()

    def on_button_toggled(self, button, spinner):

        if button.get_active():
            spinner.start()
            button.set_label("停止")

        else:
            spinner.stop()
            button.set_label("Start Spinning")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
