# Calculator

import math
import queue
import re

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# CSS
CALCULATOR_CSS = '''
button {
    padding: 5px 25px;
    margin: 1px;
}
#Base {
    background: wheat;
    margin: 2px;
}
#Display {
    color: darkgreen;
    font-size: x-large;
    padding: 10px;
    margin: 1px;
}
#Key {
}
#ClearKey {
    background: thistle;
    color: darkred;
}'''


class Calculator(Gtk.Window):
    # key layout for calculator
    num_info = [["０", 0, 5, 1, 1],
                ["１", 0, 4, 1, 1],
                ["２", 1, 4, 1, 1],
                ["３", 2, 4, 1, 1],
                ["４", 0, 3, 1, 1],
                ["５", 1, 3, 1, 1],
                ["６", 2, 3, 1, 1],
                ["７", 0, 2, 1, 1],
                ["８", 1, 2, 1, 1],
                ["９", 2, 2, 1, 1]]
    dot_info = ["・", 1, 5, 1, 1]
    ope_info = [["＋", 3, 4, 1, 2],
                ["ー", 3, 3, 1, 1],
                ["×", 3, 2, 1, 1],
                ["÷", 3, 1, 1, 1]]
    func_info = [["±", 2, 1, 1, 1],
                 ["√", 1, 1, 1, 1]]

    # operation flag
    dot_entered = False
    ope_entered = False
    reg = queue.Queue()

    # regular expression
    re1 = re.compile("([\-0-9]+)\.$")
    re2 = re.compile("([\-0-9]+\.)0$")

    # CSS
    provider = Gtk.CssProvider()
    provider.load_from_data(CALCULATOR_CSS.encode('utf-8'))

    # -------------------------------------------------------------------------
    #  CONSTRUCTOR
    # -------------------------------------------------------------------------
    def __init__(self):
        Gtk.Window.__init__(self, title="電卓")
        self.set_default_size(0, 0)
        self.set_resizable(False)

        self.gui_layout()

    def get_display_string(self, value):
        str_display = str(value)

        result = self.re2.match(str_display)
        if result:
            str_display = result.group(1)
            return str_display

        return str_display

    def get_function_result(self, text, value):
        # sign
        if text == "±":
            return value * -1
        # square root
        if text == "√":
            return math.sqrt(value)

    def get_operator(self, text):
        if text == "＋":
            return "+"
        if text == "−":
            return "-"
        if text == "×":
            return "*"
        if text == "÷":
            return "/"

    def gui_layout(self):
        self.grid = Gtk.Grid(name="Base", column_homogeneous=True)
        context = self.grid.get_style_context()
        context.add_provider(self.provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
        self.add(self.grid)

        # Widgets for display
        self.ent = Gtk.Entry(name="Display")
        self.ent.set_alignment(xalign=1.0)
        self.ent.set_editable(False)
        context = self.ent.get_style_context()
        context.add_provider(self.provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
        self.grid.attach(self.ent, 0, 0, 4, 1)

        self.key_dot()
        self.keys_func()
        self.keys_ope()
        self.keys_num()

        but_E = Gtk.Button(name="Key", label="＝")  # Equal
        but_E.connect("clicked", self.on_equal)
        context = but_E.get_style_context()
        context.add_provider(self.provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
        self.grid.attach(but_E, 2, 5, 1, 1)

        but_C = Gtk.Button(name="ClearKey", label="C")  # Clear
        but_C.connect("clicked", self.on_clear)
        context = but_C.get_style_context()
        context.add_provider(self.provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
        self.grid.attach(but_C, 0, 1, 1, 1)

        # initialize
        self.on_clear(but_C)

    def key_dot(self):
        but = Gtk.Button(name="Key", label=self.dot_info[0])
        but.connect("clicked", self.on_dot_button_clicked)
        context = but.get_style_context()
        context.add_provider(self.provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
        self.grid.attach(but, self.dot_info[1], self.dot_info[2], self.dot_info[3], self.dot_info[4])

    def keys_func(self):
        for info in self.func_info:
            but = Gtk.Button(name="Key", label=info[0])
            but.connect("clicked", self.on_func_button_clicked)
            context = but.get_style_context()
            context.add_provider(self.provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
            self.grid.attach(but, info[1], info[2], info[3], info[4])

    def keys_ope(self):
        for info in self.ope_info:
            but = Gtk.Button(name="Key", label=info[0])
            but.connect("clicked", self.on_ope_button_clicked)
            context = but.get_style_context()
            context.add_provider(self.provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
            self.grid.attach(but, info[1], info[2], info[3], info[4])

    def keys_num(self):
        for info in self.num_info:
            but = Gtk.Button(name="Key", label=info[0])
            but.connect("clicked", self.on_num_button_clicked)
            context = but.get_style_context()
            context.add_provider(self.provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
            self.grid.attach(but, info[1], info[2], info[3], info[4])

    def on_clear(self, button):
        # display
        self.set_display("0.")

        # clear flag
        self.dot_entered = False
        self.ope_entered = False

    def on_dot_button_clicked(self, button):
        # flag
        self.dot_entered = True

    def on_equal(self, button):
        expr = ""
        while not self.reg.empty():
            expr += self.reg.get()

        expr += self.ent.get_text()

        result = eval(expr)
        disp_new = self.get_display_string(result)

        # display
        self.set_display(disp_new)

        # flag
        self.ope_entered = True

    def on_func_button_clicked(self, button):
        # get current value displayed
        value_current = float(self.ent.get_text())

        # get string from key label
        text = button.get_label()

        value_new = self.get_function_result(text, value_current)
        disp_new = self.get_display_string(value_new)

        # display
        self.set_display(disp_new)

        # flag
        self.ope_entered = True

    def on_ope_button_clicked(self, button):
        # get current string displayed
        disp_current = self.ent.get_text()
        self.reg.put(disp_current)

        # get string from key label
        text = button.get_label()
        self.reg.put(self.get_operator(text))

        # flag
        self.ope_entered = True

    def on_num_button_clicked(self, button):
        text = button.get_label()
        text_ascii = self.zenkaku_to_hankaku(text)

        # get current string displayed
        disp_current = self.ent.get_text()

        # update string to display
        if self.ope_entered:
            disp_new = text_ascii + "."
            self.ope_entered = False
        else:
            if disp_current == "0.":
                if self.dot_entered:
                    disp_new = disp_current + text_ascii
                else:
                    disp_new = text_ascii + "."
            else:
                if self.dot_entered:
                    disp_new = disp_current + text_ascii
                else:
                    result = self.re1.match(disp_current)
                    if result:
                        disp_new = result.group(1) + text_ascii + "."
                    else:
                        disp_new = disp_current + text_ascii

        self.set_display(disp_new)

    def set_display(self, text):
        length = len(text)
        self.ent.set_text(text)
        self.ent.set_position(length)

    def zenkaku_to_hankaku(self, text):
        # ref: https://qiita.com/YuukiMiyoshi/items/6ce77bf402a29a99f1bf
        return text.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))


if __name__ == '__main__':
    win = Calculator()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
