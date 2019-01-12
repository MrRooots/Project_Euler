def Pythagorean_triples():
    import math  # module for sqrt()

    for init_a in range(1000):

        for init_b in range(init_a):

            if int(math.sqrt(init_a * init_a + init_b * init_b)) == math.sqrt(init_a * init_a + init_b * init_b):

                c = math.sqrt(init_a * init_a + init_b * init_b)

                if init_a + init_b + c == 1000:
                    print("Произведение чисел, сумма которых равна 1000, пифагоровой тройки равно: " + str(
                        int(init_a * init_b * c)))

                    quit()

Pythagorean_triples()