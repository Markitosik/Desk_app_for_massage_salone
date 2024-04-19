import customtkinter as ctk
from tkinter import *
from CTkMessagebox import CTkMessagebox


class Authorization(ctk.CTkToplevel):
    def __init__(self, parent):
        ctk.CTkToplevel.__init__(self, parent)
        self.parent = parent
        self.title("Авторизация")
        self.geometry("400x240")
        self.user = 'q'
        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)

        self.authorization_frame = ctk.CTkFrame(self, height=200)
        self.authorization_frame.grid(row=0, column=0, padx=20, pady=20)

        self.login_label = ctk.CTkLabel(self.authorization_frame, text="Логин:")
        self.login_entry = ctk.CTkEntry(self.authorization_frame)

        self.password_label = ctk.CTkLabel(self.authorization_frame, text="Пароль:")
        self.password_entry = ctk.CTkEntry(self.authorization_frame, show="*")
        self.login_button = ctk.CTkButton(self.authorization_frame, text="Войти", command=self.login)

        self.login_label.grid(row=0, column=0, sticky=ctk.W, padx=20, pady=(15, 0))
        self.login_entry.grid(row=1, column=0, padx=20, pady=(0, 10))
        self.password_label.grid(row=2, column=0, sticky=ctk.W, padx=20, pady=(0, 0))
        self.password_entry.grid(row=3, column=0, padx=20, pady=(0, 10))
        self.login_button.grid(row=4, column=0, padx=20, pady=(10, 25))
        self.deiconify()
        # Назначение обработчика события закрытия дочернего окна
        self.protocol("WM_DELETE_WINDOW", self.close_app)

    def close_app(self):
        self.parent.destroy()

    def login(self):
        username = self.login_entry.get()
        password = self.password_entry.get()


        if password == "":
            self.user = username
            self.parent.make_frames(username)
            self.parent.show_sidebar()
            self.withdraw()
            self.parent.deiconify()
        else:
            CTkMessagebox(title="Ошибка", message="Неправильный логин или пароль", icon="cancel")

    def logout(self):
        self.user = ''
        self.login_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.parent.withdraw()
        self.deiconify()

    def username(self):
        name = self.user
        return name
