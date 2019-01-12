def is_prime(num):  # Возвращает True, если num - простое
    from math import sqrt
    flag = True
    for init in range(2, int(sqrt(num) + 1)):
        if num % init == 0:
            flag = False
            break

    return flag

count = 0
for num in range(2, 1000001):
    if is_prime(num) is True:
        if num > 10:
            if num > 100:
                # 1512 --> len = 4 --> len/2 --> 2
                num1 = str(num)[0]  # Первая цифра числа
                num2 = str(num)[len(str(num)) - 1]  # Последняя цифра числа
                num3 = str(num)[1: len(str(num)) - 1]  # Середина числа
                num5 = str(num)[0:int((len(str(num)))/2)]  # Первая половина числа
                num6 = str(num)[int((len(str(num)))/2):len(str(num)) - 1]  # Вторая половина числа
                if is_prime(int(num1)) is True:
                    if is_prime(int(num2)) is True:
                        if is_prime(int(num3)) is True:
                            if is_prime(int(num3 + num2 + num1)) is True:
                                if is_prime(int(num2 + num1 + num3)) is True:
                                    if len(str(num)) % 2 == 0:
                                        if is_prime(int(num6 + num5)) is True:
                                            count += 1
                                    else:
                                        if len(str(num)) == 3:
                                            count += 1


            else:
                # 37 --> 73
                num1 = str(num)[0]  # Первая цифра двузначного числа
                num2 = str(num)[1]  # Вторая цифра двузначного числа
                if is_prime(int(num2 + num1)) is True:
                    count += 1

        else: count += 1

print(count)