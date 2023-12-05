#!/usr/bin/env python
# coding: utf-8
# References
# https://www.gtk.org/docs/language-bindings/python
# https://palepoli.skr.jp/wp/2021/05/03/gtk4-python-001/
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

APPID = 'com.blogspot.bitwalk'


class Example(Gtk.Window):

    def __init__(self, app):
        Gtk.Window.__init__(
            self,
            application=app,
            title='Entry'
        )

        ent = Gtk.Entry(
            primary_icon_name='accessories-text-editor',
            placeholder_text='ここは入力欄です。',
            max_length=32,
        )
        ent.connect('activate', self.on_entry_returned)
        self.set_child(ent)

    def on_entry_returned(self, entry: Gtk.Entry):
        print(entry.get_text())


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
