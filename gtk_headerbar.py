#!/usr/bin/env python
# coding: utf-8
# Reference:
# https://tannipat.blog/2023/05/pythongtk4-gtk-headerbar2/
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio

APPID = 'com.blogspot.bitwalk'
APPNAME = 'Gtk.HeaderBar sample'


class Example(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(
            self,
            application=app,
            title='HeaderBar',
            # default_height=300,
            # default_width=450
        )

        action = Gio.SimpleAction.new('button_left_clicked')
        action.connect('activate', self.on_button_left_clicked)
        self.add_action(action)

        action = Gio.SimpleAction.new('button_right_clicked')
        action.connect('activate', self.on_button_right_clicked)
        self.add_action(action)

        headerbar = Gtk.HeaderBar()
        self.set_titlebar(headerbar)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        headerbar.pack_start(box)

        button_left = Gtk.Button.new_from_icon_name('pan-start-symbolic')
        button_left.set_action_name('win.button_left_clicked')
        box.append(button_left)

        button_right = Gtk.Button.new_from_icon_name('pan-end-symbolic')
        button_right.set_action_name('win.button_right_clicked')
        box.append(button_right)

        hamburger_layout = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )
        self.popover = Gtk.Popover(
            position=Gtk.PositionType.BOTTOM,
            child=hamburger_layout
        )
        hamburger_menubutton = Gtk.MenuButton(
            popover=self.popover,
            icon_name='open-menu-symbolic'
        )
        headerbar.pack_end(hamburger_menubutton)

        hamburger_button_about = Gtk.Button(
            action_name='app.about',
            label='このアプリについて',
            has_frame=False,
            receives_default=True
        )
        hamburger_layout.append(hamburger_button_about)


    def on_button_left_clicked(self, action, param):
        print('ボタン pan-start-symbolic が押されました。')

    def on_button_right_clicked(self, action, param):
        print('ボタン pan-end-symbolic が押されました。')


class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)
        self.window = None

    def do_startup(self):
        Gtk.Application.do_startup(self)

        # 'このアプリについて'用のアクション
        action = Gio.SimpleAction.new('about')
        action.connect('activate', self.on_about)
        self.add_action(action)

    def do_activate(self):
        self.window = Example(self)
        self.window.present()

    # アクションaboutの処理
    def on_about(self, action, param):
        # popoverの非表示
        self.window.popover.set_visible(False)

        # Gtk.AboutDialogの設定
        icon = Gtk.Picture.new_for_filename('logo.png').get_paintable()
        dialog = Gtk.AboutDialog(
            modal=True,
            authors=['Fuhito Suguri'],
            comments='AboutDialog のサンプル',
            license_type=Gtk.License.MIT_X11,
            version='1.0.0',
            program_name=APPNAME,
            logo=icon,
        )

        dialog.present()


def main():
    app = MyApplication()
    app.run()


if __name__ == '__main__':
    main()
