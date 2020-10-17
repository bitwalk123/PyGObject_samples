import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf


class MyWindow(Gtk.Window):
    list_imagefile = ['images/IMG_0001.JPG',
                      'images/IMG_0002.JPG',
                      'images/IMG_0003.JPG',
                      'images/IMG_0004.JPG',
                      'images/IMG_0005.JPG', ]
    index_image = 0
    width = 300
    height = 200

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(self.width, self.height)
        self.set_border_width(2)
        self.set_resizable(False)

        hbar = Gtk.HeaderBar()
        self.set_titlebar(hbar)

        hbar.set_show_close_button(True)
        hbar.props.title = "HeaderBar"

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        hbar.pack_start(box)

        image_left = Gtk.Image.new_from_icon_name('go-previous', Gtk.IconSize.BUTTON)
        but_left = Gtk.Button()
        but_left.set_image(image_left)
        but_left.connect('clicked', self.on_arrow_left_clicked)
        box.add(but_left)

        image_right = Gtk.Image.new_from_icon_name('go-next', Gtk.IconSize.BUTTON)
        but_right = Gtk.Button()
        but_right.set_image(image_right)
        but_right.connect('clicked', self.on_arrow_right_clicked)
        box.add(but_right)

        self.get_image()
        self.darea = Gtk.DrawingArea()
        self.darea.connect("draw", self.on_draw)
        self.add(self.darea)

    def on_draw(self, wid, cr):
        Gdk.cairo_set_source_pixbuf(cr, self.img, 0, 0)
        cr.paint()

    def get_image(self):
        self.img = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            self.list_imagefile[self.index_image], self.width, self.height, True
        )

    def on_arrow_left_clicked(self, widget):
        self.index_image -= 1
        if self.index_image < 0:
            self.index_image = 0

        self.get_image()
        self.darea.queue_draw()

    def on_arrow_right_clicked(self, widget):
        self.index_image += 1
        if self.index_image >= len(self.list_imagefile):
            self.index_image = len(self.list_imagefile) - 1

        self.get_image()
        self.darea.queue_draw()

if __name__ == "__main__":
    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
