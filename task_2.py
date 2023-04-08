"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:

    def __init__(self, length, width, mass, thickness):
        self._length = length
        self._width = width
        self.mass = mass
        self.thickness = thickness

    def asfalt_mass(self):
        summary_mass = self._length*self._width*self.mass*self.thickness
        print(
            f"{self._length}*{self._width}*{self.mass}*{self.thickness} = {summary_mass}")


road_place = Road(5000, 20, 25, 0.05)
road_place.asfalt_mass()