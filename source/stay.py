import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import calendar

class Stay(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        master.state('zoomed')
        master.geometry('1000x600')  # 高さを指定
        master.title('Hello Tkinter')

        self.create_widgets()

    # ウィジェットを配置して画面作るメソッド
    def create_widgets(self):
        # Canvasとスクロールバーの設定
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame = tk.Frame(self.canvas)

        # 画面にウィジェットを配置
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # スクロールバーの配置
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # ウィジェット配置
        self._create_widgets_in_frame()

        # フレームのサイズを自動調整
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    def _create_widgets_in_frame(self):
        self.label_stay = tk.Label(self.frame, text="和室 (本館和室7.5畳)")
        self.label_stay.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.label_stay1 = tk.Label(self.frame, text="大人:八幡平ポーク")
        self.label_stay1.grid(row=0, column=1, padx=5, pady=5)
        self.label_stay2 = tk.Label(self.frame, text="子供:八幡平ポーク")
        self.label_stay2.grid(row=0, column=2, padx=5, pady=5)
        self.label_stay3 = tk.Label(self.frame, text="大人:岩手県産牛")
        self.label_stay3.grid(row=0, column=3, padx=5, pady=5)
        self.label_stay4 = tk.Label(self.frame, text="子供:岩手県産牛")
        self.label_stay4.grid(row=0, column=4, padx=5, pady=5)
        self.label_stay5 = tk.Label(self.frame, text="大人:前沢牛")
        self.label_stay5.grid(row=0, column=5, padx=5, pady=5)
        self.label_stay6 = tk.Label(self.frame, text="子供:前沢牛")
        self.label_stay6.grid(row=0, column=6, padx=5, pady=5)
    
        self.entry_stay1 = tk.Entry(self.frame, width=10)
        self.entry_stay1.grid(row=1, column=1, padx=5, pady=5)
        self.entry_stay2 = tk.Entry(self.frame, width=10)
        self.entry_stay2.grid(row=1, column=2, padx=5, pady=5)
        self.entry_stay3 = tk.Entry(self.frame, width=10)
        self.entry_stay3.grid(row=1, column=3, padx=5, pady=5)
        self.entry_stay4 = tk.Entry(self.frame, width=10)
        self.entry_stay4.grid(row=1, column=4, padx=5, pady=5)
        self.entry_stay5 = tk.Entry(self.frame, width=10)
        self.entry_stay5.grid(row=1, column=5, padx=5, pady=5)
        self.entry_stay6 = tk.Entry(self.frame, width=10)
        self.entry_stay6.grid(row=1, column=6, padx=5, pady=5)
        
        
        self.label_stay = tk.Label(self.frame, text="1F西館洋室")
        self.label_stay.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.label_stay1 = tk.Label(self.frame, text="大人")
        self.label_stay1.grid(row=2, column=1, padx=5, pady=5)
        self.label_stay2 = tk.Label(self.frame, text="子供")
        self.label_stay2.grid(row=2, column=2, padx=5, pady=5)
        
        self.entry_stay1 = tk.Entry(self.frame, width=10)
        self.entry_stay1.grid(row=3, column=1, padx=5, pady=5)
        self.entry_stay2 = tk.Entry(self.frame, width=10)
        self.entry_stay2.grid(row=3, column=2, padx=5, pady=5)
        
        
        self.label_stay = tk.Label(self.frame, text="岩手山側和室")
        self.label_stay.grid(row=4, column=0, padx=10, pady=10, sticky='e')
        self.label_stay1 = tk.Label(self.frame, text="大人")
        self.label_stay1.grid(row=4, column=1, padx=5, pady=5)
        self.label_stay2 = tk.Label(self.frame, text="子供")
        self.label_stay2.grid(row=4, column=2, padx=5, pady=5)
        
        self.entry_stay1 = tk.Entry(self.frame, width=10)
        self.entry_stay1.grid(row=5, column=1, padx=5, pady=5)
        self.entry_stay2 = tk.Entry(self.frame, width=10)
        self.entry_stay2.grid(row=5, column=2, padx=5, pady=5)
        
        
        self.label_stay = tk.Label(self.frame, text="岩手山側露天風呂付き和室")
        self.label_stay.grid(row=6, column=0, padx=10, pady=10, sticky='e')
        self.label_stay1 = tk.Label(self.frame, text="大人")
        self.label_stay1.grid(row=6, column=1, padx=5, pady=5)
        self.label_stay2 = tk.Label(self.frame, text="子供")
        self.label_stay2.grid(row=6, column=2, padx=5, pady=5)
        
        self.entry_stay1 = tk.Entry(self.frame, width=10)
        self.entry_stay1.grid(row=7, column=1, padx=5, pady=5)
        self.entry_stay2 = tk.Entry(self.frame, width=10)
        self.entry_stay2.grid(row=7, column=2, padx=5, pady=5)
        
        
        self.label_stay = tk.Label(self.frame, text="西館和室10畳")
        self.label_stay.grid(row=8, column=0, padx=10, pady=10, sticky='e')
        self.label_stay1 = tk.Label(self.frame, text="大人")
        self.label_stay1.grid(row=8, column=1, padx=5, pady=5)
        self.label_stay2 = tk.Label(self.frame, text="子供")
        self.label_stay2.grid(row=8, column=2, padx=5, pady=5)
        
        self.entry_stay1 = tk.Entry(self.frame, width=10)
        self.entry_stay1.grid(row=9, column=1, padx=5, pady=5)
        self.entry_stay2 = tk.Entry(self.frame, width=10)
        self.entry_stay2.grid(row=9, column=2, padx=5, pady=5)
        
        
        self.label_stay = tk.Label(self.frame, text="1F檜内風呂付き和洋室")
        self.label_stay.grid(row=10, column=0, padx=10, pady=10, sticky='e')
        self.label_stay1 = tk.Label(self.frame, text="大人")
        self.label_stay1.grid(row=10, column=1, padx=5, pady=5)
        self.label_stay2 = tk.Label(self.frame, text="子供")
        self.label_stay2.grid(row=10, column=2, padx=5, pady=5)
        
        self.entry_stay1 = tk.Entry(self.frame, width=10)
        self.entry_stay1.grid(row=11, column=1, padx=5, pady=5)
        self.entry_stay2 = tk.Entry(self.frame, width=10)
        self.entry_stay2.grid(row=11, column=2, padx=5, pady=5)
        
        
        self.label_stay = tk.Label(self.frame, text="西館和室28畳")
        self.label_stay.grid(row=12, column=0, padx=10, pady=10, sticky='e')
        self.label_stay1 = tk.Label(self.frame, text="大人")
        self.label_stay1.grid(row=12, column=1, padx=5, pady=5)
        self.label_stay2 = tk.Label(self.frame, text="子供")
        self.label_stay2.grid(row=12, column=2, padx=5, pady=5)
        
        self.entry_stay1 = tk.Entry(self.frame, width=10)
        self.entry_stay1.grid(row=13, column=1, padx=5, pady=5)
        self.entry_stay2 = tk.Entry(self.frame, width=10)
        self.entry_stay2.grid(row=13, column=2, padx=5, pady=5)
        
        
        self.label_stay = tk.Label(self.frame, text="和室 (本館和室7.5畳)")
        self.label_stay.grid(row=14, column=0, padx=10, pady=10, sticky='e')
        self.label_stay1 = tk.Label(self.frame, text="大人")
        self.label_stay1.grid(row=14, column=1, padx=5, pady=5)
        self.label_stay2 = tk.Label(self.frame, text="子供")
        self.label_stay2.grid(row=14, column=2, padx=5, pady=5)
        
        self.entry_stay1 = tk.Entry(self.frame, width=10)
        self.entry_stay1.grid(row=15, column=1, padx=5, pady=5)
        self.entry_stay2 = tk.Entry(self.frame, width=10)
        self.entry_stay2.grid(row=15, column=2, padx=5, pady=5)
        
        
        

        # 月のラベル
        self.label_month = tk.Label(self.frame, text="月・日")
        self.label_month.grid(row=16, column=0, padx=10, pady=10, sticky='e')

        # 月のプルダウン
        self.month_var = tk.StringVar()
        self.month_combobox = ttk.Combobox(self.frame, textvariable=self.month_var, state="readonly", width=6)
        self.month_combobox['values'] = [f"{i}月" for i in range(1, 13)]
        self.month_combobox.grid(row=16, column=1, padx=5, pady=10)
        self.month_combobox.bind("<<ComboboxSelected>>", self.update_days)

        # 日のプルダウン（※ラベルなしで月の隣に）
        self.day_var = tk.StringVar()
        self.day_combobox = ttk.Combobox(self.frame, textvariable=self.day_var, state="readonly", width=6)
        self.day_combobox['values'] = [str(i) for i in range(1, 32)]
        self.day_combobox.grid(row=16, column=2, padx=5, pady=10)


        # 宿泊数のラベル
        self.label_stay_count = tk.Label(self.frame, text="宿泊数")
        self.label_stay_count.grid(row=17, column=0, padx=5, pady=10, sticky='e')

        # 宿泊数のプルダウン
        self.stay_count_var = tk.StringVar()
        self.stay_count_combobox = ttk.Combobox(self.frame, textvariable=self.stay_count_var, state="readonly", width=5)
        self.stay_count_combobox['values'] = [str(i) for i in range(1, 11)]  # 宿泊数を1泊から10泊まで
        self.stay_count_combobox.grid(row=17, column=1, padx=5, pady=10)

        # 早割りのラベル
        self.label_early_discount = tk.Label(self.frame, text="早割り")
        self.label_early_discount.grid(row=18, column=0, padx=10, pady=10, sticky='e')

        # 早割りのラジオボタン
        self.early_discount_var = tk.StringVar(value="なし")  # デフォルトはなし
        self.radio_2000 = tk.Radiobutton(self.frame, text="土日祝+2,000", variable=self.early_discount_var, value="2000", width=20)
        self.radio_60 = tk.Radiobutton(self.frame, text="60日以前 10%", variable=self.early_discount_var, value="60", width=20)
        self.radio_90 = tk.Radiobutton(self.frame, text="90日以前 15%", variable=self.early_discount_var, value="90", width=20)
        self.radio_no_discount = tk.Radiobutton(self.frame, text="なし", variable=self.early_discount_var, value="なし", width=20)

        self.radio_2000.grid(row=18, column=1, padx=5, pady=5, sticky='w')
        self.radio_60.grid(row=19, column=1, padx=5, pady=5, sticky='w')
        self.radio_90.grid(row=20, column=1, padx=5, pady=5, sticky='w')
        self.radio_no_discount.grid(row=21, column=1, padx=5, pady=5, sticky='w')

        # 夕飯のラベル
        self.label_dinner = tk.Label(self.frame, text="夕飯")
        self.label_dinner.grid(row=22, column=0, padx=10, pady=10, sticky='e')

        # 夕飯のプルダウン
        self.dinner_var = tk.StringVar()
        self.dinner_combobox = ttk.Combobox(self.frame, textvariable=self.dinner_var, state="readonly", width=25)
        self.dinner_combobox['values'] = [
            "八幡平ポーク", 
            "岩手県産牛", 
            "前沢牛"
        ]
        self.dinner_combobox.grid(row=22, column=1, columnspan=2, padx=5, pady=10)


        # オプションのラベル
        self.label_options = tk.Label(self.frame, text="オプション")
        self.label_options.grid(row=23, column=0, padx=10, pady=10, sticky='e')
        self.label_1 = tk.Label(self.frame, text="大人")
        self.label_1.grid(row=23, column=1, padx=5, pady=5)
        self.label_2 = tk.Label(self.frame, text="子供")
        self.label_2.grid(row=23, column=2, padx=5, pady=5)

        # ドックワンオプション（大人と子供の人数入力欄）
        self.label_dog_wan = tk.Label(self.frame, text="ドックワン")
        self.label_dog_wan.grid(row=24, column=0, padx=10, pady=5, sticky='e')
        self.entry_dog_wan_adult = tk.Entry(self.frame, width=10)
        self.entry_dog_wan_adult.grid(row=24, column=1, padx=5, pady=5)
        self.entry_dog_wan_child = tk.Entry(self.frame, width=10)
        self.entry_dog_wan_child.grid(row=24, column=2, padx=5, pady=5)

        # 岩盤浴オプション（大人と子供の人数入力欄）
        self.label_rock_bath = tk.Label(self.frame, text="岩盤浴")
        self.label_rock_bath.grid(row=25, column=0, padx=10, pady=5, sticky='e')
        self.entry_rock_bath_adult = tk.Entry(self.frame, width=10)
        self.entry_rock_bath_adult.grid(row=25, column=1, padx=5, pady=5)
        self.entry_rock_bath_child = tk.Entry(self.frame, width=10)
        self.entry_rock_bath_child.grid(row=25, column=2, padx=5, pady=5)

        # パターゴルフオプション（大人と子供の人数入力欄）
        self.label_putter_golf = tk.Label(self.frame, text="パターゴルフ")
        self.label_putter_golf.grid(row=26, column=0, padx=10, pady=5, sticky='e')
        self.entry_putter_golf_adult = tk.Entry(self.frame, width=10)
        self.entry_putter_golf_adult.grid(row=26, column=1, padx=5, pady=5)
        self.entry_putter_golf_child = tk.Entry(self.frame, width=10)
        self.entry_putter_golf_child.grid(row=26, column=2, padx=5, pady=5)

        # パークゴルフオプション（大人と子供の人数入力欄）
        self.label_park_golf = tk.Label(self.frame, text="パークゴルフ")
        self.label_park_golf.grid(row=27, column=0, padx=10, pady=5, sticky='e')
        self.entry_park_golf_adult = tk.Entry(self.frame, width=10)
        self.entry_park_golf_adult.grid(row=27, column=1, padx=5, pady=5)
        self.entry_park_golf_child = tk.Entry(self.frame, width=10)
        self.entry_park_golf_child.grid(row=27, column=2, padx=5, pady=5)

        # テニスコートオプション（大人と子供の人数入力欄）
        self.label_tennis_court = tk.Label(self.frame, text="テニスコート")
        self.label_tennis_court.grid(row=28, column=0, padx=10, pady=5, sticky='e')
        self.entry_tennis_court_adult = tk.Entry(self.frame, width=10)
        self.entry_tennis_court_adult.grid(row=28, column=1, padx=5, pady=5)
        self.entry_tennis_court_child = tk.Entry(self.frame, width=10)
        self.entry_tennis_court_child.grid(row=28, column=2, padx=5, pady=5)

        # 温泉貸切オプション（大人と子供の人数入力欄）
        self.label_private_onsen = tk.Label(self.frame, text="温泉貸切")
        self.label_private_onsen.grid(row=29, column=0, padx=10, pady=5, sticky='e')
        self.entry_private_onsen_adult = tk.Entry(self.frame, width=10)
        self.entry_private_onsen_adult.grid(row=29, column=1, padx=5, pady=5)
        self.entry_private_onsen_child = tk.Entry(self.frame, width=10)
        self.entry_private_onsen_child.grid(row=29, column=2, padx=5, pady=5)

    # 月が選択されたときに日を更新するメソッド
    def update_days(self, event=None):
        selected_month = self.month_var.get().replace('月', '')
        try:
            num_days = calendar.monthrange(datetime.now().year, int(selected_month))[1]
        except ValueError:
            return
        days = [str(i) for i in range(1, num_days+1)]
        self.day_combobox['values'] = days

root = tk.Tk()
app = Stay(master=root)
app.mainloop()
