import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

APPID = 'com.blogspot.bitwalk'


def print_hello(widget: Gtk.Button):
    print(
        '%s (GTK %s.%s.%s)' % (
            widget.get_label(),
            Gtk.MAJOR_VERSION,
            Gtk.MINOR_VERSION,
            Gtk.MICRO_VERSION
        )
    )


def hello(app):
    win = Gtk.Window(application=app)
    win.set_title('Hello World')
    but = Gtk.Button(label='こんにちは、世界！')
    but.connect('clicked', print_hello)
    win.set_child(but)
    win.present()


app = Gtk.Application(application_id=APPID)
app.connect('activate', hello)
app.run()
