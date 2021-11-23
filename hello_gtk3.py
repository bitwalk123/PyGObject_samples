# Reference
# https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html#simple-example
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Hello(Gtk.Window):
    def __init__(self):
        super().__init__(title='Hello World')

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(box)

        button = Gtk.Button(label='こんにちは、世界！')
        button.connect('clicked', self.on_button_clicked)
        box.pack_start(button, True, True, 0)

    def on_button_clicked(self, widget):
        print('Hello World! (GTK+ %s.%s.%s)' % (Gtk.MAJOR_VERSION, Gtk.MINOR_VERSION, Gtk.MICRO_VERSION))


def main():
    hello = Hello()
    hello.connect("destroy", Gtk.main_quit)
    hello.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
