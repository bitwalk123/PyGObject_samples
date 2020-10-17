import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf


class MyWindow(Gtk.Window):
    list_image = ['images/IMG_0001.JPG',
                  'images/IMG_0002.JPG',
                  'images/IMG_0003.JPG',
                  'images/IMG_0004.JPG',
                  'images/IMG_0005.JPG', ]
    idx_image = 0
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
        hbar.props.title = 'HaderBar'

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        hbar.pack_start(box)

        img_left = Gtk.Image.new_from_icon_name('go-previous', Gtk.IconSize.BUTTON)
        but_left = Gtk.Button()
        but_left.set_image(img_left)
        but_left.connect('clicked', self.on_arrow_left_clicked)
        box.add(but_left)

        img_right = Gtk.Image.new_from_icon_name('go-next', Gtk.IconSize.BUTTON)
        but_right = Gtk.Button()
        but_right.set_image(img_right)
        but_right.connect('clicked', self.on_arrow_right_clicked)
        box.add(but_right)

        self.get_image()
        self.area = Gtk.DrawingArea()
        self.area.connect('draw', self.on_draw)
        self.add(self.area)

    def on_draw(self, widget, cr):
        # Sets the given pixbuf as the source pattern for cr, cairo context.
        Gdk.cairo_set_source_pixbuf(cr, self.img, 0, 0)
        cr.paint()

    def get_image(self):
        self.img = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            self.list_image[self.idx_image], self.width, self.height, True
        )

    def on_arrow_left_clicked(self, widget):
        self.idx_image -= 1
        # check scope of image index
        if self.idx_image < 0:
            self.idx_image = 0
        # update image to display
        self.get_image()
        self.area.queue_draw()

    def on_arrow_right_clicked(self, widget):
        # check scope of image index
        self.idx_image += 1
        if self.idx_image >= len(self.list_image):
            self.idx_image = len(self.list_image) - 1
        # update image to display
        self.get_image()
        self.area.queue_draw()


if __name__ == '__main__':
    win = MyWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
