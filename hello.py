#!/usr/bin/env python
# coding: utf-8
# References
# https://www.gtk.org/docs/language-bindings/python
# https://palepoli.skr.jp/wp/2021/05/03/gtk4-python-001/
import gi

gi.require_version('Gtk', '4.0')
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


class Hello(Gtk.Window):
    def __init__(self, app):
        Gtk.Window.__init__(
            self,
            application=app,
            title='Hello World'
        )

        but = Gtk.Button(label='こんにちは、世界！')
        but.connect('clicked', print_hello)
        self.set_child(but)


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
