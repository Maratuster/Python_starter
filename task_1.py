"""
1. Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, 
info_2.txt, info_3.txt и формирующий новый "отчетный" файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
"Изготовитель системы", "Название ОС", "Код продукта", "Тип системы".
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: "Изготовитель системы",
"Название ОС", "Код продукта", "Тип системы". Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;
"""
import csv


def get_data(file_name, worklist):
    params = ("Изготовитель системы", "Название ОС",
              "Код продукта", "Тип системы")
    work_dict = {}
    text_file = open(file_name, "r", encoding="utf-8")
    content = text_file.readlines()
    text_file.close()
    for item in content:
        temp_content = item.replace("\n", "").split(":")
        if temp_content[0] in params:
            temp_dict = {temp_content[0]: temp_content[1].replace(" ", "")}
            work_dict.update(temp_dict)
    worklist.append(work_dict)
    print(list_d)
    return list_d


def write_to_csv(file_name, list_d):
    get_data(file_name, list_d)
    with open("result.csv", "w+", encoding="utf-8") as result:
        result_wr = csv.DictWriter(result, fieldnames=list(list_d[0].keys()))
        result_wr.writeheader()
        for rows in list_d:
            result_wr.writerow(rows)


list_d = []
write_to_csv("info_1.txt", list_d)
write_to_csv("info_2.txt", list_d)
write_to_csv("info_3.txt", list_d)
