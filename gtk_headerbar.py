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

        action = Gio.SimpleAction.new('button1_clicked')
        action.connect('activate', self.on_button1_clicked)
        self.add_action(action)

        action = Gio.SimpleAction.new('button2_clicked')
        action.connect('activate', self.on_button2_clicked)
        self.add_action(action)

        headerbar = Gtk.HeaderBar()
        self.set_titlebar(headerbar)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        button1 = Gtk.Button.new_from_icon_name('pan-start-symbolic')
        button1.set_action_name('win.button1_clicked')
        box.append(button1)

        button2 = Gtk.Button.new_from_icon_name('pan-end-symbolic')
        button2.set_action_name('win.button2_clicked')
        box.append(button2)

        headerbar.pack_start(box)

        # Gtk.HeaderBarに追加するGtk.Popoverに載せるものの作成
        hambuger_menu = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )
        hambager_button = Gtk.Button(
            action_name='app.about',
            label='バージョン情報',
            has_frame=False,
            receives_default=True
        )
        hambuger_menu.append(hambager_button)

        # Gtk.MenuButtonにGtk.Popoverを紐付け
        self.popover = Gtk.Popover(
            position=Gtk.PositionType.BOTTOM,
            child=hambuger_menu
        )

        hamburger_button = Gtk.MenuButton(
            popover=self.popover,
            icon_name='open-menu-symbolic'
        )
        headerbar.pack_end(hamburger_button)

    def on_button1_clicked(self, action, param):
        print('ボタン pan-start-symbolic が押されました。')

    def on_button2_clicked(self, action, param):
        print('ボタン pan-end-symbolic が押されました。')


class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_startup(self):
        Gtk.Application.do_startup(self)

        # 'バージョン情報'用のアクション
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
            authors=['taniyoshima', 'Fuhito Suguri'],
            comments='AboutDialogのサンプル',
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
