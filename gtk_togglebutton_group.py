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
            title='ToggleButton'
        )

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(box)

        group_toggle = Gtk.ToggleButton()

        cb1 = Gtk.ToggleButton(
            label='トグルボタンＡ',
            group=group_toggle
        )
        cb1.connect('toggled', self.on_button_toggled, 'Ａ')
        box.append(cb1)

        cb2 = Gtk.ToggleButton(
            label='トグルボタンＢ',
            group=group_toggle
        )
        cb2.connect('toggled', self.on_button_toggled, 'Ｂ')
        box.append(cb2)

        cb3 = Gtk.ToggleButton(
            label='トグルボタンＣ',
            group=group_toggle
        )
        cb3.connect('toggled', self.on_button_toggled, 'Ｃ')
        box.append(cb3)

    @staticmethod
    def on_button_toggled(button, name):
        if button.get_active():
            state = 'オン'
        else:
            state = 'オフ'
        print('トグルボタン%sは「%s」になりました。' % (name, state))


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