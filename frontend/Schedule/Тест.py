import math
from functools import partial

from datetime import datetime
from frontend.Schedule.Тест3 import *


class TimeFrame(ctk.CTkFrame):
    def __init__(self, parent, schedule, i, j):
        ctk.CTkFrame.__init__(self, parent.scrollable_frame)

        self.label_time = None
        self.button_create = None
        self.button_update = None
        self.line = None
        self.label_name_room = None
        self.label_clients = None
        self.schedule = schedule
        self.row = i
        self.column = j
        self.preq_parent = parent
        self.parent = parent.scrollable_frame
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=5)
        self.configure(height=20, fg_color=['gray81', 'gray20'])
        widgets_in_row = self.parent.grid_slaves(row=self.row*2+1, column=self.column+1)
        if len(self.schedule) > 0:
            self.configure(fg_color='#6d9970')
            # сделать 1 лейбл?
            # сделать сложное условие отображения лейблов в зависимости от длительности ?

            self.label_time = ctk.CTkLabel(self, width=200, anchor='w',
                                           text=f'{self.schedule[0]["time_begin"]} - {self.schedule[0]["time_end"]}')
            self.label_time.grid(row=0, column=0, sticky='w', padx=(5, 5))

            self.button_update = ctk.CTkButton(self, text='u', width=26, height=26, command=partial(FormFrame, self.preq_parent))
            self.button_update.grid(row=0, column=2, padx=5, pady=5)

            self.line = ctk.CTkFrame(self, fg_color="black", height=2, corner_radius=1)
            self.line.grid(row=1, column=0, columnspan=3, sticky='we', padx=(0, 0))

            self.label_name_room = ctk.CTkLabel(self, width=200, anchor='w', wraplength=200,
                                                text=f'{self.schedule[0]['name_massage']} - {self.schedule[0]['room']}')
            self.label_name_room.grid(row=2, column=0, sticky='w', padx=(5, 5), pady=0)

            self.label_clients = ctk.CTkLabel(self, width=200, anchor='w', wraplength=200,
                                              text=f'{self.schedule[0]['name_client']}')
            self.label_clients.grid(row=3, column=0, sticky='w', padx=(5, 5), pady=0)

            interval = ((datetime.strptime(self.schedule[0]['time_end'], '%H:%M') -
                         datetime.strptime(self.schedule[0]['time_begin'], '%H:%M')).seconds / 60) / 15
            self.grid(row=self.row*2+1, column=self.column + 1, rowspan=math.ceil(interval)*2-1, sticky='nsew', padx=5, pady=0)
        elif not widgets_in_row:
            self.label_time = ctk.CTkLabel(self, text='', width=200)
            self.label_time.grid(row=0, column=0, sticky='w', padx=(5, 5))
            self.button_create = ctk.CTkButton(self, text='+', width=26, height=26, command=partial(FormFrame, self.preq_parent))
            self.button_create.grid(row=0, column=2, padx=5, pady=5, sticky='e')
            self.grid(row=self.row*2+1, column=self.column + 1, sticky='nsew', padx=5, pady=0)
