# Совершенно не понятно где ошибка, скорее всего файл косой...


def name_count():
    from string import ascii_uppercase
    file = open("name.txt")
    new = list(file)
    line = str(new)
    name_num = 1
    name_weight = 0
    result = 0
    line = line.replace('","', ',')
    line = line.replace('"', "")
    line = line.replace('[\'', "")
    line = line.replace('\']', "")
    line = line.split(",")

    for element in line:

        for init in element:
            print(init)
            name_weight += (ascii_uppercase.index(init) + 1)

        result += (name_num * name_weight)
        name_num += 1
        name_weight = 0

    return result

print(name_count())

# 871198282
# 850081394
# 849689006