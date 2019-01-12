# Прописать 2 ф-ции, одну для нахождения делитеей от числа, другую - сравнение чисел до 10000
# num1 != num2 and d(num1) = num2 and d(num2) = num1


def dividers(number): # Находит и возвращает сумму делителей числа-аргумента
    sum_divisors = 0
    for divisor in range(1, (number // 2) + 1):
        if number % divisor == 0:
            sum_divisors += divisor
    return sum_divisors


def amicable_numbers():
    number = 0
    result = 0
    while number < 10000:
        # Сумма делителей 220 = 284 ==> сумма делителей 284 д.б. равна 220
        summation = dividers(number)  # Возвращает сумму делителей number
        if (dividers(summation) == number) and (summation != number):
            result += number
        number += 1
    return result

print("Сумма всех дружественных чисел до 10000 ранва: " + str(amicable_numbers()))