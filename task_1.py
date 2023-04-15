"""
Реализовать дескрипторы для любых двух классов
"""
# Реализовано на базе Задания 3 к семинару №7.

class str_in_name:

    def __get__(self, instance, owner):
        return instance.__dict__[self.incoming_attr]

    def __set__(self, instance, value):
        # Проверка на тип данных. В ИМени должны быть строка
        if type(value) != str:
            raise ValueError("Неверный тип данных")
        # Проверка на наличие цифр и символов в имени
        error_in_name = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/',
                       '*', '$', '#', '!', '@', '%'}
        intersection = error_in_name.intersection(set(value))
        if len(intersection):
            raise ValueError("Цифры и символы не могут использоваться в имени")

    def __delete__(self, instance):
        del instance.__dict__[self.incoming_attr]

    def __set_name__(self, owner, incoming_attr):
        self.incoming_attr = incoming_attr

class get_positive_number:

    def __get__(self, instance, owner):  # Здесь
        return instance.__dict__[self.incoming_attr]

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError("Неверный тип данных")
        if value < 0:
            raise ValueError("Значение должно быть больше нуля")

    def __delete__(self, instance):
        del instance.__dict__[self.incoming_attr]

    def __set_name__(self, owner, incoming_attr):
        self.incoming_attr = incoming_attr

class Worker:
    age = get_positive_number()
    name = str_in_name()
    surname = str_in_name()
    def __init__(self, name, surname, income, age):
        self.name = name
        self.surname = surname
        self._income = income
        self.age = age

class Position(Worker):
    position = str_in_name()
    telephone = get_positive_number()

    def __init__(self, position, telephone):
        self.position = position
        self.telephone = telephone

income_dict = {"wage": 31000, "bonus": 16000}
worker_exemplar = Worker("Иван", "Иванов4", income_dict, 29)
position_exemplar = Position("Супервайзер", -9876543210)
print(worker_exemplar) # выведет 
# <__main__.Worker object at 0x00000185B978C7D0>
# если всё верно
print(position_exemplar) # выведет 
# <__main__.Position object at 0x00000185B978C810>
# если всё верно