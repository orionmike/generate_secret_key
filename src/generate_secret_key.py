
import tkinter as tk
import ttkbootstrap as ttb
from ttkbootstrap.constants import *
import pyperclip

from libs.secret import get_result


class App(ttb.Window):
    def __init__(self):
        super().__init__()

        self.style.theme_use("superhero")
        self.geometry("494x246+700+300")

        # self.wm_iconbitmap(f"src/transparent.ico")

        self.tk.call('tk', 'scaling', 1.2)
        self.title("generate secret key")
        self.resizable(False, False)

        self.textbox_count = ttb.Entry(self, width=22, bootstyle="primary")
        self.textbox_count.grid(row=0, column=0, padx=10, pady=10, sticky=NW)
        self.textbox_count.insert(0, '32')

        self.label_count_symbols = ttb.Label(self, text='Количество символов')
        self.label_count_symbols.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        self.letters_lowercase = tk.BooleanVar()
        self.letters_lowercase.set(True)
        self.btn_letters_lowercase = ttb.Checkbutton(
            bootstyle="success-outline-toolbutton", text='letters lowercase', width=20,
            variable=self.letters_lowercase, command=self.click_btn_letters_lowercase)
        self.btn_letters_lowercase.grid(row=2, column=0, padx=10, pady=4, sticky=NW)

        self.letters_uppercase = tk.BooleanVar()
        self.letters_uppercase.set(True)
        self.btn_letters_uppercase = ttb.Checkbutton(
            bootstyle="success-outline-toolbutton", text='letters uppercase',
            width=20, variable=self.letters_uppercase, command=self.click_btn_letters_uppercase)
        self.btn_letters_uppercase.grid(row=2, column=1, padx=10, pady=4, sticky=NW)

        self.digits = tk.BooleanVar()
        self.digits.set(True)
        self.btn_digits = ttb.Checkbutton(
            bootstyle="success-outline-toolbutton", text='digits',
            width=20, variable=self.digits, command=self.click_btn_digits)
        self.btn_digits.grid(row=2, column=2, padx=10, pady=4, sticky=NW)

        self.punctuation = tk.BooleanVar()
        self.punctuation.set(False)
        self.btn_punctuation = ttb.Checkbutton(
            bootstyle="success-outline-toolbutton", text='punctuation',
            width=20, variable=self.punctuation, command=self.click_btn_punctuation)
        self.btn_punctuation.grid(row=3, column=0, padx=10, pady=4, sticky=NW)

        self.bytes = tk.BooleanVar()
        self.bytes.set(0)
        self.btn_bytes = ttb.Checkbutton(
            bootstyle="info-outline-toolbutton", text='bytes',
            width=20, variable=self.bytes, command=self.click_btn_bytes)
        self.btn_bytes.grid(row=3, column=1, padx=10, pady=4, sticky=NW)

        self.result = ttb.Text(height=2, width=77)
        self.result.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky=NW)

        self.btn_generate = ttb.Button(
            self, bootstyle="success",
            text="Generate", width=20, command=self.click_btn_generate)
        self.btn_generate.grid(row=5, column=0, padx=10, pady=10, sticky=NW)

        self.btn_copy = ttb.Button(
            self, bootstyle="info",
            text="Copy", width=20, command=self.click_btn_copy)
        self.btn_copy.grid(row=5, column=1, padx=10, pady=10, sticky=NW)

        self.btn_reset = ttb.Button(
            self, bootstyle="warning-outline",
            text="Reset", width=20, command=self.click_btn_reset)
        self.btn_reset.grid(row=5, column=2, padx=10, pady=10, sticky=NW)

    def click_btn_bytes(self):
        self.digits.set(False)
        self.letters_lowercase.set(False)
        self.letters_uppercase.set(False)
        self.punctuation.set(False)

    def click_btn_digits(self):
        self.bytes.set(False)

    def click_btn_letters_lowercase(self):
        self.bytes.set(False)

    def click_btn_letters_uppercase(self):
        self.bytes.set(False)

    def click_btn_punctuation(self):
        self.bytes.set(False)

    def click_btn_generate(self):

        self.result.configure(state=NORMAL)
        self.result.delete("1.0", END)

        settings_dict = {
            'letters_lowercase': self.letters_lowercase.get(),
            'letters_uppercase': self.letters_uppercase.get(),
            'digits': self.digits.get(),
            'punctuation': self.punctuation.get(),
            'bytes': self.bytes.get()
        }

        result = get_result(settings_dict, self.textbox_count.get())
        self.result.insert('1.0', result)
        self.result.configure(state=DISABLED)

    def click_btn_copy(self):
        result = self.result.get('1.0', END)
        if result:
            pyperclip.copy(result)

    def click_btn_reset(self):
        self.result.configure(state=NORMAL)
        self.result.delete("1.0", END)
        self.result.configure(state=DISABLED)


if __name__ == "__main__":
    app = App()
    app.mainloop()
