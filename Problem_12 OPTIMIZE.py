def triangle():
    res = 0
    count = 0
    for num in range(1, 100):
        res = res + num
        for divisor in range(1, (res//2) + 1):
            if res % divisor == 0:
                count += 1

        print(res, count)

        if count >= 500:
            return res

        else:
            count = 0

print(triangle())

# 76,576,500
