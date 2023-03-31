"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.

Пример:
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""
from my_func_library import get_number


def degree_finder(num, deg):
    if deg > 1:
        num *= degree_finder(num, deg-1)  # 1) 3
    return num


number = get_number()
degree = get_number()
print(degree_finder(number, degree))
