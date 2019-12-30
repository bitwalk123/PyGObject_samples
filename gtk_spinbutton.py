import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ボタン")
        self.set_default_size(0, 0)

        sb = Gtk.SpinButton()
        adjustment = Gtk.Adjustment(value=0, lower=0, upper=100, step_increment=1, page_increment=10, page_size=0)
        sb.set_adjustment(adjustment)
        sb.set_alignment(xalign=1.0)
        sb.connect("value-changed", self.on_value_changed)
        self.add(sb)

    def on_value_changed(self, button):
        print("値が {0} に変わりました。".format(str(button.get_value_as_int())))


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
