import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import calendar

class Stay(tk.Frame):
    def __init__(self, master, name, mail):
        super().__init__(master,)
        self.pack(fill=tk.BOTH, expand=True)
        self.name = name
        self.mail = mail
        master.state('zoomed')
        master.geometry('1000x600')  # 高さを指定
        master.title('Hello Tkinter')
        self.create_widgets()
    # ウィジェットを配置して画面作るメソッド
    def create_widgets(self):
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self._create_widgets_in_frame()
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    def _create_widgets_in_frame(self):
        self.label_stay1 = tk.Label(self.frame, text="和室 (本館和室7.5畳)")
        self.label_stay1.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.label_stay1_1 = tk.Label(self.frame, text="大人:八幡平ポーク")
        self.label_stay1_1.grid(row=0, column=1, padx=5, pady=5)
        self.label_stay1_2 = tk.Label(self.frame, text="子供:八幡平ポーク")
        self.label_stay1_2.grid(row=0, column=2, padx=5, pady=5)
        self.label_stay1_3 = tk.Label(self.frame, text="大人:岩手県産牛")
        self.label_stay1_3.grid(row=0, column=3, padx=5, pady=5)
        self.label_stay1_4 = tk.Label(self.frame, text="子供:岩手県産牛")
        self.label_stay1_4.grid(row=0, column=4, padx=5, pady=5)
        self.label_stay1_5 = tk.Label(self.frame, text="大人:前沢牛")
        self.label_stay1_5.grid(row=0, column=5, padx=5, pady=5)
        self.label_stay1_6 = tk.Label(self.frame, text="子供:前沢牛")
        self.label_stay1_6.grid(row=0, column=6, padx=5, pady=5)
        self.entry_stay1_1 = tk.Entry(self.frame, width=10)
        self.entry_stay1_1.grid(row=1, column=1, padx=5, pady=5)
        self.entry_stay1_2 = tk.Entry(self.frame, width=10)
        self.entry_stay1_2.grid(row=1, column=2, padx=5, pady=5)
        self.entry_stay1_3 = tk.Entry(self.frame, width=10)
        self.entry_stay1_3.grid(row=1, column=3, padx=5, pady=5)
        self.entry_stay1_4 = tk.Entry(self.frame, width=10)
        self.entry_stay1_4.grid(row=1, column=4, padx=5, pady=5)
        self.entry_stay1_5 = tk.Entry(self.frame, width=10)
        self.entry_stay1_5.grid(row=1, column=5, padx=5, pady=5)
        self.entry_stay1_6 = tk.Entry(self.frame, width=10)
        self.entry_stay1_6.grid(row=1, column=6, padx=5, pady=5)
        
        self.label_stay2 = tk.Label(self.frame, text="1F西館洋室")
        self.label_stay2.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.label_stay2_1 = tk.Label(self.frame, text="大人")
        self.label_stay2_1.grid(row=2, column=1, padx=5, pady=5)
        self.label_stay2_2 = tk.Label(self.frame, text="子供")
        self.label_stay2_2.grid(row=2, column=2, padx=5, pady=5)
        self.label_stay2_3 = tk.Label(self.frame, text="大人")
        self.label_stay2_3.grid(row=2, column=3, padx=5, pady=5)
        self.label_stay2_4 = tk.Label(self.frame, text="子供")
        self.label_stay2_4.grid(row=2, column=4, padx=5, pady=5)
        self.label_stay2_5 = tk.Label(self.frame, text="大人")
        self.label_stay2_5.grid(row=2, column=5, padx=5, pady=5)
        self.label_stay2_6 = tk.Label(self.frame, text="子供")
        self.label_stay2_6.grid(row=2, column=6, padx=5, pady=5)
        self.entry_stay2_1 = tk.Entry(self.frame, width=10)
        self.entry_stay2_1.grid(row=3, column=1, padx=5, pady=5)
        self.entry_stay2_2 = tk.Entry(self.frame, width=10)
        self.entry_stay2_2.grid(row=3, column=2, padx=5, pady=5)
        self.entry_stay2_3 = tk.Entry(self.frame, width=10)
        self.entry_stay2_3.grid(row=3, column=3, padx=5, pady=5)
        self.entry_stay2_4 = tk.Entry(self.frame, width=10)
        self.entry_stay2_4.grid(row=3, column=4, padx=5, pady=5)
        self.entry_stay2_5 = tk.Entry(self.frame, width=10)
        self.entry_stay2_5.grid(row=3, column=5, padx=5, pady=5)
        self.entry_stay2_6 = tk.Entry(self.frame, width=10)
        self.entry_stay2_6.grid(row=3, column=6, padx=5, pady=5)

        self.label_stay3 = tk.Label(self.frame, text="岩手山側和室")
        self.label_stay3.grid(row=4, column=0, padx=10, pady=10, sticky='e')
        self.label_stay3_1 = tk.Label(self.frame, text="大人")
        self.label_stay3_1.grid(row=4, column=1, padx=5, pady=5)
        self.label_stay3_2 = tk.Label(self.frame, text="子供")
        self.label_stay3_2.grid(row=4, column=2, padx=5, pady=5)
        self.label_stay3_3 = tk.Label(self.frame, text="大人")
        self.label_stay3_3.grid(row=4, column=3, padx=5, pady=5)
        self.label_stay3_4 = tk.Label(self.frame, text="子供")
        self.label_stay3_4.grid(row=4, column=4, padx=5, pady=5)
        self.label_stay3_5 = tk.Label(self.frame, text="大人")
        self.label_stay3_5.grid(row=4, column=5, padx=5, pady=5)
        self.label_stay3_6 = tk.Label(self.frame, text="子供")
        self.label_stay3_6.grid(row=4, column=6, padx=5, pady=5)

        self.entry_stay3_1 = tk.Entry(self.frame, width=10)
        self.entry_stay3_1.grid(row=5, column=1, padx=5, pady=5)
        self.entry_stay3_2 = tk.Entry(self.frame, width=10)
        self.entry_stay3_2.grid(row=5, column=2, padx=5, pady=5)
        self.entry_stay3_3 = tk.Entry(self.frame, width=10)
        self.entry_stay3_3.grid(row=5, column=3, padx=5, pady=5)
        self.entry_stay3_4 = tk.Entry(self.frame, width=10)
        self.entry_stay3_4.grid(row=5, column=4, padx=5, pady=5)
        self.entry_stay3_5 = tk.Entry(self.frame, width=10)
        self.entry_stay3_5.grid(row=5, column=5, padx=5, pady=5)
        self.entry_stay3_6 = tk.Entry(self.frame, width=10)
        self.entry_stay3_6.grid(row=5, column=6, padx=5, pady=5)

        self.label_stay4 = tk.Label(self.frame, text="岩手山側露天風呂付き和室")
        self.label_stay4.grid(row=6, column=0, padx=10, pady=10, sticky='e')
        self.label_stay4_1 = tk.Label(self.frame, text="大人")
        self.label_stay4_1.grid(row=6, column=1, padx=5, pady=5)
        self.label_stay4_2 = tk.Label(self.frame, text="子供")
        self.label_stay4_2.grid(row=6, column=2, padx=5, pady=5)
        self.label_stay4_3 = tk.Label(self.frame, text="大人")
        self.label_stay4_3.grid(row=6, column=3, padx=5, pady=5)
        self.label_stay4_4 = tk.Label(self.frame, text="子供")
        self.label_stay4_4.grid(row=6, column=4, padx=5, pady=5)
        self.label_stay4_5 = tk.Label(self.frame, text="大人")
        self.label_stay4_5.grid(row=6, column=5, padx=5, pady=5)
        self.label_stay4_6 = tk.Label(self.frame, text="子供")
        self.label_stay4_6.grid(row=6, column=6, padx=5, pady=5)
        self.entry_stay4_1 = tk.Entry(self.frame, width=10)
        self.entry_stay4_1.grid(row=7, column=1, padx=5, pady=5)
        self.entry_stay4_2 = tk.Entry(self.frame, width=10)
        self.entry_stay4_2.grid(row=7, column=2, padx=5, pady=5)
        self.entry_stay4_3 = tk.Entry(self.frame, width=10)
        self.entry_stay4_3.grid(row=7, column=3, padx=5, pady=5)
        self.entry_stay4_4 = tk.Entry(self.frame, width=10)
        self.entry_stay4_4.grid(row=7, column=4, padx=5, pady=5)
        self.entry_stay4_5 = tk.Entry(self.frame, width=10)
        self.entry_stay4_5.grid(row=7, column=5, padx=5, pady=5)
        self.entry_stay4_6 = tk.Entry(self.frame, width=10)
        self.entry_stay4_6.grid(row=7, column=6, padx=5, pady=5)

        self.label_stay5 = tk.Label(self.frame, text="西館和室10畳")
        self.label_stay5.grid(row=8, column=0, padx=10, pady=10, sticky='e')
        self.label_stay5_1 = tk.Label(self.frame, text="大人")
        self.label_stay5_1.grid(row=8, column=1, padx=5, pady=5)
        self.label_stay5_2 = tk.Label(self.frame, text="子供")
        self.label_stay5_2.grid(row=8, column=2, padx=5, pady=5)
        self.label_stay5_3 = tk.Label(self.frame, text="大人")
        self.label_stay5_3.grid(row=8, column=3, padx=5, pady=5)
        self.label_stay5_4 = tk.Label(self.frame, text="子供")
        self.label_stay5_4.grid(row=8, column=4, padx=5, pady=5)
        self.label_stay5_5 = tk.Label(self.frame, text="大人")
        self.label_stay5_5.grid(row=8, column=5, padx=5, pady=5)
        self.label_stay5_6 = tk.Label(self.frame, text="子供")
        self.label_stay5_6.grid(row=8, column=6, padx=5, pady=5)
        self.entry_stay5_1 = tk.Entry(self.frame, width=10)
        self.entry_stay5_1.grid(row=9, column=1, padx=5, pady=5)
        self.entry_stay5_2 = tk.Entry(self.frame, width=10)
        self.entry_stay5_2.grid(row=9, column=2, padx=5, pady=5)
        self.entry_stay5_3 = tk.Entry(self.frame, width=10)
        self.entry_stay5_3.grid(row=9, column=3, padx=5, pady=5)
        self.entry_stay5_4 = tk.Entry(self.frame, width=10)
        self.entry_stay5_4.grid(row=9, column=4, padx=5, pady=5)
        self.entry_stay5_5 = tk.Entry(self.frame, width=10)
        self.entry_stay5_5.grid(row=9, column=5, padx=5, pady=5)
        self.entry_stay5_6 = tk.Entry(self.frame, width=10)
        self.entry_stay5_6.grid(row=9, column=6, padx=5, pady=5)
        
        self.label_stay6 = tk.Label(self.frame, text="1F檜内風呂付き和洋室")
        self.label_stay6.grid(row=10, column=0, padx=10, pady=10, sticky='e')
        self.label_stay6_1 = tk.Label(self.frame, text="大人")
        self.label_stay6_1.grid(row=10, column=1, padx=5, pady=5)
        self.label_stay6_2 = tk.Label(self.frame, text="子供")
        self.label_stay6_2.grid(row=10, column=2, padx=5, pady=5)
        self.label_stay6_3 = tk.Label(self.frame, text="大人")
        self.label_stay6_3.grid(row=10, column=3, padx=5, pady=5)
        self.label_stay6_4 = tk.Label(self.frame, text="子供")
        self.label_stay6_4.grid(row=10, column=4, padx=5, pady=5)
        self.label_stay6_5 = tk.Label(self.frame, text="大人")
        self.label_stay6_5.grid(row=10, column=5, padx=5, pady=5)
        self.label_stay6_6 = tk.Label(self.frame, text="子供")
        self.label_stay6_6.grid(row=10, column=6, padx=5, pady=5)
        self.entry_stay6_1= tk.Entry(self.frame, width=10)
        self.entry_stay6_1.grid(row=11, column=1, padx=5, pady=5)
        self.entry_stay6_2 = tk.Entry(self.frame, width=10)
        self.entry_stay6_2.grid(row=11, column=2, padx=5, pady=5)
        self.entry_stay6_3 = tk.Entry(self.frame, width=10)
        self.entry_stay6_3.grid(row=11, column=3, padx=5, pady=5)
        self.entry_stay6_4 = tk.Entry(self.frame, width=10)
        self.entry_stay6_4.grid(row=11, column=4, padx=5, pady=5)
        self.entry_stay6_5 = tk.Entry(self.frame, width=10)
        self.entry_stay6_5.grid(row=11, column=5, padx=5, pady=5)
        self.entry_stay6_6 = tk.Entry(self.frame, width=10)
        self.entry_stay6_6.grid(row=11, column=6, padx=5, pady=5)
        
        self.label_stay7 = tk.Label(self.frame, text="1F西館和洋室")
        self.label_stay7.grid(row=12, column=0, padx=10, pady=10, sticky='e')
        self.label_stay7_1 = tk.Label(self.frame, text="大人")
        self.label_stay7_1.grid(row=12, column=1, padx=5, pady=5)
        self.label_stay7_2 = tk.Label(self.frame, text="子供")
        self.label_stay7_2.grid(row=12, column=2, padx=5, pady=5)
        self.label_stay7_3 = tk.Label(self.frame, text="大人")
        self.label_stay7_3.grid(row=12, column=3, padx=5, pady=5)
        self.label_stay7_4 = tk.Label(self.frame, text="子供")
        self.label_stay7_4.grid(row=12, column=4, padx=5, pady=5)
        self.label_stay7_5 = tk.Label(self.frame, text="大人")
        self.label_stay7_5.grid(row=12, column=5, padx=5, pady=5)
        self.label_stay7_6 = tk.Label(self.frame, text="子供")
        self.label_stay7_6.grid(row=12, column=6, padx=5, pady=5)
        self.entry_stay7_1 = tk.Entry(self.frame, width=10)
        self.entry_stay7_1.grid(row=13, column=1, padx=5, pady=5)
        self.entry_stay7_2 = tk.Entry(self.frame, width=10)
        self.entry_stay7_2.grid(row=13, column=2, padx=5, pady=5)
        self.entry_stay7_3 = tk.Entry(self.frame, width=10)
        self.entry_stay7_3.grid(row=13, column=3, padx=5, pady=5)
        self.entry_stay7_4 = tk.Entry(self.frame, width=10)
        self.entry_stay7_4.grid(row=13, column=4, padx=5, pady=5)
        self.entry_stay7_5 = tk.Entry(self.frame, width=10)
        self.entry_stay7_5.grid(row=13, column=5, padx=5, pady=5)
        self.entry_stay7_6 = tk.Entry(self.frame, width=10)
        self.entry_stay7_6.grid(row=13, column=6, padx=5, pady=5)
        
        self.label_stay8 = tk.Label(self.frame, text="西館和室28畳")
        self.label_stay8.grid(row=14, column=0, padx=10, pady=10, sticky='e')
        self.label_stay8_1 = tk.Label(self.frame, text="大人")
        self.label_stay8_1.grid(row=14, column=1, padx=5, pady=5)
        self.label_stay8_2 = tk.Label(self.frame, text="子供")
        self.label_stay8_2.grid(row=14, column=2, padx=5, pady=5)
        self.label_stay8_3 = tk.Label(self.frame, text="大人")
        self.label_stay8_3.grid(row=14, column=3, padx=5, pady=5)
        self.label_stay8_4 = tk.Label(self.frame, text="子供")
        self.label_stay8_4.grid(row=14, column=4, padx=5, pady=5)
        self.label_stay8_5 = tk.Label(self.frame, text="大人")
        self.label_stay8_5.grid(row=14, column=5, padx=5, pady=5)
        self.label_stay8_6 = tk.Label(self.frame, text="子供")
        self.label_stay8_6.grid(row=14, column=6, padx=5, pady=5)
        self.entry_stay8_1 = tk.Entry(self.frame, width=10)
        self.entry_stay8_1.grid(row=15, column=1, padx=5, pady=5)
        self.entry_stay8_2 = tk.Entry(self.frame, width=10)
        self.entry_stay8_2.grid(row=15, column=2, padx=5, pady=5)
        self.entry_stay8_3 = tk.Entry(self.frame, width=10)
        self.entry_stay8_3.grid(row=15, column=3, padx=5, pady=5)
        self.entry_stay8_4 = tk.Entry(self.frame, width=10)
        self.entry_stay8_4.grid(row=15, column=4, padx=5, pady=5)
        self.entry_stay8_5 = tk.Entry(self.frame, width=10)
        self.entry_stay8_5.grid(row=15, column=5, padx=5, pady=5)
        self.entry_stay8_6 = tk.Entry(self.frame, width=10)
        self.entry_stay8_6.grid(row=15, column=6, padx=5, pady=5)
        
        # 月
        self.label_month = tk.Label(self.frame, text="月・日")
        self.label_month.grid(row=16, column=0, padx=10, pady=50, sticky='e')
        self.month_var = tk.StringVar()
        self.month_combobox = ttk.Combobox(self.frame, textvariable=self.month_var, state="readonly", width=6)
        self.month_combobox['values'] = [f"{i}月" for i in range(1, 13)]
        self.month_combobox.grid(row=16, column=1, padx=5, pady=10)
        self.month_combobox.bind("<<ComboboxSelected>>", self.update_days)
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
        # 土日祝日のチェックボタン(true/false)
        self.check_sunday_var = tk.BooleanVar()
        self.check_sunday = tk.Checkbutton(self.frame, text="土日祝日", variable=self.check_sunday_var, width=20)
        self.check_sunday.grid(row=18, column=1, padx=5, pady=5, sticky='w')
        # 早割りのラジオボタン
        self.early_discount_var = tk.StringVar(value="なし")  # デフォルトはなし
        # self.radio_2000 = tk.Radiobutton(self.frame, text="土日祝+2,000", variable=self.early_discount_var, value="2000", width=20)
        self.radio_60 = tk.Radiobutton(self.frame, text="60日以前 10%", variable=self.early_discount_var, value="60", width=20)
        self.radio_90 = tk.Radiobutton(self.frame, text="90日以前 15%", variable=self.early_discount_var, value="90", width=20)
        self.radio_no_discount = tk.Radiobutton(self.frame, text="なし", variable=self.early_discount_var, value="なし", width=20)
        # self.radio_2000.grid(row=18, column=1, padx=5, pady=5, sticky='w')
        self.radio_60.grid(row=19, column=1, padx=5, pady=5, sticky='w')
        self.radio_90.grid(row=20, column=1, padx=5, pady=5, sticky='w')
        self.radio_no_discount.grid(row=21, column=1, padx=5, pady=5, sticky='w')
        # オプション
        
        # ドックワン
        self.label_options = tk.Label(self.frame, text="ドックワン")
        self.label_options.grid(row=23, column=0, padx=10, pady=10, sticky='e')
        self.label_num = tk.Label(self.frame, text="数")
        self.label_num.grid(row=23, column=1, padx=5, pady=5)
        self.label_supa = tk.Label(self.frame, text="スパ入浴")
        self.label_supa.grid(row=23, column=2, padx=5, pady=5)
        self.entry_dog_wan_adult = tk.Entry(self.frame, width=10)
        self.entry_dog_wan_adult.grid(row=24, column=1, padx=5, pady=5)
        self.entry_dog_wan_child = tk.Entry(self.frame, width=10)
        self.entry_dog_wan_child.grid(row=24, column=2, padx=5, pady=5)
        
        #岩盤浴 
        self.label_gan = tk.Label(self.frame, text="岩盤浴")
        self.label_gan.grid(row=25, column=0, padx=10, pady=10, sticky='e')
        self.label_stay = tk.Label(self.frame, text="宿泊者")
        self.label_stay.grid(row=25, column=1, padx=5, pady=5)
        self.label_no_stay = tk.Label(self.frame, text="その他")
        self.label_no_stay.grid(row=25, column=2, padx=5, pady=5)
        self.entry_stay = tk.Entry(self.frame, width=10)
        self.entry_stay.grid(row=26, column=1, padx=5, pady=5)
        self.entry_no_stay = tk.Entry(self.frame, width=10)
        self.entry_no_stay.grid(row=26, column=2, padx=5, pady=5)
        # パターゴルフ
        self.label_pata = tk.Label(self.frame, text="パターゴルフ")
        self.label_pata.grid(row=27, column=0, padx=10, pady=10, sticky='e')
        self.label_pata_otona = tk.Label(self.frame, text="大人")
        self.label_pata_otona.grid(row=27, column=1, padx=5, pady=5)
        self.label_pata_kodomo= tk.Label(self.frame, text="子供")
        self.label_pata_kodomo.grid(row=27, column=2, padx=5, pady=5)
        self.entry_pata_otona = tk.Entry(self.frame, width=10)
        self.entry_pata_otona.grid(row=28, column=1, padx=5, pady=5)
        self.entry_pata_kodomo = tk.Entry(self.frame, width=10)
        self.entry_pata_kodomo.grid(row=28, column=2, padx=5, pady=5)
        # パークゴルフ
        self.label_paku = tk.Label(self.frame, text="パークゴルフ")
        self.label_paku.grid(row=29, column=0, padx=10, pady=10, sticky='e')
        self.label_paku_otona = tk.Label(self.frame, text="大人")
        self.label_paku_otona.grid(row=29, column=1, padx=5, pady=5)
        self.label_paku_kodomo = tk.Label(self.frame, text="子供")
        self.label_paku_kodomo.grid(row=29, column=2, padx=5, pady=5)
        self.entry_paku_otona = tk.Entry(self.frame, width=10)
        self.entry_paku_otona.grid(row=30, column=1, padx=5, pady=5)
        self.entry_paku_kodomo = tk.Entry(self.frame, width=10)
        self.entry_paku_kodomo.grid(row=30, column=2, padx=5, pady=5)    
        # テニスコート
        self.label_teni = tk.Label(self.frame, text="テニスコート")
        self.label_teni.grid(row=31, column=0, padx=10, pady=10, sticky='e')
        self.label_teni_stay = tk.Label(self.frame, text="宿泊者")
        self.label_teni_stay.grid(row=31, column=1, padx=5, pady=5)
        self.label_teni_no_stay = tk.Label(self.frame, text="外来者")
        self.label_teni_no_stay.grid(row=31, column=2, padx=5, pady=5)
        self.label_en = tk.Label(self.frame, text="延長(1h)")
        self.label_en.grid(row=31, column=3, padx=5, pady=5)
        self.label_ball = tk.Label(self.frame, text="ボール")
        self.label_ball.grid(row=31, column=4, padx=5, pady=5)
        self.entry_teni_stay = tk.Entry(self.frame, width=10)
        self.entry_teni_stay.grid(row=32, column=1, padx=5, pady=5)
        self.entry_teni_no_stay = tk.Entry(self.frame, width=10)
        self.entry_teni_no_stay.grid(row=32, column=2, padx=5, pady=5)
        self.entry_teni_en = tk.Entry(self.frame, width=10)
        self.entry_teni_en.grid(row=32, column=3, padx=5, pady=5)
        self.entry_teni_ball = tk.Entry(self.frame, width=10)
        self.entry_teni_ball.grid(row=32, column=4, padx=5, pady=5)
        # 温泉貸切
        self.label_kasikiri = tk.Label(self.frame, text="温泉貸切")
        self.label_kasikiri.grid(row=33, column=0, padx=10, pady=10, sticky='e')
        self.label_kasikiri_num = tk.Label(self.frame, text="人数")
        self.label_kasikiri_num.grid(row=33, column=1, padx=5, pady=5)
        self.entry_kasikiri_num = tk.Entry(self.frame, width=10)
        self.entry_kasikiri_num.grid(row=34, column=1, padx=5, pady=5)
        # （見積もりへ）ボタン
        self.button_next = tk.Button(self.frame, text="見積もりへ", command=self.goto_estimate)
        self.button_next.grid(row=36, column=0, columnspan=7, pady=20)
        # フレームのサイズを自動調整
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        # マウスホイールでスクロールできるようにする
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)  # Windows, Mac
        self.canvas.bind_all("<Button-4>", self._on_mousewheel)    # Linux (scroll up)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel)    # Linux (scroll down)
    # 月が選択されたときに日を更新するメソッド
    def update_days(self, event=None):
        selected_month = self.month_var.get().replace('月', '')
        try:
            num_days = calendar.monthrange(datetime.now().year, int(selected_month))[1]
        except ValueError:
            return
        days = [str(i) for i in range(1, num_days+1)]
        self.day_combobox['values'] = days  
        
    def _on_mousewheel(self, event):
        if event.num == 4:  # Linux scroll up
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:  # Linux scroll down
            self.canvas.yview_scroll(1, "units")
        else:  # Windows and macOS
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
               
    def goto_estimate(self):
        def safe_int(value):
            return int(value) if value.isdigit() else 0
        
        # 和室 (本館和室7.5畳)
        wasitu1_otona_poku = safe_int(self.entry_stay1_1.get())
        wasitu1_kodomo_poku = safe_int(self.entry_stay1_2.get())
        wasitu1_otona_iwategyu = safe_int(self.entry_stay1_3.get())
        wasitu1_kodomo_iwategyu = safe_int(self.entry_stay1_4.get())
        wasitu1_otona_maezawagyu = safe_int(self.entry_stay1_5.get())
        wasitu1_kodomo_maezawagyu = safe_int(self.entry_stay1_6.get())

        # 1F西館洋室
        nishikan1_otona_poku = safe_int(self.entry_stay2_1.get())
        nishikan1_kodomo_poku = safe_int(self.entry_stay2_2.get())
        nishikan1_otona_iwategyu = safe_int(self.entry_stay2_3.get())
        nishikan1_kodomo_iwategyu = safe_int(self.entry_stay2_4.get())
        nishikan1_otona_maezawagyu = safe_int(self.entry_stay2_5.get())
        nishikan1_kodomo_maezawagyu = safe_int(self.entry_stay2_6.get())

        # 岩手山側和室
        iwatesan_otona_poku = safe_int(self.entry_stay3_1.get())
        iwatesan_kodomo_poku = safe_int(self.entry_stay3_2.get())
        iwatesan_otona_iwategyu = safe_int(self.entry_stay3_3.get())
        iwatesan_kodomo_iwategyu = safe_int(self.entry_stay3_4.get())
        iwatesan_otona_maezawagyu = safe_int(self.entry_stay3_5.get())
        iwatesan_kodomo_maezawagyu = safe_int(self.entry_stay3_6.get())

        # 岩手山側露天風呂付き和室
        iwatesan_roten_otona_poku = safe_int(self.entry_stay4_1.get())
        iwatesan_roten_kodomo_poku = safe_int(self.entry_stay4_2.get())
        iwatesan_roten_otona_iwategyu = safe_int(self.entry_stay4_3.get())
        iwatesan_roten_kodomo_iwategyu = safe_int(self.entry_stay4_4.get())
        iwatesan_roten_otona_maezawagyu = safe_int(self.entry_stay4_5.get())
        iwatesan_roten_kodomo_maezawagyu = safe_int(self.entry_stay4_6.get())

        # 西館和室10畳
        nishikan10_otona_poku = safe_int(self.entry_stay5_1.get())
        nishikan10_kodomo_poku = safe_int(self.entry_stay5_2.get())
        nishikan10_otona_iwategyu = safe_int(self.entry_stay5_3.get())
        nishikan10_kodomo_iwategyu = safe_int(self.entry_stay5_4.get())
        nishikan10_otona_maezawagyu = safe_int(self.entry_stay5_5.get())
        nishikan10_kodomo_maezawagyu = safe_int(self.entry_stay5_6.get())

        # 1F檜内風呂付き和洋室
        hinoki_otona_poku = safe_int(self.entry_stay6_1.get())
        hinoki_kodomo_poku = safe_int(self.entry_stay6_2.get())
        hinoki_otona_iwategyu = safe_int(self.entry_stay6_3.get())
        hinoki_kodomo_iwategyu = safe_int(self.entry_stay6_4.get())
        hinoki_otona_maezawagyu = safe_int(self.entry_stay6_5.get())
        hinoki_kodomo_maezawagyu = safe_int(self.entry_stay6_6.get())

        # 1F西館和洋室
        nishikan1F_otona_poku = safe_int(self.entry_stay7_1.get())
        nishikan1F_kodomo_poku = safe_int(self.entry_stay7_2.get())
        nishikan1F_otona_iwategyu = safe_int(self.entry_stay7_3.get())
        nishikan1F_kodomo_iwategyu = safe_int(self.entry_stay7_4.get())
        nishikan1F_otona_maezawagyu = safe_int(self.entry_stay7_5.get())
        nishikan1F_kodomo_maezawagyu = safe_int(self.entry_stay7_6.get())

        # 西館和室28畳
        nishikan28_otona_poku = safe_int(self.entry_stay8_1.get())
        nishikan28_kodomo_poku = safe_int(self.entry_stay8_2.get())
        nishikan28_otona_iwategyu = safe_int(self.entry_stay8_3.get())
        nishikan28_kodomo_iwategyu = safe_int(self.entry_stay8_4.get())
        nishikan28_otona_maezawagyu = safe_int(self.entry_stay8_5.get())
        nishikan28_kodomo_maezawagyu = safe_int(self.entry_stay8_6.get())
        
        
        ## 現在選択されている月・日・宿泊数・早割りの内容を取得
        self.check_sunday = self.check_sunday_var.get()
        selected_month = self.month_var.get()
        selected_day = self.day_var.get()
        selected_stay_count = safe_int(self.stay_count_var.get())
        selected_early_discount = safe_int(self.early_discount_var.get())

        dog_wan_adult = safe_int(self.entry_dog_wan_adult.get())
        dog_wan_child = safe_int(self.entry_dog_wan_child.get())
        gan_stay = safe_int(self.entry_stay.get())
        gan_no_stay = safe_int(self.entry_no_stay.get())
        pata_otona = safe_int(self.entry_pata_otona.get())
        pata_kodomo = safe_int(self.entry_pata_kodomo.get())
        paku_otona = safe_int(self.entry_paku_otona.get())
        paku_kodomo = safe_int(self.entry_paku_kodomo.get())
        teni_stay = safe_int(self.entry_teni_stay.get())
        teni_no_stay = safe_int(self.entry_no_stay.get())
        teni_en = safe_int(self.entry_teni_en.get())
        teni_ball = safe_int(self.entry_teni_ball.get())
        kasikiri_num = safe_int(self.entry_kasikiri_num.get())
    
        self.frame.destroy()
        self.canvas.destroy()
        self.destroy()
        
        # 見積もり画面に遷移
        from estimateStay import EstimateStay
        EstimateStay(self.master, wasitu1_kodomo_iwategyu, wasitu1_kodomo_maezawagyu, wasitu1_otona_iwategyu, wasitu1_otona_maezawagyu, wasitu1_kodomo_poku, wasitu1_otona_poku, nishikan1_kodomo_iwategyu, nishikan1_kodomo_maezawagyu, nishikan1_otona_iwategyu, nishikan1_otona_maezawagyu, nishikan1_kodomo_poku, nishikan1_otona_poku, iwatesan_kodomo_iwategyu, iwatesan_kodomo_maezawagyu, iwatesan_otona_iwategyu, iwatesan_otona_maezawagyu, iwatesan_kodomo_poku, iwatesan_otona_poku, iwatesan_roten_kodomo_iwategyu, iwatesan_roten_kodomo_maezawagyu, iwatesan_roten_otona_iwategyu, iwatesan_roten_otona_maezawagyu, iwatesan_roten_kodomo_poku, iwatesan_roten_otona_poku, nishikan10_kodomo_iwategyu, nishikan10_kodomo_maezawagyu, nishikan10_otona_iwategyu, nishikan10_otona_maezawagyu, nishikan10_kodomo_poku, nishikan10_otona_poku,
        hinoki_kodomo_iwategyu, hinoki_kodomo_maezawagyu, hinoki_otona_iwategyu, hinoki_otona_maezawagyu, hinoki_kodomo_poku, hinoki_otona_poku, nishikan1F_kodomo_iwategyu, nishikan1F_kodomo_maezawagyu, nishikan1F_otona_iwategyu, nishikan1F_otona_maezawagyu, nishikan1F_kodomo_poku, nishikan1F_otona_poku, nishikan28_kodomo_iwategyu, nishikan28_kodomo_maezawagyu, nishikan28_otona_iwategyu, nishikan28_otona_maezawagyu, nishikan28_kodomo_poku, nishikan28_otona_poku,selected_month, selected_day, selected_stay_count, selected_early_discount, dog_wan_adult, dog_wan_child, gan_stay, gan_no_stay, pata_otona, pata_kodomo, paku_otona, paku_kodomo, teni_stay, teni_no_stay, teni_en, teni_ball, kasikiri_num, self.name, self.mail, self.check_sunday)
    
        
if __name__ == '__main__':
    root = tk.Tk()
    app = Stay(root, 1, 1)
    app.mainloop()

