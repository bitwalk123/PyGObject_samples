import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

win = Gtk.Window(title="こんにちは、世界！")
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
