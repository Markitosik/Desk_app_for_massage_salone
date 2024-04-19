from frontend.Authorization import Authorization
from frontend.CosmeticsFrame0_1 import *
from frontend.Schedule.Тест2 import *
from frontend.Massages.ServicesFrame1_0 import *

from functools import partial
import customtkinter as ctk
from PIL import Image
import math

ctk.set_appearance_mode("System")


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.list_names_frames = []
        self.list_frames = ''
        self.title("Главная")

        screen_width = self.winfo_screenwidth()  # Ширина экрана
        screen_height = self.winfo_screenheight()  # Высота экрана

        self.minsize(1536, 784)
        self.geometry(f"{1536}x{784}+0+0")

        #self.state('zoomed')
        #self.resizable(False, False)

        self.authorization = Authorization(self)
        self.user = ''
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Создание контейнера для контента
        self.container = ctk.CTkFrame(self, corner_radius=0)

        self.container.grid(row=0, column=1, rowspan=2, sticky='nsew')
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frames = {}

    def make_frames(self, root_user):
        self.user = root_user
        self.list_frames = ''
        if root_user == "superuser":
            self.list_frames = (ScheduleFrame, CosmeticsFrame, ServicesFrame, MastersFrame, RoomsFrame, ShiftsFrame,
                                AdminsFrame, TypesOfPaymentsFrame, ParametersSalonFrame)
            self.list_names_frames = ['Расписание', 'Продукция', 'Массажи', 'Массажисты', 'Комнаты', "Смены",
                                      'Администраторы', 'Типы оплаты', 'Параметры салона']
        elif root_user == "":
            self.list_frames = ScheduleFrame, CosmeticsFrame, ServicesFrame, MastersFrame, RoomsFrame, ShiftsFrame
            self.list_names_frames = ['Расписание', 'Продукция', 'Массажи', 'Массажисты', 'Комнаты', "Смены"]
        else:
            self.list_frames = ()
            self.list_names_frames = []

        for F in self.list_frames:
            page_name = F.__name__
            self.frames[page_name] = F(self.container, self)
            self.frames[page_name].configure(corner_radius=5)
            self.frames[page_name].grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.show_frame("CosmeticsFrame")

    def show_sidebar(self):
        ProfileFrame(self)
        MenuFrame(self)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class MenuFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        ctk.CTkScrollableFrame.__init__(self, parent)
        self.configure(corner_radius=0)
        self.grid(row=1, column=0, sticky='nswe')
        self.grid_columnconfigure(0, weight=1)

        buttons = {}
        for index, name in enumerate(parent.list_frames):
            buttons[index] = ctk.CTkButton(self, text=parent.list_names_frames[index], height=35, width=180,
                                           command=partial(parent.show_frame, name.__name__))
            buttons[index].grid(row=index, column=0, columnspan=4, pady=10, padx=(35, 35))


class ProfileFrame(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent)
        self.configure(corner_radius=0)
        settings_img = ctk.CTkImage(light_image=Image.open("../images/settings.jpg"),
                                    dark_image=Image.open("../images/settings.jpg"),
                                    size=(20, 20))

        exit_img = ctk.CTkImage(light_image=Image.open("../images/exit.jpg"),
                                dark_image=Image.open("../images/exit.jpg"),
                                size=(20, 20))

        label = ctk.CTkLabel(self, fg_color="grey", width=168, text=parent.authorization.username(), corner_radius=5)

        settings_button = ctk.CTkButton(self, text='', image=settings_img, height=30, width=30)

        exit_button = ctk.CTkButton(self, text='', image=exit_img, height=30, width=30,
                                    command=partial(Authorization.logout, parent.authorization))

        line = ctk.CTkFrame(self, fg_color="black", height=2, width=280, corner_radius=0)

        label.grid(row=0, column=0, pady=20, padx=(10, 5), sticky='nswe')
        settings_button.grid(row=0, column=1, pady=20, padx=(5, 5))
        exit_button.grid(row=0, column=2, pady=20, padx=(5, 10))
        line.grid(row=1, column=0, columnspan=3)

        self.grid(row=0, column=0, sticky='nswe')


