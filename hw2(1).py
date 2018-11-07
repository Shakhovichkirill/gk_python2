# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
# info_1_1.txt, info_2_2.txt, info_3_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
# В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы»,
# «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
# Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
# В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него
# названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
# данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import csv
import re

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
info_1 = []
info_2 = []
info_3 = []
info = []

def get_data( ):
    arr = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    for i in arr:
        with open(i, encoding="utf8") as f_n:
            fd = f_n.read()
            pattern = r"Изготовитель системы:[ ]{13}[A-Z]{4,6}"

            result = re.findall(pattern, fd)
            str_ = ''.join(result)
            res = re.split(r'[ ]{13}', str_)
            os_prod_list.append(res[1])

            pattern_1 = r"Название ОС:[ ]{22}Microsoft Windows [0-9]{1,2}[.| ][0-9|\w]{1,20}[ |\w]{0,20}"
            result_1 = re.findall(pattern_1, fd)
            str_1 = ''.join(result_1)
            res_1 = re.split(r'[ ]{22}', str_1)
            os_name_list.append(res_1[1])

            pattern_2 = r"Код продукта:[ ]{21}[0-9]{5}-[A-Z]{3}-[0-9]{7}-[0-9]{5}"
            result_2 = re.findall(pattern_2, fd)
            str_2 = ''.join(result_2)
            res_2 = re.split(r'[ ]{21}', str_2)
            os_code_list.append(res_2[1])

            pattern_3 = r"Тип системы:[ ]{22}[a-z][0-9]{2}-[a-z]{5}[ ][A-Z]{2}"
            result_3 = re.findall(pattern_3, fd)
            str_3 = ''.join(result_3)
            res_3 = re.split(r'[ ]{22}', str_3)
            os_type_list.append(res_3[1])

    info_1 = [os_prod_list[0], os_name_list[0], os_code_list[0], os_type_list[0]]
    info_2 = [os_prod_list[1], os_name_list[1], os_code_list[1], os_type_list[1]]
    info_3 = [os_prod_list[2], os_name_list[2], os_code_list[2], os_type_list[2]]
    header = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data = [header, info_1, info_2, info_3]
    with open("main_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(main_data)

def write_to_csv(filename):
    get_data()
    with open('main_data.csv') as f:
        f_reader = csv.reader(f)
        for row in f_reader:
            info.append(row)
    if filename == 'info1csv.csv':
        info1 = [info[0], info[1]]
        with open("info1csv.csv", "w", newline="") as f:
            f_writer = csv.writer(f)
            f_writer.writerows(info1)
    elif filename == 'info2csv.csv':
        info2 = [info[0], info[2]]
        with open("info2csv.csv", "w", newline="") as f:
            f_writer = csv.writer(f)
            f_writer.writerows(info2)
    elif filename == 'info3csv.csv':
        info3 = [info[0], info[3]]
        with open("info3csv.csv", "w", newline="") as f:
            f_writer = csv.writer(f)
            f_writer.writerows(info3)

write_to_csv('info1csv.csv')
write_to_csv('info2csv.csv')
write_to_csv('info3csv.csv')