from tkinter import StringVar
import customtkinter as ctk
import tkinter as tk
import math
import screeninfo


# Для админа
class CosmeticsFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        self.grid_columnconfigure((0, 6), weight=1)
        self.grid_columnconfigure(1, minsize=150, weight=0)
        self.grid_rowconfigure((1, 2, 3), weight=1)

        label = ctk.CTkLabel(self, text="Продукция")
        label.grid(row=0, column=0, columnspan=7, padx=10, pady=(10, 0), sticky='we')

        self.selected_product = ''
        self.rows_frames = {}
        self.names_product = {}
        self.countries_product = {}
        self.categories_product = {}
        self.prices_product = {}

        self.number_product = {}
        self.description_product = {}
        self.activity_product = {}

        self.products = [
            {
                "id": "1",
                "название": "Крем для кожи лица",
                "страна": "Россия",
                "категория": "Массаж по маслу",
                "цена": 3900,
                "описание": """Один из древних методов релаксации и оздоровления - процедура с теплыми камушками (мы используем камни из природного минерала шунгита, известного своими оздоровительными качествами).
Программа благоприятно влияет на деятельность обменных процессов, снимает напряжение.
Ощущение физического и душевного равновесия гарантировано!"""
            },
            {
                "id": "2",
                "название": "Двойной удар по весу и целлюлиту",
                "страна": "Россия",
                "категория": "Антицеллюлитный массаж",
                "цена": 4500,
                "описание": """Эта согревающая SPA-программа, разработанная по древним восточным традициям и предназначенная для коррекции фигуры, удаления растяжек и уменьшения объема до 3 см !!! благодаря ярко выраженному лимфодренажному эффекту.
Комплексная программа состоит из нанесения смеси Param из белой глины, грязи Мертвого моря, экстракта жгучего перца, кокосового масла, гвоздики, мускатного ореха и интенсивного массажа с элементами уникальной тайской техники, направленной на укрепление кожи тела, потерю избыточного веса и избавление от целлюлита.
Это настоящее земное волшебство, способствующее быстрому достижению идеальной фигуры.

Эффекты процедуры:
избавление от лишних килограммов и целлюлита;
уменьшение растяжек,
подтяжка вялой кожи, ее интенсивное увлажнение,
сильная активизация микроциркуляции, вывод межклеточной жидкости;
упругость кожи."""
            },
            {
                "id": "3",
                "название": "Шелковый бриз",
                "страна": "Корея",
                "категория": "Массаж по маслу",
                "цена": 2700,
                "описание": """Комплексная программа основана на воздействии на энергетические каналы и точки на теле человека.
Виртуозные техники мастеров из Таиланда позволят снять напряжение с усталых ног и плеч, принесут облегчение при болях в затылке, бессоннице, улучшат общее самочувствие."""
            },
            {
                "id": "4",
                "название": "Шелковый бриз1",
                "страна": "Индия",
                "категория": "Массаж по маслу",
                "цена": 2700,
                "описание": """Комплексная программа основана на воздействии на энергетические каналы и точки на теле человека.
        Виртуозные техники мастеров из Таиланда позволят снять напряжение с усталых ног и плеч, принесут облегчение при болях в затылке, бессоннице, улучшат общее самочувствие."""
            },
            {
                "id": "5",
                "название": "Шелковый бриз2",
                "страна": "США",
                "категория": "Массаж по маслу",
                "цена": 2700,
                "описание": """Комплексная программа основана на воздействии на энергетические каналы и точки на теле человека.
        Виртуозные техники мастеров из Таиланда позволят снять напряжение с усталых ног и плеч, принесут облегчение при болях в затылке, бессоннице, улучшат общее самочувствие."""
            },
            {
                "id": "6",
                "название": "Шелковый бриз3",
                "страна": "Тайланд",
                "категория": "Массаж по маслу",
                "цена": 2700,
                "описание": """Комплексная программа основана на воздействии на энергетические каналы и точки на теле человека.
        Виртуозные техники мастеров из Таиланда позволят снять напряжение с усталых ног и плеч, принесут облегчение при болях в затылке, бессоннице, улучшат общее самочувствие."""
            },
            {
                "id": "7",
                "название": "Шелковый бриз4",
                "страна": "Вьетнам",
                "категория": "Массаж по маслу",
                "цена": 2700,
                "описание": """Комплексная программа основана на воздействии на энергетические каналы и точки на теле человека.
        Виртуозные техники мастеров из Таиланда позволят снять напряжение с усталых ног и плеч, принесут облегчение при болях в затылке, бессоннице, улучшат общее самочувствие."""
            },
        ]

        self.make_filter_frame()
        self.make_product_info_frame(parent)
        self.make_products_table_frame()

    def make_filter_frame(self):
        filter_frame = ctk.CTkFrame(self)

        filter_frame.grid(row=1, column=1, rowspan=4, pady=(20, 20), padx=(15, 10), sticky='ns')

        filter_frame.grid_columnconfigure((0, 3), weight=1)

        filter_label = ctk.CTkLabel(filter_frame, text='Фильтр')
        filter_label.grid(row=0, column=0, padx=(15, 5), pady=(5, 0), sticky='w')

        clear_button = ctk.CTkButton(filter_frame, text="Очистить", width=90, fg_color='grey20')
        clear_button.grid(row=0, column=2, columnspan=2, pady=10, padx=(5, 15))

        search_entry = ctk.CTkEntry(filter_frame, placeholder_text="Название", width=180)
        search_entry.grid(row=1, column=0, columnspan=3, pady=(10, 15), padx=(15, 5))

        search_button = ctk.CTkButton(filter_frame, text="Поиск", width=50)
        search_button.grid(row=1, column=3, columnspan=1, pady=(10, 15), padx=(5, 15))

        prices_frame = ctk.CTkFrame(filter_frame)
        prices_frame.grid(row=2, column=0, columnspan=4, padx=15, pady=(0, 15))

        price_label = ctk.CTkLabel(prices_frame, text='Цена, руб.')
        price_label.grid(row=0, column=0, columnspan=2, padx=10, sticky='w')

        price_from_entry = ctk.CTkEntry(prices_frame, placeholder_text="От", width=100)
        price_from_entry.grid(row=1, column=0, padx=10, pady=(0, 5))

        price_to_entry = ctk.CTkEntry(prices_frame, placeholder_text="До", width=100)
        price_to_entry.grid(row=1, column=1, padx=10, pady=(0, 5))

        countries_scrollframe = ctk.CTkScrollableFrame(filter_frame, label_text="Страны", height=100, width=220)
        countries_scrollframe.grid(row=3, column=0, columnspan=4, padx=15, pady=(0, 15))

        countries_scrollframe.grid_columnconfigure((0, 1), weight=1)
        countries_scrollframe._scrollbar.configure(height=0)
        scrollable_frame_checkboxes = []
        # Получаем все категории активных массажей из бд
        categories = {'Россия', 'США', 'Корея', 'Индия'}
        check_var = {}
        for i, category in enumerate(categories):
            check_var[i] = ctk.StringVar(value="off")
            checkbox = ctk.CTkCheckBox(countries_scrollframe, text=category, variable=check_var[i], onvalue="on",
                                       offvalue="off")
            checkbox.grid(row=math.floor(i), column=0, padx=0, pady=(0, 10), sticky='w')
            scrollable_frame_checkboxes.append(checkbox)


        categories_scrollframe = ctk.CTkScrollableFrame(filter_frame, label_text="Категории", height=100, width=220)
        categories_scrollframe.grid(row=4, column=0, columnspan=4, padx=15, pady=(0, 15))

        categories_scrollframe.grid_columnconfigure((0, 1), weight=1)
        categories_scrollframe._scrollbar.configure(height=0)
        scrollable_frame_checkboxes = []
        #Получаем все категории активных массажей из бд
        categories = {'Массаж по маслу', 'Антицеллюлитный массаж', 'лицо'}
        check_var = {}
        for i, category in enumerate(categories):
            check_var[i] = ctk.StringVar(value="off")
            checkbox = ctk.CTkCheckBox(categories_scrollframe, text=category, variable=check_var[i], onvalue="on",
                                       offvalue="off")
            checkbox.grid(row=math.floor(i), column=0, padx=0, pady=(0, 10), sticky='w')
            scrollable_frame_checkboxes.append(checkbox)

        activity_frame = ctk.CTkFrame(filter_frame)

        activity_frame.grid(row=5, column=0, columnspan=4, padx=15, pady=(0, 15))

        activity_label = ctk.CTkLabel(activity_frame, text='Статус')

        activity_label.grid(row=0, column=0, padx=10, sticky='w')

        var = StringVar()
        var.set("Все варианты")
        activity_option_menu = ctk.CTkOptionMenu(activity_frame, dynamic_resizing=False, variable=var,
                                                 values=["Все варианты", "Активный", "На стопе"],
                                                 width=220)
        activity_option_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 5), sticky='we')

        availability_frame = ctk.CTkFrame(filter_frame)

        availability_frame.grid(row=6, column=0, columnspan=4, padx=15, pady=0)

        availability_label = ctk.CTkLabel(availability_frame, text='Наличие на складе')

        availability_label.grid(row=0, column=0, padx=10, sticky='w')

        var = StringVar()
        var.set("Все варианты")
        availability_option_menu = ctk.CTkOptionMenu(availability_frame, dynamic_resizing=False, variable=var,
                                                 values=["Все варианты", "Нет в наличии", "В наличии"],
                                                 width=220)
        availability_option_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 5), sticky='we')

    def make_product_info_frame(self, parent):
        monitor = screeninfo.get_monitors()[0]
        if parent.master.user == 'superuser':
            self.product_frame = ctk.CTkFrame(self)
            self.product_frame.columnconfigure(2, weight=1)
            self.product_frame.rowconfigure(0, weight=1)
            self.product_frame.grid(row=1, column=2, rowspan=3, columnspan=3, pady=(20, 10), padx=(10, 15),
                                    sticky='nswe')

            product_review_frame = ctk.CTkScrollableFrame(self.product_frame, label_text='Карточка продукта')
            product_review_frame.rowconfigure(0, weight=1)
            #product_review_frame._label.grid(row=0, column=0)
            #product_review_frame.columnconfigure(1, weight=1)

            product_review_frame.grid(row=0, column=0, columnspan=4, padx=(15, 15), pady=(10, 5), sticky='nswe')
        else:
            self.product_frame = ctk.CTkScrollableFrame(self, label_text='Карточка продукта')

            product_review_frame = self.product_frame
            #product_review_frame._label.grid(row=0, column=0, sticky='we')
            product_review_frame.columnconfigure(1, weight=1)
            product_review_frame.grid(row=1, column=2, rowspan=3, columnspan=3, pady=(20, 10), padx=(10, 15),
                                      sticky='nswe')

        name_product_label = ctk.CTkLabel(product_review_frame, text="Название", width=80, anchor='e')
        name_product_label.grid(row=0, column=0, padx=(15, 5), pady=(10, 15), sticky='e')

        self.name_product_entry = ctk.CTkEntry(product_review_frame, width=350)
        self.name_product_entry.insert(0, "")
        self.name_product_entry.grid(row=0, column=1, columnspan=2, padx=(5, 10), pady=(10, 15), sticky='w')
        self.name_product_entry.configure(state="disabled")

        category_product_label = ctk.CTkLabel(product_review_frame, text="Категория", width=80, anchor='e')
        category_product_label.grid(row=1, column=0, padx=(15, 5), pady=(10, 15), sticky='e')

        var = StringVar(parent)
        var.set("")
        self.category_product_entry = ctk.CTkOptionMenu(product_review_frame, dynamic_resizing=False, variable=var,
                                                    values=["Value 1", "Value 2", "Value Long Long Long"], width=350)
        self.category_product_entry.grid(row=1, column=1, columnspan=2, padx=(5, 10), pady=(10, 15), sticky='w')
        self.category_product_entry.configure(state="disabled")

        country_product_label = ctk.CTkLabel(product_review_frame, text="Страна", width=40)
        country_product_label.grid(row=3, column=3, padx=(10, 5), pady=(10, 15), sticky='en')

        self.country_product_entry = ctk.CTkEntry(product_review_frame, width=150)
        self.country_product_entry.insert(0, "")
        self.country_product_entry.grid(row=3, column=4, rowspan=1, padx=(5, 15), pady=(10, 15), sticky='wen')
        self.country_product_entry.configure(state="disabled")

        price_product_label = ctk.CTkLabel(product_review_frame, text="Цена(руб.)", width=40)
        price_product_label.grid(row=1, column=3, padx=(10, 5), pady=(10, 15), sticky='e')

        self.price_product_entry = ctk.CTkEntry(product_review_frame, width=150)
        self.price_product_entry.insert(0, "")
        self.price_product_entry.grid(row=1, column=4, padx=(5, 15), pady=(10, 15), sticky='we')
        self.price_product_entry.configure(state="disabled")


        activity_product_label = ctk.CTkLabel(product_review_frame, text="Статус", width=40)
        activity_product_label.grid(row=0, column=3, padx=(10, 5), pady=(10, 15), sticky='e')

        self.activity_product_entry = ctk.CTkSwitch(product_review_frame, switch_width = 40, text='На стопе')
        self.activity_product_entry.grid(row=0, column=4, padx=(5, 15), pady=(10, 15), sticky='we')
        self.activity_product_entry.configure(state="disabled")


        description_product_label = ctk.CTkLabel(product_review_frame, text="Описание")
        description_product_label.grid(row=2, column=0, padx=(15, 10), pady=(10, 5), sticky='w')

        self.description_product_textbox = ctk.CTkTextbox(product_review_frame, height=225, width=440)
        self.description_product_textbox.insert(0.0, "")
        self.description_product_textbox.grid(row=3, column=0, columnspan=3, rowspan=10, padx=(15, 10), pady=(10, 15), sticky='wns')
        self.description_product_textbox.configure(state="disabled")
        product_review_frame.grid_columnconfigure(3, weight=1)

        if self.parent.master.user == 'superuser':
            #когда открыта карточка для просмотра
            self.edit_product_button = ctk.CTkButton(self.product_frame, text='Редактировать')
            #self.edit_product_button.grid(row=1, column=0, padx=(15, 5), pady=(5, 15), sticky='w')

            #когда открыта карточка для просмотра
            self.delete_product_button = ctk.CTkButton(self.product_frame, text='Удалить')
            #self.delete_product_button.grid(row=1, column=1, padx=(5, 15), pady=(5, 15), sticky='w')

            #когда находимся в режиме создания или редактирования
            self.cancel_product_button = ctk.CTkButton(self.product_frame, text='Отменить')
            #self.cancel_product_button.grid(row=1, column=2, padx=(15, 5), pady=(5, 15), sticky='e')

            #когда находимся в режиме создания или редактирования
            self.save_product_button = ctk.CTkButton(self.product_frame, text='Сохранить')
            #self.save_product_button.grid(row=1, column=3, padx=(15, 5), pady=(5, 15), sticky='e')

            #когда создается карточка
            self.clear_form_product_button = ctk.CTkButton(self.product_frame, text='Очистить')
            #self.clear_form_product_button.grid(row=1, column=2, padx=(15, 5), pady=(5, 15), sticky='e')

            #когда ничего не открыто или когда открыта карточка для просмотра
            self.create_product_button = ctk.CTkButton(self.product_frame, text='Создать', command=self.create_product)
            self.create_product_button.grid(row=1, column=3, padx=15, pady=(5, 10), sticky='e')

    def make_products_table_frame(self):
        product_table_frame = ctk.CTkFrame(self, height=150)
        product_table_frame.grid(row=4, column=2, columnspan=3, pady=(10, 20), padx=(10, 15), sticky='we')
        product_table_frame.rowconfigure(1, weight=1)

        column_names_frame = ctk.CTkFrame(product_table_frame)
        column_names_frame.grid(row=0, column=0, columnspan=4, sticky='we', padx=(10, 22), pady=(5, 0))

        columns1 = ctk.CTkLabel(column_names_frame, text="Название", width=225)
        columns2 = ctk.CTkLabel(column_names_frame, text="Страна", width=150)
        columns3 = ctk.CTkLabel(column_names_frame, text="Категория", width=225)
        columns4 = ctk.CTkLabel(column_names_frame, text="Цена(руб.)", width=150)

        columns1.grid(row=0, column=0, sticky='we', padx=(2, 1), pady=5)
        columns2.grid(row=0, column=1, sticky='we', padx=1, pady=5)
        columns3.grid(row=0, column=2, sticky='we', padx=1, pady=5)
        columns4.grid(row=0, column=3, sticky='we', padx=(1, 2), pady=5)
        self.table1 = ctk.CTkScrollableFrame(product_table_frame, fg_color='transparent',
                                             corner_radius=0, height=160)
        monitor = screeninfo.get_monitors()[0]
        if monitor.height > 1440:
            self.table1.configure(height=275)
        self.table1._scrollbar.configure(height=0)
        self.table1.grid(row=1, column=0, columnspan=4, padx=(10, 0), pady=(5, 10), sticky='we')

        for i, product in enumerate(self.products):
            self.rows_frames[i] = ctk.CTkFrame(self.table1, fg_color=['gray81', 'gray20'], corner_radius=7)
            self.rows_frames[i].grid(row=i + 1, column=0, columnspan=4, sticky='we', padx=(0, 8), pady=1)
            self.names_product[i] = ctk.CTkLabel(self.rows_frames[i], text=product['название'], width=225)
            self.countries_product[i] = ctk.CTkLabel(self.rows_frames[i], text=product['страна'], width=150)
            self.categories_product[i] = ctk.CTkLabel(self.rows_frames[i], text=product['категория'], width=225)
            self.prices_product[i] = ctk.CTkLabel(self.rows_frames[i], text=product['цена'], width=150)

            self.names_product[i].grid(row=i + 1, column=0, sticky='we', pady=2, padx=(2, 1))
            self.names_product[i].bind("<Button-1>", lambda event, row=i: self.callback(row))
            self.countries_product[i].grid(row=i + 1, column=1, sticky='we', pady=2, padx=(2, 1))
            self.countries_product[i].bind("<Button-1>", lambda event, row=i: self.callback(row))
            self.categories_product[i].grid(row=i + 1, column=2, sticky='we', pady=2, padx=1)
            self.categories_product[i].bind("<Button-1>", lambda event, row=i: self.callback(row))
            self.prices_product[i].grid(row=i + 1, column=3, sticky='we', pady=2, padx=(1, 2))
            self.prices_product[i].bind("<Button-1>", lambda event, row=i: self.callback(row))

    def callback(self, row):
        self.selected_product = row
        if self.parent.master.user == 'superuser':
            print('С фига ли')
            #когда открыта карточка для просмотра
            self.edit_product_button.grid(row=1, column=0, padx=(15, 5), pady=(5, 10), sticky='w')

            #когда открыта карточка для просмотра
            self.delete_product_button.grid(row=1, column=1, padx=(5, 15), pady=(5, 10), sticky='w')

            #когда ничего не открыто или когда открыта карточка для просмотра
            self.create_product_button.grid(row=1, column=3, padx=15, pady=(5, 10), sticky='e')

            # когда находимся в режиме создания или редактирования
            self.cancel_product_button.grid_remove()

            # когда находимся в режиме создания или редактирования
            self.save_product_button.grid_remove()

            # когда создается карточка
            self.clear_form_product_button.grid_remove()

        # сделать ограничение на длину строки в ячейке
        #print("Номер строки:", row)
        for i, product in enumerate(self.products):
            self.rows_frames[i].configure(fg_color=['gray81', 'gray20'])
        self.rows_frames[row].configure(fg_color='#1f6aa5')
        self.name_product_entry.configure(state="normal")
        self.name_product_entry.delete(0, tk.END)
        self.name_product_entry.insert(0, self.products[row]['название'])
        self.name_product_entry.configure(state="disabled")

        var = StringVar(self.parent)
        var.set(self.products[row]['категория'])

        self.category_product_entry.configure(variable=var)
        self.category_product_entry.configure(state="disabled")

        self.price_product_entry.configure(state="normal")
        self.price_product_entry.delete(0, tk.END)
        self.price_product_entry.insert(0, self.products[row]['цена'])
        self.price_product_entry.configure(state="disabled")


        self.description_product_textbox.configure(state="normal")
        self.description_product_textbox.delete("0.0", "end")
        self.description_product_textbox.insert(0.0, self.products[row]['описание'])
        self.description_product_textbox.configure(state="disabled")

    def create_product(self):
        # когда открыта карточка для просмотра
        self.edit_product_button.grid_remove()

        # когда открыта карточка для просмотра
        self.delete_product_button.grid_remove()

        # когда находимся в режиме создания или редактирования
        self.cancel_product_button.grid(row=1, column=2, padx=(15, 5), pady=(5, 10), sticky='e')

        # когда находимся в режиме создания или редактирования
        self.save_product_button.grid(row=1, column=3, padx=(5, 15), pady=(5, 10), sticky='e')

        # когда создается карточка
        self.clear_form_product_button.grid_remove()

        # когда ничего не открыто или когда открыта карточка для просмотра
        self.create_product_button.grid_remove()

        if self.selected_product != '':
            self.rows_frames[self.selected_product].configure(fg_color='#3b3b3b')

        self.name_product_entry.configure(state="normal")
        self.name_product_entry.delete(0, tk.END)

        var = StringVar(self.parent)
        var.set('')
        self.category_product_entry.configure(state="normal")
        self.category_product_entry.configure(variable=var)

        self.price_product_entry.configure(state="normal")
        self.price_product_entry.delete(0, tk.END)


        self.description_product_textbox.configure(state="normal")
        self.description_product_textbox.delete("0.0", "end")
