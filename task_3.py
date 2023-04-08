"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        print(f"{self.name} {self.surname}")
    def get_total_income(self):
        summary = 0
        for key, value in self._income.items():
            summary += value
        print(f"{summary}")

income_dict = {"wage": 31000, "bonus": 16000}
worker_exemplar = Worker("Иван", "Иванов", "Супервайзер", income_dict)
position_exemplar = Position("Иван", "Иванов", "Супервайзер", income_dict)
position_exemplar.get_full_name()
position_exemplar.get_total_income()
