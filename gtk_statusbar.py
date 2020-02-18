import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class MyWindow(Gtk.ApplicationWindow):
    # a window

    def __init__(self, app):
        Gtk.Window.__init__(self, title="StatusBar Example", application=app)
        self.set_default_size(200, 100)

        # a label
        label = Gtk.Label(label="Press any key or ")

        # a button
        button = Gtk.Button(label="click me.")
        # connected to a callback
        button.connect("clicked", self.button_clicked_cb)

        # the statusbar
        self.statusbar = Gtk.Statusbar()
        # its context_id - not shown in the UI but needed to uniquely identify
        # the source of a message
        self.context_id = self.statusbar.get_context_id("example")
        # we push a message onto the statusbar's stack
        self.statusbar.push(
            self.context_id, "Waiting for you to do something...")

        # a grid to attach the widgets
        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
        grid.attach(label, 0, 0, 1, 1)
        grid.attach_next_to(button, label, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach(self.statusbar, 0, 1, 2, 1)

        # add the grid to the window
        self.add(grid)

    # callback function for the button clicked
    # if the button is clicked the event is signaled to the statusbar
    # onto which we push a new status
    def button_clicked_cb(self, button):
        self.statusbar.push(self.context_id, "You clicked the button.")

    # event handler
    def do_key_press_event(self, event):
        # any signal from the keyboard is signaled to the statusbar
        # onto which we push a new status with the symbolic name
        # of the key pressed
        self.statusbar.push(self.context_id, Gdk.keyval_name(event.keyval) +
                            " key was pressed.")
        # stop the signal emission
        return True


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
