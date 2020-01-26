import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="TEST")

        # List
        self.store = Gtk.ListStore(str, str, str)
        self.store.append(['https://www.youtube.com/watch?v=dQw4w9WgXcQ',  # URL
                           'Rick Astley - Never Gonna Give You Up',  # Title
                           'edit-delete'])  # Action icon
        tree = Gtk.TreeView(model=self.store)
        tree.set_size_request(600, 400)
        self.add(tree)

        # Editable URL
        url = Gtk.CellRendererText()
        url.set_property("editable", True)
        column_url = Gtk.TreeViewColumn("YouTube URL", url, text=0)
        column_url.set_min_width(300)
        tree.append_column(column_url)

        # Title
        title = Gtk.CellRendererText()
        column_title = Gtk.TreeViewColumn("Title", title, text=1)
        tree.append_column(column_title)

        # Action icon
        action_icon = Gtk.CellRendererPixbuf()
        self.column_action_icon = Gtk.TreeViewColumn("", action_icon, icon_name=2)
        tree.append_column(self.column_action_icon)

        # Make a click activate a row such that we get the row_activated signal when it is clicked
        tree.set_activate_on_single_click(True)

        # Connect a listener to the row_activated signal to check whether the correct column was clicked
        tree.connect("row_activated", self.action_icon_clicked)

    def action_icon_clicked(self, treeview, path, column):
        # If the column clicked is the action column remove the clicked row
        if column is self.column_action_icon:
            # Get the iter that points to the clicked row
            iter = self.store.get_iter(path)

            # Remove it from the ListStore
            self.store.remove(iter)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
