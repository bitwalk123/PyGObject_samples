import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    prefectures = ["北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県",
                   "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県",
                   "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県",
                   "静岡県", "愛知県", "新潟県", "富山県", "石川県", "福井県", "山梨県",
                   "長野県", "岐阜県", "静岡県", "愛知県", "鳥取県", "島根県", "岡山県",
                   "広島県", "山口県", "徳島県", "香川県", "愛媛県", "高知県", "福岡県",
                   "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"]

    def __init__(self):
        Gtk.Window.__init__(self, title="コンボボックス")
        self.set_default_size(0, 0)

        combo = Gtk.ComboBoxText()
        combo.set_entry_text_column(0)
        combo.connect("changed", self.on_currency_combo_changed)

        for pref in self.prefectures:
            combo.append_text(pref)

        combo.set_active(0)
        self.add(combo)

    def on_currency_combo_changed(self, combobox):
        text = combobox.get_active_text()
        if text is not None:
            print("「%s」が選択されました。" % text)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
