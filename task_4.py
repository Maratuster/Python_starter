"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""
from my_func_library import get_number


def strange_summ(num, res, start_num):
    if num == 0:
        return print(res)
    else:
        num -= 1
        res += start_num
        start_num /= -2
        return strange_summ(num, res, start_num)


number = get_number()
print(number)
strange_summ(number, 0, 1)
