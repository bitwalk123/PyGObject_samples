# reference
# https://stackoverflow.com/questions/54076575/how-to-pass-return-data-from-gtk-dialog-to-main-application-class
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyDialog(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "My Dialog", parent, 0)
        self.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)
        self.add_button(Gtk.STOCK_OK, Gtk.ResponseType.OK)

        self.result = ""
        self.set_default_size(150, 100)
        self.connect("response", self.on_response)

        label = Gtk.Label(label="Type something")
        self.entry = Gtk.Entry()

        box = self.get_content_area()
        box.add(label)
        box.add(self.entry)
        self.show_all()

    def on_response(self, widget, response_id):
        self.result = self.entry.get_text()

    def get_result(self):
        return self.result


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Dialog Example")
        self.set_border_width(6)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box)

        button = Gtk.Button(label="Open dialog")
        button.connect("clicked", self.on_button_clicked)
        box.add(button)

        self.label = Gtk.Label()
        box.add(self.label)

    def on_button_clicked(self, widget):
        dialog = MyDialog(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            self.label.set_text(dialog.get_result())
            print("The OK button was clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("The Cancel button was clicked")

        dialog.destroy()


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
