import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Calculator(Gtk.Window):
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
    func_info = [["±", 2, 1, 1, 1],
                 ["＋", 3, 4, 1, 2],
                 ["ー", 3, 3, 1, 1],
                 ["×", 3, 2, 1, 1],
                 ["÷", 3, 1, 1, 1],
                 ["＝", 2, 5, 1, 1]]

    def __init__(self):
        Gtk.Window.__init__(self, title="電卓")
        self.set_default_size(0, 0)
        self.set_resizable(False)

        self.grid = Gtk.Grid(column_homogeneous=True)
        self.add(self.grid)

        # Widgets
        self.ent = Gtk.Entry()
        self.ent.set_alignment(xalign=1.0)
        self.ent.set_editable(False)
        self.grid.attach(self.ent, 0, 0, 4, 1)

        self.num_keys()
        self.dot_key()
        self.func_keys()

        but_A = Gtk.Button(label="AC")  # All Clear
        but_C = Gtk.Button(label="C")  # Clear

        # Layout

        self.grid.attach(but_A, 0, 1, 1, 1)
        self.grid.attach(but_C, 1, 1, 1, 1)

        # initialize
        self.set_value_to_display("0.")

    def num_keys(self):
        for info in self.num_info:
            but = Gtk.Button(label=info[0])
            but.connect("clicked", self.on_num_button_clicked)
            self.grid.attach(but, info[1], info[2], info[3], info[4])

    def dot_key(self):
        but = Gtk.Button(label=self.dot_info[0])
        but.connect("clicked", self.on_dot_button_clicked)
        self.grid.attach(but, self.dot_info[1], self.dot_info[2], self.dot_info[3], self.dot_info[4])

    def func_keys(self):
        for info in self.func_info:
            but = Gtk.Button(label=info[0])
            but.connect("clicked", self.on_func_button_clicked)
            self.grid.attach(but, info[1], info[2], info[3], info[4])

    def on_num_button_clicked(self, button):
        text = button.get_label()
        print("ボタン「" + text + "」がクリックされました。")

    def on_dot_button_clicked(self, button):
        text = button.get_label()
        print("ボタン「" + text + "」がクリックされました。")

    def on_func_button_clicked(self, button):
        text = button.get_label()
        print("ボタン「" + text + "」がクリックされました。")

    def set_value_to_display(self, text):
        length = len(text)
        self.ent.set_text(text)
        self.ent.set_position(length)


win = Calculator()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
