#!/usr/bin/env python
# coding: utf-8
# Reference:
# https://tannipat.blog/2023/09/pythongtk4-gtk-fontbutton/
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Pango

APPID = 'com.blogspot.bitwalk'


class Example(Gtk.Window):
    def __init__(self, app):
        Gtk.Window.__init__(
            self,
            application=app,
            title='Font selection',
            # default_width=350,
            # default_height=80
        )

        fontdialog = Gtk.FontDialog(
            title='select font',
            modal=True,
        )

        fontdialogbutton = Gtk.FontDialogButton(
            dialog=fontdialog,
        )
        fontdialogbutton.connect(
            'notify::font-desc',
            self.on_fontdialogbutton_font_changed
        )

        self.set_child(fontdialogbutton)

    def on_fontdialogbutton_font_changed(self, fontdialogbutton, pspec):
        font = fontdialogbutton.get_font_desc()
        print(f'Family:  {font.get_family()}')
        print(f'Style:   {font.get_style()}')
        print(f'Stretch: {font.get_stretch()}')
        print(f'Variant: {font.get_variant()}')
        print(f'Sizde:   {font.get_size() / Pango.SCALE}')


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