class ScheduleFrame1(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.configure(fg_color="red")
        label = ctk.CTkLabel(self, text="Расписание")

        label.pack(padx=10, pady=10)


class ParametersSalonFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        #self.configure(fg_color="red")
        label = ctk.CTkLabel(self, text="Параметры салона")

        label.pack(padx=10, pady=10)


class CosmeticsFrame1(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        self.grid_columnconfigure((0, 4), weight=1)
        self.grid_rowconfigure(3, weight=1)
        label = ctk.CTkLabel(self, text="Косметика")
        label.grid(row=0, column=1, columnspan=3, padx=10, pady=(10, 0), sticky='we')

        #add_button = ctk.CTkButton(self, text="Добавить", width=107)
        #add_button.grid(row=1, column=3, pady=10, padx=(10, 0), sticky='we')

        filter_frame = ctk.CTkFrame(self)
        filter_frame.grid(row=1, column=1, rowspan=2, pady=(25, 25), padx=(25, 10), sticky='nswe')

        filter_frame.grid_columnconfigure((0, 1), weight=1)

        filter_label = ctk.CTkLabel(filter_frame, text='Фильтр')
        filter_label.grid(row=0, column=0, columnspan=2, padx=15, pady=(5, 0))

        search_entry = ctk.CTkEntry(filter_frame, width=175, placeholder_text="Название")
        search_entry.grid(row=1, column=0, pady=10, padx=(15, 5), sticky='we')

        search_button = ctk.CTkButton(filter_frame, text="Поиск", width=57, command=self.filter_table)
        search_button.grid(row=1, column=1, pady=10, padx=(5, 15), sticky='we')

        prices_frame = ctk.CTkFrame(filter_frame)
        prices_frame.grid(row=2, column=0, columnspan=2, padx=15, pady=10, sticky='nswe')

        price_label = ctk.CTkLabel(prices_frame, text='Цена, руб.')
        price_label.grid(row=0, column=0, padx=15)

        price_from_entry = ctk.CTkEntry(prices_frame, placeholder_text="От")
        price_from_entry.grid(row=1, column=0, padx=15, pady=(0, 5), sticky='we')

        price_to_entry = ctk.CTkEntry(prices_frame, placeholder_text="До")
        price_to_entry.grid(row=1, column=1, padx=15, pady=(0, 5))

        categories_scrollframe = ctk.CTkScrollableFrame(filter_frame, label_text="Категории", height=135)
        categories_scrollframe.grid(row=3, column=0, columnspan=2, padx=15, pady=10, sticky='we')

        categories_scrollframe.grid_columnconfigure((0, 1), weight=1)
        categories_scrollframe._scrollbar.configure(height=0)
        self.scrollable_frame_checkboxes = []
        categories = {'губы', 'глаза', 'лицо'}
        check_var = {}
        for i, category in enumerate(categories):
            check_var[i] = ctk.StringVar(value="off")
            checkbox = ctk.CTkCheckBox(categories_scrollframe, text=category, variable=check_var[i], onvalue="on", offvalue="off")
            checkbox.grid(row=math.floor(i), column=0, padx=0, pady=(0, 10), sticky='w')
            self.scrollable_frame_checkboxes.append(checkbox)

        cosmetic_frame = ctk.CTkFrame(self, fg_color='green')
        cosmetic_frame.columnconfigure(2, weight=1)
        cosmetic_frame.grid(row=1, column=2, columnspan=2, pady=(25, 10), padx=(10, 25), sticky='nswe')

        cosmetic_review_frame = ctk.CTkFrame(cosmetic_frame, fg_color='grey', bg_color="transparent")
        cosmetic_review_frame.grid(row=0, column=0, columnspan=4, padx=(0,0.5), sticky='nswe')

        cosmetic_review_label = ctk.CTkLabel(cosmetic_review_frame, text='Обзор')
        cosmetic_review_label.grid(row=0, column=0, padx=15, pady=(5, 5), sticky='we')

        name_cosmetic_label = ctk.CTkLabel(cosmetic_review_frame, text="Название")
        name_cosmetic_label.grid(row=1, column=0, padx=15, pady=(10, 10), sticky='we')

        name_cosmetic_entry = ctk.CTkEntry(cosmetic_review_frame)
        name_cosmetic_entry.insert(0, "1 имя")
        name_cosmetic_entry.grid(row=1, column=1, padx=15, pady=(10, 10), sticky='we')
        name_cosmetic_entry.configure(state="disabled")

        category_cosmetic_label = ctk.CTkLabel(cosmetic_review_frame, text="Категория")
        category_cosmetic_label.grid(row=2, column=0, padx=15, pady=(10, 10), sticky='we')

        var = StringVar(root)
        var.set("1 категория")
        category_cosmetic_entry = ctk.CTkOptionMenu(cosmetic_review_frame, dynamic_resizing=False, variable=var,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"])
        category_cosmetic_entry.grid(row=2, column=1, padx=15, pady=(10, 10), sticky='we')
        category_cosmetic_entry.configure(state="disabled")

        price_cosmetic_label = ctk.CTkLabel(cosmetic_review_frame, text="Цена(руб.)")
        price_cosmetic_label.grid(row=3, column=0, padx=15, pady=(10, 10), sticky='we')

        price_cosmetic_entry = ctk.CTkEntry(cosmetic_review_frame)
        price_cosmetic_entry.insert(0, "1500")
        price_cosmetic_entry.grid(row=3, column=1, padx=15, pady=(10, 10), sticky='we')
        price_cosmetic_entry.configure(state="disabled")

        quantity_cosmetic_label = ctk.CTkLabel(cosmetic_review_frame, text="Количество")
        quantity_cosmetic_label.grid(row=4, column=0, padx=15, pady=(10, 10), sticky='we')

        quantity_cosmetic_entry = ctk.CTkEntry(cosmetic_review_frame)
        quantity_cosmetic_entry.insert(0, "5")
        quantity_cosmetic_entry.grid(row=4, column=1, padx=15, pady=(10, 10), sticky='we')
        quantity_cosmetic_entry.configure(state="disabled")

        description_cosmetic_label = ctk.CTkLabel(cosmetic_review_frame, text="Описание")
        description_cosmetic_label.grid(row=1, column=2, padx=15, pady=(10, 10), sticky='we')

        description_cosmetic_textbox = ctk.CTkTextbox(cosmetic_review_frame, height=125)
        description_cosmetic_textbox.insert(0.0, "Очень-очень хороший кремушек для лица. Покупайте на здоровье)")
        description_cosmetic_textbox.grid(row=2, column=2, rowspan=3, columnspan=2, padx=15, pady=(10, 10), sticky='we')
        description_cosmetic_textbox.configure(state="disabled")
        cosmetic_review_frame.grid_columnconfigure(3, weight=1)

        edit_cosmetic_button = ctk.CTkButton(cosmetic_frame, text='Редактировать')
        edit_cosmetic_button.grid(row=1, column=0, padx=(15, 5), pady=(10, 10), sticky='w')

        delete_cosmetic_button = ctk.CTkButton(cosmetic_frame, text='Удалить')
        delete_cosmetic_button.grid(row=1, column=1, padx=(5, 15), pady=(10, 10), sticky='w')

        create_cosmetic_button = ctk.CTkButton(cosmetic_frame, text='Создать')
        create_cosmetic_button.grid(row=1, column=3, padx=15, pady=(10, 10), sticky='e')

        #три кнопки "Создать запись", "Редактировать", "Удалить"
        #куда добавить управление категориями?
        #cosmetic_review_frame.grid_rowconfigure((2, 3, 4), weight=1)

        cosmetics_table_frame = ctk.CTkFrame(self)
        cosmetics_table_frame.grid(row=2, column=2, columnspan=2, pady=(10, 25), padx=(10, 25), sticky='nswe')

        columns1 = ctk.CTkLabel(cosmetics_table_frame, fg_color='green', text="Название", width=200)
        columns2 = ctk.CTkLabel(cosmetics_table_frame, fg_color='blue', text="Количество(шт.)", width=150)
        columns3 = ctk.CTkLabel(cosmetics_table_frame, fg_color='blue', text="Категория", width=150)
        columns4 = ctk.CTkLabel(cosmetics_table_frame, fg_color='green', text="Цена(руб.)", width=150)

        columns1.grid(row=0, column=0, sticky='we', padx=(10, 0))
        columns2.grid(row=0, column=1, sticky='we', padx=0)
        columns3.grid(row=0, column=2, sticky='we', padx=0)
        columns4.grid(row=0, column=3, sticky='we', padx=(0, 14))
        self.table1 = ctk.CTkScrollableFrame(cosmetics_table_frame, fg_color='transparent', height=250,
                                        corner_radius=0)

        self.table1.grid(row=1, column=0, columnspan=4, padx=(10, 0), pady=(0, 10), sticky='we')

        self.names = {}
        self.counts = {}
        self.categories = {}
        self.prices = {}
        self.cosmetics = [
            {
                "id": "1",
                "название": "Помада",
                "количество": 10,
                "категория": "губы",
                "цена": 100,
                "описание": "Сочный цвет и увлажнение для губ."
            },
            {
                "id": "2",
                "название": "Тушь для ресниц",
                "количество": 20,
                "категория": "глаза",
                "цена": 150,
                "описание": "Создайте захватывающий объем и длину ресниц."
            },
            {
                "id": "3",
                "название": "Тональный крем",
                "количество": 5,
                "категория": "лицо",
                "цена": 200,
                "описание": "Обеспечивает равномерное покрытие и скрытие несовершенств кожи."
            },
        ]
        for i, cosmetic in enumerate(self.cosmetics):
            self.names[i] = ctk.CTkLabel(self.table1, text=cosmetic['название'], width=200)
            self.counts[i] = ctk.CTkLabel(self.table1, text=cosmetic['количество'], width=150)
            self.categories[i] = ctk.CTkLabel(self.table1, text=cosmetic['категория'], width=150)
            self.prices[i] = ctk.CTkLabel(self.table1, text=cosmetic['цена'], width=150)

            self.names[i].grid(row=i + 1, column=0)
            self.counts[i].grid(row=i + 1, column=1)
            self.categories[i].grid(row=i + 1, column=2)
            self.prices[i].grid(row=i + 1, column=3)

            self.names[i].bind('<ButtonPress-1>', command=self.label_click)

    def label_click(self, event):
        print("Кликнули по Label")
        print(event)
        #использовать прокрутку для расписания
        #table1.after(10, table1._parent_canvas.yview_moveto, 1.0)

    def filter_table(self):
        # Очистить таблицу
        for widget in self.table1.winfo_children():
            widget.destroy()

        # Получить выбранные категории
        checked_categories = [checkbox.cget('text') for checkbox in self.scrollable_frame_checkboxes if
                              checkbox.get() == 'on']


        # Отфильтровать косметику по выбранным категориям
        filtered_cosmetics = [cosmetic for cosmetic in self.cosmetics if cosmetic['категория'] in checked_categories]

        idents = {}
        names = {}
        counts = {}
        categories = {}
        prices = {}
        # Отображение отфильтрованных данных
        for i, cosmetic in enumerate(filtered_cosmetics):
            idents[i] = cosmetic['id']
            names[i] = ctk.CTkLabel(self.table1, text=cosmetic['название'], width=200)
            counts[i] = ctk.CTkLabel(self.table1, text=cosmetic['количество'], width=150)
            categories[i] = ctk.CTkLabel(self.table1, text=cosmetic['категория'], width=150)
            prices[i] = ctk.CTkLabel(self.table1, text=cosmetic['цена'], width=150)

            names[i].grid(row=i + 1, column=0)
            counts[i].grid(row=i + 1, column=1)
            categories[i].grid(row=i + 1, column=2)
            prices[i].grid(row=i + 1, column=3)

            names[i].bind('<ButtonPress-1>',  self.label_click)



class MastersFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Массажисты")

        label.pack(padx=10, pady=10)


class RoomsFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Комнаты")

        label.pack(padx=10, pady=10)


class ShiftsFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Смены")

        label.pack(padx=10, pady=10)


class AdminsFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Администраторы")

        label.pack(padx=10, pady=10)


class TypesOfPaymentsFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Виды платежей")

        label.pack(padx=10, pady=10)


if __name__ == "__main__":
    root = MainWindow()

    root.withdraw()
    root.mainloop()
