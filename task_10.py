"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""
import random
n = int(input('Введите количество монеток, которое лежит на столе: '))
coins_array = []
for el in range(1, n+1):
    side = random.randint(0, 1)
    coins_array.append("орёл") if side == 0 else coins_array.append("решка")
print(coins_array)
obverse_side = 0
reverse_side = 0
index = 0
for el in coins_array:
    if coins_array[index] == "решка":
        obverse_side += 1
    else:
        reverse_side += 1
    index += 1
if obverse_side <= reverse_side:
    print(
        f'Чтобы все монетки были одинаковой стороной вверх, переверните {obverse_side} монет')
else:
    print(
        f'Чтобы все монетки были одинаковой стороной вверх, переверните {reverse_side} монет')
