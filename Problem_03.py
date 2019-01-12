# Надо оптимизировать алгоритм (time == 10 sec) :(
def primeFactor():
    import math
    number = 600851475143
    factor = 2
    max_factor = 0
    divisor_flag = True
    while factor < int(math.sqrt(number)):
        for init in range(2, int(math.sqrt(factor)) + 1):
            if factor % init == 0:
                divisor_flag = False
                break
        if divisor_flag == True:
            if number % factor == 0:
                if factor > max_factor:
                    max_factor = factor
        divisor_flag = True
        factor += 1
    print(max_factor)

primeFactor()