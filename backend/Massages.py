from datetime import datetime
import sqlite3 as sq


class MassagesData:
    def __init__(self):
        self.conn = sq.connect('../makebd/Salon.db')
        self.curs = self.conn.cursor()

    def create_tbl_categories_massages(self):
        # Создание таблицы categories_massages
        self.curs.execute('''CREATE TABLE categories_massages (
            id_category_massage INTEGER PRIMARY KEY AUTOINCREMENT,
            name_category_massage TEXT NOT NULL CHECK(length(name_category_massage) <= 60)
        )''')
        self.conn.commit()

    def create_tbl_rooms(self):
        # Создание таблицы rooms
        self.curs.execute('''CREATE TABLE rooms (
            id_room INTEGER PRIMARY KEY AUTOINCREMENT,
            name_room TEXT NOT NULL CHECK(length(name_room) <= 60),
            activity_room TEXT NOT NULL CHECK(activity_room IN ('активна', 'на стопе', 'удалена'))
        )''')
        self.conn.commit()

    def create_tbl_massages(self):
        # Создание таблицы Massages
        self.curs.execute('''CREATE TABLE massages (
            id_massage INTEGER PRIMARY KEY AUTOINCREMENT,
            name_massage TEXT NOT NULL CHECK(length(name_massage) <= 60),
            massage_id_category INTEGER,
            number_persons_massage INTEGER NOT NULL CHECK(number_persons_massage IN (1, 2)),
            duration_massage TEXT NOT NULL,
            break_massage TEXT NOT NULL,
            description_massage TEXT CHECK(length(description_massage) <= 1500),
            activity_massage TEXT NOT NULL CHECK(activity_massage IN ('удален', 'на стопе', 'активен')),
            FOREIGN KEY(massage_id_category) REFERENCES categories_massages(id_category_massage)
        )''')
        self.conn.commit()

    def create_tbl_connections_massages_rooms(self):
        # Создание таблицы для связи многие ко многим между Massages и Rooms
        self.curs.execute('''CREATE TABLE connections_massages_rooms (
            id_connection INTEGER PRIMARY KEY AUTOINCREMENT,
            massage_id INTEGER,
            room_id INTEGER,
            FOREIGN KEY(massage_id) REFERENCES massages(id_massage),
            FOREIGN KEY(room_id) REFERENCES rooms(id_room)
        )''')
        self.conn.commit()

    def create_tbl_prices_massages(self):
        # Создание таблицы Prices_massages
        self.curs.execute('''CREATE TABLE  prices_massages (
                            id_price_massage INTEGER PRIMARY KEY AUTOINCREMENT,
                            price_massage REAL,
                            price_change_date TEXT,
                            massage_id INTEGER,
                            FOREIGN KEY(massage_id) REFERENCES massages(id_massage)
                        )''')
        self.conn.commit()

    def create_massage(self, name, category_id, activity, price, rooms_ids, duration, break_time,
                       number_persons, description=None):
        # записываем массаж
        if description:
            query_massage = ("INSERT INTO massages (name_massage, massage_id_category, number_persons_massage, "
                             "duration_massage, break_massage, description_massage, activity_massage) "
                             "VALUES (?, ?, ?, ?, ?, ?, ?)")
            values_massage = (name, category_id, number_persons, duration, break_time, description, activity)
        else:
            query_massage = ("INSERT INTO massages (name_massage, massage_id_category, number_persons_massage, "
                             "duration_massage, break_massage, activity_massage) VALUES (?, ?, ?, ?, ?, ?)")
            values_massage = (name, category_id, number_persons, duration, break_time, activity)

        self.curs.execute(query_massage, values_massage)
        new_massage_id = self.curs.lastrowid
        self.conn.commit()

        # записываем связь массажа с комнатами
        for id_room in rooms_ids:
            query_connection = "INSERT INTO connections_massages_rooms (massage_id, room_id) VALUES (?, ?)"
            values_connection = (new_massage_id, id_room)
            self.curs.execute(query_connection, values_connection)
        self.conn.commit()

        # записываем цену массажа
        cur_datetime = datetime.now()
        cur_datetime = cur_datetime.strftime('%Y-%m-%d %H:%M:%S')

        query_price = "INSERT INTO prices_massages (price_massage, price_change_date, massage_id) VALUES (?, ?, ?)"
        values_price = (price, cur_datetime, new_massage_id)
        self.curs.execute(query_price, values_price)
        self.conn.commit()

    def delete_massage(self, id_massage):
        query_massage = "UPDATE massages SET activity_massage = 'удален' WHERE id_massage = ?"
        values_massage = (id_massage,)
        self.curs.execute(query_massage, values_massage)
        self.conn.commit()

        query_last_price = ("SELECT price_massage FROM prices_massages WHERE massage_id = ? "
                            "ORDER BY price_change_date DESC LIMIT 1")
        values_last_price = (id_massage,)
        self.curs.execute(query_last_price, values_last_price)
        last_price = self.curs.fetchall()[0][0]
        self.conn.commit()

        cur_datetime = datetime.now()
        cur_datetime = cur_datetime.strftime('%Y-%m-%d %H:%M:%S')
        query_price = ("INSERT INTO prices_massages (price_massage, price_change_date, massage_id)"
                       " VALUES (?, ?, ?)")
        values_price = (last_price, cur_datetime, id_massage)
        self.curs.execute(query_price, values_price)
        self.conn.commit()

    def update_massage(self, id_massage, name=None, category_id=None, activity=None, price=None, rooms_ids=None,
                       duration=None, break_time=None, number_persons=None, description=None):
        query_massage = "UPDATE massages SET "
        values_massage = []

        if name is not None:
            query_massage += "name_massage = ?, "
            values_massage.append(name)
        if category_id is not None:
            query_massage += "massage_id_category = ?, "
            values_massage.append(category_id)
        if activity is not None:
            query_massage += "activity_massage = ?, "
            values_massage.append(activity)
        if duration is not None:
            query_massage += "duration_massage = ?, "
            values_massage.append(duration)
        if break_time is not None:
            query_massage += "break_massage = ?, "
            values_massage.append(break_time)
        if number_persons is not None:
            query_massage += "number_persons_massage = ?, "
            values_massage.append(number_persons)
        if description is not None:
            query_massage += "description_massage = ?, "
            values_massage.append(description)

        query_massage = query_massage.rstrip(", ") + " WHERE id_massage = ?"
        values_massage.append(id_massage)
        self.curs.execute(query_massage, values_massage)
        self.conn.commit()

        if price is not None:
            query_last_price = ("SELECT price_massage FROM prices_massages WHERE massage_id = ? "
                                "ORDER BY price_change_date DESC LIMIT 1")
            values_last_price = (id_massage,)
            self.curs.execute(query_last_price, values_last_price)
            last_price = self.curs.fetchall()[0][0]
            self.conn.commit()

            if int(last_price) != price:
                cur_datetime = datetime.now()
                cur_datetime = cur_datetime.strftime('%Y-%m-%d %H:%M:%S')
                query_price = ("INSERT INTO prices_massages (price_massage, price_change_date, massage_id)"
                               " VALUES (?, ?, ?)")
                values_price = (price, cur_datetime, id_massage)
                self.curs.execute(query_price, values_price)
                self.conn.commit()

        if rooms_ids is not None:
            query_delete_connections = "DELETE FROM connections_massages_rooms WHERE massage_id = ?"
            values_delete_connections = (id_massage,)
            self.curs.execute(query_delete_connections, values_delete_connections)
            self.conn.commit()

            for id_room in rooms_ids:
                query_connections = "INSERT INTO connections_massages_rooms (massage_id, room_id) VALUES (?, ?)"
                values_connections = (id_massage, id_room)
                self.curs.execute(query_connections, values_connections)
            self.conn.commit()

    def read_tbl_categories_massages(self):
        self.curs.execute('SELECT * FROM categories_massages')
        categories_data = self.curs.fetchall()
        print(categories_data)
        categories_dict = {name_category: id_category for id_category, name_category in categories_data}
        print(categories_dict)

        return categories_dict

    def read_tbl_rooms(self):
        self.curs.execute('SELECT id_room, name_room FROM rooms')
        rooms_data = self.curs.fetchall()
        rooms_dict = {name_room: id_room for id_room, name_room in rooms_data}
        print(rooms_dict)

        return rooms_dict


if __name__ == '__main__':
    bd = MassagesData()

    # print(bd.create_massage('Сила Сибири123', None, 'активен', '2200.55', [1, 3],
    #                          '01:30', '00:30', 1, 'Какой-то крутой массаж лица'))
