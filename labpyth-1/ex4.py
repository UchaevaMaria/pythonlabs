import numpy as np

#генерация случайных матриц
A = np.random.randint(1, 11, (5, 5))
B = np.random.randint(1, 11, (5, 5))

print("Матрица A:", A)
print("Матрица B:", B)
elementwise_product = A * B
print("Поэлементное произведение", elementwise_product) #поэлементное произведение матриц

#матричное умножение
matrix_product = np.dot(A, B)
# Или эквивалентно: matrix_product = A @ B
print("Матричное произведение A @ B:", matrix_product)

#определитель матрицы A
det_A = np.linalg.det(A)
print("Определитель матрицы A:", det_A)

#транспонированная матрица B
B_T = B.T
print("Транспонированная матрица B:", B_T)

#обратная матрица для A 
if det_A != 0:
    A_inv = np.linalg.inv(A)
    print("Обратная матрица A:", A_inv)
else:
    print("Матрица A вырожденная, обратная матрица не существует.")

#решение системы линейных уравнений
# где C - вектор-столбец сумм строк матрицы A
C = np.sum(A, axis=1).reshape(-1, 1)  # вектор-столбец
print("Вектор C (сумма строк A):", C)

#проверяем, можно ли решить систему
if det_A != 0:
    x = np.linalg.solve(A, C)
    print("Решение системы A * x = C:", x)
else:
    print("Система не имеет уникального решения, так как A вырожденная.")