def factorial_digits_sum():
    result = 1
    out = 0
    for number in range(1, 101):
        result *= number
    for number in str(result):
        out += int(number)
    return out

print(factorial_digits_sum())