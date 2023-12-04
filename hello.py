#!/usr/bin/env python
# coding: utf-8
# References
# https://www.gtk.org/docs/language-bindings/python
# https://palepoli.skr.jp/wp/2021/05/03/gtk4-python-001/
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class Hello(Gtk.Window):
    def __init__(self, app):
        Gtk.Window.__init__(self, application=app, title="Hello World")
        # Box layout
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(box)
        # Button
        button = Gtk.Button(label='こんにちは、世界！')
        button.connect('clicked', self.on_button_clicked)
        box.append(button)

    def on_button_clicked(self, widget):
        print(
            'Hello World! (GTK %s.%s.%s)' % (
                Gtk.MAJOR_VERSION,
                Gtk.MINOR_VERSION,
                Gtk.MICRO_VERSION
            )
        )


class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(
            self,
            application_id='com.blogspot.bitwalk'
        )

    def do_activate(self):
        win = Hello(self)
        win.present()


def main():
    app = MyApplication()
    app.run()


if __name__ == '__main__':
    main()
