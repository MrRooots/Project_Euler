def d_multiply():
    line = ""
    for init in range(1, 1000000):
        line += str(init)

    result = int(line[0]) * int(line[9]) * int(line[99]) * int(line[999]) * int(line[9999]) * int(line[99999]) * int(line[999999])

    return result

print(d_multiply())