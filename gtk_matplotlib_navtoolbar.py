#!/usr/bin/env python
# coding: utf-8
# Reference:
# https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_gtk4_panzoom_sgskip.html
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
from matplotlib.backends.backend_gtk4 import (
    NavigationToolbar2GTK4 as NavigationToolbar,
)
from matplotlib.backends.backend_gtk4agg import (
    FigureCanvasGTK4Agg as FigureCanvas,
)
from matplotlib.figure import Figure
import pandas as pd

APPID = 'com.blogspot.bitwalk'


def get_example_chart() -> Figure:
    # example dataframe
    df = pd.DataFrame({
        'Sample': list(range(1, 11)),
        'Y': [9.030, 8.810, 9.402, 8.664, 8.773, 8.774, 8.416, 9.101, 8.687, 8.767]
    })

    fig = Figure(dpi=100)
    ax = fig.add_subplot(
        title='Plot sample',
        xlabel='Sample',
        ylabel='Value',
    )
    ax.plot(
        df['Sample'],
        df['Y'],
        color='red',
        marker='o',
        markersize=5,
    )
    ax.grid(True)
    return fig


class Example(Gtk.Window):
    def __init__(self, app):
        Gtk.Window.__init__(
            self,
            application=app,
            title='Matplotlib',
            default_width=600,
            default_height=500,
        )
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(vbox)

        swin = Gtk.ScrolledWindow(
            margin_top=2,
            margin_bottom=2,
            margin_start=2,
            margin_end=2,
        )
        vbox.append(swin)

        figure = get_example_chart()
        canvas = FigureCanvas(figure)
        canvas.set_size_request(500, 300) # set minimu size
        swin.set_child(canvas)

        toolbar = NavigationToolbar(canvas)
        vbox.append(toolbar)


class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_activate(self):
        win = Example(self)
        win.present()


def main():
    app = MyApplication()
    app.run()


if __name__ == '__main__':
    main()
