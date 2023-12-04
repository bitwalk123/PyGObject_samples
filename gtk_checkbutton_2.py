#!/usr/bin/env python
# coding: utf-8
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class Example(Gtk.Window):
    def __init__(self, app):
        Gtk.Window.__init__(
            self,
            application=app,
            title='チェックボタン (2)'
        )
        # Box layout
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(box)
        #
        group_rb = Gtk.CheckButton()
        #
        rb1 = Gtk.CheckButton(
            label='チェック（ラジオ）ボタンＡ',
            group = group_rb
        )
        rb1.connect(
            'toggled',
            self.on_button_toggled,
            'Ａ'
        )
        box.append(rb1)
        #
        rb2 = Gtk.CheckButton(
            label='チェック（ラジオ）ボタンＢ',
            group = group_rb
        )
        rb2.connect(
            'toggled',
            self.on_button_toggled,
            'Ｂ'
        )
        box.append(rb2)
        #
        rb3 = Gtk.CheckButton(
            label='チェック（ラジオ）ボタンＣ',
            group = group_rb
        )
        rb3.connect(
            'toggled',
            self.on_button_toggled,
            'Ｃ'
        )
        box.append(rb3)

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = 'オン'
        else:
            state = 'オフ'
        print('チェックボタン%sは「%s」になりました。' % (name, state))


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
