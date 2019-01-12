def consider_counter():
    num = []
    for a in range(2, 101):
        for b in range(2,101):
            if a**b not in num:
                num.append(a**b)

    return len(num)

print(consider_counter())