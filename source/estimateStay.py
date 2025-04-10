import tkinter as tk
from tkinter import ttk
import json
import datetime

class EstimateStay(tk.Frame):
  def __init__(self, master, wasitu1_kodomo_iwategyu, wasitu1_kodomo_maezawagyu, wasitu1_otona_iwategyu, wasitu1_otona_maezawagyu, wasitu1_kodomo_poku, wasitu1_otona_poku, nishikan1_kodomo_iwategyu, nishikan1_kodomo_maezawagyu, nishikan1_otona_iwategyu, nishikan1_otona_maezawagyu, nishikan1_kodomo_poku, nishikan1_otona_poku, iwatesan_kodomo_iwategyu, iwatesan_kodomo_maezawagyu, iwatesan_otona_iwategyu, iwatesan_otona_maezawagyu, iwatesan_kodomo_poku, iwatesan_otona_poku, iwatesan_roten_kodomo_iwategyu, iwatesan_roten_kodomo_maezawagyu, iwatesan_roten_otona_iwategyu, iwatesan_roten_otona_maezawagyu, iwatesan_roten_kodomo_poku, iwatesan_roten_otona_poku, nishikan10_kodomo_iwategyu, nishikan10_kodomo_maezawagyu, nishikan10_otona_iwategyu, nishikan10_otona_maezawagyu, nishikan10_kodomo_poku, nishikan10_otona_poku,
        hinoki_kodomo_iwategyu, hinoki_kodomo_maezawagyu, hinoki_otona_iwategyu, hinoki_otona_maezawagyu, hinoki_kodomo_poku, hinoki_otona_poku, nishikan1F_kodomo_iwategyu, nishikan1F_kodomo_maezawagyu, nishikan1F_otona_iwategyu, nishikan1F_otona_maezawagyu, nishikan1F_kodomo_poku, nishikan1F_otona_poku, nishikan28_kodomo_iwategyu, nishikan28_kodomo_maezawagyu, nishikan28_otona_iwategyu, nishikan28_otona_maezawagyu, nishikan28_kodomo_poku, nishikan28_otona_poku,selected_month, selected_day, selected_stay_count, selected_early_discount, dog_wan_adult, dog_wan_child, gan_stay, gan_no_stay, pata_otona, pata_kodomo, paku_otona, paku_kodomo, teni_stay, teni_no_stay, teni_en, teni_ball, kasikiri_num, name, mail, check_sunday):
    super().__init__(master)
    self.pack()
    
    self.check_sunday = check_sunday
    self.name = name
    self.mail = mail
    self.wasitu1_kodomo_iwategyu = wasitu1_kodomo_iwategyu
    self.wasitu1_kodomo_maezawagyu = wasitu1_kodomo_maezawagyu
    self.wasitu1_otona_iwategyu = wasitu1_otona_iwategyu
    self.wasitu1_otona_maezawagyu = wasitu1_otona_maezawagyu
    self.wasitu1_kodomo_poku = wasitu1_kodomo_poku
    self.wasitu1_otona_poku = wasitu1_otona_poku
    self.nishikan1_kodomo_iwategyu = nishikan1_kodomo_iwategyu
    self.nishikan1_kodomo_maezawagyu = nishikan1_kodomo_maezawagyu
    self.nishikan1_otona_iwategyu = nishikan1_otona_iwategyu
    self.nishikan1_otona_maezawagyu = nishikan1_otona_maezawagyu
    self.nishikan1_kodomo_poku = nishikan1_kodomo_poku
    self.nishikan1_otona_poku = nishikan1_otona_poku
    self.iwatesan_kodomo_iwategyu = iwatesan_kodomo_iwategyu
    self.iwatesan_kodomo_maezawagyu = iwatesan_kodomo_maezawagyu
    self.iwatesan_otona_iwategyu = iwatesan_otona_iwategyu
    self.iwatesan_otona_maezawagyu = iwatesan_otona_maezawagyu
    self.iwatesan_kodomo_poku = iwatesan_kodomo_poku
    self.iwatesan_otona_poku = iwatesan_otona_poku
    self.iwatesan_roten_kodomo_iwategyu = iwatesan_roten_kodomo_iwategyu
    self.iwatesan_roten_kodomo_maezawagyu = iwatesan_roten_kodomo_maezawagyu
    self.iwatesan_roten_otona_iwategyu = iwatesan_roten_otona_iwategyu
    self.iwatesan_roten_otona_maezawagyu = iwatesan_roten_otona_maezawagyu
    self.iwatesan_roten_kodomo_poku = iwatesan_roten_kodomo_poku
    self.iwatesan_roten_otona_poku = iwatesan_roten_otona_poku
    self.nishikan10_kodomo_iwategyu = nishikan10_kodomo_iwategyu
    self.nishikan10_kodomo_maezawagyu = nishikan10_kodomo_maezawagyu
    self.nishikan10_otona_iwategyu = nishikan10_otona_iwategyu
    self.nishikan10_otona_maezawagyu = nishikan10_otona_maezawagyu
    self.nishikan10_kodomo_poku = nishikan10_kodomo_poku
    self.nishikan10_otona_poku = nishikan10_otona_poku
    self.hinoki_kodomo_iwategyu = hinoki_kodomo_iwategyu
    self.hinoki_kodomo_maezawagyu = hinoki_kodomo_maezawagyu
    self.hinoki_otona_iwategyu = hinoki_otona_iwategyu
    self.hinoki_otona_maezawagyu = hinoki_otona_maezawagyu
    self.hinoki_kodomo_poku = hinoki_kodomo_poku
    self.hinoki_otona_poku = hinoki_otona_poku
    self.nishikan1F_kodomo_iwategyu = nishikan1F_kodomo_iwategyu
    self.nishikan1F_kodomo_maezawagyu = nishikan1F_kodomo_maezawagyu
    self.nishikan1F_otona_iwategyu = nishikan1F_otona_iwategyu
    self.nishikan1F_otona_maezawagyu = nishikan1F_otona_maezawagyu
    self.nishikan1F_kodomo_poku = nishikan1F_kodomo_poku
    self.nishikan1F_otona_poku = nishikan1F_otona_poku
    self.nishikan28_kodomo_iwategyu = nishikan28_kodomo_iwategyu
    self.nishikan28_kodomo_maezawagyu = nishikan28_kodomo_maezawagyu
    self.nishikan28_otona_iwategyu = nishikan28_otona_iwategyu
    self.nishikan28_otona_maezawagyu = nishikan28_otona_maezawagyu
    self.nishikan28_kodomo_poku = nishikan28_kodomo_poku
    self.nishikan28_otona_poku = nishikan28_otona_poku
    self.selected_month = selected_month
    self.selected_day = selected_day
    self.selected_stay_count = selected_stay_count
    self.selected_early_discount = selected_early_discount
    self.dog_wan_adult = dog_wan_adult
    self.dog_wan_child = dog_wan_child
    self.gan_stay = gan_stay
    self.gan_no_stay = gan_no_stay
    self.pata_otona = pata_otona
    self.pata_kodomo = pata_kodomo
    self.paku_otona = paku_otona
    self.paku_kodomo = paku_kodomo
    self.teni_stay = teni_stay
    self.teni_no_stay = teni_no_stay
    self.teni_en = teni_en
    self.teni_ball = teni_ball
    self.kasikiri_num = kasikiri_num
    self.kasikiri_num = kasikiri_num
    
    master.state('zoomed')
    master.geometry('420x550')
    master.title('見積もり画面（宿泊）')

    self.create_widgets()

  # ウィジェットを配置して画面作るメソッド
  def create_widgets(self):
      tk.Label(self, text='').grid(row=0, column=0, padx=10, pady=5)
      tk.Label(self, text='宿泊').grid(row=1, column=0, padx=10, pady=5)
      ttk.Separator(self, orient='vertical').grid(row=1, column=1, rowspan=18, sticky='ns', padx=5)
      
      tk.Label(self, text='単価（八幡平豚）').grid(row=1, column=2, padx=10, pady=5)
      tk.Label(self, text='単価（岩手県産牛）').grid(row=1, column=3, padx=10, pady=5)
      tk.Label(self, text='単価（前沢牛）').grid(row=1, column=4, padx=10, pady=5)
      tk.Label(self, text='注文数').grid(row=1, column=5, padx=10, pady=5)
      tk.Label(self, text='合計').grid(row=1, column=6, padx=10, pady=5)
      ttk.Separator(self, orient='vertical').grid(row=1, column=7, rowspan=18, sticky='ns', padx=5)
      tk.Label(self, text='宿泊').grid(row=1, column=8, padx=10, pady=5)
      ttk.Separator(self, orient='vertical').grid(row=1, column=9, rowspan=18, sticky='ns', padx=5)
      tk.Label(self, text='単価').grid(row=1, column=10, padx=10, pady=5)
      tk.Label(self, text='注文数').grid(row=1, column=11, padx=10, pady=5)
      tk.Label(self, text='合計').grid(row=1, column=12, padx=10, pady=5)
      
      ttk.Separator(self, orient='horizontal').grid(row=2, column=0, columnspan=14, sticky='ew', pady=5)
      
      tk.Label(self, text='1F和室(本館和室7.5畳)　大人').grid(row=3, column=0, padx=10, pady=5)
      tk.Label(self, text='1F和室(本館和室7.5畳)　子供').grid(row=4, column=0, padx=10, pady=5)
      tk.Label(self, text='1F西館洋室　大人').grid(row=5, column=0, padx=10, pady=5)
      tk.Label(self, text='1F西館洋室　子供').grid(row=6, column=0, padx=10, pady=5)
      tk.Label(self, text='岩手山側和室　大人').grid(row=7, column=0, padx=10, pady=5)
      tk.Label(self, text='岩手山側和室　子供').grid(row=8, column=0, padx=10, pady=5)
      tk.Label(self, text='岩手山側露天風呂付き和室　大人').grid(row=9, column=0, padx=10, pady=5)
      tk.Label(self, text='岩手山側露天風呂付き和室　子供').grid(row=10, column=0, padx=10, pady=5)
      tk.Label(self, text='西館和室10畳　大人').grid(row=11, column=0, padx=10, pady=5)
      tk.Label(self, text='西館和室10畳　子供').grid(row=12, column=0, padx=10, pady=5)
      tk.Label(self, text='1F檜内風呂付き和洋室　大人').grid(row=13, column=0, padx=10, pady=5)
      tk.Label(self, text='1F檜内風呂付き和洋室　子供').grid(row=14, column=0, padx=10, pady=5)
      tk.Label(self, text='1F西館和洋室　大人').grid(row=15, column=0, padx=10, pady=5)
      tk.Label(self, text='1F西館和洋室　子供').grid(row=16, column=0, padx=10, pady=5)
      tk.Label(self, text='西館和室28畳　大人').grid(row=17, column=0, padx=10, pady=5)
      tk.Label(self, text='西館和室28畳　子供').grid(row=18, column=0, padx=10, pady=5)
      tk.Label(self, text='ドックワン　宿泊').grid(row=3, column=8, padx=10, pady=5)
      tk.Label(self, text='ドックワン　スパ').grid(row=4, column=8, padx=10, pady=5)
      tk.Label(self, text='岩盤浴（宿泊者）').grid(row=5, column=8, padx=10, pady=5)
      tk.Label(self, text='岩盤浴（外来）').grid(row=6, column=8, padx=10, pady=5)
      tk.Label(self, text='パークゴルフ　大人').grid(row=7, column=8, padx=10, pady=5)
      tk.Label(self, text='パークゴルフ　子供').grid(row=8, column=8, padx=10, pady=5)
      tk.Label(self, text='パターゴルフ　大人').grid(row=9, column=8, padx=10, pady=5)
      tk.Label(self, text='パターゴルフ　子供').grid(row=10, column=8, padx=10, pady=5)
      tk.Label(self, text='テニスコート　宿泊者').grid(row=11, column=8, padx=10, pady=5)
      tk.Label(self, text='テニスコート　外来').grid(row=12, column=8, padx=10, pady=5)
      tk.Label(self, text='テニスコート　延長').grid(row=13, column=8, padx=10, pady=5)
      tk.Label(self, text='テニスコート　ボール').grid(row=14, column=8, padx=10, pady=5)
      tk.Label(self, text='温泉貸し切り').grid(row=15, column=8, padx=10, pady=5)
      
      tk.Label(self, text='12400').grid(row=3, column=2, padx=10, pady=5)
      tk.Label(self, text='').grid(row=4, column=2, padx=10, pady=5)
      tk.Label(self, text='12400').grid(row=5, column=2, padx=10, pady=5)
      tk.Label(self, text='').grid(row=6, column=2, padx=10, pady=5)
      tk.Label(self, text='12400').grid(row=7, column=2, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=8, column=2, padx=10, pady=5)
      tk.Label(self, text='14400').grid(row=9, column=2, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=10, column=2, padx=10, pady=5)
      tk.Label(self, text='12400').grid(row=11, column=2, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=12, column=2, padx=10, pady=5)
      tk.Label(self, text='15400').grid(row=13, column=2, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=14, column=2, padx=10, pady=5)
      tk.Label(self, text='12400').grid(row=15, column=2, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=16, column=2, padx=10, pady=5)
      tk.Label(self, text='12400').grid(row=17, column=2, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=18, column=2, padx=10, pady=5)
      
      tk.Label(self, text='15400').grid(row=3, column=3, padx=10, pady=5)
      tk.Label(self, text='').grid(row=4, column=3, padx=10, pady=5)
      tk.Label(self, text='15400').grid(row=5, column=3, padx=10, pady=5)
      tk.Label(self, text='').grid(row=6, column=3, padx=10, pady=5)
      tk.Label(self, text='15400').grid(row=7, column=3, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=8, column=3, padx=10, pady=5)
      tk.Label(self, text='17400').grid(row=9, column=3, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=10, column=3, padx=10, pady=5)
      tk.Label(self, text='15400').grid(row=11, column=3, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=12, column=3, padx=10, pady=5)
      tk.Label(self, text='18400').grid(row=13, column=3, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=14, column=3, padx=10, pady=5)
      tk.Label(self, text='15400').grid(row=15, column=3, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=16, column=3, padx=10, pady=5)
      tk.Label(self, text='15400').grid(row=17, column=3, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=18, column=3, padx=10, pady=5)
      
      tk.Label(self, text='18400').grid(row=3, column=4, padx=10, pady=5)
      tk.Label(self, text='').grid(row=4, column=4, padx=10, pady=5)
      tk.Label(self, text='18400').grid(row=5, column=4, padx=10, pady=5)
      tk.Label(self, text='').grid(row=6, column=4, padx=10, pady=5)
      tk.Label(self, text='18400').grid(row=7, column=4, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=8, column=4, padx=10, pady=5)
      tk.Label(self, text='20400').grid(row=9, column=4, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=10, column=4, padx=10, pady=5)
      tk.Label(self, text='18400').grid(row=11, column=4, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=12, column=4, padx=10, pady=5)
      tk.Label(self, text='21400').grid(row=13, column=4, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=14, column=4, padx=10, pady=5)
      tk.Label(self, text='18400').grid(row=15, column=4, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=16, column=4, padx=10, pady=5)
      tk.Label(self, text='18400').grid(row=17, column=4, padx=10, pady=5)
      tk.Label(self, text='7200').grid(row=18, column=4, padx=10, pady=5)
      
      tk.Label(self, text='1000').grid(row=3, column=10, padx=10, pady=5)
      tk.Label(self, text='1800(二頭目以降1000増)').grid(row=4, column=10, padx=10, pady=5)
      tk.Label(self, text='1500').grid(row=5, column=10, padx=10, pady=5)
      tk.Label(self, text='2000').grid(row=6, column=10, padx=10, pady=5)
      tk.Label(self, text='600').grid(row=7, column=10, padx=10, pady=5)
      tk.Label(self, text='300').grid(row=8, column=10, padx=10, pady=5)
      tk.Label(self, text='500').grid(row=9, column=10, padx=10, pady=5)
      tk.Label(self, text='250').grid(row=10, column=10, padx=10, pady=5)
      tk.Label(self, text='1000').grid(row=11, column=10, padx=10, pady=5)
      tk.Label(self, text='1500').grid(row=12, column=10, padx=10, pady=5)
      tk.Label(self, text='1000').grid(row=13, column=10, padx=10, pady=5)
      tk.Label(self, text='300').grid(row=14, column=10, padx=10, pady=5)
      tk.Label(self, text='2500').grid(row=15, column=10, padx=10, pady=5)
      
      # 合計ラベル
      wasitu1_total = (12400 * self.wasitu1_otona_poku + 15400 * self.wasitu1_otona_iwategyu + 18400 * self.wasitu1_otona_maezawagyu) * self.selected_stay_count
      tk.Label(self, text=wasitu1_total).grid(row=3, column=6, padx=10, pady=5)
      tk.Label(self, text='').grid(row=4, column=6, padx=10, pady=5)
      nishikan1_total = (12400 * self.nishikan1_otona_poku + 15400 * self.nishikan1_otona_iwategyu + 18400 * self.nishikan1_otona_maezawagyu) * self.selected_stay_count
      tk.Label(self, text=nishikan1_total).grid(row=5, column=6, padx=10, pady=5)
      tk.Label(self, text='').grid(row=6, column=6, padx=10, pady=5)
      iwatesan_total = (12400 * self.iwatesan_otona_poku + 15400 * self.iwatesan_otona_iwategyu + 18400 * self.iwatesan_otona_maezawagyu) * self.selected_stay_count
      tk.Label(self, text=iwatesan_total).grid(row=7, column=6, padx=10, pady=5)
      iwatesan_kodomo_total = (7200 * (self.iwatesan_kodomo_poku + self.iwatesan_kodomo_iwategyu + self.iwatesan_kodomo_maezawagyu)) * self.selected_stay_count
      tk.Label(self, text=iwatesan_kodomo_total).grid(row=8, column=6, padx=10, pady=5)
      iwatesan_roten_total = (14400 * self.iwatesan_roten_otona_poku + 17400 * self.iwatesan_roten_otona_iwategyu + 20400 * self.iwatesan_roten_otona_maezawagyu) * self.selected_stay_count
      tk.Label(self, text=iwatesan_roten_total).grid(row=9, column=6, padx=10, pady=5)
      iwatesan_roten_kodomo_total = (7200 * (self.iwatesan_roten_kodomo_poku + self.iwatesan_roten_kodomo_iwategyu + self.iwatesan_roten_kodomo_maezawagyu)) * self.selected_stay_count
      tk.Label(self, text=iwatesan_roten_kodomo_total).grid(row=10, column=6, padx=10, pady=5)
      nishikan10_total = (12400 * self.nishikan10_otona_poku + 15400 * self.nishikan10_otona_iwategyu + 18400 * self.nishikan10_otona_maezawagyu) * self.selected_stay_count
      tk.Label(self, text=nishikan10_total).grid(row=11, column=6, padx=10, pady=5)
      nishikan10_kodomo_total = (7200 * (self.nishikan10_kodomo_poku + self.nishikan10_kodomo_iwategyu + self.nishikan10_kodomo_maezawagyu)) * self.selected_stay_count
      tk.Label(self, text=nishikan10_kodomo_total).grid(row=12, column=6, padx=10, pady=5)
      hinoki_total = (15400 * self.hinoki_otona_poku + 18400 * self.hinoki_otona_iwategyu + 21400 * self.hinoki_otona_maezawagyu) * self.selected_stay_count
      tk.Label(self, text=hinoki_total).grid(row=13, column=6, padx=10, pady=5)
      hinoki_kodomo_total = (7200 * (self.hinoki_kodomo_poku + self.hinoki_kodomo_iwategyu + self.hinoki_kodomo_maezawagyu)) * self.selected_stay_count
      tk.Label(self, text=hinoki_kodomo_total).grid(row=14, column=6, padx=10, pady=5)
      nishikan1F_total = (12400 * self.nishikan1F_otona_poku + 15400 * self.nishikan1F_otona_iwategyu + 18400 * self.nishikan1F_otona_maezawagyu) * self.selected_stay_count
      tk.Label(self, text=nishikan1F_total).grid(row=15, column=6, padx=10, pady=5)
      nishikan1F_kodomo_total = (7200 * (self.nishikan1F_kodomo_poku + self.nishikan1F_kodomo_iwategyu + self.nishikan1F_kodomo_maezawagyu)) * self.selected_stay_count
      tk.Label(self, text=nishikan1F_kodomo_total).grid(row=16, column=6, padx=10, pady=5)
      nishikan28_total = (12400 * self.nishikan28_otona_poku + 15400 * self.nishikan28_otona_iwategyu + 18400 * self.nishikan28_otona_maezawagyu) * self.selected_stay_count
      tk.Label(self, text=nishikan28_total).grid(row=17, column=6, padx=10, pady=5)
      nishikan28_kodomo_total = (7200 * (self.nishikan28_kodomo_poku + self.nishikan28_kodomo_iwategyu + self.nishikan28_kodomo_maezawagyu)) * self.selected_stay_count
      tk.Label(self, text=nishikan28_kodomo_total).grid(row=18, column=6, padx=10, pady=5)
      tk.Label(self, text=1000 * self.dog_wan_adult).grid(row=3, column=12, padx=10, pady=5)
      dog_wan_child_plas = 0
      if self.dog_wan_child > 1:
          dog_wan_child_plas = 1000 * (self.dog_wan_child - 1)
      tk.Label(self, text=1800 * self.dog_wan_child + dog_wan_child_plas).grid(row=4, column=12, padx=10, pady=5)
      tk.Label(self, text=1500 * self.gan_stay).grid(row=5, column=12, padx=10, pady=5)
      tk.Label(self, text=2000 * self.gan_no_stay).grid(row=6, column=12, padx=10, pady=5)
      tk.Label(self, text=600 * self.paku_otona).grid(row=7, column=12, padx=10, pady=5)
      tk.Label(self, text=300 * self.paku_kodomo).grid(row=8, column=12, padx=10, pady=5)
      tk.Label(self, text=500 * self.pata_otona).grid(row=9, column=12, padx=10, pady=5)
      tk.Label(self, text=250 * self.pata_kodomo).grid(row=10, column=12, padx=10, pady=5)
      tk.Label(self, text=1000 * self.teni_stay).grid(row=11, column=12, padx=10, pady=5)
      tk.Label(self, text=1500 * self.teni_no_stay).grid(row=12, column=12, padx=10, pady=5)
      tk.Label(self, text=1000 * self.teni_en).grid(row=13, column=12, padx=10, pady=5)
      tk.Label(self, text=300 * self.teni_ball).grid(row=14, column=12, padx=10, pady=5)
      tk.Label(self, text=2500 * self.kasikiri_num).grid(row=15, column=12, padx=10, pady=5)
      
      # 注文数ラベル
      tk.Label(self, text=self.wasitu1_otona_poku + self.wasitu1_otona_iwategyu + self.wasitu1_otona_maezawagyu).grid(row=3, column=5, padx=10, pady=5)
      tk.Label(self, text='').grid(row=4, column=5, padx=10, pady=5)
      tk.Label(self, text=self.nishikan1_otona_poku + self.nishikan1_otona_iwategyu + self.nishikan1_otona_maezawagyu).grid(row=5, column=5, padx=10, pady=5)
      tk.Label(self, text='').grid(row=6, column=5, padx=10, pady=5)
      tk.Label(self, text=self.iwatesan_otona_poku + self.iwatesan_otona_iwategyu + self.iwatesan_otona_maezawagyu).grid(row=7, column=5, padx=10, pady=5)
      tk.Label(self, text=self.iwatesan_kodomo_poku + self.iwatesan_kodomo_iwategyu + self.iwatesan_kodomo_maezawagyu).grid(row=8, column=5, padx=10, pady=5)
      tk.Label(self, text=self.iwatesan_roten_otona_poku + self.iwatesan_roten_otona_iwategyu + self.iwatesan_roten_otona_maezawagyu).grid(row=9, column=5, padx=10, pady=5)
      tk.Label(self, text=self.iwatesan_roten_kodomo_poku + self.iwatesan_roten_kodomo_iwategyu + self.iwatesan_roten_kodomo_maezawagyu).grid(row=10, column=5, padx=10, pady=5)
      tk.Label(self, text=self.nishikan10_otona_poku + self.nishikan10_otona_iwategyu + self.nishikan10_otona_maezawagyu).grid(row=11, column=5, padx=10, pady=5)
      tk.Label(self, text=self.nishikan10_kodomo_poku + self.nishikan10_kodomo_iwategyu + self.nishikan10_kodomo_maezawagyu).grid(row=12, column=5, padx=10, pady=5)
      tk.Label(self, text=self.hinoki_otona_poku + self.hinoki_otona_iwategyu + self.hinoki_otona_maezawagyu).grid(row=13, column=5, padx=10, pady=5)
      tk.Label(self, text=self.hinoki_kodomo_poku + self.hinoki_kodomo_iwategyu + self.hinoki_kodomo_maezawagyu).grid(row=14, column=5, padx=10, pady=5)
      tk.Label(self, text=self.nishikan1F_otona_poku + self.nishikan1F_otona_iwategyu + self.nishikan1F_otona_maezawagyu).grid(row=15, column=5, padx=10, pady=5)
      tk.Label(self, text=self.nishikan1F_kodomo_poku + self.nishikan1F_kodomo_iwategyu + self.nishikan1F_kodomo_maezawagyu).grid(row=16, column=5, padx=10, pady=5)
      tk.Label(self, text=self.nishikan28_otona_poku + self.nishikan28_otona_iwategyu + self.nishikan28_otona_maezawagyu).grid(row=17, column=5, padx=10, pady=5)
      tk.Label(self, text=self.nishikan28_kodomo_poku + self.nishikan28_kodomo_iwategyu + self.nishikan28_kodomo_maezawagyu).grid(row=18, column=5, padx=10, pady=5)
      
      
      tk.Label(self, text=self.dog_wan_adult).grid(row=3, column=11, padx=10, pady=5)
      tk.Label(self, text=self.dog_wan_child).grid(row=4, column=11, padx=10, pady=5)
      tk.Label(self, text=self.gan_stay).grid(row=5, column=11, padx=10, pady=5)
      tk.Label(self, text=self.gan_no_stay).grid(row=6, column=11, padx=10, pady=5)
      tk.Label(self, text=self.paku_otona).grid(row=7, column=11, padx=10, pady=5)
      tk.Label(self, text=self.paku_kodomo).grid(row=8, column=11, padx=10, pady=5)
      tk.Label(self, text=self.pata_otona).grid(row=9, column=11, padx=10, pady=5)
      tk.Label(self, text=self.pata_kodomo).grid(row=10, column=11, padx=10, pady=5)
      tk.Label(self, text=self.teni_stay).grid(row=11, column=11, padx=10, pady=5)
      tk.Label(self, text=self.teni_no_stay).grid(row=12, column=11, padx=10, pady=5)
      tk.Label(self, text=self.teni_en).grid(row=13, column=11, padx=10, pady=5)
      tk.Label(self, text=self.teni_ball).grid(row=14, column=11, padx=10, pady=5)
      tk.Label(self, text=self.kasikiri_num).grid(row=15, column=11, padx=10, pady=5)
      
      tk.Label(self, text='土日祝日').grid(row=19, column=0, padx=10, pady=5)
      tk.Label(self, text='合計金額').grid(row=20, column=0, padx=10, pady=5)
      if self.check_sunday:
        tk.Label(self, text='有').grid(row=19, column=1, padx=10, pady=5)
      else:
        tk.Label(self, text='無').grid(row=19, column=1, padx=10, pady=5)
        
      tk.Label(self, text='10%').grid(row=19, column=3, padx=10, pady=5)
      if self.selected_early_discount == 60:
        tk.Label(self, text='有').grid(row=19, column=4, padx=10, pady=5)
      else:
        tk.Label(self, text='無').grid(row=19, column=4, padx=10, pady=5)
        
      tk.Label(self, text='15%').grid(row=19, column=6, padx=10, pady=5)
      if self.selected_early_discount == 90:
        tk.Label(self, text='有').grid(row=19, column=7, padx=10, pady=5)
      else:
        tk.Label(self, text='無').grid(row=19, column=7, padx=10, pady=5)

      self.total_price = (
          wasitu1_total + nishikan1_total + iwatesan_total + iwatesan_kodomo_total +
          iwatesan_roten_total + iwatesan_roten_kodomo_total + nishikan10_total + nishikan10_kodomo_total +
          hinoki_total + hinoki_kodomo_total + nishikan1F_total + nishikan1F_kodomo_total +
          nishikan28_total + nishikan28_kodomo_total + (1000 * self.dog_wan_adult) +
          (1800 * self.dog_wan_child + dog_wan_child_plas) + (1500 * self.gan_stay) +
          (2000 * self.gan_no_stay) + (600 * self.paku_otona) + (300 * self.paku_kodomo) +
          (500 * self.pata_otona) + (250 * self.pata_kodomo) + (1000 * self.teni_stay) +
          (1500 * self.teni_no_stay) + (1000 * self.teni_en) + (300 * self.teni_ball) +
          (2500 * self.kasikiri_num)
      )
      if self.check_sunday:
        self.total_price += 2000
      if self.selected_early_discount == 60:
        self.total_price = self.total_price - self.total_price * 0.1
        self.total_price = int(self.total_price)
      if self.selected_early_discount == 90:
        self.total_price = self.total_price - self.total_price * 0.15
        self.total_price = int(self.total_price)
      tk.Label(self, text=self.total_price).grid(row=20, column=1, padx=10, pady=5)

      self.mail_btn = tk.Button(self, text='メール送信', command=self.send_mail)
      self.mail_btn.grid(row=20, column=3, padx=10, pady=5)
      self.jason_btn = tk.Button(self, text='ジェイソンファイル保存', command=self.save_to_json)
      self.jason_btn.grid(row=20, column=4, padx=10, pady=5)
      
      self.return_btn = tk.Button(self, text='戻る', command=self.returnbtn2)
      self.return_btn.grid(row=20, column=5, padx=10, pady=5, sticky='ew')
  def returnbtn2(self):
      from stay import Stay  # Banquet クラスをインポート
      self.destroy()  # 現在のウィンドウを閉じる
      Stay(self.master, self.name, self.mail)  # 新しい画面を表示
      
    
  def send_mail(self):
    from mail import send_mail

    self.selected_day = str(self.selected_day)
    self.selected_month = str(self.selected_month)
    self.selected_stay_count = str(self.selected_stay_count)
    self.total_price = str(self.total_price)
    self.name = str(self.name)
    self.mail = str(self.mail)
    body = f"""
    {self.name}様の見積もり内容です。
    <br>宿泊日：{self.selected_month}月{self.selected_day}日
    <br>宿泊数：{self.selected_stay_count}泊
    <br>合計金額：{self.total_price}円
    """
    send_mail(self.mail, '宿泊見積もり', body)

    
  
  def save_to_json(self):
    data = {
        "wasitu1_kodomo_iwategyu": self.wasitu1_kodomo_iwategyu,
        "wasitu1_kodomo_maezawagyu": self.wasitu1_kodomo_maezawagyu,
        "wasitu1_otona_iwategyu": self.wasitu1_otona_iwategyu,
        "wasitu1_otona_maezawagyu": self.wasitu1_otona_maezawagyu,
        "wasitu1_kodomo_poku": self.wasitu1_kodomo_poku,
        "wasitu1_otona_poku": self.wasitu1_otona_poku,
        "nishikan1_kodomo_iwategyu": self.nishikan1_kodomo_iwategyu,
        "nishikan1_kodomo_maezawagyu": self.nishikan1_kodomo_maezawagyu,
        "nishikan1_otona_iwategyu": self.nishikan1_otona_iwategyu,
        "nishikan1_otona_maezawagyu": self.nishikan1_otona_maezawagyu,
        "nishikan1_kodomo_poku": self.nishikan1_kodomo_poku,
        "nishikan1_otona_poku": self.nishikan1_otona_poku,
        "selected_month": self.selected_month,
        "selected_day": self.selected_day,
        "selected_stay_count": self.selected_stay_count,
        "selected_early_discount": self.selected_early_discount,
        "dog_wan_adult": self.dog_wan_adult,
        "dog_wan_child": self.dog_wan_child,
        "gan_stay": self.gan_stay,
        "gan_no_stay": self.gan_no_stay,
        "pata_otona": self.pata_otona,
        "pata_kodomo": self.pata_kodomo,
        "paku_otona": self.paku_otona,
        "paku_kodomo": self.paku_kodomo,
        "teni_stay": self.teni_stay,
        "teni_no_stay": self.teni_no_stay,
        "teni_en": self.teni_en,
        "teni_ball": self.teni_ball,
        "kasikiri_num": self.kasikiri_num
    }

    filename = f"{self.name}（{self.mail}）さんの見積もりデータ（宿泊）　estimate_{datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


      
if __name__ == '__main__':
  root = tk.Tk()
  app = EstimateStay(root, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,False)
  app.mainloop()
