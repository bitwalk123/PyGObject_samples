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
            title='SpinButton'
        )

        adjuster = Gtk.Adjustment(
            value=0,
            lower=0,
            upper=100,
            step_increment=1,
            page_increment=10,
            page_size=0
        )
        sb = Gtk.SpinButton(adjustment=adjuster, xalign=1.0)
        sb.connect('value-changed', self.on_value_changed)
        self.set_child(sb)

    @staticmethod
    def on_value_changed(spinbutton: Gtk.SpinButton):
        print("値が {0} に変わりました。".format(
            str(spinbutton.get_value_as_int()))
        )


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
