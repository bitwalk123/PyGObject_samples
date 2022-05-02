#!/usr/bin/env python
# coding: utf-8
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class Example(Gtk.Window):
    def __init__(self, app):
        Gtk.Window.__init__(self, application=app, title="リンクボタン")
        # LinkButton
        lb = Gtk.LinkButton(uri="https://pygobject.readthedocs.io/", label="PyGObject サイトへ")
        self.set_child(lb)


class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id='com.blogspot.bitwalk')

    def do_activate(self):
        win = Example(self)
        win.present()


def main():
    app = MyApplication()
    app.run()


if __name__ == '__main__':
    main()
