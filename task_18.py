"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""
import random

def get_array(array_lenght):
    my_array = []
    array_index = 0
    while array_index < array_lenght:
        my_array.append(random.randint(0, 10))
        array_index +=1
    print(my_array)
    return my_array

def nearby_mean(array):
    find_number = int(input("Введите искомое число: "))
    count = 0
    min_range = 10000
    find_index = 0
    while count < len(array):
        if abs(array[count] - find_number) < min_range:
            min_range = abs(array[count] - find_number)
            find_index = count
        count += 1 
    return array[find_index]

lenght_of_array = int(input("Введите длину массива: "))
work_array = get_array(lenght_of_array)

print(nearby_mean(work_array))