"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
    4 
"""
from my_func_library import get_number


def summ_finder(num_1, num_2, summary):
    if num_1 != 0 and num_2 != 0:
        num_1 -= 1
        num_2 -= 1
        summary = summary+1+1
        return summ_finder(num_1, num_2, summary)
    elif num_1 == 0 and num_2 == 0:
        return summary
    elif num_1 != 0 and num_2 == 0:
        num_1 -= 1
        summary += 1
        return summ_finder(num_1, num_2, summary)
    elif num_2 != 0 and num_1 == 0:
        num_2 -= 1
        summary += 1
        return summ_finder(num_1, num_2, summary)


number_1 = get_number()
number_2 = get_number()
print(summ_finder(number_1, number_2, 0))
