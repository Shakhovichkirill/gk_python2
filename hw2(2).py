# 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
# цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных
# в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json
from pathlib import Path

def write_order_to_json(item, quantity, price, buyer, date):
    path = Path('orders.json')
    data = json.loads(path.read_text(encoding="utf=8"))
    ord = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    data['orders'].append(ord)
    path.write_text(json.dumps(data, indent=4, separators=(',', ': ')), encoding='utf-8')

write_order_to_json("dell", 2, 500, "Ivanov", "24.09.17")