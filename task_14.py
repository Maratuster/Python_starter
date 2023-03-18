"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""
while True:
    try:
        number_N = int(input("Введите число: "))
        break
    except Exception:
        print("Вы ввели не число! Попробуйте ещё раз.")
deegre_of_two = 1
deegre_list = []
count = 0
while deegre_of_two < number_N:
    deegre_of_two = 2**count
    if deegre_of_two < number_N:
        deegre_list.append(deegre_of_two)
        count +=1
print(deegre_list)