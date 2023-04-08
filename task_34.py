"""
Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам  
"""
def vowel_counter(list):
    vowels = set("аеёиуоюяыэ")
    new_list = []
    for item in list:
        count = 0
        for string in item:
            if string in vowels:
                count += 1
        new_list.append(str(count))
    return new_list

def frase_rithm(list):
    count = 0
    temp_result = False
    while count < len(list) - 1:
        if list[count] == list [count + 1]:
            temp_result = True
        else: temp_result = False
        count += 1
    print('Парам пам-пам') if temp_result == True else print('Пам парам')

frase_list = input("Введиет фразу: ").split(" ")
count_list = vowel_counter(frase_list)
frase_rithm(count_list)