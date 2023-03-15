"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""
import random
value_x, value_y = random.randint(0, 1000), random.randint(0, 1000)
print(value_x, value_y)
print(
    f"Петя загадал два числа - X и Y.\nСумма чисел равна {value_x+value_y}, а произведение равно {value_x*value_y}.\nУгадай числа.")


def give_answer():
    try:
        answer = int(input())
    except Exception:
        print("Вы ввели не число. Попробуйте ещё раз.")
        give_answer()
    return

print('Чему равно число X?')
answer_x = give_answer()
print('Чему равно число Y?')
answer_y = give_answer()
if value_x == answer_x and value_y == answer_y:
    print('Всё верно! Поздравляю!')
else:
    print('Не верно. Попробуй ещё раз')
