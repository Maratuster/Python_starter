"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint
from my_func_library import get_number


def play_game(num, try_count):
    if try_count > 0:
        answer = get_number()
        if answer == num:
            print("Молодец! Это верное число.")
        elif answer < num:
            print(
                f"Загаданное число больше {answer}. У тебя осталось {try_count - 1} попыток!")
            return play_game(num, try_count-1)
        elif answer > num:
            print(
                f"Загаданное число меньше {answer}. У тебя осталось {try_count - 1} попыток!")
            return play_game(num, try_count-1)
    else:
        print("Попытки закончились. Не расстраивайся!")


print("Я хочу сыграть с тобой в игру! Я загадал число от 0 до 100. Угадай за 10 попыток")
number = randint(0, 100)
print(number)
play_game(number, 10)
