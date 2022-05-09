"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате
JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение
данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров —
товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей
в нее значений каждого параметра.
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as file_out:
        data = json.load(file_out)

    with open('orders.json', 'w', encoding='utf-8') as file_in:
        orders_list = data['orders']
        order_info = {'item': item,
                      'quantity': quantity,
                      'price': price,
                      'buyer': buyer,
                      'date': date}
        orders_list.append(order_info)

        json.dump(data, file_in, indent=4, ensure_ascii=False)


write_order_to_json('ноутбук', '3', '35000', 'Kim A.K.', '09.05.2022')
write_order_to_json('МФУ', '1', '24000', 'Nine J.O.', '08.05.2022')
write_order_to_json('PC', '2', '58000', 'Apa K.J.', '07.05.2022')
write_order_to_json('iPad', '5', '43000', 'Tsui S.M.', '07.05.2022')
write_order_to_json('гарнитура', '10', '5000', 'Pine P.V.', '07.05.2022')
