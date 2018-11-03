# Задание №1
# Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
# и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление
# в формат Unicode и также проверить тип и содержимое переменных.

result = []
str = ["разработка", "сокет", "декоратор"]
for i in str:
    enc_str = i.encode('utf-8')
    type_ = type(i)
    print(f'{i} - тип {type_}')
    print(enc_str)

dec = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0', b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82', b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80']

for j in dec:
    dec_str = j.decode('utf-8')
    type_dec = type(j)
    result.append(dec_str)
    print (j, type_dec)
    print(dec_str)

for i in str:
    for j in result:
        if i == j:
            print("true")