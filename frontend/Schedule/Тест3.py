import customtkinter as ctk


class FormFrame(ctk.CTkFrame):
    def __init__(self, schedule_frame):
        ctk.CTkFrame.__init__(self, schedule_frame)
        print(schedule_frame)
        print('создаем')

        self.schedule_frame = schedule_frame

        self.grid(row=0, column=0, rowspan=6, columnspan=4, sticky='nsew',
                  padx=20, pady=20)
        self.create_schedule_interface()

    def create_schedule_interface(self):
        self.create_control_buttons()

    def create_control_buttons(self):
        self.save_record_button = ctk.CTkButton(self, text='Сохранить')
        self.save_record_button.grid(row=1, column=4, padx=(20, 10), pady=(5, 5), sticky='nsew')

        self.delete_record_button = ctk.CTkButton(self, text='Удалить')
        self.delete_record_button.grid(row=1, column=3, padx=(20, 10), pady=(5, 5), sticky='nsew')

        self.close_record_button = ctk.CTkButton(self, text='Закрыть', command=self.close_record)
        self.close_record_button.grid(row=1, column=0, padx=(20, 10), pady=(5, 5), sticky='nsew')

    def close_record(self):
        self.schedule_frame.update_only_schedule_interface()
        self.destroy()
