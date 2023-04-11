"""
3. Написать скрипт, автоматизирующий сохранение данных
в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml
work_dict = {"list_key": ["name", "surname", "thirdname"],
             "int_key": 124,
             "dict_key": {'first_key': "12"+str(chr(354)),
                           'second_key': "15"+str(chr(210)),
                           'third_key': "8"+str(chr(655))}}


with open('file.yaml', 'w', encoding="utf-8") as file:
    ya_write = yaml.dump(
        work_dict, file, default_flow_style=False, allow_unicode=True)

with open('file.yaml', 'r', encoding="utf-8") as file:
    data = yaml.safe_load(file)

print('Данные совпадают с исходными') if data == work_dict else print(
    'Данные не совпадают с исходными')
