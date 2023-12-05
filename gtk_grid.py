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
            title='Grid'
        )

        grid = Gtk.Grid()
        self.set_child(grid)

        but0 = Gtk.Button(label='0')
        but1 = Gtk.Button(label='1')
        but2 = Gtk.Button(label='2')
        but3 = Gtk.Button(label='3')
        but4 = Gtk.Button(label='4')
        but5 = Gtk.Button(label='5')
        but6 = Gtk.Button(label='6')
        but7 = Gtk.Button(label='7')
        but8 = Gtk.Button(label='8')
        but9 = Gtk.Button(label='9')

        grid.attach(but0, 0, 0, 1, 1)
        grid.attach(but1, 1, 0, 1, 1)
        grid.attach(but2, 2, 0, 1, 1)
        grid.attach(but3, 3, 0, 1, 1)

        grid.attach(but4, 0, 1, 1, 1)
        grid.attach(but5, 1, 1, 1, 1)
        grid.attach(but6, 2, 1, 1, 1)
        grid.attach(but7, 3, 1, 1, 2)

        grid.attach(but8, 0, 2, 2, 1)
        grid.attach(but9, 2, 2, 1, 1)


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
