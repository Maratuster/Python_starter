"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
number = input('Введите целое положительное число:')
two_digit = number + number
three_digit = number + number + number
summary = int(number) + int(two_digit) + int(three_digit)
print(f'{number} + {two_digit} + {three_digit} = {summary}')