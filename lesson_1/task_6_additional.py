"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
"""

ticket_number = input('Введите шестизначный номер билета: ')
index = 0
rev_index = 1
summ_1_half = 0
summ_2_half = 0
while index < len(ticket_number)//2:
    summ_1_half += int(ticket_number[index])
    summ_2_half += int(ticket_number[len(ticket_number)-rev_index])
    index += 1
    rev_index += 1
print(summ_1_half, summ_2_half)
if summ_1_half == summ_2_half:
    print(f'Поздравляю! Ваш билетик {ticket_number} - счастливый!')
else:
    print(f'Сожалею! Билетик {ticket_number} - не является счастливым!')
