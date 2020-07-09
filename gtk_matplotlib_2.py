import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas
)
from matplotlib.figure import Figure
import numpy as np
import pandas as pd

df = pd.DataFrame({'Sample': list(range(1, 11)),
                   'Y': [9.030, 8.810, 9.402, 8.664, 8.773, 8.774, 8.416, 9.101, 8.687, 8.767]})
# SPC metrics
spec_usl = 9.97
spec_target = 8.70
spec_lsl = 7.43


win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)
win.set_default_size(800, 600)
win.set_title("SPC Chart")

f = Figure(dpi=100)
a = f.add_subplot(111, title="SPC Chart Example", ylabel='Value')
a.grid(True)
# horizontal lines
a.axhline(y=spec_usl, linewidth=1, color='red', label='USL')
a.axhline(y=spec_target, linewidth=1, color='blue', label='Target')
a.axhline(y=spec_lsl, linewidth=1, color='red', label='LSL')
# trend
a.plot(df['Sample'], df['Y'], color="gray", marker="o", markersize=10)

# text label
x_label = a.get_xlim()[1]
a.text(x_label, spec_usl, " USL", color="red")
a.text(x_label, spec_target, " Target", color="blue")
a.text(x_label, spec_lsl, " LSL", color="red")

sw = Gtk.ScrolledWindow()
win.add(sw)
sw.set_border_width(10)

canvas = FigureCanvas(f)  # a Gtk.DrawingArea
canvas.set_size_request(800, 600)
sw.add(canvas)

win.show_all()
Gtk.main()
