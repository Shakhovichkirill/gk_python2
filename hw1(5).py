# Задание №5
# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess
n = ['ping', 'youtube.com']
m = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(n, stdout=subprocess.PIPE)
subproc_ping_1 = subprocess.Popen(m, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))
for line in subproc_ping_1.stdout:
            line1 = line.decode('cp866').encode('utf-8')
            print(line1.decode('utf-8'))