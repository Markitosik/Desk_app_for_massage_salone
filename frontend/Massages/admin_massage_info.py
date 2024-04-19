import customtkinter as ctk
import math
from tkinter import StringVar
from backend.Massages import *
import tkinter as tk


class AdminMassageInfoFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        self.massages = None
        self.selected_row = None
        ctk.CTkScrollableFrame.__init__(self, parent, label_text='Карточка массажа')

        name_massage_label = ctk.CTkLabel(self, text="Название", width=80, anchor='e')
        name_massage_label.grid(row=0, column=0, padx=(15, 5), pady=(10, 15), sticky='e')

        self.name_massage_entry = ctk.CTkEntry(self, width=350)
        self.name_massage_entry.insert(0, "")
        self.name_massage_entry.grid(row=0, column=1, columnspan=2, padx=(5, 10), pady=(10, 15), sticky='w')
        self.name_massage_entry.configure(state="disabled")

        category_massage_label = ctk.CTkLabel(self, text="Категория", width=80, anchor='e')
        category_massage_label.grid(row=1, column=0, padx=(15, 5), pady=(10, 15), sticky='e')

        var = StringVar()
        var.set("")
        self.category_massage_entry = ctk.CTkOptionMenu(self, dynamic_resizing=False, variable=var, width=350)
        self.category_massage_entry.grid(row=1, column=1, columnspan=2, padx=(5, 10), pady=(10, 15), sticky='w')
        self.category_massage_entry.configure(state="disabled")

        self.rooms_massage_scrollframe = ctk.CTkScrollableFrame(self, label_text="Комнаты", height=100)
        self.rooms_massage_scrollframe.configure(fg_color=['gray81', 'gray20'])
        self.rooms_massage_scrollframe.grid(row=3, column=3, columnspan=2, padx=(10, 15), pady=(10, 15), sticky='we')

        self.rooms_massage_scrollframe.grid_columnconfigure((0, 1), weight=1)
        self.rooms_massage_scrollframe._scrollbar.configure(height=0)

        # Получаем все категории активных массажей из бд
        bd = MassagesData()
        self.rooms_dict = bd.read_tbl_rooms()
        check_var = {}
        self.checkboxes = {}
        for i, (name_room, id_room) in enumerate(self.rooms_dict.items()):
            check_var[i] = ctk.StringVar(value="off")
            self.checkboxes[i] = ctk.CTkCheckBox(self.rooms_massage_scrollframe, text=name_room, variable=check_var[i],
                                                 onvalue="on", offvalue="off")
            self.checkboxes[i].grid(row=math.floor(i), column=0, padx=0, pady=(0, 10), sticky='w')
            self.checkboxes[i].configure(state="disabled")

        duration_massage_label = ctk.CTkLabel(self, text="Длительность", width=40)
        duration_massage_label.grid(row=4, column=3, padx=(10, 5), pady=(10, 15), sticky='e')

        self.duration_massage_entry = ctk.CTkEntry(self, width=150)
        self.duration_massage_entry.insert(0, "")
        self.duration_massage_entry.grid(row=4, column=4, padx=(5, 15), pady=(10, 15), sticky='we')
        self.duration_massage_entry.configure(state="disabled")

        break_massage_label = ctk.CTkLabel(self, text="Перерыв", width=40)
        break_massage_label.grid(row=5, column=3, padx=(10, 5), pady=(10, 15), sticky='e')

        self.break_massage_entry = ctk.CTkEntry(self, width=150)
        self.break_massage_entry.insert(0, "")
        self.break_massage_entry.grid(row=5, column=4, padx=(5, 15), pady=(10, 15), sticky='we')
        self.break_massage_entry.configure(state="disabled")

        price_massage_label = ctk.CTkLabel(self, text="Цена(руб.)", width=40)
        price_massage_label.grid(row=1, column=3, padx=(10, 5), pady=(10, 15), sticky='e')

        self.price_massage_entry = ctk.CTkEntry(self, width=150)
        self.price_massage_entry.insert(0, "")
        self.price_massage_entry.grid(row=1, column=4, padx=(5, 15), pady=(10, 15), sticky='we')
        self.price_massage_entry.configure(state="disabled")

        number_persons_massage_label = ctk.CTkLabel(self, text="Количество", width=40)
        number_persons_massage_label.grid(row=6, column=3, padx=(10, 5), pady=(10, 15), sticky='e')

        self.number_persons_massage_entry = ctk.CTkSwitch(self, width=40, text='1 человек')
        self.number_persons_massage_entry.grid(row=6, column=4, padx=(5, 15), pady=(10, 15), sticky='we')
        self.number_persons_massage_entry.configure(state="disabled")

        activity_massage_label = ctk.CTkLabel(self, text="Статус", width=40)
        activity_massage_label.grid(row=0, column=3, padx=(10, 5), pady=(10, 15), sticky='e')

        self.activity_massage_entry = ctk.CTkSwitch(self, switch_width=40, text='На стопе')
        self.activity_massage_entry.grid(row=0, column=4, padx=(5, 15), pady=(10, 15), sticky='we')
        self.activity_massage_entry.configure(state="disabled")

        description_massage_label = ctk.CTkLabel(self, text="Описание")
        description_massage_label.grid(row=2, column=0, padx=(15, 10), pady=(10, 5), sticky='w')

        self.description_massage_textbox = ctk.CTkTextbox(self, height=225, width=440)
        self.description_massage_textbox.insert(0.0, "")
        self.description_massage_textbox.grid(row=3, column=0, columnspan=3, rowspan=7, padx=(15, 10), pady=(10, 15),
                                              sticky='wns')
        self.description_massage_textbox.configure(state="disabled")
        self.grid_columnconfigure(3, weight=1)

    def update_info_frame(self, massages, row):
        self.massages = massages
        self.selected_row = row
        print('Тык сюда ', row)

        # название
        self.name_massage_entry.configure(state="normal")
        self.name_massage_entry.delete(0, tk.END)
        self.name_massage_entry.insert(0, self.massages[row]['название'])
        self.name_massage_entry.configure(state="disabled")

        # категория
        var = StringVar()
        var.set(self.massages[row]['категория'])
        self.category_massage_entry.configure(variable=var)
        self.category_massage_entry.configure(state="disabled")

        # статус
        self.activity_massage_entry.configure(state="normal")
        if self.massages[row]['активность'] == "активен":
            self.activity_massage_entry.select()
            self.activity_massage_entry.configure(text='активен')
        elif self.massages[row]['активность'] == "на стопе":
            self.activity_massage_entry.deselect()
            self.activity_massage_entry.configure(text='на стопе')
        self.activity_massage_entry.configure(state="disabled")

        # цена
        self.price_massage_entry.configure(state="normal")
        self.price_massage_entry.delete(0, tk.END)
        self.price_massage_entry.insert(0, self.massages[row]['цена'])
        self.price_massage_entry.configure(state="disabled")

        # описание
        self.description_massage_textbox.configure(state="normal")
        self.description_massage_textbox.delete(0.0, 'end')
        self.description_massage_textbox.insert(0.0, self.massages[row]['описание'])
        self.description_massage_textbox.configure(state="disabled")

        # комнаты
        for i, checkbox in enumerate(self.checkboxes):
            self.checkboxes[i].configure(state="normal")
            if self.checkboxes[i].cget('text') in self.massages[row]['названия_комнат']:
                self.checkboxes[i].configure(variable=ctk.StringVar(value="on"))
            else:
                self.checkboxes[i].configure(variable=ctk.StringVar(value="off"))
            self.checkboxes[i].configure(state="disabled")

        # длительность
        self.duration_massage_entry.configure(state="normal")
        self.duration_massage_entry.delete(0, tk.END)
        self.duration_massage_entry.insert(0, self.massages[row]['длительность'])
        self.duration_massage_entry.configure(state="disabled")

        # перерыв
        self.break_massage_entry.configure(state="normal")
        self.break_massage_entry.delete(0, tk.END)
        self.break_massage_entry.insert(0, self.massages[row]['перерыв'])
        self.break_massage_entry.configure(state="disabled")

        # количество
        self.number_persons_massage_entry.configure(state="normal")
        print(self.massages[row]['количество_человек'])
        if self.massages[row]['количество_человек'] == 2:
            self.number_persons_massage_entry.select()
            self.number_persons_massage_entry.configure(text='2 человека')
        elif self.massages[row]['количество_человек'] == 1:
            self.number_persons_massage_entry.deselect()
            self.number_persons_massage_entry.configure(text='1 человек')
        self.number_persons_massage_entry.configure(state="disabled")
