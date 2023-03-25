"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
Пример:

5
    1 2 3 4 5
    3
    -> 1
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

def count_of_means(array):
    find_number = int(input("Введите искомое число: "))
    count = 0
    for item in array:
        if item == find_number: count += 1 
    return count

lenght_of_array = int(input("Введите длину массива: "))
work_array = get_array(lenght_of_array)

print(count_of_means(work_array))