def fifth_powers():
    res = 0
    result = 0
    prev = []
    for num in range(2, 500000):
        for init in str(num):
            prev.append(init)

        for element in prev:
            res += int(element)**5

        if res == num:
            result += num

        prev = []
        res = 0
    return result

print(fifth_powers())