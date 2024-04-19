from frontend.Massages.filter import *
from frontend.Massages.table import *
from frontend.Massages.super_massage_info import *
from frontend.Massages.admin_massage_info import *


# Для админа
class ServicesFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        self.grid_columnconfigure((0, 6), weight=1)
        self.grid_columnconfigure(1, minsize=150, weight=0)
        self.grid_rowconfigure((1, 2, 3), weight=1)

        # заголовок
        label = ctk.CTkLabel(self, text="Массажи")
        label.grid(row=0, column=0, columnspan=7, padx=10, pady=(10, 0), sticky='we')

        # фрейм таблицы с выводом массажей
        table_frame = TableFrame(self, parent.master)
        table_frame.grid(row=4, column=2, columnspan=3, pady=(10, 20), padx=(10, 15), sticky='we')

        # фрейм фильтра для поиска массажей
        filter_frame = FilterFrame(self, parent, table_frame.update_table)
        filter_frame.grid(row=1, column=1, rowspan=4, pady=(20, 20), padx=(15, 10), sticky='ns')

        # фрейм информации о конкретном массаже
        if parent.master.user == 'superuser':
            massage_info_frame = SuperMassageInfoFrame(self, table_frame, filter_frame)
            massage_info_frame.grid(row=1, column=2, rowspan=3, columnspan=3, pady=(20, 10), padx=(10, 15),
                                    sticky='nswe')
        else:
            massage_info_frame = AdminMassageInfoFrame(self)
            massage_info_frame.grid(row=1, column=2, rowspan=3, columnspan=3, pady=(20, 10), padx=(10, 15),
                                      sticky='nswe')

        table_frame.set_info(massage_info_frame)

