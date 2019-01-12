def curious_nums():
    # 1! + 4! + 5! = 1 + 24 + 120 = 145.
    result = 0
    num = 3
    lag = 0
    factorial = 1

    while num < 100000:

        for digit in str(num):

            for element in range(1, int(digit) + 1):
                factorial *= element

            lag += factorial
            factorial = 1

        if lag == num:
            result += num
            print(num)

        num += 1
        lag = 0

    return result

print("Sum of curious numbers = {a}".format(a = curious_nums()))
