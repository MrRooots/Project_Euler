def Route_counter(length, height):
    matrix = []
    number = 0
    puller_column = 2
    puller_row = 2

    # Содание матрицы
    for row in range(height):
        matrix.append([])
        for column in range(length):
            matrix[row].append(number)

    # Заполнить первый __ряд__ и __столбец__ цифрами по порядку
    for column in range(len(matrix)): # Заполнение __столбца__ (2..n)
        matrix[column][0] = puller_column
        puller_column += 1

    for row in range(len(matrix[0])): # Заполнения __ряда__ (2..n)
        matrix[0][row] = puller_row
        puller_row += 1

    # Заполнение последующих рядов матрицы
    for init in range(1, height):
        kwarg_2 = 0
        for kwarg_1 in range(1, length):
                matrix[init][kwarg_1] = matrix[init - 1][kwarg_1] + matrix[init][kwarg_2]
                kwarg_2 += 1

    # Работает при любых размерах сетки!!!
    return matrix[-1][-1]

print("Количество путей, ведущих в нижний правый угол: {}".format(Route_counter(int(input("Введите длину сетки: ")), int(input("Введите ширину сетки: ")))))
