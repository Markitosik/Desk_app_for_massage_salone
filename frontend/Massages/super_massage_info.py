from functools import partial

from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import math
from tkinter import StringVar
from backend.Massages import *
import tkinter as tk
import re


class SuperMassageInfoFrame(ctk.CTkFrame):
    def __init__(self, parent, table_frame, filter_frame):
        self.massages = None
        self.selected_row = None
        self.table_frame = table_frame
        self.filter_frame = filter_frame

        ctk.CTkFrame.__init__(self, parent)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        massage_review_frame = ctk.CTkScrollableFrame(self, label_text='Карточка массажа')
        massage_review_frame.rowconfigure(0, weight=1)
        massage_review_frame.grid(row=0, column=0, columnspan=4, padx=(15, 15), pady=(10, 5), sticky='nswe')

        # название
        name_massage_label = ctk.CTkLabel(massage_review_frame, text="Название", width=80, anchor='e')
        name_massage_label.grid(row=0, column=0, padx=(15, 5), pady=(10, 15), sticky='e')

        self.name_massage_entry = ctk.CTkEntry(massage_review_frame, width=350)
        self.name_massage_entry.insert(0, "")
        self.name_massage_entry.grid(row=0, column=1, columnspan=2, padx=(5, 10), pady=(10, 15), sticky='w')
        self.name_massage_entry.configure(state="disabled")

        # категория
        category_massage_label = ctk.CTkLabel(massage_review_frame, text="Категория", width=80, anchor='e')
        category_massage_label.grid(row=1, column=0, padx=(15, 5), pady=(10, 15), sticky='e')

        # Получаем все категории активных массажей из бд
        bd = MassagesData()
        self.categories_dict = bd.read_tbl_categories_massages()
        categories = []
        for i, (name_category, id_category) in enumerate(self.categories_dict.items()):
            categories.append(name_category)

        var = StringVar()
        self.category_massage_entry = ctk.CTkOptionMenu(massage_review_frame, dynamic_resizing=False, variable=var,
                                                        values=categories, width=350)
        self.category_massage_entry.grid(row=1, column=1, columnspan=2, padx=(5, 10), pady=(10, 15), sticky='w')
        self.category_massage_entry.configure(state="disabled")

        # статус
        activity_massage_label = ctk.CTkLabel(massage_review_frame, text="Статус", width=40)
        activity_massage_label.grid(row=0, column=3, padx=(10, 5), pady=(10, 15), sticky='e')

        self.activity_massage_entry = ctk.CTkSwitch(massage_review_frame, switch_width=40, text='На стопе')
        self.activity_massage_entry.grid(row=0, column=4, padx=(5, 15), pady=(10, 15), sticky='we')
        self.activity_massage_entry.configure(state="disabled")
        self.activity_massage_entry.bind("<Button-1>", command=self.click_status)

        # цена
        price_massage_label = ctk.CTkLabel(massage_review_frame, text="Цена(руб.)", width=40)
        price_massage_label.grid(row=1, column=3, padx=(10, 5), pady=(10, 15), sticky='e')

        self.price_massage_entry = ctk.CTkEntry(massage_review_frame, width=150)
        self.price_massage_entry.insert(0, "")
        self.price_massage_entry.grid(row=1, column=4, padx=(5, 15), pady=(10, 15), sticky='we')
        self.price_massage_entry.configure(state="disabled")

        # комнаты
        self.rooms_massage_scrollframe = ctk.CTkScrollableFrame(massage_review_frame, label_text="Комнаты", height=100)
        self.rooms_massage_scrollframe.grid(row=3, column=3, columnspan=2, padx=(10, 15), pady=(10, 15), sticky='we')

        self.rooms_massage_scrollframe.grid_columnconfigure((0, 1), weight=1)
        self.rooms_massage_scrollframe.scrollbar.configure(height=0)
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

        # длительность
        duration_massage_label = ctk.CTkLabel(massage_review_frame, text="Длительность", width=40)
        duration_massage_label.grid(row=4, column=3, padx=(10, 5), pady=(10, 15), sticky='e')

        self.duration_massage_entry = ctk.CTkEntry(massage_review_frame, width=150)
        self.duration_massage_entry.insert(0, "")
        self.duration_massage_entry.grid(row=4, column=4, padx=(5, 15), pady=(10, 15), sticky='we')
        self.duration_massage_entry.configure(state="disabled")

        # перерыв
        break_massage_label = ctk.CTkLabel(massage_review_frame, text="Перерыв", width=40)
        break_massage_label.grid(row=5, column=3, padx=(10, 5), pady=(10, 15), sticky='e')

        self.break_massage_entry = ctk.CTkEntry(massage_review_frame, width=150)
        self.break_massage_entry.insert(0, "")
        self.break_massage_entry.grid(row=5, column=4, padx=(5, 15), pady=(10, 15), sticky='we')
        self.break_massage_entry.configure(state="disabled")

        # количество
        number_persons_massage_label = ctk.CTkLabel(massage_review_frame, text="Количество", width=40)
        number_persons_massage_label.grid(row=6, column=3, padx=(10, 5), pady=(10, 15), sticky='e')

        self.number_persons_massage_entry = ctk.CTkSwitch(massage_review_frame, width=40, text=' 1 человек')
        self.number_persons_massage_entry.grid(row=6, column=4, padx=(5, 15), pady=(10, 15), sticky='we')
        self.number_persons_massage_entry.configure(state="disabled")
        self.number_persons_massage_entry.bind("<Button-1>", command=self.click_number_persons)

        # описание
        description_massage_label = ctk.CTkLabel(massage_review_frame, text="Описание")
        description_massage_label.grid(row=2, column=0, padx=(15, 10), pady=(10, 5), sticky='w')

        self.description_massage_textbox = ctk.CTkTextbox(massage_review_frame, height=225, width=440)
        self.description_massage_textbox.insert(0.0, "")
        self.description_massage_textbox.grid(row=3, column=0, columnspan=3, rowspan=7, padx=(15, 10), pady=(10, 15),
                                              sticky='wns')
        self.description_massage_textbox.configure(state="disabled")
        massage_review_frame.grid_columnconfigure(3, weight=1)

        # кнопки
        # когда открыта карточка для просмотра
        self.edit_massage_button = ctk.CTkButton(self, text='Редактировать', command=self.click_edit_massage)
        # self.edit_massage_button.grid(row=1, column=0, padx=(15, 5), pady=(5, 15), sticky='w')

        # когда открыта карточка для просмотра
        self.delete_massage_button = ctk.CTkButton(self, text='Удалить', command=self.click_delete_massage)
        # self.delete_massage_button.grid(row=1, column=1, padx=(5, 15), pady=(5, 15), sticky='w')

        # когда находимся в режиме создания или редактирования
        self.cancel_massage_button = ctk.CTkButton(self, text='Отменить', command=self.click_cancel)
        # self.cancel_massage_button.grid(row=1, column=2, padx=(15, 5), pady=(5, 15), sticky='e')

        # когда находимся в режиме создания или редактирования
        self.save_massage_button = ctk.CTkButton(self, text='Сохранить',
                                                 command=partial(self.click_save_massage, 'create'))
        # self.save_massage_button.grid(row=1, column=3, padx=(15, 5), pady=(5, 15), sticky='e')

        # когда создается карточка
        # self.clear_form_massage_button = ctk.CTkButton(self, text='Очистить')
        # self.clear_form_massage_button.grid(row=1, column=2, padx=(15, 5), pady=(5, 15), sticky='e')

        # когда ничего не открыто или когда открыта карточка для просмотра
        self.create_massage_button = ctk.CTkButton(self, text='Создать', command=self.click_create_massage)
        self.create_massage_button.grid(row=1, column=3, padx=15, pady=(5, 10), sticky='e')

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
        self.price_massage_entry.insert(0, "{:.2f}".format(float(self.massages[row]['цена'])))
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

        self.cancel_massage_button.grid_forget()
        self.save_massage_button.grid_forget()

        self.edit_massage_button.grid(row=1, column=0, padx=(15, 5), pady=(5, 10), sticky='w')
        self.delete_massage_button.grid(row=1, column=1, padx=(5, 15), pady=(5, 10), sticky='w')
        self.create_massage_button.grid(row=1, column=3, padx=15, pady=(5, 10), sticky='e')

    def click_save_massage(self, action):
        name_massage = self.name_massage_entry.get()
        category_massage = self.category_massage_entry.get()
        activity_massage = self.activity_massage_entry.cget('text')
        price_massage = self.price_massage_entry.get()
        description_massage = self.description_massage_textbox.get(0.0, 'end')
        rooms_massage = []

        for i, checkbox in enumerate(self.checkboxes):
            if self.checkboxes[i].get() == "on":
                rooms_massage.append(self.rooms_dict[self.checkboxes[i].cget('text')])

        duration_massage = self.duration_massage_entry.get()
        break_massage = self.break_massage_entry.get()
        if self.number_persons_massage_entry.get():
            number_persons_massage = 2
        else:
            number_persons_massage = 1

        errors = {
            'отсутствие': [],
            'формат': []
        }
        # название +
        if not name_massage:
            errors['отсутствие'].append('название')
        else:
            # проверка на количество символов(до 60?)
            if len(name_massage) > 60:
                errors['формат'].append('Название должно быть не более 60 символов')
            else:
                # получить все названия
                pass

        # категория +
        if not category_massage:
            errors['отсутствие'].append('категория')
        else:
            category_massage = self.categories_dict[self.category_massage_entry.get()]

        # цена +
        if not price_massage:
            errors['отсутствие'].append('цена')
        else:
            try:
                price = float(price_massage)
                price_massage = round(price, 2)
            except ValueError:
                errors['формат'].append('Цена должна быть числом')

        # описание(может быть пустым) +
        if description_massage:
            # проверка на количество символов(до 3000?)
            if len(description_massage) > 3001:
                errors['формат'].append('Описание должно содержать не более 3000 символов')

        # комнаты +
        if not rooms_massage:
            errors['отсутствие'].append('комнаты')

        # длительность +
        if not duration_massage:
            errors['отсутствие'].append('длительность')
        else:
            time_regex = r'^(0[0-4]):([0-5]\d)$'
            if not re.match(time_regex, duration_massage):
                errors['формат'].append('Длительность должна иметь формат HH:MM и быть 00:00-04:59')

        # перерыв +
        if not break_massage:
            errors['отсутствие'].append('перерыв')
        else:
            time_regex = r'^(00):([0-5]\d)$'
            if not re.match(time_regex, break_massage):
                errors['формат'].append('Перерыв должен иметь формат HH:MM и быть 00:00-00:59')

        if errors['отсутствие']:
            message = f"Не заполнено - {errors['отсутствие'][0]}"
            CTkMessagebox(title="Ошибка", message=message, icon="cancel")
            return
        elif errors['формат']:
            message = errors['формат'][0]
            CTkMessagebox(title="Ошибка", message=message, icon="cancel")
            return

        if action == 'edit':
            print('Будем редактировать')
            id_massage = self.massages[self.selected_row]['id_массажа']
            bd = MassagesData()
            bd.update_massage(id_massage, name_massage, category_massage, activity_massage, price_massage, rooms_massage,
                              duration_massage, break_massage, number_persons_massage, description_massage)
            CTkMessagebox(title="Успешно", message="Массаж успешно отредактирован", icon="check", option_1="Окей")
            self.click_cancel()
            self.filter_frame.update_massages_table_frame()
        elif action == 'create':
            print('Будем создавать')
            bd = MassagesData()
            bd.create_massage(name_massage, category_massage, activity_massage, price_massage, rooms_massage,
                              duration_massage, break_massage, number_persons_massage, description_massage)
            CTkMessagebox(title="Успешно", message="Массаж успешно записан", icon="check", option_1="Окей")
            self.click_cancel()
            self.filter_frame.update_massages_table_frame()

    def click_delete_massage(self):
        # добавить проверку услуги в расписании
        id_massage = self.massages[self.selected_row]['id_массажа']
        bd = MassagesData()
        bd.delete_massage(id_massage)
        CTkMessagebox(title="Успешно", message="Массаж удален", icon="check", option_1="Окей")
        self.click_cancel()
        self.filter_frame.update_massages_table_frame()

    def click_create_massage(self):
        self.table_frame.unselect_massage()

        self.clear_info_frame()

        self.edit_massage_button.grid_forget()
        self.delete_massage_button.grid_forget()
        self.create_massage_button.grid_forget()

        self.cancel_massage_button.grid(row=1, column=2, padx=(15, 5), pady=(5, 10), sticky='e')
        self.save_massage_button.grid(row=1, column=3, padx=(5, 15), pady=(5, 10), sticky='e')

        self.save_massage_button.configure(command=partial(self.click_save_massage, 'create'))

    def click_edit_massage(self):
        # название
        self.name_massage_entry.configure(state="normal")

        # категория
        self.category_massage_entry.configure(state="normal")

        # статус
        self.activity_massage_entry.configure(state="normal")

        # цена
        self.price_massage_entry.configure(state="normal")

        # описание
        self.description_massage_textbox.configure(state="normal")

        # комнаты
        for i, checkbox in enumerate(self.checkboxes):
            self.checkboxes[i].configure(state="normal")

        # длительность
        self.duration_massage_entry.configure(state="normal")

        # перерыв
        self.break_massage_entry.configure(state="normal")

        # количество
        self.number_persons_massage_entry.configure(state="normal")

        self.edit_massage_button.grid_forget()
        self.delete_massage_button.grid_forget()
        self.create_massage_button.grid_forget()

        self.cancel_massage_button.grid(row=1, column=2, padx=(15, 5), pady=(5, 10), sticky='e')
        self.save_massage_button.grid(row=1, column=3, padx=(5, 15), pady=(5, 10), sticky='e')

        self.save_massage_button.configure(command=partial(self.click_save_massage, 'edit'))

    def click_cancel(self):
        self.table_frame.unselect_massage()
        self.clear_info_frame('disabled')

        self.edit_massage_button.grid_forget()
        self.delete_massage_button.grid_forget()
        self.save_massage_button.grid_forget()
        self.cancel_massage_button.grid_forget()

        self.create_massage_button.grid(row=1, column=3, padx=15, pady=(5, 10), sticky='e')

    def clear_info_frame(self, state='normal'):
        # название
        self.name_massage_entry.configure(state="normal")
        self.name_massage_entry.delete(0, tk.END)
        if state == 'disabled':
            self.name_massage_entry.configure(state=state)

        # категория
        self.category_massage_entry.configure(state="normal")
        var = StringVar()
        self.category_massage_entry.configure(variable=var)
        if state == 'disabled':
            self.category_massage_entry.configure(state=state)

        # статус
        self.activity_massage_entry.configure(state="normal")
        self.activity_massage_entry.deselect()
        self.activity_massage_entry.configure(text='на стопе')
        if state == 'disabled':
            self.activity_massage_entry.configure(state=state)

        # цена
        self.price_massage_entry.configure(state="normal")
        self.price_massage_entry.delete(0, tk.END)
        if state == 'disabled':
            self.price_massage_entry.configure(state=state)

        # описание
        self.description_massage_textbox.configure(state="normal")
        self.description_massage_textbox.delete(0.0, 'end')
        if state == 'disabled':
            self.description_massage_textbox.configure(state=state)

        # комнаты
        for i, checkbox in enumerate(self.checkboxes):
            self.checkboxes[i].configure(state="normal")
            self.checkboxes[i].configure(variable=ctk.StringVar(value="off"))
            if state == 'disabled':
                self.checkboxes[i].configure(state=state)

        # длительность
        self.duration_massage_entry.configure(state="normal")
        self.duration_massage_entry.delete(0, tk.END)
        if state == 'disabled':
            self.duration_massage_entry.configure(state=state)

        # перерыв
        self.break_massage_entry.configure(state="normal")
        self.break_massage_entry.delete(0, tk.END)
        if state == 'disabled':
            self.break_massage_entry.configure(state=state)

        # количество
        self.number_persons_massage_entry.configure(state="normal")
        self.number_persons_massage_entry.deselect()
        self.number_persons_massage_entry.configure(text='1 человек')
        if state == 'disabled':
            self.number_persons_massage_entry.configure(state=state)

    def click_status(self, event):
        if self.activity_massage_entry.cget('state') == 'normal':
            if self.activity_massage_entry.get():
                self.activity_massage_entry.configure(text='активен')
            else:
                self.activity_massage_entry.configure(text='на стопе')

    def click_number_persons(self, event):
        if self.number_persons_massage_entry.cget('state') == 'normal':
            if self.number_persons_massage_entry.get():
                self.number_persons_massage_entry.configure(text='2 человека')
            else:
                self.number_persons_massage_entry.configure(text='1 человек')
