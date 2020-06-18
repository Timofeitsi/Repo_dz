# понимая что сложение возможно только для одинаковых по размеру матриц
# приведение к одинаковому размеру осуществлялось добавенниеи нулей в столбцах
# там где необходимо и нулевых строк
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        m1 = self.matrix
        m2 = other.matrix
        if len(m1) != len(m2):
            while len(m1) != len(m2):
                if len(m1) > len(m2):
                    m2.append([0])
                else:
                    m1.append([0])
        #if len(m1) == len(m2):
        temp_mat = []
        for i in range(len(m1)):
            temp_row = []
            if len(m1[i]) != len(m2[i]):
                while len(m1[i]) != len(m2[i]):
                    if len(m1[i]) > len(m2[i]):
                        m2[i].append(0)
                    else:
                        m1[i].append(0)
            for j in range(len(m1[i])):
                sum_mat = m1[i][j] + m2[i][j]
                temp_row.append(sum_mat)
            temp_mat.append(temp_row)
        print("Сложение выполнено")
        return Matrix(temp_mat)

    def __str__(self):
        mat_prn = ('\n'.join(['\t\t'.join(map(str, self.matrix[i])) for i in range(len(self.matrix))]))
        return f"Матрица в виде прямоугольной схемы\n" \
            f"{mat_prn}"


#A = Matrix([[1, 2, 5], [3, 4], [5, 6], [1, 2], [3, 4]])
#B = Matrix([[1, 2], [3, 4], [5, 6], [1, 2, 8], [3, 4], [5, 6]])
#C = Matrix([[120, 130, 140, 150, 6], [1, 2, 8], [5, 6]])

A = Matrix([[31, 22], [37, 43], [51, 86]])
B = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
C = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print('Матрица А')
print(A)
print('Матрица В')
print(B)
print('Матрица С')
print(C)
print('Сумма А + В')
print(A + B)
print('Сумма А + В + С')
print(A + B + C)

import random
a = 5 # количество строк
b = 3 # количество столбцов
mat = []
for i in range(a):
    el_row = []
    for j in range(b):
        el = random.randint(-20, 20)
        el_row.append(el)
    mat.append(el_row)
print('Рандомная матрица')
print(mat)

mat = Matrix(mat)
print(mat)
print('Сумма матриц А и рандомной')
print(mat + A)
