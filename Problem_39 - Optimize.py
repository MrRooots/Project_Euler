def triangle_sides_variants():
    var_count = [0]*1000
    for perimeter in range(1001): # Перебор вариантов периметра
        for a in range(1000):
            for b in range(1000):
                for c in range(1000):
                    if max(a, b, c) == a:
                        if a**2 == b**2 + c**2:
                            var_count[perimeter] += 1
                    if max(a, b, c) == b:
                        if b**2 == a**2 + c**2:
                            var_count[perimeter] += 1
                    if max(a, b, c) == c:
                        if c**2 == a**2 + b**2:
                            var_count[perimeter] += 1

    return max(var_count)

print(triangle_sides_variants())