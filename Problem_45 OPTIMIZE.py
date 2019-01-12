def triangle_hexagonal_pentagonal():

    triangle = []
    for n in range(10000, 10000001):
        triangle.append(int((n*(n+1))/2))

    hexagonal = []
    for n in range(10000, 10000001):
        hexagonal.append(int(n*(2*n-1)))

    pentagonal = []
    for n in range(10000, 10000001):
        pentagonal.append(int((n*(3*n-1))/2))

    for element in triangle:
        if element in hexagonal:
            if element in pentagonal:
                if element > 40755:
                    return element

print(triangle_hexagonal_pentagonal())