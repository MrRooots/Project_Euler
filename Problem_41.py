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

def pan_digital_primes():
    flag = True
    m_num = 0
    for num in range(10000000, 100000000):
        if is_prime(num) is True:
            for element in str(num):
                if str(num).count(element) > 1:
                    flag = False
                    break
        else: flag = False

        if flag is True:
            if num > m_num:
                m_num = num
        flag = True

    return m_num

print(pan_digital_primes())
