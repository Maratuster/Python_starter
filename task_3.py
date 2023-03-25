"""
3. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def print_user_info(name, surname, birth_year, city, email, phone_number):
    print(f"{name} {surname} {birth_year} года рождения, проживает в городе {city}, email: {email}, телефон: {phone_number}")

input_name = input("Введите имя: ")
input_surname = input("Введите Фамилию: ")
input_birth_year = input("Введите дату рождения: ")
input_city = input("Введите город проживания: ")
input_email = input("Введите адрес электронной почты: ")
input_phone_number = input("Введите номер телефона: ")

print_user_info(name = input_name, surname = input_surname, birth_year = input_birth_year, city = input_city, email = input_email, phone_number = input_phone_number)