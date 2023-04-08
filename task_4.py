"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:
    def __init__(self, list_of_list):
        self.lists_list = list_of_list
    
    def __str__(self):
        print(*[item for item in self.lists_list], sep='\n')

    
    def __add__(self, other):
        new_list = []
        for item_1 in range(len(self.lists_list)):
            row = []
            for item_2 in range(len(self.lists_list[0])):
                row.append(self.lists_list[item_1][item_2] + other.lists_list[item_1][item_2])
            new_list.append(row)
    
        return new_list
                

matrix_1 = Matrix([[1, 6, 4], [3, 9, 2]])
matrix_2 = Matrix([[2, 7, 5], [2, 8, 1]])
print(matrix_1.__str__())
print(matrix_2.__str__())
print(*(matrix_1.__add__(matrix_2)), sep= "\n")