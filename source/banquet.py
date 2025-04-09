import tkinter as tk
from tkinter import ttk

class Banquet(tk.Frame):
    def __init__(self, master, name, mail):
        super().__init__(master)
        self.pack()
        
        self.name = name
        self.mail = mail
        master.state('zoomed')
        master.geometry('700x550')
        master.title('宴会画面')

        self.create_widgets()

    def create_widgets(self):
        # 人数
        tk.Label(self, text='人数').grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.people_input = tk.Entry(self, width=10)
        self.people_input.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self, text='人').grid(row=0, column=2, padx=10, pady=5)

        # 日付選択
        tk.Label(self, text='日付').grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.month_pulldown = ttk.Combobox(self, width=4, values=[f"{i}月" for i in range(1, 13)])
        self.month_pulldown.current(0)
        self.month_pulldown.grid(row=1, column=1, padx=5, pady=5)
        self.day_pulldown = ttk.Combobox(self, width=4, values=[f"{i}日" for i in range(1, 32)])
        self.day_pulldown.current(0)
        self.day_pulldown.grid(row=1, column=2, padx=5, pady=5)

        # コース
        tk.Label(self, text='コース').grid(row=2, column=0, padx=10, pady=5, sticky="w")
        courses = ["豪華", "雅（みやび）", "錦（にしき）", "椿（つばき）"]
        self.course_inputs = {}

        for i, course in enumerate(courses):
            tk.Label(self, text=course).grid(row=3+i, column=0, padx=10, pady=5, sticky="w")
            self.course_inputs[course] = tk.Entry(self, width=10)
            self.course_inputs[course].grid(row=3+i, column=1, padx=10, pady=5)
            tk.Label(self, text='人').grid(row=3+i, column=2, padx=10, pady=5)

        # 飲み放題
        tk.Label(self, text='飲み放題').grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.nomi_input = tk.Entry(self, width=10)
        self.nomi_input.grid(row=8, column=1, padx=10, pady=5)
        tk.Label(self, text='人分').grid(row=8, column=2, padx=10, pady=5)

        # 追加料理
        tk.Label(self, text='追加料理').grid(row=9, column=0, padx=10, pady=5, sticky="w")
        dishes = ["八幡平牛ロースのしゃぶしゃぶ", "大更ホルモン鍋", "岩手県産牛の串焼き"]
        self.dish_inputs = {}

        for i, dish in enumerate(dishes):
            tk.Label(self, text=dish).grid(row=10+i, column=0, padx=10, pady=5, sticky="w")
            self.dish_inputs[dish] = tk.Entry(self, width=10)
            self.dish_inputs[dish].grid(row=10+i, column=1, padx=10, pady=5)
            tk.Label(self, text="人前").grid(row=10+i, column=2, padx=10, pady=5)

        # 部屋グレード
        tk.Label(self, text='部屋グレード').grid(row=13, column=0, padx=10, pady=5, sticky="w")
        rooms = ["岩手山展望露天風呂付和室", "檜の内風呂付和洋室"]
        self.room_inputs = {}

        for i, room in enumerate(rooms):
            tk.Label(self, text=room).grid(row=14+i, column=0, padx=10, pady=5, sticky="w")
            self.room_inputs[room] = tk.Entry(self, width=10)
            self.room_inputs[room].grid(row=14+i, column=1, padx=10, pady=5)
            tk.Label(self, text="部屋").grid(row=14+i, column=2, padx=10, pady=5)

        # 土日祝日
        tk.Label(self, text='土日祝日').grid(row=16, column=0, padx=10, pady=5, sticky="w")
        self.increase_date_value = tk.BooleanVar(value=False)
        tk.Checkbutton(self, variable=self.increase_date_value).grid(row=16, column=1, padx=10, pady=5)
        
        # # 合計金額
        # tk.Label(self, text='合計金額').grid(row=17, column=0, padx=10, pady=5, sticky="w")
        # self.total_amount = 0
        # tk.Label(self, text=f'{self.total_amount}円').grid(row=17, column=1, padx=10, pady=5)
        
        
        # 見積もり画面へ
        tk.Button(self, text='見積もりへ', command=self.btn).grid(row=19, column=2, padx=10, pady=5)
        
    def btn(self):
        def safe_int(value):
         return int(value) if value.isdigit() else 0
        
        mounth = self.month_pulldown.get()
        date = self.day_pulldown.get()
        num_people = safe_int(self.people_input.get())
        num_gouka = safe_int(self.course_inputs['豪華'].get())
        num_miyabi = safe_int(self.course_inputs['雅（みやび）'].get())
        num_nishiki = safe_int(self.course_inputs['錦（にしき）'].get())
        num_tubaki = safe_int(self.course_inputs['椿（つばき）'].get())
        num_nomi = safe_int(self.nomi_input.get())
        num_loin = safe_int(self.dish_inputs["八幡平牛ロースのしゃぶしゃぶ"].get())
        num_hormone = safe_int(self.dish_inputs["大更ホルモン鍋"].get())
        num_kushiyaki = safe_int(self.dish_inputs["岩手県産牛の串焼き"].get())
        num_iwatehuro = safe_int(self.room_inputs['岩手山展望露天風呂付和室'].get())
        num_hinokihuro = safe_int(self.room_inputs['檜の内風呂付和洋室'].get())
        increse_date = self.increase_date_value.get()
        
        self.destroy()
        from estimateBanquet import EstimateBanquet
        EstimateBanquet(self.master, num_people, mounth, date, num_gouka, num_miyabi, num_nishiki, num_tubaki, num_nomi, num_loin, num_hormone, num_kushiyaki, num_iwatehuro, num_hinokihuro, increse_date, self.mail, self.name)
    


if __name__ == '__main__':
    root = tk.Tk()
    app = Banquet(root, 1, 1)
    app.mainloop()
