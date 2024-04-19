import sqlite3


def filter_massages(name='', categories=None, persons=None, start_duration='', end_duration='',
                    min_price='', max_price='', activities=None):
    conn = sqlite3.connect('../makebd/Salon.db')
    c = conn.cursor()

    query = """SELECT 
        massages.id_massage, 
        massages.name_massage, 
        categories_massages.id_category_massage, 
        categories_massages.name_category_massage, 
        massages.number_persons_massage, 
        massages.duration_massage, 
        massages.break_massage, 
        massages.description_massage, 
        massages.activity_massage, 
        sub.price_massage, 
        MAX(prices_massages.price_change_date) AS last_price_change_date, 
        (SELECT GROUP_CONCAT(rooms.id_room || ': ' || rooms.name_room, ', ') 
         FROM connections_massages_rooms 
         JOIN rooms ON connections_massages_rooms.room_id = rooms.id_room 
         WHERE connections_massages_rooms.massage_id = massages.id_massage 
               AND connections_massages_rooms.room_id IN (1, 2, 3)) AS rooms_list 
    FROM 
        massages 
    JOIN 
        connections_massages_rooms ON massages.id_massage = connections_massages_rooms.massage_id 
    JOIN 
        prices_massages ON massages.id_massage = prices_massages.massage_id 
    JOIN 
        categories_massages ON massages.massage_id_category = categories_massages.id_category_massage 
    JOIN 
        rooms ON connections_massages_rooms.room_id = rooms.id_room 
    JOIN 
        (SELECT 
             prices_massages.massage_id, 
             prices_massages.price_massage, 
             ROW_NUMBER() OVER (PARTITION BY prices_massages.massage_id ORDER BY prices_massages.price_change_date DESC) as rn 
         FROM 
             prices_massages) sub ON massages.id_massage = sub.massage_id AND sub.rn = 1 
    WHERE 
        1=1 
    """

    group = """GROUP BY 
        massages.id_massage, 
        massages.name_massage, 
        categories_massages.id_category_massage, 
        categories_massages.name_category_massage, 
        massages.number_persons_massage, 
        massages.duration_massage, 
        massages.break_massage, 
        massages.description_massage, 
        massages.activity_massage, 
        sub.price_massage;"""

    params = []
    filters = []

    if name:
        filters.append("name_massage LIKE ?")
        params.append('%' + name + '%')

    filters.append("massage_id_category IN ({})".format(','.join('?' * len(categories))))
    params.extend(categories)

    if persons:
        filters.append("number_persons_massage IN ({})".format(','.join('?' * len(persons))))
        params.extend(persons)

    if min_price and max_price and min_price.isdigit() and max_price.isdigit():
        min_price = int(min_price)
        max_price = int(max_price)
        filters.append("sub.price_massage BETWEEN ? AND ?")
        params.extend([min_price, max_price])
    elif min_price and min_price.isdigit():
        min_price = int(min_price)
        filters.append("sub.price_massage >= ?")
        params.append(min_price)
    elif max_price and max_price.isdigit():
        max_price = int(max_price)
        filters.append("sub.price_massage <= ?")
        params.append(max_price)

    if start_duration and end_duration:
        filters.append("duration_massage BETWEEN ? AND ?")
        params.extend([start_duration, end_duration])
    elif start_duration:
        filters.append("duration_massage >= ?")
        params.append(start_duration)
    elif end_duration:
        filters.append("duration_massage <= ?")
        params.append(end_duration)

    if activities:
        filters.append("activity_massage IN ({})".format(','.join('?' * len(activities))))
        params.extend(activities)

    if filters:
        query += "AND " + "\nAND ".join(filters) + "\n"

    # Выполнение запроса с фильтром
    c.execute(query + group, params)

    # Получение результатов
    results = c.fetchall()
    # Закрытие соединения
    conn.close()

    return results


# Пример вызова функции с передачей параметров
# filtered_results = filter_massages(name='', categories=[1, 2, 3], persons=[1, 2], start_duration='00:30',
#                                    end_duration='01:30', min_price='1500', max_price='4500', activities=["активен"])
# print(filtered_results)
