import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title='Icon Button')
        self.set_default_size(0, 0)
        self.set_resizable(False)
        box = Gtk.Box()
        self.add(box)

        list_icon = ['document-open', 'edit-copy', 'edit-cut', 'edit-paste', 'dialog-information', 'application-exit']
        for icon_name in list_icon:
            image = Gtk.Image.new_from_icon_name(icon_name, Gtk.IconSize.BUTTON)
            but = Gtk.Button()
            but.set_image(image)
            box.pack_start(but, True, True, 0)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
