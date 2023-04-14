"""
2. Написать скрипт, автоматизирующий заполнение данными файла orders
в формате JSON с информацией о заказах.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    dictionary = ({"item": item, "quantity": quantity,
                  "price": price, "buyer": buyer, "date": date}, )
    with open('orders.json') as f:
        data = json.load(f)
        print(data)
    data["orders"] += list(dictionary)
    with open('orders.json', 'w') as f:
        json.dump(data, f, indent=4)


write_order_to_json("Motherboard", 21, 150, "Petrov I. I.", "24.09.2023")
