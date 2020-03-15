import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject


class MyClass(GObject.Object):

    @GObject.Signal(flags=GObject.SignalFlags.RUN_LAST, return_type=bool, arg_types=(object,), accumulator=GObject.signal_accumulator_true_handled)
    def test(self, *args):
        print("Handler", args)

    @GObject.Signal
    def noarg_signal(self):
        print("noarg_signal")


instance = MyClass()


def test_callback(inst, obj):
    print("Handled", inst, obj)
    return True


instance.connect("test", test_callback)

instance.emit("test", object())
instance.emit("noarg_signal")
