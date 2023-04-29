"""
Задание 3.
Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b''
(без encode decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
В Python можно записать строковые литералы с помощью маркировки b''
только для символов, которые представлены одним байтом в кодировке ASCII.
Поэтому слово "класс" невозможно записать в байтовом типе с помощью
маркировки b'', так как в нем содержится символ, который не является
символом ASCII. """
words_list = ["attribute", "класс", "функция", "type"]
for word in words_list:
    try:
        byte_word = bytes(word, 'ascii')
        print(f"Слово '{word}' можно записать в байтовом типе: {byte_word}")
    except UnicodeEncodeError:
        byte_word = bytes(word, 'utf-8')
        print(f"Слово '{word}' нельзя записать в байтовом типе в кодировке ASCII.\nНо можно записать в кодовых точках utf-8: {byte_word}")