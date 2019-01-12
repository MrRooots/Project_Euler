def Fibonacci_numbers():
    number = 1
    number_1 = 2
    result = 2
    fibonacci_number = 0
    flag = False
    while flag == False:
        if fibonacci_number < 4000000:
            fibonacci_number = number + number_1
            number = number_1
            number_1 = fibonacci_number
            if fibonacci_number % 2 == 0:
                result += fibonacci_number
        else: flag = True
    print(result)

Fibonacci_numbers()