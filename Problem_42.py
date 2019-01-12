# Функция пдсчета веса слова, получает на вход строку, возвращает ее вес
def name_wight_counter(line):
    from string import ascii_uppercase
    name_weight = 0
    for element in line:
        if element in ascii_uppercase:
            name_weight += ascii_uppercase.index(element) + 1

    return name_weight


# Составление списка треугольных чисел по формуле: t(n) = 1/2 * n * (n + 1)
def triangle_numbers():
    numbers = []
    count = 0
    file = open("words.txt")
    for u in range(1, 101):
        numbers.append(int((u / 2) * (u + 1)))

    for line in file:
        if name_wight_counter(line) in numbers:
            count += 1

    return count

# Вывод конечного результата
print(triangle_numbers())
