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
            title='TextView',
            width_request=200,
            height_request=200,
        )

        tv = Gtk.TextView()
        tv.set_wrap_mode(wrap_mode=Gtk.WrapMode.WORD)

        scr = Gtk.ScrolledWindow(child=tv)
        self.set_child(scr)


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
