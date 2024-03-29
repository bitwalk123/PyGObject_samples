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
            title='Button'
        )

        but = Gtk.Button(label='クリックして下さい')
        but.connect('clicked', self.on_button_clicked)
        self.set_child(but)

    @staticmethod
    def on_button_clicked(button: Gtk.Button):
        print('ボタン「%s」がクリックされました。' % button.get_label())


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
