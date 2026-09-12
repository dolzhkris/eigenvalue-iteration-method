import numpy as np

def input_sym_matrix(n):
    matrix = np.zeros((n, n))
    print("Введите элементы симметричной матрицы:")
    for i in range(n):
        for j in range(n):
            element = float(input(f"Элемент [{i}][{j}]: "))
            matrix[i][j] = element
    return matrix

def iteration(A, num_iterations):
    n = A.shape[0]
    x = np.random.rand(n)  # начальное приближение собственного вектора
    for _ in range(num_iterations):
        y = np.dot(A, x)  # умножаем матрицу на вектор
        x = y / np.linalg.norm(y)  # нормируем полученный вектор
    eigenvalue = np.dot(x, np.dot(A, x))  # вычисляем собственное значение
    return eigenvalue, x

n = int(input("Введите размерность матрицы: "))

# Ввод симметричной матрицы
matrix = input_sym_matrix(n)

# Вывод исходной симметричной матрицы
print("Исходная симметричная матрица:")
print(matrix)

# Вызов метода итераций
num_iterations = 3
eigenvalue, eigenvector = iteration(matrix, num_iterations)

# Вывод результатов
print("Найденное наибольшее собственное значение:", eigenvalue)
print("Соответствующий собственный вектор:", eigenvector)
