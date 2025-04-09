import tkinter as tk
from tkinter import ttk
import json
import datetime

class EstimateBanquet(tk.Frame):
  def __init__(self, master, num_people, month, date, num_gouka, num_miyabi, num_nishiki, num_tubaki, num_nomi, num_loin, num_hormone, num_kushiyaki, num_iwatehuro, num_hinokihuro, increse_date):
    super().__init__(master)
    self.pack()
    
    master.state('zoomed')
    master.geometry('420x550')
    master.title('見積もり画面（宴会）')
    
        # 受け取ったパラメータをインスタンス変数として保存
    self.num_people = num_people
    self.month = month
    self.date = date
    self.num_gouka = num_gouka
    self.num_miyabi = num_miyabi
    self.num_nishiki = num_nishiki
    self.num_tubaki = num_tubaki
    self.num_nomi = num_nomi
    self.num_loin = num_loin
    self.num_hormone = num_hormone
    self.num_kushiyaki = num_kushiyaki
    self.num_iwatehuro = num_iwatehuro
    self.num_hinokihuro = num_hinokihuro
    self.increse_date = increse_date
    
    self.create_widgets()

  # ウィジェットを配置して画面作るメソッド
  def create_widgets(self):
      tk.Label(self, text='').grid(row=0, column=0, padx=10, pady=5)
      tk.Label(self, text='宴会').grid(row=1, column=0, padx=10, pady=5)
      ttk.Separator(self, orient='vertical').grid(row=1, column=1, rowspan=14, sticky='ns', padx=5)
      tk.Label(self, text='単価').grid(row=1, column=2, padx=10, pady=5)
      tk.Label(self, text='注文数').grid(row=1, column=4, padx=10, pady=5)
      tk.Label(self, text='合計').grid(row=1, column=5, padx=10, pady=5)
      ttk.Separator(self, orient='horizontal').grid(row=2, column=0, columnspan=14, sticky='ew', pady=5)
      tk.Label(self, text='豪華コース').grid(row=3, column=0, padx=10, pady=5)
      tk.Label(self, text='雅コース').grid(row=4, column=0, padx=10, pady=5)
      tk.Label(self, text='錦コース').grid(row=5, column=0, padx=10, pady=5)
      tk.Label(self, text='椿コース').grid(row=6, column=0, padx=10, pady=5)
      tk.Label(self, text='飲み放題').grid(row=7, column=0, padx=10, pady=5)
      tk.Label(self, text='追加料理').grid(row=8, column=0, padx=10, pady=5)
      tk.Label(self, text='八幡平牛ロースのしゃぶしゃぶ').grid(row=9, column=0, padx=10, pady=5)
      tk.Label(self, text='大更ホルモン鍋').grid(row=10, column=0, padx=10, pady=5)
      tk.Label(self, text='岩手県産牛の串焼き').grid(row=11, column=0, padx=10, pady=5)
      tk.Label(self, text='部屋グレード').grid(row=12, column=0, padx=10, pady=5)
      tk.Label(self, text='岩手山展望露天風呂付和室').grid(row=13, column=0, padx=10, pady=5)
      tk.Label(self, text='檜の内風呂付和洋室').grid(row=14, column=0, padx=10, pady=5)
      tk.Label(self, text='').grid(row=15, column=0, padx=10, pady=5)
      tk.Label(self, text='土日祝日').grid(row=16, column=0, padx=10, pady=5)
      if self.increse_date == 0:
        tk.Label(self, text='無').grid(row=16, column=1, padx=10, pady=5)
      else:
        tk.Label(self, text='有').grid(row=16, column=1, padx=10, pady=5)
      tk.Label(self, text='合計料金').grid(row=17, column=0, padx=10, pady=5)
      
      tk.Label(self, text='21600').grid(row=3, column=2, padx=10, pady=5)
      tk.Label(self, text='18600').grid(row=4, column=2, padx=10, pady=5)
      tk.Label(self, text='15800').grid(row=5, column=2, padx=10, pady=5)
      tk.Label(self, text='12600').grid(row=6, column=2, padx=10, pady=5)
      tk.Label(self, text='2800').grid(row=7, column=2, padx=10, pady=5)
      tk.Label(self, text='4000').grid(row=9, column=2, padx=10, pady=5)
      tk.Label(self, text='1100').grid(row=10, column=2, padx=10, pady=5)
      tk.Label(self, text='750').grid(row=11, column=2, padx=10, pady=5)
      tk.Label(self, text='2000').grid(row=13, column=2, padx=10, pady=5)
      tk.Label(self, text='3000').grid(row=14, column=2, padx=10, pady=5)
      
      tk.Label(self, text=self.num_gouka).grid(row=3, column=4, padx=10, pady=5)
      tk.Label(self, text=self.num_miyabi).grid(row=4, column=4, padx=10, pady=5)
      tk.Label(self, text=self.num_nishiki).grid(row=5, column=4, padx=10, pady=5)
      tk.Label(self, text=self.num_tubaki).grid(row=6, column=4, padx=10, pady=5)
      tk.Label(self, text=self.num_nomi).grid(row=7, column=4, padx=10, pady=5)
      tk.Label(self, text=self.num_loin).grid(row=9, column=4, padx=10, pady=5)
      tk.Label(self, text=self.num_hormone).grid(row=10, column=4, padx=10, pady=5)
      tk.Label(self, text=self.num_kushiyaki).grid(row=11, column=4, padx=10, pady=5)
      tk.Label(self, text=self.num_iwatehuro).grid(row=13, column=4, padx=10, pady=5)
      tk.Label(self, text=self.num_hinokihuro).grid(row=14, column=4, padx=10, pady=5)
      
      tk.Label(self, text=21600 * self.num_gouka).grid(row=3, column=5, padx=10, pady=5)
      tk.Label(self, text=18600 * self.num_miyabi).grid(row=4, column=5, padx=10, pady=5)
      tk.Label(self, text=15800 * self.num_nishiki).grid(row=5, column=5, padx=10, pady=5)
      tk.Label(self, text=12600 * self.num_tubaki).grid(row=6, column=5, padx=10, pady=5)
      tk.Label(self, text=2800 * self.num_nomi).grid(row=7, column=5, padx=10, pady=5)
      tk.Label(self, text=4000 * self.num_loin).grid(row=9, column=5, padx=10, pady=5)
      tk.Label(self, text=1100 * self.num_hormone).grid(row=10, column=5, padx=10, pady=5)
      tk.Label(self, text=750 * self.num_kushiyaki).grid(row=11, column=5, padx=10, pady=5)
      tk.Label(self, text=2000 * self.num_iwatehuro).grid(row=13, column=5, padx=10, pady=5)
      tk.Label(self, text=3000 * self.num_hinokihuro).grid(row=14, column=5, padx=10, pady=5)
      
      self.total = 21600 * self.num_gouka + 18600 * self.num_miyabi + 15800 * self.num_nishiki + 12600 * self.num_tubaki + 2800 * self.num_nomi + 4000 * self.num_loin + 1100 * self.num_hormone + 750 * self.num_kushiyaki + 2000 * self.num_iwatehuro + 3000 * self.num_hinokihuro
      if self.increse_date:
        self.total += 2200
      tk.Label(self, text=self.total).grid(row=17, column=1, padx=10, pady=5)
      
      self.mail_btn = tk.Button(self, text='メール送信' ,command=self.send_mail)
      self.mail_btn.grid(row=18, column=0, padx=10, pady=5)
      self.jason_btn = tk.Button(self, text='ジェイソンファイル保存', command=self.save_to_json)
      self.jason_btn.grid(row=18, column=1, padx=10, pady=5)
      

  def save_to_json(self):
        data = {
            "num_people": self.num_people,
            "month": self.month,
            "date": self.date,
            "num_gouka": self.num_gouka,
            "num_miyabi": self.num_miyabi,
            "num_nishiki": self.num_nishiki,
            "num_tubaki": self.num_tubaki,
            "num_nomi": self.num_nomi,
            "num_loin": self.num_loin,
            "num_hormone": self.num_hormone,
            "num_kushiyaki": self.num_kushiyaki,
            "num_iwatehuro": self.num_iwatehuro,
            "num_hinokihuro": self.num_hinokihuro,
            "increse_date": self.increse_date,
            "total": self.total
        }

        filename = f"estimate_{datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"{filename} に保存しました！")
    
  def send_mail(self):
    pass
 
      
if __name__ == '__main__':
  root = tk.Tk()
  app = EstimateBanquet(root, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
  app.mainloop()
