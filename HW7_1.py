# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f'{sum(self.matrix, [])[0]}\t{sum(self.matrix, [])[1]}\n{sum(self.matrix, [])[2]}\t{sum(self.matrix, [])[3]}\n{sum(self.matrix, [])[4]}\t{sum(self.matrix, [])[5]}\n'

    def __add__(self, other):
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])

matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
print(matrix_1 + matrix_2 + matrix_2)
