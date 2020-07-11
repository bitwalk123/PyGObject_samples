import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas
)
from matplotlib.figure import Figure
import pandas as pd

from pptx import Presentation
from pptx.util import Pt, Inches
from pptx.dml.color import RGBColor


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
        image_path = "./chart.png"
        figure.savefig(image_path)
        self.gen_powerpoint(image_path)

    def gen_powerpoint(self, image_path):
        # ---------------------------------------------------
        # "テンプレート、出力ファイル名の設定"
        # ---------------------------------------------------
        # templateとなるpptxファイルを指定する。
        template_path = "./template.pptx"
        # 出力するpptxファイルを指定する。(存在しない場合、自動作成されます)
        save_path = "./output.pptx"
        # ---------------------------------------------------
        # "空のスライドの挿入"
        # ---------------------------------------------------
        presentation = Presentation(template_path)
        title_slide_layout = presentation.slide_layouts[1]  # レイアウトや書式を元ファイルから参照する
        slide = presentation.slides.add_slide(title_slide_layout)
        shapes = slide.shapes
        # ---------------------------------------------------
        # タイトルテキストの挿入"
        # ---------------------------------------------------
        # 入力したい文字列
        slide_title = "TEST TITLE"
        shapes.title.text = slide_title
        # ---------------------------------------------------
        # "imageの挿入"
        # ---------------------------------------------------
        # 挿入する位置
        pic_left = self.Centis(1)
        pic_top = self.Centis(5)
        # imageの高さを指定
        pic_height = self.Centis(7.9)
        slide.shapes.add_picture(image_path, pic_left, pic_top, height=pic_height)
        # ---------------------------------------------------
        # "tableの挿入"
        # ---------------------------------------------------
        # 入力したいtable状のデータ
        sample_table = [["1.1", "1.2", "1.3"]
            , ["2.1", "2.2", "2.3"]
            , ["3.1", "3.2", "3.3"]]
        # cell内のフォントサイズ
        cell_font = 20
        # 挿入する位置
        table_left = self.Centis(9.4)
        table_top = self.Centis(5)
        # tableの幅と高さ（仮）
        table_width = self.Centis(15)
        table_height = self.Centis(10)
        # tableの行数と列数(tableのサイズ)
        rows = len(sample_table)
        cols = len(sample_table[0])
        table = slide.shapes.add_table(rows, cols, table_left, table_top, table_width, table_height).table
        # 表の各セルの中身を記入
        for i in range(rows):
            for j in range(cols):
                cell = table.cell(i, j)
                cell.text = sample_table[i][j]
                cell.text_frame.paragraphs[0].font.size = Pt(cell_font)
        # tableの高さを再調整
        table.rows[0].height = self.Centis(1.5)
        table.rows[1].height = self.Centis(4.9)
        table.rows[2].height = self.Centis(1.5)
        # tableの幅を再調整
        table.columns[0].width = self.Centis((15) / 3)
        table.columns[1].width = self.Centis((15) / 3)
        table.columns[2].width = self.Centis((15) / 3)
        # ---------------------------------------------------
        # "テキストボックスの挿入"
        # ---------------------------------------------------
        # 文字列
        sample_str = "Test Text"
        # テキストボックスの位置
        text_left = self.Centis(1)
        text_top = self.Centis(13.4)
        # テキストボックスの幅と高さ
        text_width = self.Centis(25.4 - 2)
        text_height = self.Centis(5)
        # 文字のフォントサイズ
        text_font = 20
        # 塗りつぶし色指定(R, G, B)
        color = RGBColor(150, 255, 255)
        text_box = slide.shapes.add_textbox(text_left, text_top, text_width, text_height)
        text_box.text = sample_str
        text_box.text_frame.add_paragraph().font.size = Pt(text_font)
        text_box.fill.solid()
        text_box.fill.fore_color.rgb = color
        # ---------------------------------------------------
        # "ファイル保存"
        # ---------------------------------------------------
        presentation.save(save_path)

    def Centis(self, length):
        centi = Inches(length / 2.54)
        return centi


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
