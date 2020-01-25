import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


# reference
# https://www.tutorialspoint.com/pygtk/pygtk_treeview_class.htm
class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ツリービュー")
        self.set_default_size(200, 300)
        vbox = Gtk.VBox()

        treeview = Gtk.TreeView(model=self.create_store())
        tvcolumn = Gtk.TreeViewColumn('GUI ツールキット')
        treeview.append_column(tvcolumn)

        cell = Gtk.CellRendererText()
        tvcolumn.pack_start(cell, True)
        tvcolumn.add_attribute(cell, 'text', 0)
        vbox.add(treeview)

        self.add(vbox)

    def create_store(self):
        store = Gtk.TreeStore(str)

        row1 = store.append(None, ['JAVA'])
        store.append(row1, ['AWT'])
        store.append(row1, ['Swing'])
        store.append(row1, ['JavaFX'])

        row2 = store.append(None, ['Python'])
        store.append(row2, ['PyQt'])
        store.append(row2, ['wxPython'])
        store.append(row2, ['PyGTK'])

        return store


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()