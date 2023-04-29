"""
Задание 2.
Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
words_list = ['class', 'function', 'method']
byte_words_list = []
for item in words_list:
    byte_words_list.append(bytes(item, 'utf-8'))
for item in byte_words_list:
    print(
        f'Тип переменной - {type(item)}\nСодержимое переменной - {item}\nДлина переменной - {len(item)}')
