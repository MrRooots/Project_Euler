# Pentagonal numbers
# n(3n−1) / 2
def pentagonal_numbers():
    numbers = []
    for init in range(1, 100):
        numbers.append(int((init*(3*init - 1))/2))

    return numbers

print(pentagonal_numbers())
