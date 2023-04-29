"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
words_list = ["разработка", "администрирование", "protocol", "standard"]
byte_words_list = []
for word in words_list: byte_words_list.append(word.encode())
for item, byte_word in enumerate(byte_words_list):
    print(f"{words_list[item]} = {byte_word}")
decoded_words = []
for byte_word in byte_words_list: decoded_words.append(byte_word.decode())
for word in decoded_words:
    print(word)