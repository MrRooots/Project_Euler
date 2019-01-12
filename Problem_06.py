def square_difference():
    s1 = 0
    s2 = 0
    for number in range(1, 101):
        s1 += number
        s2 += number**2
    s1 = s1 ** 2
    res = s1 - s2
    return res

print(square_difference())