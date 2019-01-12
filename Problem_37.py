# Truncatable numbers


def is_prime(num):  # Возвращает True, если num - простое
    from math import sqrt
    flag = True
    if num >= 2:
        for init in range(2, int(sqrt(num) + 1)):
            if num % init == 0:
                flag = False
                break

    else: flag = False

    return flag

count = 0
num = 11
result = 0
while count != 11:
    flag_1 = True
    if is_prime(num) is True:  # Если число простое

        # Проверка слева направо
        for element in range(1, len(str(num)) + 1):
            if is_prime(int(str(num)[0:element])) is True:  # Если при переборе числа от первой цифры
                continue
            else:  # Если хоть одна часть - не простая --> выход из цикла
                flag_1 = False
                break

        # Проверка справа налево
        for element in range(1, len(str(num))):
            if is_prime(int(str(num)[element:len(str(num))])) is True:
                continue
            else:
                flag_1 = False
                break

        if flag_1 is True:
            count += 1
            result += num
        else:
            flag_1 = True

    num += 1

print(result)

