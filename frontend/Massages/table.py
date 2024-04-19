import customtkinter as ctk
import screeninfo


class TableFrame(ctk.CTkFrame):
    def __init__(self, parent, preq_parent):
        ctk.CTkFrame.__init__(self, parent, height=150)
        self.preq_parent = preq_parent
        self.massages = {}
        self.info_frame = None

        self.rows_frames = {}
        self.names = {}
        self.duration_massage = {}
        self.categories = {}
        self.prices = {}
        self.rowconfigure(1, weight=1)
        self.q = ''
        column_names_frame = ctk.CTkFrame(self)
        column_names_frame.grid(row=0, column=0, columnspan=4, sticky='we', padx=(10, 22), pady=(5, 0))

        columns1 = ctk.CTkLabel(column_names_frame, text="Название", width=225)
        columns2 = ctk.CTkLabel(column_names_frame, text="Длительность", width=150)
        columns3 = ctk.CTkLabel(column_names_frame, text="Категория", width=225)
        columns4 = ctk.CTkLabel(column_names_frame, text="Цена(руб.)", width=150)

        columns1.grid(row=0, column=0, sticky='we', padx=(2, 1), pady=5)
        columns2.grid(row=0, column=1, sticky='we', padx=1, pady=5)
        columns3.grid(row=0, column=2, sticky='we', padx=1, pady=5)
        columns4.grid(row=0, column=3, sticky='we', padx=(1, 2), pady=5)
        self.table1 = ctk.CTkScrollableFrame(self, fg_color='transparent',
                                             corner_radius=0, height=160)
        monitor = screeninfo.get_monitors()[0]
        if monitor.height > 1440:
            self.table1.configure(height=275)
        self.table1.scrollbar.configure(height=0)
        self.table1.grid(row=1, column=0, columnspan=4, padx=(10, 0), pady=(5, 10), sticky='we')

    def set_info(self, info_frame):
        self.info_frame = info_frame

    def update_table(self, massages):
        self.massages = massages
        if len(self.rows_frames) != 0:
            for i, row_frame in enumerate(self.rows_frames):
                self.rows_frames[i].grid_forget()
            self.rows_frames = {}
            self.names = {}
            self.duration_massage = {}
            self.categories = {}
            self.prices = {}

        for i, massage in enumerate(massages):
            self.rows_frames[i] = ctk.CTkFrame(self.table1, fg_color=['gray81', 'gray20'], corner_radius=7)
            self.rows_frames[i].grid(row=i + 1, column=0, columnspan=4, sticky='we', padx=(0, 8), pady=1)
            self.names[i] = ctk.CTkLabel(self.rows_frames[i], text=massage['название'], width=225)
            self.duration_massage[i] = ctk.CTkLabel(self.rows_frames[i], text=massage['длительность'], width=150)
            self.categories[i] = ctk.CTkLabel(self.rows_frames[i], text=massage['категория'], width=225)
            self.prices[i] = ctk.CTkLabel(self.rows_frames[i], text=massage['цена'], width=150)

            self.names[i].grid(row=i + 1, column=0, sticky='we', pady=2, padx=(2, 1))
            self.names[i].bind("<Button-1>", lambda event, row=i: self.select_massage(row))
            self.duration_massage[i].grid(row=i + 1, column=1, sticky='we', pady=2, padx=1)
            self.duration_massage[i].bind("<Button-1>", lambda event, row=i: self.select_massage(row))
            self.categories[i].grid(row=i + 1, column=2, sticky='we', pady=2, padx=1)
            self.categories[i].bind("<Button-1>", lambda event, row=i: self.select_massage(row))
            self.prices[i].grid(row=i + 1, column=3, sticky='we', pady=2, padx=(1, 2))
            self.prices[i].bind("<Button-1>", lambda event, row=i: self.select_massage(row))

    def select_massage(self, row):
        self.selected_massage = row
        #if self.preq_parent.master.user == 'superuser':
            #print('С фига ли')
            #когда открыта карточка для просмотра
            #self.edit_massage_button.grid(row=1, column=0, padx=(15, 5), pady=(5, 10), sticky='w')

            #когда открыта карточка для просмотра
            #self.delete_massage_button.grid(row=1, column=1, padx=(5, 15), pady=(5, 10), sticky='w')

            #когда ничего не открыто или когда открыта карточка для просмотра
            #self.create_massage_button.grid(row=1, column=3, padx=15, pady=(5, 10), sticky='e')

            # когда находимся в режиме создания или редактирования
            #self.cancel_massage_button.grid_remove()

            # когда находимся в режиме создания или редактирования
            #self.save_massage_button.grid_remove()

            # когда создается карточка
            #self.clear_form_massage_button.grid_remove()

        # сделать ограничение на длину строки в ячейке
        #print("Номер строки:", row)
        for i, massage in enumerate(self.massages):
            self.rows_frames[i].configure(fg_color=['gray81', 'gray20'])
        self.rows_frames[row].configure(fg_color='#1f6aa5')
        self.info_frame.update_info_frame(self.massages, row)

        # self.name_massage_entry.configure(state="normal")
        # self.name_massage_entry.delete(0, tk.END)
        # self.name_massage_entry.insert(0, self.massages[row]['название'])
        # self.name_massage_entry.configure(state="disabled")
        #
        # var = StringVar(self.parent)
        # var.set(self.massages[row]['категория'])
        #
        # self.category_massage_entry.configure(variable=var)
        # self.category_massage_entry.configure(state="disabled")
        #
        # self.price_massage_entry.configure(state="normal")
        # self.price_massage_entry.delete(0, tk.END)
        # self.price_massage_entry.insert(0, self.massages[row]['цена'])
        # self.price_massage_entry.configure(state="disabled")
        #
        # self.duration_massage_entry.configure(state="normal")
        # self.duration_massage_entry.delete(0, tk.END)
        # self.duration_massage_entry.insert(0, self.massages[row]['длительность'])
        # self.duration_massage_entry.configure(state="disabled")
        #
        # self.description_massage_textbox.configure(state="normal")
        # self.description_massage_textbox.delete("0.0", "end")
        # self.description_massage_textbox.insert(0.0, self.massages[row]['описание'])
        # self.description_massage_textbox.configure(state="disabled")

    def unselect_massage(self):
        for i, massage in enumerate(self.massages):
            self.rows_frames[i].configure(fg_color=['gray81', 'gray20'])

    #def update_info(self):
    #    pass


