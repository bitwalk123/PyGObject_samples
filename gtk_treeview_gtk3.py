import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject


# reference
# https://www.tutorialspoint.com/pygtk/pygtk_treeview_class.htm
class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ツリービュー")
        self.set_default_size(200, 300)
        vbox = Gtk.VBox()
        self.add(vbox)

        tree = Gtk.TreeView(model=self.create_store())
        column = Gtk.TreeViewColumn(title='GUI ツールキット')
        tree.append_column(column)

        cell = Gtk.CellRendererText()
        column.pack_start(cell, True)
        column.add_attribute(cell, 'text', 0)

        select = tree.get_selection()
        select.connect("changed", self.on_tree_selection_changed)

        tree.connect("row-activated", self.on_tree_doubleclicked)
        vbox.add(tree)

    def create_store(self):
        # for GObject.TYPE_XXXX, see following URL:
        # https://developer.gnome.org/pygtk/stable/class-gtkliststore.html
        store = Gtk.TreeStore(GObject.TYPE_STRING)

        row1 = store.append(None, ['Java'])
        store.append(row1, ['AWT'])
        store.append(row1, ['SWT'])
        store.append(row1, ['Swing'])
        store.append(row1, ['JavaFX'])

        row2 = store.append(None, ['Python'])
        store.append(row2, ['PyQt'])
        store.append(row2, ['wxPython'])
        store.append(row2, ['PyGObject'])

        return store


    # -------------------------------------------------------------------------
    def on_tree_selection_changed(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            print(model[treeiter][0], "が選択されました。")

    # -------------------------------------------------------------------------
    def on_tree_doubleclicked(self, tree, path, col, userdata=None):
        model = tree.get_model()
        treeiter = model.get_iter(path)
        if treeiter is not None:
            print(model[treeiter][0], "がダブルクリックされました。")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()