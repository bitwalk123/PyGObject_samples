# Reference
# https://www.gtk.org/docs/language-bindings/python
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


def on_activate(app):
    win = Gtk.ApplicationWindow(application=app, title='Hello')
    btn = Gtk.Button(label='こんにちは、世界！')
    btn.connect('clicked', lambda x: win.close())
    win.set_child(btn)
    win.present()


app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)
