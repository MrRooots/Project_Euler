def Multiples_of_3_and_5():

    result = 0

    for init in range(0, 1000):

        if (init % 3 == 0) or (init % 5 == 0):

            result += init

    print(result)

Multiples_of_3_and_5()