# Задание №3
# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

n = ['attribute', 'класс', 'функция', 'type']
for i in n:
    bytes_ = i.encode('utf-8')
    type_ = type(bytes_)
    print(bytes_, type_)

# Такие слова отсутствуют