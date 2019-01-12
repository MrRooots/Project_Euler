def primeSum(count):
    # Составить список простых чисел
    # Составить максимально эффективный алгоритм поиска простых чисел в диапозоне до..

    import math

    prime_number = 0
    flag = True

    for isNumber_prime in range(2, count + 1):

        for divisor in range(2, int(math.sqrt(isNumber_prime)) + 1):

            if isNumber_prime % divisor == 0:
                flag = False

                break

        if flag == True:
            prime_number += isNumber_prime

        flag = True

    print("Сумма простых чисел в диапазоне от 2 до " + str(count) + " равна: " + str(prime_number))

primeSum(count = int(input("Введите конечное число диапазона: ")))