import customtkinter as ctk
import math
from tkinter import StringVar
from backend.Massages import *
import tkinter as tk
from backend.search_massages import *


class FilterFrame(ctk.CTkFrame):
    def __init__(self, parent, preq_parent, update_table_frame):
        ctk.CTkFrame.__init__(self, parent)
        print("Пользователь ", preq_parent.master.user)
        self.grid_columnconfigure((0, 3), weight=1)
        self.update_table_frame = update_table_frame

        filter_label = ctk.CTkLabel(self, text='Фильтр')
        filter_label.grid(row=0, column=0, padx=(15, 5), pady=(5, 0), sticky='w')

        clear_button = ctk.CTkButton(self, text="Очистить", width=90, fg_color='grey20'
                                     , command=self.clear_filter_frame)
        clear_button.grid(row=0, column=2, columnspan=2, pady=10, padx=(5, 15))

        self.search_entry = ctk.CTkEntry(self, placeholder_text="Название", width=180)
        self.search_entry.grid(row=1, column=0, columnspan=3, pady=(10, 15), padx=(15, 5))

        search_button = ctk.CTkButton(self, text="Поиск", width=50, command=self.update_massages_table_frame)
        search_button.grid(row=1, column=3, columnspan=1, pady=(10, 15), padx=(5, 15))

        prices_frame = ctk.CTkFrame(self)
        prices_frame.grid(row=2, column=0, columnspan=4, padx=15, pady=(0, 15))

        price_label = ctk.CTkLabel(prices_frame, text='Цена, руб.')
        price_label.grid(row=0, column=0, columnspan=2, padx=10, sticky='w')

        self.price_from_entry = ctk.CTkEntry(prices_frame, placeholder_text="От", width=100)
        self.price_from_entry.grid(row=1, column=0, padx=10, pady=(0, 5))

        self.price_to_entry = ctk.CTkEntry(prices_frame, placeholder_text="До", width=100)
        self.price_to_entry.grid(row=1, column=1, padx=10, pady=(0, 5))

        duration_frame = ctk.CTkFrame(self)

        duration_frame.grid(row=3, column=0, columnspan=4, padx=15, pady=(0, 15))

        duration_label = ctk.CTkLabel(duration_frame, text='Длительность')

        duration_label.grid(row=0, column=0, columnspan=2, padx=10, sticky='w')

        self.duration_from_entry = ctk.CTkEntry(duration_frame, placeholder_text="От", width=100)

        self.duration_from_entry.grid(row=1, column=0, padx=10, pady=(0, 5))

        self.duration_to_entry = ctk.CTkEntry(duration_frame, placeholder_text="До", width=100)

        self.duration_to_entry.grid(row=1, column=1, padx=10, pady=(0, 5))

        categories_scrollframe = ctk.CTkScrollableFrame(self, label_text="Категории", height=130, width=220)
        categories_scrollframe.grid(row=4, column=0, columnspan=4, padx=15, pady=(0, 15))

        categories_scrollframe.grid_columnconfigure((0, 1), weight=1)
        categories_scrollframe.scrollbar.configure(height=0)
        scrollable_frame_checkboxes = []
        # Получаем все категории активных массажей из бд
        bd = MassagesData()
        self.categories_dict = bd.read_tbl_categories_massages()
        check_var = {}
        self.checkboxes = {}
        check_var[0] = ctk.StringVar(value="on")
        self.checkboxes[0] = ctk.CTkCheckBox(categories_scrollframe, text='Все', variable=check_var[0], onvalue="on",
                                             offvalue="off")
        self.checkboxes[0].grid(row=math.floor(0), column=0, padx=0, pady=(0, 10), sticky='w')
        self.checkboxes[0].bind("<Button-1>", command=self.click_category_all)

        for i, (name_category, id_category) in enumerate(self.categories_dict.items()):
            check_var[i + 1] = ctk.StringVar(value="on")
            self.checkboxes[i + 1] = ctk.CTkCheckBox(categories_scrollframe, text=name_category,
                                                     variable=check_var[i + 1],
                                                     onvalue="on",
                                                     offvalue="off")
            self.checkboxes[i + 1].grid(row=math.floor(i + 1), column=0, padx=0, pady=(0, 10), sticky='w')
            self.checkboxes[i + 1].bind("<Button-1>", command=self.click_one_category)
            scrollable_frame_checkboxes.append(self.checkboxes[i])

        activity_frame = ctk.CTkFrame(self)

        activity_frame.grid(row=5, column=0, columnspan=4, padx=15, pady=(0, 15))

        activity_label = ctk.CTkLabel(activity_frame, text='Статус')

        activity_label.grid(row=0, column=0, padx=10, sticky='w')

        var = StringVar()
        var.set("Все варианты")
        self.activity_option_menu = ctk.CTkOptionMenu(activity_frame, dynamic_resizing=False, variable=var,
                                                      values=["Все варианты", "Активен", "На стопе"],
                                                      width=220)
        self.activity_option_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 5), sticky='we')

        number_persons_frame = ctk.CTkFrame(self)

        number_persons_frame.grid(row=6, column=0, columnspan=4, padx=15, pady=(0, 0))

        number_persons_label = ctk.CTkLabel(number_persons_frame, text='Для двоих')

        number_persons_label.grid(row=0, column=0, padx=10, sticky='w')

        var = StringVar()
        var.set("Все варианты")
        self.number_persons_option_menu = ctk.CTkOptionMenu(number_persons_frame, dynamic_resizing=False, variable=var,
                                                            values=["Все варианты", "Для одного", "Для двоих"],
                                                            width=220)
        self.number_persons_option_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 5), sticky='we')

        self.update_massages_table_frame()

    def clear_filter_frame(self):
        self.search_entry.delete(0, tk.END)
        self.price_from_entry.delete(0, tk.END)
        self.price_to_entry.delete(0, tk.END)
        self.duration_from_entry.delete(0, tk.END)
        self.duration_to_entry.delete(0, tk.END)

        check_vars = {}
        for i, checkbox in enumerate(self.checkboxes):
            check_vars[i] = ctk.StringVar(value="on")
            self.checkboxes[i].configure(variable=check_vars[i])

        var = StringVar()
        var.set("Все варианты")
        self.activity_option_menu.configure(variable=var)

        var = StringVar()
        var.set("Все варианты")
        self.number_persons_option_menu.configure(variable=var)

    def click_category_all(self, event):
        if self.checkboxes[0].get() == 'on':
            for i, checkbox in enumerate(self.checkboxes):
                if self.checkboxes[i].get() == "off" and i != 0:
                    self.checkboxes[i].configure(variable=ctk.StringVar(value="on"))
        elif self.checkboxes[0].get() == 'off':
            for i, checkbox in enumerate(self.checkboxes):
                if self.checkboxes[i].get() == "on" and i != 0:
                    self.checkboxes[i].configure(variable=ctk.StringVar(value="off"))

    def click_one_category(self, event):
        for i, checkbox in enumerate(self.checkboxes):
            if i != 0:
                if self.checkboxes[i].get() == "on":
                    continue
                else:
                    self.checkboxes[0].configure(variable=ctk.StringVar(value="off"))
                    return
        self.checkboxes[0].configure(variable=ctk.StringVar(value="on"))

    def update_massages_table_frame(self):
        name = self.search_entry.get()
        min_price = self.price_from_entry.get()
        max_price = self.price_to_entry.get()
        start_duration = self.duration_from_entry.get()
        end_duration = self.duration_to_entry.get()

        categories = []

        for i, checkbox in enumerate(self.checkboxes):
            if self.checkboxes[i].get() == "on" and i != 0:
                categories.append(self.categories_dict[self.checkboxes[i].cget('text')])

        activities = ["на стопе", "активен"]
        if self.activity_option_menu.get() == "Активен":
            activities = ['активен']
        elif self.activity_option_menu.get() == "На стопе":
            activities = ['на стопе']

        persons = [1, 2]
        if self.number_persons_option_menu.get() == "Для одного":
            persons = [1]
        elif self.number_persons_option_menu.get() == "Для двоих":
            persons = [2]

        # берем с backend
        massages_data = filter_massages(name, categories, persons, start_duration, end_duration,
                                        min_price, max_price, activities)

        massages = []
        for item in massages_data:
            massage_info = {
                'id_массажа': item[0],
                'название': item[1],
                'id_категории': item[2],
                'категория': item[3],
                'количество_человек': item[4],
                'длительность': item[5],
                'перерыв': item[6],
                'описание': item[7],
                'активность': item[8],
                'цена': item[9],
                'дата_изменения': item[10],
                'ids_комнат': [],
                'названия_комнат': []
            }

            room_data = item[11]
            rooms = room_data.split(', ')
            for room in rooms:
                room_info = room.split(': ')
                massage_info['ids_комнат'].append(int(room_info[0]))
                massage_info['названия_комнат'].append(room_info[1])

            massages.append(massage_info)

        # Вывод результатов
        print('результат поиска')
        for massage in massages:
            print(massage)
        self.update_table_frame(massages)
