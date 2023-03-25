"""
2. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!
Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0
Process finished with exit code 0
"""
def division_of_numbers(num_1, num_2):
    result = None
    try:
        result = round(float(num_1/num_2), 2)
    except Exception:
        print("Вы что? Пытаетесь делить на 0!")
        result = "На ноль делить нельзя!"
    return result

def get_number():
    result = input()
    try:
        result = float(result)
    except Exception:
        print("Вы ввели не число. Попробуйте ещё раз.")
        get_number()
    return result

print(f"Введите делимое:")
dividend = get_number()
print(f"Введите делитель:")
divider = get_number()
print(division_of_numbers(dividend, divider))