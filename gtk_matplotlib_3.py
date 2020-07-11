import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas
)
from matplotlib.figure import Figure
import pandas as pd


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="SPC Chart")
        self.set_default_size(800, 600)

        # SPC chart
        figure = self.gen_example_chart()

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(box)

        # frame
        b_bar = self.gen_button_bar(figure)
        box.pack_start(b_bar, False, True, 0)

        # plot area
        p_area = self.gen_plot_area(figure)
        box.pack_start(p_area, True, True, 0)

    def gen_button_bar(self, figure):
        frame = Gtk.Frame()

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        frame.add(hbox)

        pixbuf = GdkPixbuf.Pixbuf.new_from_file('powerpoint-128.png')
        pixbuf = pixbuf.scale_simple(32, 32, GdkPixbuf.InterpType.BILINEAR)

        but = Gtk.Button()
        but.add(Gtk.Image.new_from_pixbuf(pixbuf))
        but.connect("clicked", self.on_button_clicked, figure)
        hbox.pack_end(but, False, True, 0)

        return frame

    def gen_plot_area(self, figure):
        sw = Gtk.ScrolledWindow()
        sw.set_border_width(10)
        canvas = FigureCanvas(figure)  # a Gtk.DrawingArea
        canvas.set_size_request(800, 600)
        sw.add(canvas)
        return sw

    def gen_example_chart(self):
        # example dataframe
        df = pd.DataFrame({
            'Sample': list(range(1, 11)),
            'Y': [9.030, 8.810, 9.402, 8.664, 8.773, 8.774, 8.416, 9.101, 8.687, 8.767]
        })
        # SPC metrics
        spec_usl = 9.97
        spec_target = 8.70
        spec_lsl = 7.43

        # spc chart
        fig = Figure(dpi=100)
        splot = fig.add_subplot(111, title="SPC Chart Example", ylabel='Value')
        splot.grid(True)

        # horizontal lines
        splot.axhline(y=spec_usl, linewidth=1, color='red', label='USL')
        splot.axhline(y=spec_target, linewidth=1, color='blue', label='Target')
        splot.axhline(y=spec_lsl, linewidth=1, color='red', label='LSL')

        # trend
        splot.plot(df['Sample'], df['Y'], color="gray", marker="o", markersize=10)

        # text label
        x_label = splot.get_xlim()[1]
        splot.text(x_label, spec_usl, " USL", color="red")
        splot.text(x_label, spec_target, " Target", color="blue")
        splot.text(x_label, spec_lsl, " LSL", color="red")

        return fig

    def on_button_clicked(self, button, figure):
        print("ボタンがクリックされました。")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
