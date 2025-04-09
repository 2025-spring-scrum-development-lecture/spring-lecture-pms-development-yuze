import tkinter as tk
from tkinter import messagebox  # エラーメッセージ用

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        master.geometry('420x550')
        master.title('宴会、宿泊選択画面')

        self.create_widgets()

    def create_widgets(self):
        self.name_placeholder = "例）山田太郎"
        self.mail_placeholder = "例）mailadd@gmail.com"

        self.name_label = tk.Label(self, text='nama')
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.name_entry = tk.Entry(self, width=25, fg='gray')
        self.name_entry.insert(0, self.name_placeholder)
        self.name_entry.bind("<FocusIn>", self.on_name_entry_click)
        self.name_entry.bind("<FocusOut>", self.on_name_focus_out)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.gmail_label = tk.Label(self, text='mail')
        self.gmail_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.mail_entry = tk.Entry(self, width=25, fg='gray')
        self.mail_entry.insert(0, self.mail_placeholder)
        self.mail_entry.bind("<FocusIn>", self.on_mail_entry_click)
        self.mail_entry.bind("<FocusOut>", self.on_mail_focus_out)
        self.mail_entry.grid(row=1, column=1, padx=10, pady=5)

        import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        master.geometry('420x550')
        master.title('宴会、宿泊選択画面')

        self.create_widgets()

    # テキストボックス
    def create_widgets(self):
        self.name_placeholder = "例）山田太郎"
        self.mail_placeholder = "例）example@gmail.com"

        self.name_label = tk.Label(self, text='nama')
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.name_entry = tk.Entry(self, width=20, fg='gray')
        self.name_entry.insert(0, self.name_placeholder)
        self.name_entry.bind("<FocusIn>", self.on_name_entry_click)
        self.name_entry.bind("<FocusOut>", self.on_name_focus_out)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.gmail_label = tk.Label(self, text='mail')
        self.gmail_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.mail_entry = tk.Entry(self, width=20, fg='gray')
        self.mail_entry.insert(0, self.mail_placeholder)
        self.mail_entry.bind("<FocusIn>", self.on_mail_entry_click)
        self.mail_entry.bind("<FocusOut>", self.on_mail_focus_out)
        self.mail_entry.grid(row=1, column=1, padx=10, pady=5)

        #   ラジオボタン
        self.gender_var = tk.StringVar(value="宴会")
        self.radio_frame = tk.Frame(self)
        self.radio_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.enkai = tk.Radiobutton(self.radio_frame, text='宴会', variable=self.gender_var, value='宴会')
        self.enkai.pack(side='left', padx=20)

        self.syukuhaku = tk.Radiobutton(self.radio_frame, text='宿泊', variable=self.gender_var, value='宿泊')
        self.syukuhaku.pack(side='left', padx=20)

    # 完了ボタン
        self.button = tk.Button(self, text='完了', command=self.print_input_info)
        self.button.grid(row=3, column=0, columnspan=2, pady=10)

    def on_name_entry_click(self, event):
        if self.name_entry.get() == self.name_placeholder:
            self.name_entry.delete(0, "end")
            self.name_entry.config(fg='black')

    def on_name_focus_out(self, event):
        if self.name_entry.get() == '':
            self.name_entry.insert(0, self.name_placeholder)
            self.name_entry.config(fg='gray')

    def on_mail_entry_click(self, event):
        if self.mail_entry.get() == self.mail_placeholder:
            self.mail_entry.delete(0, "end")
            self.mail_entry.config(fg='black')

    def on_mail_focus_out(self, event):
        if self.mail_entry.get() == '':
            self.mail_entry.insert(0, self.mail_placeholder)
            self.mail_entry.config(fg='gray')

    def print_input_info(self):
        name = self.name_entry.get()
        mail = self.mail_entry.get()
        selection = self.gender_var.get()

        if name == self.name_placeholder:
            name = ""
        if mail == self.mail_placeholder:
            mail = ""

        if not name or not mail:
            messagebox.showerror("入力エラー", "名前とメールを入力してください。")
            return

        if "@" not in mail or "." not in mail:
            messagebox.showerror("形式エラー", "正しいメールアドレスを入力してください。")
            return

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()
