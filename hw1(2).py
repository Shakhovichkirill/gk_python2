# Задание №2
# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

import subprocess

n = [b'class', b'function', b'method']
for i in n:
    type_ = type(i)
    len_ = len(i)
    print(f'содержимое {i}, тип {type_}, длинна {len_}')
