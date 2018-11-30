# Задание №4
# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

m = ["разработка", "администрирование", "protocol", "standard"]
for i in m:
    enc_m = i.encode('utf-8')
    print(enc_m)
    dec_m = enc_m.decode('utf-8')
    print(dec_m)
