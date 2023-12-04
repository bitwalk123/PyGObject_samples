#!/usr/bin/env python
# coding: utf-8
# Reference:
# https://tannipat.blog/2023/09/pythongtk4-gtk-colordialogbutton/
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gdk

APPID = 'com.blogspot.bitwalk'


class Example(Gtk.Window):

    def __init__(self, app):
        Gtk.Window.__init__(
            self, application=app,
            title='ColorDialog',
            # default_width=300,
        )

        color = Gdk.RGBA()
        color.red = 1
        color.green = 0
        color.blue = 0.2
        color.alpha = 1

        colordialog = Gtk.ColorDialog(
            title='Select color', modal=True, with_alpha=False,
        )

        self.colordialogbutton = Gtk.ColorDialogButton(
            rgba=color, dialog=colordialog,
        )

        button = Gtk.Button(
            label='Color Infomration'
        )
        button.connect('clicked', self.on_button_clicked)
        box = Gtk.Box(
            # margin_top=20, margin_bottom=20,
            # margin_start=20, margin_end=20,
            # spacing=20,
        )
        box.append(self.colordialogbutton)
        box.append(button)

        self.set_child(box)

    def on_button_clicked(self, button):
        color = self.colordialogbutton.get_rgba()
        print(f'R={color.red:.3f}, G={color.green:.3f}, B={color.blue:.3f}')


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
