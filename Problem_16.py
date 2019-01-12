def Sum(number):
    number =2 ** 1000
    result = 0
    for digit in str(number):
        result += int(digit)
    return result

print(Sum(int(input("Enter a number: "))))