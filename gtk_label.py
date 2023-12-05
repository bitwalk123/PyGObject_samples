#!/usr/bin/env python
# coding: utf-8
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

APPID = 'com.blogspot.bitwalk'


class Example(Gtk.Window):

    def __init__(self, app):
        Gtk.Window.__init__(self, application=app, title='Label')

        lab = Gtk.Label(label='これはラベルです。')
        self.set_child(lab)


class Gtk4TestApp(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_activate(self):
        window = Example(self)
        window.present()


def main():
    app = Gtk4TestApp()
    app.run()


if __name__ == '__main__':
    main()
