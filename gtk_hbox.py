#!/usr/bin/env python
# coding: utf-8
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

APPID = 'com.blogspot.bitwalk'


class Example(Gtk.Window):

    def __init__(self, app):
        Gtk.Window.__init__(
            self,
            application=app,
            title='Horizontal Box'
        )

        box = Gtk.Box()
        self.set_child(box)

        but1 = Gtk.Button(label='1', hexpand=True)
        box.append(but1)

        but2 = Gtk.Button(label='2', hexpand=True)
        box.append(but2)

        but3 = Gtk.Button(label='3', hexpand=True)
        box.append(but3)


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_activate(self):
        win = Example(self)
        win.present()


def main():
    app = MyApplication()
    app.run()


if __name__ == '__main__':
    main()
