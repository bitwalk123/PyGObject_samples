import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


# a Gtk ApplicationWindow


class MyWindow(Gtk.ApplicationWindow):
    # constructor: the title is "Welcome to GNOME" and the window belongs
    # to the application app

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Welcome to GNOME", application=app)


class MyApplication(Gtk.Application):
    # constructor of the Gtk Application

    def __init__(self):
        Gtk.Application.__init__(self)

    # create and activate a MyWindow, with self (the MyApplication) as
    # application the window belongs to.
    # Note that the function in C activate() becomes do_activate() in Python
    def do_activate(self):
        win = MyWindow(self)
        # show the window and all its content
        # this line could go in the constructor of MyWindow as well
        win.show_all()

    # start up the application
    # Note that the function in C startup() becomes do_startup() in Python
    def do_startup(self):
        Gtk.Application.do_startup(self)


# create and run the application, exit with the value returned by
# running the program
app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
