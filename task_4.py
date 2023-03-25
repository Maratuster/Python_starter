"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(num_1, num_2, num_3):
    result = None
    if (num_1 <= num_2 and num_1 < num_3) or (num_1 < num_2 and num_1 <= num_3) or num_1 == num_2 == num_3:
        result = num_2 + num_3
    elif (num_2 <= num_1 and num_2 < num_3) or (num_2 < num_1 and num_2 <= num_3):
        result = num_1 + num_3
    elif (num_3 <= num_1 and num_3 < num_2) or (num_3 < num_1 and num_3 <= num_2):
        result = num_1 + num_2
    return result

def my_func_sort(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    my_list.sort(reverse=True)
    result = int(my_list[0]) + int(my_list[1])
    return result

def get_number():
    number = input()
    try:
        number = int(number)
    except Exception:
        print("Вы ввыели не число. Попробуйте ещё раз!")
        number = get_number()
    return number

print("Введите первое число: ")
number_1 = get_number()
print("Введите второе число: ")
number_2 = get_number()
print("Введите третье число: ")
number_3 = get_number()
print(my_func(number_1, number_2, number_3))
print(my_func_sort(number_1, number_2, number_3))