from datetime import timedelta

from tkcalendar import Calendar
from frontend.Schedule.Тест import *
from frontend.Schedule.Тест3 import *


class ScheduleFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.time = datetime.now().strftime('%H:%M')
        self.today = datetime.now().date()
        self.line_b = None
        self.root = parent
        self.days_of_week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
        self.schedules = {
            'Мастер 1': [
                {
                    'id_massage': 1,
                    'name_massage': 'массаж 1',
                    'time_begin': '10:30',
                    'time_end': '12:30',
                    'name_client': 'Попов Алексей Петрович',
                    'comment': 'Классический массаж спины',
                    'room': 'Кабинет №1'
                },
                {
                    'id_massage': 2,
                    'name_massage': 'массаж 2',
                    'time_begin': '13:00',
                    'time_end': '15:00',
                    'name_client': 'Иванова Елена Сергеевна',
                    'comment': 'Антицеллюлитный массаж бедер',
                    'room': 'Кабинет №1'
                },
                {
                    'id_massage': 3,
                    'name_massage': 'массаж 3',
                    'time_begin': '15:30',
                    'time_end': '17:30',
                    'name_client': 'Сидоров Василий Иванович',
                    'comment': 'Лимфодренажный массаж лица',
                    'room': 'Кабинет №2'
                },
                {
                    'id_massage': 4,
                    'name_massage': 'массаж 4',
                    'time_begin': '18:00',
                    'time_end': '20:00',
                    'name_client': 'Кузнецова Анна Павловна',
                    'comment': 'Массаж для беременных',
                    'room': 'Кабинет №3'
                },
                {
                    'id_massage': 5,
                    'name_massage': 'массаж 5',
                    'time_begin': '20:00',
                    'time_end': '21:00',
                    'name_client': 'Григорьев Дмитрий Николаевич',
                    'comment': 'Тайский массаж',
                    'room': 'Кабинет №3'
                }
            ],
            'Мастер 2': [
                {
                    'id_massage': 6,
                    'name_massage': 'массаж 6',
                    'time_begin': '09:45',
                    'time_end': '11:00',
                    'name_client': 'Смирнова Ольга Игоревна',
                    'comment': 'Релаксационный массаж спины',
                    'room': 'Кабинет №1'
                },
                {
                    'id_massage': 7,
                    'name_massage': 'массаж 7',
                    'time_begin': '11:30',
                    'time_end': '13:30',
                    'name_client': 'Никитин Максим Александрович',
                    'comment': 'Активный массаж шеи',
                    'room': 'Кабинет №2'
                },
                {
                    'id_massage': 8,
                    'name_massage': 'массаж 8',
                    'time_begin': '14:00',
                    'time_end': '16:00',
                    'name_client': 'Петров Артем Владимирович',
                    'comment': 'Массаж для спортсменов',
                    'room': 'Кабинет №2'
                },
                {
                    'id_massage': 9,
                    'name_massage': 'массаж 9',
                    'time_begin': '16:30',
                    'time_end': '18:30',
                    'name_client': 'Андреева Мария Ивановна',
                    'comment': 'Лечебный массаж плечевого пояса',
                    'room': 'Кабинет №3'
                },
                {
                    'id_massage': 10,
                    'name_massage': 'массаж 10',
                    'time_begin': '19:00',
                    'time_end': '21:00',
                    'name_client': 'Казаков Денис Сергеевич',
                    'comment': 'Массаж для улучшения сна',
                    'room': 'Кабинет №3'
                }
            ],
            'Мастер 3': [
                {
                    'id_massage': 11,
                    'name_massage': 'массаж 11',
                    'time_begin': '08:30',
                    'time_end': '10:30',
                    'name_client': 'Федорова Екатерина Павловна',
                    'comment': 'Антистрессовый массаж всего тела',
                    'room': 'Кабинет №1'
                },
                {
                    'id_massage': 12,
                    'name_massage': 'массаж 12',
                    'time_begin': '11:00',
                    'time_end': '13:00',
                    'name_client': 'Михайлов Илья Васильевич',
                    'comment': 'Массаж для снятия мышечного напряжения',
                    'room': 'Кабинет №1'
                },
                {
                    'id_massage': 13,
                    'name_massage': 'массаж 13',
                    'time_begin': '13:30',
                    'time_end': '15:30',
                    'name_client': 'Соколова Анастасия Сергеевна',
                    'comment': 'Расслабляющий массаж спины и шеи',
                    'room': 'Кабинет №2'
                },
                {
                    'id_massage': 14,
                    'name_massage': 'массаж 14',
                    'time_begin': '16:00',
                    'time_end': '18:00',
                    'name_client': 'Волков Владислав Игоревич',
                    'comment': 'Массаж для улучшения циркуляции крови',
                    'room': 'Кабинет №2'
                },
                {
                    'id_massage': 15,
                    'name_massage': 'массаж 15',
                    'time_begin': '18:30',
                    'time_end': '20:30',
                    'name_client': 'Тарасова Алина Дмитриевна',
                    'comment': 'Антистрессовый массаж с ароматическими маслами',
                    'room': 'Кабинет №3'
                }
            ]
        }

        self.start_time = datetime.strptime('9:00', '%H:%M')
        self.end_time = datetime.strptime('21:00', '%H:%M')
        self.selected_date = datetime.now()

        self.frames_times = {}
        self.labels_times = {}
        self.labels_empty = {}
        self.labels_masters = {}
        self.frames = {}

        self.create_schedule_interface()

    def create_schedule_interface(self):
        self.create_calendar()
        self.create_control_buttons()

        self.create_date_frame()
        self.create_names_columns()
        self.create_schedule_frames()
        self.create_line()

    def update_schedule_interface(self):
        self.create_date_frame()
        self.create_names_columns()
        self.create_schedule_frames()
        self.create_line()

    def update_only_schedule_interface(self):
        self.create_schedule_frames()

    def create_line(self):
        self.time = datetime.now().strftime('%H:%M')
        time = datetime.strptime(self.time, '%H:%M')
        if hasattr(self, 'line_b'):
            # Если элементы существуют, удаляем их
            if self.line_b:
                self.line_b.destroy()
                # Очищаем переменные
                del self.line_b
                self.line_b = None

        if self.selected_date.date() == self.today:
            if self.start_time <= time <= self.end_time:
                c_time = self.start_time
                q = 0

                while c_time < time:
                    q += 1
                    c_time += timedelta(minutes=60 // 4)

                # Создание или обновление фрейма
                if self.line_b:
                    self.line_b.destroy()  # Уничтожение объекта фрейма

                if time.minute % 15 == 0:
                    self.line_b = ctk.CTkFrame(self.scrollable_frame, fg_color="red", height=2, corner_radius=1)
                    self.line_b.grid(row=q * 2, column=0, columnspan=4, sticky='we', padx=(45, 5), pady=(0, 0))
                elif time.minute % 15 < 5:
                    self.line_b = ctk.CTkFrame(self.scrollable_frame, fg_color="red", height=2, corner_radius=1)
                    self.line_b.grid(row=(q-1) * 2, column=0, columnspan=4, sticky='we', padx=(45, 5), pady=(0, 0))
                else:
                    self.line_b = ctk.CTkFrame(self.scrollable_frame, fg_color="red", height=2, corner_radius=1)
                    print((time.minute % 15)/5*16-6)
                    self.line_b.grid(row=q * 2 - 1, column=0, columnspan=4, sticky='nwe', padx=(45, 5), pady=((time.minute % 15)/5*16-6, 0))

        current_time = datetime.now().replace(microsecond=0)
        minutes_until_next_update = (5 - current_time.minute % 5) * 60 - current_time.second

        # Запланировать следующее обновление через нужное количество секунд
        self.scrollable_frame.after(minutes_until_next_update * 1000, self.create_line)

    def create_date_frame(self):
        # self = ctk.CTkFrame(self.root)
        # self.grid(row=0, column=0, sticky='nsew', padx=(250, 40), pady=(50, 40))
        print('проверка')
        print(self)

        if hasattr(self, 'frame_date'):
            # Если элементы существуют, удаляем их
            self.frame_date.destroy()
            # Очищаем переменные
            del self.frame_date
            del self.label_date
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_columnconfigure(2, weight=4)
        self.grid_columnconfigure(3, weight=40)
        self.grid_rowconfigure(5, weight=1)

        self.frame_date = ctk.CTkFrame(self)
        self.frame_date.grid(row=0, column=0, columnspan=2, padx=(20, 10), pady=(20, 10), sticky='nsew')
        self.frame_date.grid_columnconfigure(0, weight=1)

        self.label_date = ctk.CTkLabel(self.frame_date, text=self.selected_date.strftime('%d.%m.%y, ') +
                                       self.days_of_week[self.selected_date.weekday()],
                                       anchor='center')
        self.label_date.grid(row=0, column=0, padx=(5, 10), pady=5, sticky='nsew')

    def create_calendar(self):
        self.calendar = Calendar(self, locale='ru_RU', height=300, font=('', 8))
        self.calendar.bind("<<CalendarSelected>>", self.show_selected_date)
        self.calendar.grid(row=3, column=0, columnspan=2, padx=(30, 10), pady=(5, 5), sticky='nsew')

    def create_control_buttons(self):
        self.now_date_button = ctk.CTkButton(self, text='Сегодня', command=self.show_now_date)
        self.now_date_button.grid(row=1, column=0, columnspan=2, padx=(20, 10), pady=(5, 5), sticky='nsew')

        self.back_button = ctk.CTkButton(self, text='<', width=40, command=self.preq_date)
        self.back_button.grid(row=2, column=0, padx=(20, 5), pady=(5, 5), sticky='nsew')

        self.next_button = ctk.CTkButton(self, text='>', width=40, command=self.next_date)
        self.next_button.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky='nsew')

        self.new_schedule_button = ctk.CTkButton(self, text='Записать', width=40, command=partial(FormFrame, self))
        self.new_schedule_button.grid(row=4, column=0, columnspan=2, padx=(20, 10), pady=(5, 5), sticky='nsew')

    def create_names_columns(self):
        # Проверяем, существуют ли уже элементы интерфейса
        if hasattr(self, 'frame_names_columns'):
            # Если элементы существуют, удаляем их
            self.frame_names_columns.destroy()
            # Очищаем переменные
            del self.frame_names_columns
            del self.label_time
            del self.labels_masters
            self.labels_masters = {}

        self.frame_names_columns = ctk.CTkFrame(self)
        self.frame_names_columns.grid(row=0, column=2, columnspan=2, sticky='nsew', padx=(10, 20), pady=(20, 10))

        self.label_time = ctk.CTkLabel(self.frame_names_columns, text='Время', width=50)
        self.label_time.grid(row=0, column=0, padx=(5, 10), pady=5, sticky='nsew')

        masters = list(self.schedules.keys())
        for j, master in enumerate(masters):
            self.frame_names_columns.grid_columnconfigure(1 + j, weight=4)
            self.labels_masters[j] = ctk.CTkLabel(self.frame_names_columns, text=master, width=150, anchor='center')
            self.labels_masters[j].grid(row=0, column=j + 1, padx=5, pady=5, sticky='nsew')

            if j == len(masters) - 1:
                self.labels_masters[j].grid(row=0, column=j + 1, padx=(5, 20), pady=5, sticky='we')

    def create_schedule_frames(self):
        if hasattr(self, 'scrollable_frame'):
            # Если элементы существуют, удаляем их
            self.scrollable_frame.destroy()
            # Очищаем переменные
            del self.scrollable_frame
            del self.labels_times
            del self.labels_empty
            del self.frames_times
            self.frames_times = {}
            self.labels_times = {}
            self.labels_empty = {}
            self.labels_masters = {}

        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame._parent_canvas.yview("scroll", 1500, "units") # листаем

        self.scrollable_frame.grid(row=1, column=2, rowspan=5, columnspan=2, sticky='nsew', padx=(10, 20),
                                   pady=(10, 20))

        current_time = self.start_time
        i = 0
        masters = list(self.schedules.keys())

        while current_time < self.end_time:
            self.labels_times[i] = ctk.CTkLabel(self.scrollable_frame, text=current_time.strftime('%H:%M'), width=50, height=12)

            if i % 2 == 0:
                self.labels_times[i].configure(anchor='nw', font=('', 15))
            else:
                self.labels_times[i].configure(anchor='n', font=('', 12))
            self.labels_times[i].grid(row=i * 2, column=0, padx=(0, 10), pady=0, sticky='ew')

            self.labels_empty[i] = ctk.CTkLabel(self.scrollable_frame, text='', width=50, height=36)
            self.labels_empty[i].grid(row=i*2+1, column=0, sticky='nsew', padx=5, pady=0)

            self.frames_times[i] = {}

            for j, master in enumerate(masters):
                schedule = [entry for entry in self.schedules[master] if entry['time_begin'] == str(current_time.strftime('%H:%M'))]

                self.scrollable_frame.grid_columnconfigure(1 + j, weight=4)
                self.frames_times[i][j] = TimeFrame(self, schedule, i, j)
            i += 1
            current_time += timedelta(minutes=60 // 4)

        last_index = len(self.labels_times)
        self.labels_times[last_index] = ctk.CTkLabel(self.scrollable_frame, text=self.end_time.strftime('%H:%M'), width=50,
                                            height=12, anchor='nw', font=('', 15))
        self.labels_times[last_index].grid(row=last_index * 2, column=0, padx=(0, 10), pady=0, sticky='ew')

    def show_selected_date(self, event):
        self.selected_date = self.calendar.selection_get()
        self.label_date.configure(text=self.selected_date.strftime('%d.%m.%y, ') +
                                  self.days_of_week[self.selected_date.weekday()])

        self.selected_date = datetime(self.selected_date.year, self.selected_date.month, self.selected_date.day)
        self.update_schedule_interface()

    def show_now_date(self):
        now_date = datetime.now()
        self.selected_date = now_date
        self.calendar.selection_set(self.selected_date)
        self.label_date.configure(text=self.selected_date.strftime('%d.%m.%y, ') +
                                  self.days_of_week[self.selected_date.weekday()])
        self.update_schedule_interface()

    def preq_date(self):
        self.selected_date -= timedelta(days=1)
        self.calendar.selection_set(self.selected_date)
        self.label_date.configure(text=self.selected_date.strftime('%d.%m.%y, ') +
                                  self.days_of_week[self.selected_date.weekday()])
        self.update_schedule_interface()

    def next_date(self):
        self.selected_date += timedelta(days=1)
        self.calendar.selection_set(self.selected_date)
        self.label_date.configure(text=self.selected_date.strftime('%d.%m.%y, ') +
                                  self.days_of_week[self.selected_date.weekday()])
        self.update_schedule_interface()


if __name__ == "__main__":
    root = ctk.CTk()
    root.minsize(1536, 784)
    root.geometry(f"{1536}x{784}+0+0")
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(1, weight=1)
    container = ctk.CTkFrame(root, corner_radius=0)

    container.grid(row=0, column=1, rowspan=2, sticky='nsew')
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    frame = ScheduleFrame(container, '')
    frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    root.mainloop()
