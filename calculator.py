# -----------------------------------------------------------------------------
# Calculator
#
# created by Fuhito Suguri
# -----------------------------------------------------------------------------

import math
import queue
import re

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Calculator(Gtk.Window):
    # -------------------------------------------------------------------------
    #  CONSTANT
    # -------------------------------------------------------------------------
    # key layout for calculator
    keys_info = [
        {"label": "Ｃ", "x": 0, "y": 1, "w": 1, "h": 1, "name": "Cls", "method": "on_clear"},
        {"label": "√", "x": 1, "y": 1, "w": 1, "h": 1, "name": "Fnc", "method": "on_function"},
        {"label": "±", "x": 2, "y": 1, "w": 1, "h": 1, "name": "Fnc", "method": "on_function"},
        {"label": "÷", "x": 3, "y": 1, "w": 1, "h": 1, "name": "Ope", "method": "on_operation"},
        {"label": "７", "x": 0, "y": 2, "w": 1, "h": 1, "name": "Key", "method": "on_number"},
        {"label": "８", "x": 1, "y": 2, "w": 1, "h": 1, "name": "Key", "method": "on_number"},
        {"label": "９", "x": 2, "y": 2, "w": 1, "h": 1, "name": "Key", "method": "on_number"},
        {"label": "×", "x": 3, "y": 2, "w": 1, "h": 1, "name": "Ope", "method": "on_operation"},
        {"label": "４", "x": 0, "y": 3, "w": 1, "h": 1, "name": "Key", "method": "on_number"},
        {"label": "５", "x": 1, "y": 3, "w": 1, "h": 1, "name": "Key", "method": "on_number"},
        {"label": "６", "x": 2, "y": 3, "w": 1, "h": 1, "name": "Key", "method": "on_number"},
        {"label": "−", "x": 3, "y": 3, "w": 1, "h": 1, "name": "Ope", "method": "on_operation"},
        {"label": "１", "x": 0, "y": 4, "w": 1, "h": 1, "name": "Key", "method": "on_number"},
        {"label": "２", "x": 1, "y": 4, "w": 1, "h": 1, "name": "Key", "method": "on_number"},
        {"label": "３", "x": 2, "y": 4, "w": 1, "h": 1, "name": "Key", "method": "on_number"},
        {"label": "＋", "x": 3, "y": 4, "w": 1, "h": 2, "name": "Ope", "method": "on_operation"},
        {"label": "０", "x": 0, "y": 5, "w": 1, "h": 1, "name": "Key", "method": "on_number"},
        {"label": "・", "x": 1, "y": 5, "w": 1, "h": 1, "name": "Key", "method": "on_dot"},
        {"label": "＝", "x": 2, "y": 5, "w": 1, "h": 1, "name": "Ope", "method": "on_equal"},
    ]

    # initial display
    display_initial = "0."
    # max length
    max_chars = 16

    # regular expression
    re1 = re.compile("([\-0-9]+)\.$")
    re2 = re.compile("([\-0-9]+\.)0$")

    # -------------------------------------------------------------------------
    #  INITIAL VALUE
    # -------------------------------------------------------------------------
    # operation flag
    flag_dot = False
    flag_operation = False
    flag_error = False

    # register for calculation
    reg = queue.Queue()

    # CSS
    provider = Gtk.CssProvider()
    # provider.load_from_data(CALCULATOR_CSS.encode('utf-8'))
    provider.load_from_path('./calculator.css')

    # -------------------------------------------------------------------------
    #  CONSTRUCTOR
    # -------------------------------------------------------------------------
    def __init__(self):
        Gtk.Window.__init__(self, title="電卓")
        self.set_icon_from_file("calculator.png")
        self.set_default_size(0, 0)
        self.set_resizable(False)

        self.gui_layout()

    # -------------------------------------------------------------------------
    #  gui_layout
    # -------------------------------------------------------------------------
    def gui_layout(self):
        self.grid = Gtk.Grid(name="Base", column_homogeneous=True)
        context = self.grid.get_style_context()
        context.add_provider(self.provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
        self.add(self.grid)

        # Widgets for display
        self.ent = Gtk.Entry(name="Display")
        self.ent.set_text(self.display_initial)
        self.ent.set_alignment(xalign=1.0)
        self.ent.set_editable(False)
        self.ent.set_can_focus(False)
        context = self.ent.get_style_context()
        context.add_provider(self.provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
        self.grid.attach(self.ent, 0, 0, 4, 1)

        for key in self.keys_info:
            but = Gtk.Button(name=key["name"], label=key["label"])
            method_name = key["method"]
            method = getattr(self, method_name)
            but.connect("clicked", method)
            context = but.get_style_context()
            context.add_provider(self.provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
            self.grid.attach(but, key["x"], key["y"], key["w"], key["h"])

    # -------------------------------------------------------------------------
    #  get_display_string
    #
    #  argument
    #    value : value to display
    #
    #  return
    #    string to display
    # -------------------------------------------------------------------------
    def get_display_string(self, value):
        str_display = str(value)

        result = self.re2.match(str_display)
        if result:
            str_display = result.group(1)
            return str_display

        return str_display

    # -------------------------------------------------------------------------
    #  get_function_result
    #
    #  arguments
    #    text  : function operator
    #    value : value of function parameter
    #
    #  return
    #    value calculated specified function
    # -------------------------------------------------------------------------
    def get_function_result(self, text, value):
        # sign
        if text == "±":
            return value * -1
        # square root
        if text == "√":
            try:
                return math.sqrt(value)
            except Exception as e:
                self.flag_error = True
                return e

    # -------------------------------------------------------------------------
    #  get_operator
    #
    #  argument
    #    text : label string of calculator key pad
    #
    #  return
    #    operator string
    # -------------------------------------------------------------------------
    def get_operator(self, text):
        if text == "＋":
            return "+"
        if text == "−":
            return "-"
        if text == "×":
            return "*"
        if text == "÷":
            return "/"

    # -------------------------------------------------------------------------
    #  set_display
    #
    #  argument
    #    text : string to display
    # -------------------------------------------------------------------------
    def set_display(self, text):
        length = len(text)
        self.ent.set_text(text)
        self.ent.set_position(length)

    # -------------------------------------------------------------------------
    #  zenkaku_to_hankaku
    #
    #  argument
    #    text : zenkaku string
    #
    #  return
    #    hankaku (ascii) string
    # -------------------------------------------------------------------------
    def zenkaku_to_hankaku(self, text):
        # ref: https://qiita.com/YuukiMiyoshi/items/6ce77bf402a29a99f1bf
        return text.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))

    # =========================================================================
    #  BINDINGS
    # =========================================================================
    # -------------------------------------------------------------------------
    #  on_clear
    # -------------------------------------------------------------------------
    def on_clear(self, button):
        # display
        self.set_display(self.display_initial)

        # clear flag
        self.flag_dot = False
        self.flag_operation = False
        self.flag_error = False

    # -------------------------------------------------------------------------
    #  on_dot
    # -------------------------------------------------------------------------
    def on_dot(self, button):
        if self.flag_error:
            return

        # flag
        self.flag_dot = True

    # -------------------------------------------------------------------------
    #  on_equal
    # -------------------------------------------------------------------------
    def on_equal(self, button):
        if self.flag_error:
            return

        expr = ""
        while not self.reg.empty():
            expr += self.reg.get()

        expr += self.ent.get_text()

        try:
            result = eval(expr)
        except Exception as e:
            result = e
            self.flag_error = True

        disp_new = self.get_display_string(result)

        # display
        self.set_display(disp_new)

        # flag
        self.flag_operation = True

    # -------------------------------------------------------------------------
    #  on_function
    # -------------------------------------------------------------------------
    def on_function(self, button):
        if self.flag_error:
            return

        # get current value displayed
        value_current = float(self.ent.get_text())

        # get string from key label
        text = button.get_label()

        value_new = self.get_function_result(text, value_current)
        disp_new = self.get_display_string(value_new)

        # display
        self.set_display(disp_new)

        # flag
        self.flag_operation = True

    # -------------------------------------------------------------------------
    #  on_operation
    # -------------------------------------------------------------------------
    def on_operation(self, button):
        if self.flag_error:
            return

        # get current string displayed
        disp_current = self.ent.get_text()
        self.reg.put(disp_current)

        # get string from key label
        text = button.get_label()
        self.reg.put(self.get_operator(text))

        # flag
        self.flag_operation = True

    # -------------------------------------------------------------------------
    #  on_number
    # -------------------------------------------------------------------------
    def on_number(self, button):
        if self.flag_error:
            return

        # get current string displayed
        disp_current = self.ent.get_text()

        # get string from key label
        text = button.get_label()
        text_ascii = self.zenkaku_to_hankaku(text)

        # update string to display
        if self.flag_operation:
            disp_new = text_ascii + "."
            self.flag_operation = False
        else:
            if disp_current == "0.":
                if self.flag_dot:
                    disp_new = disp_current + text_ascii
                else:
                    disp_new = text_ascii + "."
            else:
                # check charcter length (digit)
                if len(disp_current) > self.max_chars:
                    return

                if self.flag_dot:
                    disp_new = disp_current + text_ascii
                else:
                    result = self.re1.match(disp_current)
                    if result:
                        disp_new = result.group(1) + text_ascii + "."
                    else:
                        disp_new = disp_current + text_ascii

        self.set_display(disp_new)


# -----------------------------------------------------------------------------
#  MAIN
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    win = Calculator()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

# ---
# PROGRAM END
