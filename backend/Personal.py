from datetime import datetime
import sqlite3 as sq


class PersonalData:
    def __init__(self):
        self.conn = sq.connect('../makebd/Salon.db')
        self.curs = self.conn.cursor()

    def create_tbl_employees(self):
        # Создание таблицы administrators
        self.curs.execute("""CREATE TABLE employees (
            id_employee INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT CHECK(LENGTH(full_name) >= 6) NOT NULL,
            login TEXT CHECK(LENGTH(login) >= 4 OR LENGTH(login) = 0),
            password TEXT CHECK(LENGTH(password) >= 6 OR LENGTH(password) = 0),
            position_id INTEGER,
            hire_date DATE NOT NULL,
            dismissal_date DATE,
            FOREIGN KEY (position_id) REFERENCES Positions (id_position));""")
        self.conn.commit()

    def create_employees(self):

        # SQL-запросы для добавления сотрудников
        employees = [
            ('Прохоров Марк Алексеевич', 'markitosik', 'Nooxoh6r', 3, '2024-04-10', None),
            ('Иванов Иван Иванович', 'ivanov', '111111', 2, '2024-04-11', None),
            ('Петров Петр Петрович', 'petrov', 'petr123', 2, '2024-04-12', None),
            ('Сидоров Сидор Сидорович', None, None, 1, '2024-04-11', None),
            ('Козлова Анна Ивановна', None, None, 1, '2024-04-12', None),
            ('Смирнов Алексей Петрович', None, None, 1, '2024-04-12', None),
            ('Кузнецова Екатерина Сергеевна', 'katya', 'katya222', 2, '2024-04-13', '2024-04-18')
        ]

        for employee in employees:
            self.curs.execute(
                "INSERT INTO employees (full_name, login, password, position_id, hire_date, dismissal_date) VALUES (?, ?, ?, ?, ?, ?)",
                employee)

        # Фиксируем изменения в базе данных
        self.conn.commit()

    def create_tbl_positions(self):
        # Создание таблицы masters
        self.curs.execute("""CREATE TABLE positions (
            id_position INTEGER PRIMARY KEY AUTOINCREMENT,
            name_position TEXT NOT NULL,
            rights INTEGER NOT NULL);""")
        self.conn.commit()

    def create_positions(self):

        # SQL-запросы для добавления записей (должностей)
        positions = [
            ('superuser', 3),
            ('administrator', 2),
            ('master', 1)
        ]

        # Вставляем каждую запись в таблицу positions
        for position in positions:
            self.curs.execute("INSERT INTO positions (name_position, rights) VALUES (?, ?)", position)

        # Фиксируем изменения в базе данных
        self.conn.commit()

    def authorization(self, login, password):
        # Выполняем запрос к базе данных для проверки логина и пароля
        self.curs.execute(
            "SELECT e.full_name, e.login, p.name_position, p.rights FROM employees e JOIN positions p ON e.position_id = p.id_position WHERE e.login = ? AND e.password = ?",
            (login, password))
        # Получаем результат запроса
        result = self.curs.fetchone()
        if result:
            # Если сотрудник найден, возвращаем его информацию
            full_name, login, position, rights = result
            return f"ФИО: {full_name}, Логин: {login}, Должность: {position}, Права: {rights}"
        else:
            return "Неверные логин или пароль"

    def create_tbl_shifts(self):
        pass


if __name__ == '__main__':
    bd = PersonalData()
    #bd.create_tbl_employees()
    #bd.create_tbl_positions()
    #bd.create_positions()
    #bd.create_employees()

    # Проверяем логин и пароль
    login = None
    password = None
    print(bd.authorization(login, password))