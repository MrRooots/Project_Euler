def Prime_10001():
    from math import sqrt
    prime_numbers = []
    num = 2
    flag = True
    while len(prime_numbers) < 10001:
        for init in range(2, int(sqrt(num) + 1)):
            if num % init == 0:
               flag = False
               break
        if flag == True:
            prime_numbers.append(num)
        flag = True
        num += 1
    print(prime_numbers)
    print(max(prime_numbers))

Prime_10001()