#!/usr/bin/env python
# coding: utf-8
# References
# https://www.gtk.org/docs/language-bindings/python
# https://palepoli.skr.jp/wp/2021/05/03/gtk4-python-001/
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

APPID = 'com.blogspot.bitwalk'


class Hello(Gtk.Window):
    def __init__(self, app):
        Gtk.Window.__init__(self, application=app, title="Hello World")
        # Box layout
        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(layout)
        # Button
        button = Gtk.Button(label='こんにちは、世界！')
        button.connect('clicked', self.on_button_clicked)
        layout.append(button)

    @staticmethod
    def on_button_clicked(widget: Gtk.Button):
        print(
            '%s (GTK %s.%s.%s)' % (
                widget.get_label(),
                Gtk.MAJOR_VERSION,
                Gtk.MINOR_VERSION,
                Gtk.MICRO_VERSION
            )
        )


class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_activate(self):
        win = Hello(self)
        win.present()


def main():
    app = MyApplication()
    app.run()


if __name__ == '__main__':
    main()
